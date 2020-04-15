# Basic Website

This is the pile of code meant to be my website. It's actually slightly
responsive thanks to `flexbox` modeling! If you didn't notice, it's my resume
for now, but will evolve!

## Colouring Scheme

Using [mrmrs/colors](https://github.com/mrmrs/colors) for the colour scheme.

## Building

Use [Pipenv](https://pipenv.pypa.io/en/latest/) to create a Virtual Environment
with the required Packages.

```bash
pip install pipenv

pipenv install
pipenv shell

(resume) ./render.py
# Open test.html with web browser
```

Also use [Sass](https://sass-lang.com/) to render the CSS.

```bash
sass scss/style.scss:style.css
```

## Updating

If everything from the test render looks good, move `test.html`
over `index.html`:

```bash
(resume) ./render.py
(resume) mv test.html index.html
```

Or re-render with the output file set.

```bash
(resume) ./render.py --output index.html
```
