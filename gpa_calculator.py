from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        print(request.form)  # This will show the submitted form data
        try:
            num_courses = int(request.form['num_courses'])
            total_points = 0
            total_credit_hours = 0

            for i in range(num_courses):
                GP = request.form[f'grade_{i}'].upper()
                CH = int(request.form[f'credit_hours_{i}'])

                # Calculate points based on the grade
                if GP == "A":
                    points = 4.0 * CH
                elif GP == "A-":
                    points = 3.67 * CH
                elif GP == "B+":
                    points = 3.33 * CH
                elif GP == "B":
                    points = 3.0 * CH
                elif GP == "B-":
                    points = 2.67 * CH
                elif GP == "C+":
                    points = 2.33 * CH
                elif GP == "C":
                    points = 2.0 * CH
                elif GP == "C-":
                    points = 1.67 * CH
                elif GP == "D+":
                    points = 1.33 * CH
                elif GP == "D":
                    points = 1.0 * CH
                elif GP == "F":
                    points = 0 * CH
                else:
                    return "Invalid grade entered. Please enter a valid grade."

                total_points += points
                total_credit_hours += CH

            # Formula for GPA
            GPA = total_points / total_credit_hours if total_credit_hours > 0 else 0
            return render_template('result.html', gpa=GPA)

        except Exception as e:
            return f"An error occurred: {e}"

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
