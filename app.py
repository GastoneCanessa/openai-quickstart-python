import os
from query import Query
from service import insert_generation, get_generations, create_connection
from pypika import Table, Field, Column


import openai
from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)
openai.api_key = os.getenv("OPENAI_API_KEY")
data = {}


@app.route("/", methods=("GET", "POST"))
def index():
    if request.method == "POST":
        animal = request.form["animal"]
        data['prompt'] = animal
        response = openai.Completion.create(
            model="text-davinci-002",
            prompt=generate_prompt(animal),
            temperature=0.6,
        )

        data['output'] = response.choices[0].text
        # print(data)
        generations = Table('generations')
        create_generations = Query.insert_dict(generations, data)
        # print(create_generations)
        insert_generation(create_generations)
        get_generations()


        return redirect(url_for("index", result=response.choices[0].text))

    result = request.args.get("result")
    return render_template("index.html", result=result)


def generate_prompt(animal):
    return """Suggest three names for an animal that is a superhero.

Animal: sea
Names: surf , boat , kayak
Animal: land
Names: car, truck, motorbike
Animal: {}
Names:""".format(
        animal.capitalize()
    )
