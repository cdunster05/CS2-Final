import tkinter as tk
from tkinter import messagebox


class CandidateEntry(tk.Toplevel):
    def __init__(self, master):
        super().__init__(master)
        self.title("Candidate Entry")
        self.geometry("400x250")
        self.master = master
        self.create_widgets()

    def create_widgets(self):
        self.label = tk.Label(self, text="Enter Candidate Names (one per line):")
        self.label.pack()

        self.text_entry = tk.Text(self, height=5, width=30)
        self.text_entry.pack()

        self.vote_count_label = tk.Label(self, text="Enter votes required to win:")
        self.vote_count_label.pack()

        self.vote_count_entry = tk.Entry(self)
        self.vote_count_entry.pack()

        self.confirm_button = tk.Button(self, text="Confirm", command=self.confirm_candidates)
        self.confirm_button.pack()

    def confirm_candidates(self):
        candidates = self.text_entry.get("1.0", tk.END).strip().split("\n")
        candidates = [candidate.strip() for candidate in candidates if candidate.strip()]
        votes_needed = self.vote_count_entry.get().strip()

        if not candidates:
            messagebox.showerror("Error", "Please enter at least one candidate.")
            return
        if not votes_needed.isdigit():
            messagebox.showerror("Error", "Please enter a valid number of votes needed to win.")
            return

        self.master.candidates = {candidate: 0 for candidate in candidates}
        self.master.votes_needed = int(votes_needed)
        self.destroy()
        self.master.create_voting_screen()


class VoteApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Vote App")
        self.geometry("300x200")
        self.candidates = {}
        self.votes_needed = 0
        self.voters = {}
        self.create_candidate_entry_screen()

    def create_candidate_entry_screen(self):
        self.candidate_entry_screen = CandidateEntry(self)

    def create_voting_screen(self):
        self.title("Voting Screen")
        self.geometry("400x250")
        self.create_widgets()

    def create_widgets(self):
        for widget in self.winfo_children():
            widget.destroy()

        self.label_name = tk.Label(self, text="Enter Your Name:")
        self.label_name.pack()

        self.entry_name = tk.Entry(self)
        self.entry_name.pack()

        self.label_candidate = tk.Label(self, text="Select a Candidate:")
        self.label_candidate.pack()

        self.selected_candidate = tk.StringVar(self)
        self.selected_candidate.set(None)

        for candidate, _ in self.candidates.items():
            radio_button = tk.Radiobutton(self, text=candidate, variable=self.selected_candidate, value=candidate)
            radio_button.pack(anchor=tk.W)

        self.vote_button = tk.Button(self, text="Vote", command=self.cast_vote)
        self.vote_button.pack()

    def cast_vote(self):
        voter_name = self.entry_name.get().strip()
        candidate = self.selected_candidate.get()

        if not voter_name:
            messagebox.showerror("Error", "Please enter your name.")
            return
        if not candidate:
            messagebox.showerror("Error", "Please select a candidate.")
            return
        if voter_name in self.voters:
            messagebox.showerror("Error", "You have already voted.")
            return

        self.voters[voter_name] = candidate
        self.candidates[candidate] += 1

        if self.candidates[candidate] >= self.votes_needed:
            self.open_victory_screen(candidate)
        else:
            self.open_results_window()

    def open_victory_screen(self, winner):
        victory_window = tk.Toplevel(self)
        victory_window.title("Victory!")
        victory_window.geometry("400x200")

        winner_label = tk.Label(victory_window, text=f"{winner} wins with {self.votes_needed} votes!")
        winner_label.pack()

        voted_for_label = tk.Label(victory_window, text="Votes:")
        voted_for_label.pack()

        votes_text = ""
        for voter, voted_candidate in self.voters.items():
            if voted_candidate == winner:
                votes_text += f"{voter} voted for {voted_candidate}\n"
            else:
                votes_text += f"{voter} voted for {voted_candidate} (Lost)\n"
        votes_label = tk.Label(victory_window, text=votes_text)
        votes_label.pack()

        button = tk.Button(victory_window, text="Close", command=victory_window.destroy)
        button.pack()

    def open_results_window(self):
        results_window = ResultsWindow(self)
        results_window.mainloop()


class ResultsWindow(tk.Toplevel):
    def __init__(self, master):
        super().__init__(master)
        self.title("Voting Results")
        self.geometry("300x250")
        self.master = master
        self.create_widgets()

    def create_widgets(self):
        total_votes = sum(self.master.candidates.values())
        result_text = ""
        for candidate, votes in self.master.candidates.items():
            result_text += f"{candidate}: {votes} votes\n"
        result_text += f"Total votes cast: {total_votes}"

        self.result_label = tk.Label(self, text=result_text)
        self.result_label.pack()

        self.another_vote_button = tk.Button(self, text="Cast Another Vote", command=self.cast_another_vote)
        self.another_vote_button.pack()

        self.close_button = tk.Button(self, text="Close", command=self.destroy)
        self.close_button.pack()

    def cast_another_vote(self):
        self.destroy()
        self.master.create_voting_screen()


if __name__ == "__main__":
    app = VoteApp()
    app.mainloop()
