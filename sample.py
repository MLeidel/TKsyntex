import tkinter as tk
from Tksyntex import SyntaxHighlighter

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Tksyntex Demo")

    # Create a Text widget
    text = tk.Text(root, wrap="none")
    text.pack(fill="both", expand=True)

    # Insert some C++ code
    code = '''#include <iostream>

int main() {
    std::cout << "Hello, world!" << std::endl;
    return 0;
}
'''
    text.insert("1.0", code)

    # Create the highlighter (debounce only matters during live editing)
    highlighter = SyntaxHighlighter(
        text_widget=text,
        language="cpp",
        font_name="consolas",
        font_size=14,
        style_name="material",  # monokai for dark, default for light
        debounce_ms=100
    )

    highlighter.highlight() # "text" for no highlighting

    root.mainloop()

