from flask import Flask, request, redirect, url_for, render_template
import json

app = Flask(__name__)

# Load contacts from file
def load_contacts():
    try:
        with open("contacts.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

# Save contacts to file
def save_contacts(contacts):
    with open("contacts.json", "w") as file:
        json.dump(contacts, file)

contacts = load_contacts()

@app.route('/')
def index():
    return render_template('index.html', contacts=contacts)

@app.route('/add', methods=['POST'])
def add_contact():
    name = request.form.get('name')
    phone = request.form.get('phone')
    email = request.form.get('email')
    address = request.form.get('address')
    if name and phone:
        contacts.append({'name': name, 'phone': phone, 'email': email, 'address': address})
        save_contacts(contacts)
    return redirect(url_for('index'))

@app.route('/delete/<int:index>', methods=['POST'])
def delete_contact(index):
    if 0 <= index < len(contacts):
        contacts.pop(index)
        save_contacts(contacts)
    return redirect(url_for('index'))

@app.route('/update/<int:index>', methods=['POST'])
def update_contact(index):
    if 0 <= index < len(contacts):
        name = request.form.get('name')
        phone = request.form.get('phone')
        email = request.form.get('email')
        address = request.form.get('address')
        if name and phone:
            contacts[index] = {'name': name, 'phone': phone, 'email': email, 'address': address}
            save_contacts(contacts)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
