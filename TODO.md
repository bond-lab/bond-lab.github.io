# Bond Lab Website - Content Update TODO

Items to update now that the site has been ported to frozen-flask.
Updated: 2026-02-06

## Completed ✓

### Affiliation / Identity
- [x] Rebranded to "Computational Linguistics Lab" (UPOL)
- [x] Updated `index.html` description with UPOL affiliation
- [x] Updated `contact.html` with new contact info (email, GitHub, affiliations)
- [x] Navigation footer updated with UPOL address

### Members Page (`members.html`)
- [x] Francis Bond updated to Extraordinary Professor at UPOL
- [x] Added Joanna Sio (Docent, UPOL)
- [x] Added Ivona Barešová (Docent, UPOL)
- [x] Moved Luís, Siew Yeng, Tommaso to alumni
- [x] Removed Michael Goodman (now in alumni)

### Alumni Page (`alumni.html`)
- [x] Converted from tables to Bootstrap grid
- [x] Fixed broken links (Wang Shan, Jim Breen, Lê Tuấn Anh, Hannah Choi)
- [x] Updated positions (Wang Shan, Song Sanghoun to Associate Professor)
- [x] Added Michael Goodman as alumni (Software Engineer at Xero)
- [x] Added Elvis Bin Toni Google Scholar link
- [x] Reversed order (most recent first)
- [x] Added graduates: Siew Yeng (2022), Luis (2022), Tommaso (2021), Yoshioka Haruka (2023)

### Publications (`pubs.html`)
- [x] Added publications from 2022–2026 (15 new entries)

### Theses (`theses.html`)
- [x] Added 2021 section (Tommaso Petrolito)
- [x] Added 2022 section (Chow Siew Yeng, Luís Morgado da Costa)
- [x] Added 2023 section (Yoshioka Haruka)
- [x] Updated intro text to mention both UPOL and NTU

### Infrastructure
- [x] Ported site to frozen-flask
- [x] GitHub Pages configured for `docs/` directory
- [x] Old root-level HTML files removed
- [x] Flask-port branch merged and deleted

## High Priority - Still TODO

### Courses (`courses.html`)
- [ ] Most recent semester listed is AY21/22 Sem 1 — add subsequent semesters
- [ ] Course links may be broken (were relative to NTU compling base URL)
- [ ] Note which courses are historical vs. current (if no longer teaching at NTU)

### Events (`events.html`)
- [ ] Most recent event is from 2020 — add events from 2020–2026

### Projects (`projects.html`)
- [ ] "Current" project is from NTU era — update current projects
- [ ] Move completed NTU projects to "Finished"
- [ ] Add any new projects at UPOL/EdUHK

## Medium Priority - Broken/Outdated Links

### Index Page "Current Research" Links
- [ ] `http://compling.hss.ntu.edu.sg/omw/` — OMW has moved to https://omwn.org/
- [ ] `http://compling.hss.ntu.edu.sg/wnja/index.en.html` — Japanese Wordnet, check URL
- [ ] `http://compling.hss.ntu.edu.sg/ntumc/` — NTU Multilingual Corpus, likely dead
- [ ] `http://mow.nonochnein.com/` — Myanmar Open Wordnet, check if still live
- [ ] `http://wn-msa.sourceforge.net/` — Wordnet Bahasa, check if still live
- [ ] DELPH-IN links — check if still live

### Links Page (`links.html`)
- [ ] `http://blogs.ntu.edu.sg/chriskhoo/nlp/` — may be dead
- [ ] `http://ucri.nict.go.jp/en/index.html` — may have moved
- [ ] `http://www.kecl.ntt.co.jp/icl/lirg/index.html` — may have moved
- [ ] NTU-specific section may need updating

### General Link Issues
- [ ] Many links use `http://` — should be updated to `https://` where available
- [ ] Various event subpages in `events/` link to external sites that may be dead

## Low Priority - Cosmetic/Structural

### Group Photos
- [ ] Most recent group photo is from 2016 — add newer photos if available

### Event/Project Subpages
- [ ] Standalone pages in `events/` and `projects/` are static HTML, not Flask templates

### Favicon
- [ ] Add favicon for the site

### General Cleanup
- [ ] `news.html` and `doc.html` in `docs/` are OMW pages — decide if they should stay
