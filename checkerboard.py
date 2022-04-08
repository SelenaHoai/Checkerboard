from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
@app.route('/<int:column>')
@app.route('/<int:column>/<int:row>')
@app.route('/<int:column>/<int:row>/<string:columncolor>/<string:rowcolor>')
def cookie_function2(columncolor="red", rowcolor="blue", column=4, row=4):
    return render_template('index.html', columncolor=columncolor, rowcolor=rowcolor, column=column, row=row)


if __name__ == "__main__":
    app.run(debug=True)
