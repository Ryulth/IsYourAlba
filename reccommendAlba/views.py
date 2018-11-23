from django.shortcuts import render, get_object_or_404, redirect
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import Profile, OHaeng
from .MBTIdescription import types
from django.views.decorators.csrf import csrf_protect

def test(request):
    return render(request, 'reccommendAlba/test.html')


def index(request):
    if request.method == "POST":
        profiles = Profile.objects.filter(username=request.POST.get('username'))
        if len(profiles) == 0:
            profile = Profile()
            profile.username = request.POST.get('username')
            tmp_date = request.POST.get('birth_date')
            profile.gender = request.POST.get('gender')

            date = tmp_date.split('/')
            date_string = date[0] + date[1] + date[2]
            profile.birth_date = date_string
            profile.save()
            # return HttpResponseRedirect(reverse('test_EI', args=profile.username))
            return render(request, 'reccommendAlba/test_EI.html', {'username': profile.username})
        else:
            profile = profiles[0]
            usertype = profile.type_EI + profile.type_SN + profile.type_TF + profile.type_JP
            ohaengs = OHaeng.objects.filter(birth_date=profile.birth_date)
            if len(ohaengs) == 0:
                ohaeng = OHaeng.objects.get(birth_date="19181115")
            else:
                ohaeng = ohaengs[0]
            MBTI_description = types[usertype].__str__()
            return render(request, 'reccommendAlba/result.html',
                          {'profile': profile, 'description': MBTI_description, 'ohaeng': ohaeng})
    elif request.method == "GET":
        return render(request, 'reccommendAlba/index.html')


def test_EI(request, username):
    print(username)
    profiles = Profile.objects.filter(username=username)
    profile = profiles[0]

    num_E = 0
    for i in range(6):
        question_num = "Q{}".format(i + 1)
        if request.POST.get(question_num) == question_num + "_E":
            num_E += 1

    num_I = 6 - num_E

    if num_E >= 3:
        profile.type_EI = "E"
    else:
        profile.type_EI = "I"

    profile.num_E = num_E
    profile.num_I = num_I

    profile.save()
    return render(request, 'reccommendAlba/test_SN.html', {'username': profile.username})


def test_SN(request, username):
    print(username)
    profiles = Profile.objects.filter(username=username)
    profile = profiles[0]

    num_N = 0
    for i in range(6, 12):
        question_num = "Q{}".format(i + 1)
        if request.POST.get(question_num) == question_num + "_N":
            num_N += 1

    if num_N >= 3:
        profile.type_SN = "N"
    else:
        profile.type_SN = "S"

    num_S = 6 - num_N

    profile.num_N = num_N
    profile.num_S = num_S

    profile.save()
    return render(request, 'reccommendAlba/test_TF.html', {'username': profile.username})


def test_TF(request, username):
    print(username)
    profiles = Profile.objects.filter(username=username)
    profile = profiles[0]

    num_F = 0
    for i in range(12, 18):
        question_num = "Q{}".format(i + 1)
        if request.POST.get(question_num) == question_num + "_F":
            num_F += 1

    num_T = 6 - num_F

    if num_F >= 3:
        profile.type_TF = "F"
    else:
        profile.type_TF = "T"

    profile.num_F = num_F
    profile.num_T = num_T

    profile.save()
    return render(request, 'reccommendAlba/test_JP.html', {'username': profile.username})


def test_JP(request, username):
    print(username)
    profiles = Profile.objects.filter(username=username)
    profile = profiles[0]

    num_P = 0
    for i in range(18, 24):
        question_num = "Q{}".format(i + 1)
        if request.POST.get(question_num) == question_num + "_P":
            num_P += 1

    num_J = 6 - num_P

    if num_P >= 3:
        profile.type_JP = "P"
    else:
        profile.type_JP = "J"

    profile.num_P = num_P
    profile.num_J = num_J
    profile.save()

    usertype = profile.type_EI + profile.type_SN + profile.type_TF + profile.type_JP
    ohaengs = OHaeng.objects.filter(birth_date=profile.birth_date)
    if len(ohaengs) == 0:
        ohaeng = OHaeng.objects.get(birth_date="19181115")
    else:
        ohaeng = ohaengs[0]
    MBTI_description = types[usertype].__str__()

    """
    BELOW
    

    model2 = torch.load('saved_model')

    input_ = [ohaeng.tree, ohaeng.fire, ohaeng.soil, ohaeng.metal, ohaeng.water, profile.num_E, profile.num_I,
              profile.num_S,
              profile.num_N, profile.num_T, profile.num_F, profile.num_J, profile.num_P]
    input_ = np.array(input_, dtype=np.float32)
    input_ = Variable(torch.from_numpy(input_))

    output = model2(input_)
    output = output.view(-1)
    list = [i[0] for i in sorted(enumerate(output), key=lambda x: x[1], reverse=True)]
    pos_list = sorted(output, reverse=True)
    sum_ = sum(pos_list)

    # 레이블 vocab 만들기
    file = open('./vocabulary.txt', 'r', encoding='euc-kr')
    labels = []
    while True:
        line = file.readline()
        line = line[:-1]
        if not line: break
        labels.append(line)
    vocab = set()
    vocab_label = np.array(labels)
    vocab.update()
    label_vocab = {word: i for i, word in enumerate(vocab)}

    # 내림차순한 직업 순서
    job_list_ = []
    for num in list:
        a = [name for name, age in label_vocab.items() if age == num]
        job_list_.append(a[0])

    # 정규화한 확률
    pos_list_ = []
    for num in pos_list:
        pos_list_.append(num / sum_)
        """

    return render(request, 'reccommendAlba/result.html',
                  {'profile': profile, 'description': MBTI_description, 'ohaeng': ohaeng})
