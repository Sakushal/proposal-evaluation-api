from flask import Flask, request, jsonify
from flask_cors import CORS
import re

app = Flask(__name__)
CORS(app)

class Proposal:
    def __init__(self, name, age, income, medical_history, plan):
        self.name = name
        self.age = age
        self.income = income
        self.medical_history = [condition.strip().lower() for condition in medical_history]
        self.plan = plan

    def evaluate(self):
        reasons = []
        unacceptable_conditions = ["cancer", "heart disease", "stroke"]

        if self.plan == '1':
            if self.age < 18 or self.age > 60:
                reasons.append("Age not within the acceptable range for Plan 1.")
            if self.income < 30000:
                reasons.append("Income below minimum threshold for Plan 1.")
        elif self.plan == '2':
            if self.age < 28 or self.age > 60:
                reasons.append("Age not within the acceptable range for Plan 2.")
            if self.income < 50000:
                reasons.append("Income below minimum threshold for Plan 2.")
        elif self.plan == '3':
            if self.age < 25 or self.age > 55:
                reasons.append("Age not within the acceptable range for Plan 3.")
            if self.income < 70000:
                reasons.append("Income below minimum threshold for Plan 3.")
        else:
            reasons.append("Invalid Plan Selection.")

        if any(condition in self.medical_history for condition in unacceptable_conditions):
            reasons.append("Medical history contains unacceptable conditions.")

        if reasons:
            return "Proposal Rejected: \n" + "\n".join(reasons)
        else:
            return "Proposal Accepted: All conditions met."

@app.route('/evaluate_proposal', methods=['POST'])
def evaluate_proposal():
    try:
        data = request.get_json()

        if not data or not all(k in data for k in ['name', 'age', 'salary', 'health_condition', 'plan']):
            return jsonify({'error': 'Missing required fields: name, age, salary, health_condition, plan'}), 400

        name = data.get('name')
        age = data.get('age')
        salary = data.get('salary')
        health_condition = data.get('health_condition')
        plan = data.get('plan')

        if not isinstance(name, str) or not re.match(r'^[a-zA-Z\s]+$', name):
            return jsonify({'error': 'Invalid name format. Only letters and spaces are allowed.'}), 400

        try:
            age = int(age)
            salary = int(salary)
        except ValueError:
            return jsonify({'error': 'Age and salary must be integers.'}), 400

        if age < 0 or salary < 0:
            return jsonify({'error': 'Age and salary must be non-negative.'}), 400

        if not isinstance(health_condition, str) or not re.match(r'^[a-zA-Z\s,]*$', health_condition):
            return jsonify({'error': 'Invalid health condition format. Only letters, spaces, and commas are allowed.'}), 400

        medical_history = [cond.strip().lower() for cond in health_condition.split(',') if cond.strip()]

        proposal = Proposal(name, age, salary, medical_history, plan)
        decision = proposal.evaluate()

        if "Rejected:" in decision:
            reasons = decision.split("Rejected:")[1].split('\n')
            formatted_reasons = ["- " + reason.strip() for reason in reasons if reason.strip()]
            decision = "Proposal Rejected:<br>" + "<br>".join(formatted_reasons)

        return jsonify({'decision': decision})

    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)