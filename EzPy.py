#KAXXX0
import subprocess
import tkinter as tk
import threading


class CodeRunner:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("EzPy - Testing Edition")

        self.input_box = tk.Text(self.root, height=10, width=50)
        self.input_box.pack()

        self.output_box = tk.Text(self.root, height=10, width=50)
        self.output_box.pack()
        self.output_box.config(state=tk.DISABLED)

        self.input_box.bind("<KeyRelease>", self.update_output)

        self.root.mainloop()

    def update_output(self, event):
        code = self.input_box.get("1.0", "end-1c")

        thread = threading.Thread(target=self.run_code, args=(code,))
        thread.start()

    def run_code(self, code):
        result = subprocess.run(["python", "-c", code], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, creationflags=subprocess.CREATE_NO_WINDOW)

        self.output_box.config(state=tk.NORMAL)
        self.output_box.delete("1.0", "end")
        if result.stderr:
            self.output_box.insert("1.0", result.stderr)
        else:
            self.output_box.insert("1.0", result.stdout)
        self.output_box.config(state=tk.DISABLED)


if __name__ == "__main__":
    runner = CodeRunner()
