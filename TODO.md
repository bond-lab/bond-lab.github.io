# Bond Lab Website - Content Update TODO

Items to update now that the site has been ported to frozen-flask.
Based on reviewing all pages as of 2026-02-05.

## High Priority - Factual Updates

### Affiliation / Identity
- [ ] The site still says "NTU Computational Linguistics Lab" throughout,
      but Francis Bond is now at Palacký University Olomouc (and adjunct at EdUHK).
      **Decision needed:** Is this still the "NTU CL Lab" site, or should it be
      rebranded (e.g., "Bond Lab" / "Computational Linguistics Lab")?
- [ ] Update `index.html` description — currently says the lab is "centered in
      the Division of Linguistics and Multilingual Studies, NTU"
- [ ] Update `contact.html` — still lists NTU HSS building, NTU phone number
- [ ] Navigation footer references NTU links — update or remove

### Members Page (`members.html`)
- [ ] Francis Bond listed as "Associate Professor, Linguistics, NTU" — update title and affiliation
- [ ] Michael Goodman listed as "Post-Doctoral Fellow, NTU" — he graduated in 2018 and
      is already on the alumni page. Remove from current members?
- [ ] Luís Morgado da Costa listed as "Ph.D. Student, NTU" — likely graduated by now.
      Move to alumni?
- [ ] Chow Siew Yeng listed as "M.A. Student" — likely graduated. Move to alumni?
- [ ] Tommaso Petrolito listed as "M.A. Student, Università di Pisa" — likely graduated.
      Move to alumni?
- [ ] **Add any current lab members** (students, postdocs, collaborators at UPOL/EdUHK)

### Alumni Page (`alumni.html`)
- [ ] Move graduated members from members page to alumni
- [ ] Update positions/affiliations of existing alumni if known
- [ ] Add Luís Morgado da Costa (if graduated)
- [ ] Add any other graduates since 2019

### Publications (`pubs.html`)
- [ ] Last publication listed is 2021 — add publications from 2022–2026
- [ ] Two broken PDF links (marked with `href="#"`):
  - Liling Tan (2011) FYP — `2011-fyp-tan-liling.pdf` missing
  - Yamada et al. (2011) — `2011-ipsj-wiki.pdf` missing (had FIXME in original)

### Courses (`courses.html`)
- [ ] Most recent semester listed is AY21/22 Sem 1 — add subsequent semesters
- [ ] Still has `<base href="http://compling.hss.ntu.edu.sg/">` references in course
      links (removed from head but some relative links like `courses/hg2051/` may
      be broken since they were relative to that base URL)
- [ ] If no longer teaching at NTU, note which courses are historical vs. current

### Theses (`theses.html`)
- [ ] Most recent theses are from 2019 — add any theses from 2020–2026
- [ ] Luís Morgado da Costa's PhD thesis (if completed)

### Events (`events.html`)
- [ ] Most recent event is from 2020 — add events from 2020–2026

### Projects (`projects.html`)
- [ ] "Current" project is from NTU era — update current projects
- [ ] Move completed NTU projects to "Finished"
- [ ] Add any new projects at UPOL/EdUHK

## Medium Priority - Broken/Outdated Links

### Sidebar "Current Research" Links (now on index.html)
- [ ] `http://compling.hss.ntu.edu.sg/omw/` — likely dead (NTU server).
      OMW has moved to https://omwn.org/
- [ ] `http://compling.hss.ntu.edu.sg/wnja/index.en.html` — likely dead.
      Japanese Wordnet may have a new URL (bond-lab.github.io/wnja/)
- [ ] `http://compling.hss.ntu.edu.sg/ntumc/` — likely dead (NTU Multilingual Corpus)
- [ ] `http://mow.nonochnein.com/` — Myanmar Open Wordnet, check if still live
- [ ] `http://wn-msa.sourceforge.net/` — Wordnet Bahasa, check if still live
- [ ] `http://www.delph-in.net/jacy/` — check if still live
- [ ] `http://moin.delph-in.net/ZhongTop` — check if still live
- [ ] `http://moin.delph-in.net/IndraTop` — check if still live

### Links Page (`links.html`)
- [ ] `http://blogs.ntu.edu.sg/chriskhoo/nlp/` — may be dead
- [ ] `http://ucri.nict.go.jp/en/index.html` — may have moved
- [ ] `http://www.kecl.ntt.co.jp/icl/lirg/index.html` — may have moved
- [ ] NTU-specific section may need updating if lab is no longer at NTU

### General Link Issues
- [ ] Many links use `http://` — should be updated to `https://` where available
- [ ] `http://www.soh.ntu.edu.sg/Programmes/linguistics/Pages/Home.aspx` appears
      on many pages — check if still valid
- [ ] Various event subpages in `events/` link to external sites that may be dead

## Low Priority - Cosmetic/Structural

### Group Photos
- [ ] Most recent group photo is from 2016 — add newer photos if available

### Event/Project Subpages
- [ ] The standalone pages in `events/` and `projects/` are not yet Flask templates —
      they're copied as-is to `docs/`. Consider converting them or leaving as-is.

### GitHub Pages Configuration
- [ ] Configure GitHub Pages to serve from `docs/` directory instead of repo root
      (Settings → Pages → Source → `docs/` folder)

### General Cleanup
- [ ] `news.html` and `doc.html` in repo root are OMW pages, not lab pages —
      decide if they should stay, be moved, or removed
- [ ] The old HTML files in the repo root (index.html, members.html, etc.) can be
      removed once the flask-port branch is merged and GitHub Pages points to `docs/`
- [ ] Old `static/` directory at repo root (clg.css, clg.js) can be removed
- [ ] Old `images/` and `pdf/` directories at repo root can be removed
      (now in `web/static/img/` and `web/static/pdf/`)
