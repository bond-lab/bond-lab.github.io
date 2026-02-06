from web import create_app

app = create_app()
app.config.from_pyfile('settings.py')

if __name__ == '__main__':
    app.run(debug=True)
