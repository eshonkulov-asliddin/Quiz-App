
from django.shortcuts import render, redirect
from .models import Subject, Quiz
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from .forms import AnswerOptionsForm
from .models import QuizInstance
from django.contrib.auth.decorators import login_required
from .forms import QuizInstanceForm, CreateSubjectForm, CreateQuestionForm

# Create your views here.
def homePage(request):
    return render(request, 'home.html')

def quizCard(request):
    form = QuizInstanceForm()
    subjects = Subject.objects.all()     
    # exam = QuizInstance.objects.get(id=request.user.id)
    context = {'subjects': subjects, 'form':form}
    return render(request, 'quiz-card.html', context)    

@login_required(login_url='sign-in')
def getQuestion(request, id): 
    subject = Subject.objects.get(id=id)
    form = AnswerOptionsForm()
    obj = subject.quiz_set.all()
    p = Paginator(obj, 1)
    submitted = False
    try:
        page = int(request.GET.get('page', '1'))
    except:
        page = 1
    try:
        questions = p.page(page)

    except(EmptyPage, InvalidPage):
        return redirect('result', int(subject.id))
       
        
    # print(p.num_pages)
    if request.method == 'POST':
        submitted = True
        question = questions.object_list[0]
        currentQuestion = Quiz.objects.get(question=question)
        currentQuestion.submitted = True
        ans = request.POST.get('options')
        if currentQuestion.answer == ans:
            exam_taker = QuizInstance.objects.get_or_create(taker=request.user.username, quiz=subject.name)[0]
            exam_taker.score += 1
            exam_taker.save()
        
    context = {'obj': obj, 'questions': questions, 'page':page, 'form': form, 'submitted': submitted, 'subject': subject}
    return render(request, 'questions.html', context)    

@login_required(login_url='sign-in')
def result(request, id):
    user = request.user.useraccount
    subject = Subject.objects.get(id=id)
    number_of_questions = len(subject.quiz_set.all())
    user.completed_subject.add(subject)
    user.save()
    exam = QuizInstance.objects.get(
            taker=request.user.username,
            quiz=subject,
        )    
    exam.complete = True
    exam.save()
    wrongAnswer = number_of_questions-exam.score
    context = {'user': user, 'subject': subject, 'correctAnswer': exam.score, 'wrongAnswer': wrongAnswer}
    return render(request, 'result.html', context)


@login_required(login_url='sign-in')
def retakeQuiz(request, id):
    subject = Subject.objects.get(id=id)
    exam_taker = QuizInstance.objects.get(
            taker=request.user.username,
            quiz=subject,
        )
    exam_taker.score = 0
    exam_taker.save()
    
    return redirect('question', id)

def createQuiz(request):
    form = CreateSubjectForm()

    if request.method == 'POST':
        form = CreateSubjectForm(request.POST, request.FILES)
        if form.is_valid:
            numberOfquestion = request.POST['numberOfquestion']
            
            subject = form.save()
        
            return redirect('create-question', numberOfquestion, subject)
    context = {'form': form}
    return render(request, 'quiz/create_quiz.html', context)

def createQuestion(request, num, subject):
    form = CreateQuestionForm()
    subjectInstance = Subject.objects.get(name=subject)
    if request.method == 'POST':
        for i in range(num):
            form = CreateQuestionForm(request.POST)
            if form.is_valid():
                question = form.save(commit=False)
                question.subject = subjectInstance
                question.save()
        return redirect('quiz-card')        

    context = {'form': form, 'n': range(num)}
    return render(request, 'quiz/create_question.html', context)
