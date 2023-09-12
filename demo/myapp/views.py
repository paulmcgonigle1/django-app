from django.shortcuts import render, HttpResponse
from .models import TodoItem
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views import View
from .utils.langchainmethods import (
    get_conversation_chain,
    get_pdf_text,
    get_text_chunks,
    get_vectorstore,
)
import uuid

# Create your views here.


def home(request):
    return render(request, "home.html")


def todos(request):
    items = TodoItem.objects.all()
    return render(request, "todos.html", {"todos": items})


class Process(View):
    @csrf_exempt
    def post(self, request):
        session_id = str(uuid.uuid4())
        # Returning a dummy session_id for testing
        return JsonResponse({"session_id": session_id}, status=200)


class ReturnDummy(View):
    @csrf_exempt
    def post(self, request):
        # Returning a dummy answer for testing
        return JsonResponse(
            {"answer": "This is a dummy answer for testing purposes."}, status=200
        )
