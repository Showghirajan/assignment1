from django.shortcuts import render
from app1.forms import InputForm

def home(request):
    combinations = []
    if request.method == "POST":
        form = InputForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            input_word = data.get("input_word")
            # Generate all possible combinations manually
            combinations = generate_combinations(input_word)
            return render(request, "app1/index.html", {'combinations': combinations, 'form': form})
    else:
        form = InputForm()
    return render(request, "app1/index.html", {'form': form})

def generate_combinations(word):
    # Assuming word has exactly 3 characters
    a, b, c = word
    combinations = [
        a + b + c,
        a + c + b,
        b + a + c,
        b + c + a,
        c + a + b,
        c + b + a,
    ]
    return combinations
