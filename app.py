from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Proposal Class Definition
class Proposal:
    def __init__(self, name, age, income, medical_history):
        self.name = name
        self.age = age
        self.income = income
        self.medical_history = [condition.strip().lower() for condition in medical_history]

    def evaluate(self):
        reasons = []  # List to store rejection reasons

        # Check age
        if self.age < 18 or self.age > 60:
            reasons.append("Age not within the acceptable range.")

        # Check income
        if self.income < 30000:
            reasons.append("Income below minimum threshold.")

        # Check medical conditions
        unacceptable_conditions = ["cancer", "heart disease", "stroke"]
        if any(condition in self.medical_history for condition in unacceptable_conditions):
            reasons.append("Medical history contains unacceptable conditions.")

        if reasons:  # If any rejection reasons were found
            return "Proposal Rejected: \n" + "\n".join(reasons)
        else:
            return "Proposal Accepted: All conditions met."

# API endpoint to evaluate the proposal
@app.route('/evaluate_proposal', methods=['POST'])
def evaluate_proposal():
    try:
        data = request.get_json()

        if not data or not all(k in data for k in ['name', 'age', 'salary', 'health_condition']):
            return jsonify({'error': 'Missing required fields: name, age, salary, health_condition'}), 400

        name = data.get('name')
        age = int(data.get('age'))
        salary = int(data.get('salary'))
        health_condition = data.get('health_condition')

        medical_history = [health_condition.lower()]

        proposal = Proposal(name, age, salary, medical_history)
        decision = proposal.evaluate()

        
       # Add hyphens and replace newlines with HTML line breaks
        if "Rejected:" in decision:
            reasons = decision.split("Rejected:")[1].split('\n')
            formatted_reasons = ["- " + reason.strip() for reason in reasons if reason.strip()] #add hyphens and remove empty lines
            decision = "Proposal Rejected:<br>" + "<br>".join(formatted_reasons)
        
        return jsonify({'decision': decision})

    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)