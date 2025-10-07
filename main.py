from dashboard.app import app
from dashboard.layouts.main_layout import layout

app.layout = layout

if __name__ == '__main__':
    app.run(debug=True)