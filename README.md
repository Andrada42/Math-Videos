# Math Videos

Making sense of math = **see, don't memorize**  

Visual mathematical animations  



## TODO - projects 🧩

🟢  
- [x] Pi = circumference of a circle / diameter
- [ ] Pythagorean Theorem
- [ ] Linear functions
- [ ] Fibbonaci Sequence (spiral)
- [ ] Caesar Cipher
- [ ] Matrix Multiplication
- [ ] Perimeter & Area

🟡  
- [ ] Trigonometric Circle
- [ ] Trigonometric Functions
- [ ] Derivatives
- [ ] Integrals
- [ ] Sorting Algorithms: ...

🟠  
- [ ] Bezier Curves
- [ ] Linear Algebra (matrix transformation/rotation)
- [ ] Eigenvalues & Eigenvectors
- [ ] Fourier Series (draw any shape from rotating circles)
- [ ] Fast Fourier Transform (FFT)
- [ ] Monty Hall Problem

🔴  
- [ ] Pi Approximation
- [ ] Buffon's Needle
- [ ] Gradient Descent 3D
- [ ] Singular Value Decomposition (SVD)
- [ ] PageRank Algorithm


✔️✅⭐
## TODO - features 🚩
- Group projects by category (difficulty / Math field)

---



## Setup

```bash
# ------------------ Method 1 ------------------
mkdir -p ex/simple_ex
cd ex/simple_ex
touch example.py
# from manim import *
# class CreateCircle(Scene): ...

manim -ql example.py CreateCircle   # => media/videos/example/480p15 dir
# -p = preview (not useful in WSL)
# -q... = quality ...
#     l = low       =  480p 15fps
#     m = medium    =  720p 30fps
#     h = high      = 1080p 60fps
#     k = 4K        = 2160p 60fps
```

```bash
# ------------------ Method 2 ------------------
uv init ex/uv_ex
cd ex/uv_ex
uv add manim

uv run manim -ql main.py CreateCircle
```



## Setup Makefile

```bash
cd ~/bin
which mk        # Make sure you don't have alreay an mk executable in ~/bin. If you do, use another name
touch ~/bin/mk  # Create an executable

cat << 'EOF' > ~/bin/mk
#!/bin/bash
PROJ=$(basename "$PWD")                                 # the last path segment = the name of the project
MAKEFILE_DIR="$(git rev-parse --show-toplevel)/prjs"    # the absolute path to Makefile = the absolute path to the git repo /prjs

make -C "$MAKEFILE_DIR" PROJ="$PROJ" "$@"
# -C "$MAKEFILE_DIR"    = change directory to the path of the Makefile
# PROJ="$PROJ"          = the name of the project we are currently in
# $@ = all arguments (ex: for mk render, $@ = render)
EOF

chmod +x ~/bin/mk   # Grant permission to execute
```


## Installation

```bash
# Install uv
curl -LsSf https://astral.sh/uv/install.sh | sh
```

```bash
# Install Latex

# if you have at least 7GB free
sudo apt update
sudo apt install texlive-full

# for less space:
wget -qO- "https://tinytex.yihui.org/install-bin-unix.sh" | sh
nano ~/.bashrc      # add:      # For TinyTeX (for Manim)
                    #           export PATH="$HOME/bin:$PATH"
source ~/.bashrc    # or close and open the terminal
tlmgr install amsmath babel-english cbfonts-fd cm-super count1to ctex doublestroke dvisvgm everysel fontspec frcursive fundus-calligra gnu-freefont jknapltx latex-bin mathastext microtype multitoc physics preview prelim2e ragged2e relsize rsfs setspace standalone tipa wasy wasysym xcolor xetex xkeyval  # => packets with .sty files
```

```bash
# Install dependencies
sudo apt update
sudo apt install build-essential python3-dev libcairo2-dev libpango1.0-dev
```

```bash
# Install Manim
pip install manim
```

```bash
# Project set-up for installation testing
uv init manimations
cd manimations
uv add manim

uv run manim checkhealth    # and render a preview
```

```bash
# Fix .dvi files to SVG
sudo apt install dvisvgm
kpsewhich amsmath.sty                       # => ~/.TinyTeX/texmf-dist/tex/latex = the path where tlmgr downloaded the packets
ls /usr/lib/x86_64-linux-gnu/libgs.so*      # => path to libgs.so is: /usr/lib/x86_64-linux-gnu/libgs.so.10
nano ~/.bashrc      # under:    # For TinyTeX (for Manim)
                    #           export PATH="$HOME/bin:$PATH"
                    # add:      export PATH="$HOME/.TinyTeX/bin/x86_64-linux:$PATH"
                    #           export LIBGS="/usr/lib/x86_64-linux-gnu/libgs.so.10"
                    #           export TEXMFHOME="$HOME/.TinyTeX/texmf-dist:$HOME/texmf"
source ~/.bashrc    # or close and open the terminal

uv run manim checkhealth    # and render a preview => tries to open the preview
# => "No applications found for mimetype: video/mp4" is normal if you work in WSL
```


## Learning Resources
https://docs.manim.community/en/stable/installation/uv.html  
https://yihui.org/tinytex/#for-other-users  
https://www.youtube.com/watch?v=MpG5_Zop00o  

https://docs.manim.community/en/stable/tutorials/quickstart.html  
https://docs.devtaoism.com/docs/html/index.html  
https://www.youtube.com/watch?v=tFxN5EoU58A&list=PL2B6OzTsMUrzNwj-XL_rRewYV48NHwypi&index=5  
