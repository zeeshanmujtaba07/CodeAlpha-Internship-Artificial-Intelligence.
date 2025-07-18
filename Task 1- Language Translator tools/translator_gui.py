import tkinter as tk
from tkinter import ttk, messagebox
from deep_translator import GoogleTranslator

# Supported languages
translator = GoogleTranslator(source='auto', target='en')
language_names = translator.get_supported_languages(as_dict=True)
lang_name_to_code = {v.title(): k for k, v in language_names.items()}
language_list = sorted(list(lang_name_to_code.keys()))  # Sorted alphabetically

def translate_text():
    src_name = source_lang.get()
    dest_name = target_lang.get()
    src = lang_name_to_code.get(src_name, "en")
    dest = lang_name_to_code.get(dest_name, "hi")
    text = text_input.get("1.0", tk.END).strip()


    if not text:
        messagebox.showwarning("Input Required", "Please enter text to translate.")
        return

    try:
        translated = GoogleTranslator(source=src, target=dest).translate(text)
        text_output.delete("1.0", tk.END)
        text_output.insert(tk.END, translated)
    except Exception as e:
        messagebox.showerror("Translation Error", str(e))

# Main Window
root = tk.Tk()
root.title("🌍 Language Translator")
root.geometry("750x550")
root.config(bg="#12813b")

# Style
style = ttk.Style()
style.theme_use('clam')
style.configure("TCombobox", fieldbackground="white", background="white")

# Title
tk.Label(root, text="Language Translator", font=("Helvetica", 20, "bold"), fg="#1a73e8", bg="#e8f0fe").pack(pady=20)

# Input Text
tk.Label(root, text="Enter Text to Translate:", font=("Arial", 12), bg="#e8f0fe").pack(anchor='w', padx=20)
text_input = tk.Text(root, height=7, width=80, font=("Arial", 11), bd=2, relief="groove")
text_input.pack(padx=20, pady=10)

# Language Selection
lang_frame = tk.Frame(root, bg="#e8f0fe")
lang_frame.pack(pady=10)

tk.Label(lang_frame, text="From:", font=("Arial", 11), bg="#e8f0fe").grid(row=0, column=0, padx=10, pady=5)
source_lang = ttk.Combobox(lang_frame, values=language_list, width=25, state="readonly")
source_lang.set("English")
source_lang.grid(row=0, column=1, padx=10)

tk.Label(lang_frame, text="To:", font=("Arial", 11), bg="#e8f0fe").grid(row=0, column=2, padx=10, pady=5)
target_lang = ttk.Combobox(lang_frame, values=language_list, width=25, state="readonly")
target_lang.set("Hindi")
target_lang.grid(row=0, column=3, padx=10)

# Translate Button
translate_btn = tk.Button(root, text="Translate", command=translate_text,
                          font=("Arial", 12, "bold"), bg="#000000", fg="white",
                          activebackground="#000000", activeforeground="white", bd=0, padx=20, pady=8)
translate_btn.pack(pady=20)

# Output Text
tk.Label(root, text="Translated Text:", font=("Arial", 12), bg="#e8f0fe").pack(anchor='w', padx=20)
text_output = tk.Text(root, height=7, width=80, font=("Arial", 11), bd=2, relief="groove")
text_output.pack(padx=20, pady=10)

root.mainloop()