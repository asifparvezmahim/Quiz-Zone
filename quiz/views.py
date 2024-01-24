from django.shortcuts import render
from django.http import HttpResponse
from category.models import Category
from .models import Question, UserSubmittedAnswer


# Create your views here.


def showCat(request):
    cat_data = Category.objects.all()
    t = Category.objects.all().count()
    print(t)
    return render(request, "topic_selection.html", {"data": cat_data})  #


def cat_questions(request, cat_id):
    x = UserSubmittedAnswer.objects.filter(user=request.user).delete()
    # category = Category.objects.all()
    cat = Category.objects.get(id=cat_id)
    question = Question.objects.filter(category=cat).order_by("id").first()
    # means id er respect e dec. order e sajiye first question pick korlam
    return render(request, "exam_page.html", {"question": question, "category": cat})


def submit_form(request, cat_id, quest_id):
    if request.method == "POST":
        cat = Category.objects.get(id=cat_id)
        question = (
            Question.objects.filter(category=cat, id__gt=quest_id)
            .exclude(id=quest_id)
            .order_by("id")
            .first()
        )

        # After Clicking Submit Butti=on
        quest = Question.objects.get(id=quest_id)
        user = request.user
        answer = request.POST["answer"]
        UserSubmittedAnswer.objects.create(
            user=user, question=quest, given_answer=answer
        )
        if (
            question
        ):  # jodi previous question efr por r o question thake taile segulo dekhabo
            print("Line 71")
            return render(
                request, "exam_page.html", {"question": question, "category": cat}
            )

        else:
            result = UserSubmittedAnswer.objects.filter(user=request.user)
            skipped = UserSubmittedAnswer.objects.filter(
                user=request.user, given_answer="Not Submitted"
            ).count()

            rightAnswer = 0
            wrongAnswer = 0
            for row in result:
                if row.question.right_answer == row.given_answer:
                    rightAnswer = rightAnswer + 1
                else:
                    wrongAnswer = wrongAnswer + 1
            percentage = (rightAnswer / (rightAnswer + wrongAnswer)) * 100
            return render(
                request,
                "result.html",
                {
                    "result": result,
                    "skipped": skipped,
                    "rightAnswer": rightAnswer,
                    "wrongAnswer": wrongAnswer,
                    "percentage": percentage,
                },
            )
    else:
        return HttpResponse("Method is not Allowed")


def result_history(request):
    result = UserSubmittedAnswer.objects.filter(user=request.user)
    return render(request, "result.html", {"result": result})


def delete_result_history(request):
    result = UserSubmittedAnswer.objects.filter(user=request.user).delete()
    return render(request, "result.html", {"result": result})


# def showQuiz (request):
