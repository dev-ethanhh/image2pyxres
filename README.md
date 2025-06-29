### Quick explanation
The program scans the input image and tries to match each pixel to the closest color in the Pyxel color palette, which is quite limited.
It then generates one or more .pyxres files, multiple files may be needed due to Pyxel's limitations.
Finally, the program displays all the generated .pyxres files aligned side by side to reconstruct and preview the full converted image. For very large images, the result may appear zoomed out.

### Setting up the program
<hr>
To install this program, you just need <a href="https://www.python.org/downloads/">Python</a>.
Once the repository is installed, extract it.
You’ll need to edit the main.py file, from lines 6 to 19, all instructions are provided there.
However, you can also test the program right away using the example image to see what it does.

If you don’t have a code editor, I strongly recommend <a href="https://vscodium.com/">VSCodium</a>, which is like VS Code but without Microsoft’s data collection.

Then, install the required libraries by running:
```sh
pip install numpy pillow pyxel
```
Finally, navigate to the repository folder in your terminal and run:
```sh
python main.py
```

The program should work out of the box, but since it was created a couple of years ago, some updates might be needed.
If you run into issues, feel free to fix them, it shouldn’t be too complicated. Otherwise, you can contact me by email (check my profile).
