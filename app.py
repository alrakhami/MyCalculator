import os
import logging
from flask import Flask, render_template, request

app = Flask(__name__)

# Create a folder for logs if it doesn't exist
logs_folder = 'App_logs'
os.makedirs(logs_folder, exist_ok=True)

# Configure logging to save logs in the App_logs folder
log_file = os.path.join(logs_folder, 'app.log')
logging.basicConfig(filename=log_file, level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        try:
            num1 = int(request.form['num1'])
            num2 = int(request.form['num2'])
            result = num1 - num2
            app.logger.info(f"Performed subtraction: {num1} - {num2} = {result}")
            return f"Result: {num1} - {num2} = {result}"
        except ValueError as e:
            app.logger.error(f"ValueError: {e}")
            return "Please enter valid integers."

#   return '''
#       <form method="POST">
#            <label for="num1">Enter the first number:</label>
#            <input type="text" name="num1" id="num1">
#            <br>
#            <label for="num2">Enter the second number:</label>
#            <input type="text" name="num2" id="num2">
#            <br>
#            <input type="submit" value="Subtract">
#        </form>
#    '''

    return render_template('index.html')
if __name__ == '__main__':
    app.run(debug=True)
