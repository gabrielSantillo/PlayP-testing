from flask import Flask
from flask_cors import CORS
from dbcreds import production_mode

# calling the Flask function which will return a value that will be used in my API
app = Flask(__name__)
CORS(app)


############## We put all endpoints here ##############

#######################################################
# Endpoint example
# @app.post('/api/consultant')
# def post_consultant():
#    return endpoints.consultant.post()



# if statement to check if the production_mode variable is true, if yes, run in production mode, if not, run in testing mode
if (production_mode):
    print("Running in Production Mode")
    import bjoern  # type: ignore
    bjoern.run(app, "0.0.0.0", 5010)
else:
    from flask_cors import CORS
    CORS(app)
    print("Running in Testing Mode")
    app.run(debug=True)