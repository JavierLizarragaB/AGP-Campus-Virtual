from random import sample, shuffle
from flask import render_template, request, jsonify

from . import api
from ..models import MultipleChoiceQuestion, QUESTION_TOPICS

# Reposnds with HTML for the flashed messages
@api.route("/flashed-messages", methods=["POST"])
def flashed_messages():
    # TODO: remove this test
    return render_template("_flash.html")
"""
QUESTION_TOPICS = (
    "tstc", # Cancer testicular
    "crvu", # Cancer cervicouterino
    "plmn", # Cancer en pulmon
    "psta", # Cancer en prostata
    "mama", # Cancer de mama
    "diag"  # Examen diagnostico
)
"""



"""
{
    "quiz_topic": "tstc",
    "num_questions": 4
}

"""

DEFAULT_QUIZ_TOPIC = "diag"
DEFAULT_NUM_QUESTIONS = 3


# Responds with JSON for random quiz given the topic code and number of questions
@api.route("/generate-quiz", methods=["GET"])
def generate_quiz():
    
    # Validate the quiz topic
    quiz_topic = request.args.get("topic", DEFAULT_QUIZ_TOPIC)
    if quiz_topic not in QUESTION_TOPICS:
        quiz_topic = DEFAULT_QUIZ_TOPIC

    # Get the number of questions
    num_questions = request.args.get("num_questions", DEFAULT_NUM_QUESTIONS)
    num_questions = int(num_questions)

    # Sample the database
    db_questions = MultipleChoiceQuestion.objects(topic=quiz_topic)
    total_num_db_questions = db_questions.count()

    # Generate the sample indexes for the db entries    
    sample_indexes = []
    if num_questions >= total_num_db_questions:
        # More entires are demanded, return all of them
        sample_indexes = [i for i in  range(total_num_db_questions)]
        shuffle(sample_indexes)
    else:
        # Valid number of entries asked
        sample_indexes = sample(range(total_num_db_questions), num_questions)
    
    questions = []
    for i in sample_indexes:
        questions.append(db_questions[i].to_json())

    return  jsonify(questions)