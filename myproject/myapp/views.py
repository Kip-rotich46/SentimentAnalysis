# sentimentanalysis/views.py

from django.shortcuts import render
from .models import UserInput
from transformers import pipeline

# Load the sentiment analysis model
sentiment_analysis = pipeline("sentiment-analysis")


def home(request):
    print("Home view accessed.")
    if request.method == "POST":
        text = request.POST.get("user_input", "")
        print(f"Received text: {text}")

        # Perform sentiment analysis using BERT-based model
        result = sentiment_analysis(text)[0]
        predicted_sentiment = result["label"]

        # Save user input and predicted sentiment to the database
        UserInput.objects.create(text=text, sentiment=predicted_sentiment)

    # Fetch recent user inputs from the database
    recent_user_inputs = UserInput.objects.all().order_by("-id")[:5]

    context = {"recent_user_inputs": recent_user_inputs}
    return render(request, "home.html", context)
