"""Route declaration."""
import os

from flask import current_app as app
from flask import render_template

from .bib2html import load_bibliography, render_bibliography

# Load and render the lab bibliography once at startup. Lab membership is
# recorded per entry with a `lab` field rather than inferred from authors,
# so papers by lab members without Francis Bond are included too.
_BIB_DIR = os.path.join(os.path.dirname(__file__), 'static', 'bib')
_BIB_ENTRIES = load_bibliography(
    os.path.join(_BIB_DIR, 'abb.bib'),
    os.path.join(_BIB_DIR, 'mtg.bib'),
    os.path.join(_BIB_DIR, 'talks.bib'),
)
_BIB_HTML = render_bibliography(_BIB_ENTRIES, lab_filter=('ntu', 'upol'))

nav = {
    'index': {"name": "Home",
              'desc': "Computational Linguistics Lab"},
    'events': {"name": "News & Events",
               'desc': "News and events from the CL Lab"},
    'members': {"name": "Members",
                'desc': "Current members of the CL Lab"},
    'alumni': {"name": "Alumni",
               'desc': "Former members of the CL Lab"},
    'pubs': {"name": "Publications",
             'desc': "Publications from the CL Lab"},
    'theses': {"name": "Theses",
               'desc': "Theses and URECA projects from the CL Lab"},
    'projects': {"name": "Projects",
                 'desc': "Funded projects from the CL Lab"},
    'courses': {"name": "Courses",
                'desc': "Courses related to Computational Linguistics"},
    'links': {"name": "Links",
              'desc': "Related sites and collaborators"},
    'contact': {"name": "Contact",
                'desc': "Contact information for the CL Lab"},
}


@app.route("/<page>.html")
def show(page):
    """Show a page"""
    return render_template(
        f"{page}.html",
        page=page,
        nav=nav,
        title=nav[page]['name'],
        description=nav[page]['desc'],
    )

@app.route("/pubs.html")
def pubs():
    """Publications page (generated from BibTeX)."""
    return render_template(
        'pubs.html',
        page='pubs',
        nav=nav,
        title=nav['pubs']['name'],
        description=nav['pubs']['desc'],
        bib_html=_BIB_HTML,
    )


@app.route("/")
def home():
    """show the home page"""
    return show('index')
