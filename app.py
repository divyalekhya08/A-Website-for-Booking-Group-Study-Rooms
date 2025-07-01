from flask import Flask, render_template, request, redirect

app = Flask(__name__)
bookings = []

@app.route('/')
def index():
    return render_template('index.html', bookings=bookings)

@app.route('/book', methods=['POST'])
def book():
    name = request.form['name']
    room = request.form['room']
    date = request.form['date']
    time = request.form['time']

    for b in bookings:
        if b['room'] == room and b['date'] == date and b['time'] == time:
            return "Slot already booked. <a href='/'>Go back</a>"

    bookings.append({'name': name, 'room': room, 'date': date, 'time': time})
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
