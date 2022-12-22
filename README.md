# Columbus Classical Academy Blog

## Setup
_One-time setup instructions._

- Create `blog/` repo and clone
- Install [Pelican](https://getpelican.com/#quickstart)
- Set up [Papyrus](https://aleylara.github.io/Papyrus/installation.html) theme
  - `mkdir themes`
  - `cd themes`
  - `git clone https://github.com/aleylara/Papyrus.git` (Actually, I cloned it elsewhere and copy/pasted the docs into the blog folder. I want to edit this theme and version control the edits.)
  - `mkdir pelican-plugins`
  - `cd pelican-plugins`
  - `git clone https://github.com/ingwinlu/pelican-toc.git`
- Modify Papyrus theme:
  - `templates/base.html`
    - update footer
- Update `pelicanconf.py` settings
- Update repository settings:
  - Settings > Pages > Branch > Main > /docs > Save
  - Check "Enforce HTTPS"


## Publish Site
- `cd blog`
- `make publish`
- delete `docs/`
- rename `output/` to `docs/`
- commit and push changes
