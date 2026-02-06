"""Route declaration."""
from flask import current_app as app
from flask import render_template

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

@app.route("/")
def home():
    """show the home page"""
    return show('index')
