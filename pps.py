from flask import Flask, render_template, request
import csv

app = Flask(__name__)

class VaccinationSystem:
    def __init__(self):
        self.users = []

    def add_user(self, name, age, city):
        vaccine = 'None'
        if city.lower() == 'mumbai':
            vaccine = 'v1' if age < 15 else 'v2'
        elif city.lower() == 'jaipur':
            vaccine = 'v3' if age < 15 else 'v4'
        self.users.append([name, age, city, vaccine])

    def save_to_csv(self):
        with open('data.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(self.users)

vaccination_system = VaccinationSystem()

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form.get('name')
        age = int(request.form.get('age'))
        city = request.form.get('city')
        vaccination_system.add_user(name, age, city)
        vaccination_system.save_to_csv()
    return render_template('index.html', users=vaccination_system.users)

if __name__ == '__main__':
    app.run(debug=True)
