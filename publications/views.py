from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .models import Publication
from django.utils import timezone
from django.db.models import Q
from django.views import View


class Home(View):
    template_name = 'publications/list.html'



def index(request):
    latest_pub_numbers = 15
    latest_pub_dict = Publication.objects.order_by('-pub_date').values()[:latest_pub_numbers]
    latest_publications = list()
    makes_and_models_mx = ['1', '1500', '2', '200', '2008', '208', '2500', '3', '300', '3008', '300c', '301', '308', '370z', '4', '4000', '4c', '5', '500', '5008', '500l', '6', '7', '700', '718', '911', 'a', 'a1', 'a3', 'a4', 'a5', 'a6', 'a7', 'a8', 'acadia', 'accent', 'accord', 'acura', 'adventure', 'alfa', 'altima', 'amarok', 'armada', 'arona', 'ateca', 'ats', 'attitude', 'audi', 'avanza', 'aveo', 'baic', 'beat', 'beetle', 'bentayga', 'bentley', 'bj20', 'bj40', 'bmw', 'bolt', 'boxster', 'br v', 'brv', 'br-v', 'brz', 'buick', 'c', 'c hr', 'cab', 'cabstar', 'caddy', 'cadillac', 'camaro', 'camry', 'captur', 'caravan', 'cavalier', 'cayenne', 'cayman', 'challenger', 'charger', 'cherokee', 'chevrolet', 'chevy', 'chr', 'c-hr', 'chrysler', 'ciaz', 'city', 'civic', 'cla', 'clase', 'cls', 'clubman', 'colorado', 'compass', 'continental', 'convertible', 'cooper', 'corolla', 'corvette', 'country', 'countryman', 'coupe', 'cr v', 'crafter', 'creta', 'crew', 'cross', 'crossfox', 'crossgolf', 'cruiser', 'cruze', 'crv', 'cr-v', 'cts', 'cx 3', 'cx 5', 'cx 9', 'cx3', 'cx-3', 'cx5', 'cx-5', 'cx9', 'cx-9', 'd20', 'discovery', 'dodge', 'ducato', 'durango', 'duster', 'e', 'e pace', 'ecosport', 'edge', 'elantra', 'elf', 'elf100', 'enclave', 'encore', 'envision', 'epace', 'e-pace', 'equinox', 'ertiga', 'escalade', 'escape', 'evoque', 'expedition', 'expert', 'explorer', 'express', 'f 150', 'f 250', 'f 350', 'f 450', 'f 550', 'f pace', 'f type', 'f150', 'f-150', 'f250', 'f-250', 'f350', 'f-350', 'f450', 'f-450', 'f550', 'f-550', 'fe', 'fiat', 'fiesta', 'figo', 'fit', 'flying', 'focus', 'ford', 'forester', 'forfour', 'forte', 'fortwo', 'fpace', 'f-pace', 'frontier', 'ftype', 'f-type', 'fusion', 'fx', 'g', 'g37', 'giulia', 'giulietta', 'gla', 'glc', 'gle', 'gls', 'gmc', 'gol', 'golf', 'grand', 'gt', 'gt r', 'gtr', 'gt-r', 'hatchback', 'hiace', 'highlander', 'hilux', 'honda', 'hr v', 'hrv', 'hr-v', 'hybrid', 'hyundai', 'i pace', 'i10', 'i3', 'i8', 'ibiza', 'ignis', 'ilx', 'impreza', 'infiniti', 'insight', 'interceptor', 'ioniq', 'ipace', 'i-pace', 'isuzu', 'jaguar', 'jeep', 'jetta', 'journey', 'juke', 'jx', 'kangoo', 'kia', 'kicks', 'koleos', 'l200', 'land', 'leaf', 'legacy', 'leon', 'lincoln', 'lobo', 'logan', 'macan', 'malibu', 'manager', 'march', 'maxima', 'mazda', 'mdx', 'mercedes amg', 'mercedes benz', 'mercedesamg', 'mercedes-amg', 'mercedesbenz', 'mercedes-benz', 'mini', 'mirage', 'mito', 'mitsubishi', 'mkc', 'mkx', 'mkz', 'mobi', 'montero', 'murano', 'mustang', 'mx 5', 'mx5', 'mx-5', 'navigator', 'neon', 'niro', 'nissan', 'notchback', 'note', 'np300', 'nsx', 'nv2500', 'odyssey', 'optima', 'oroch', 'outback', 'outlander', 'pacifica', 'palio', 'panamera', 'partner', 'passat', 'pathfinder', 'peugeot', 'pilot', 'police', 'polo', 'porsche', 'prius', 'promaster', 'q2', 'q3', 'q5', 'q50', 'q60', 'q7', 'q70', 'qx', 'qx30', 'qx50', 'qx60', 'qx70', 'qx80', 'r', 'r8', 'ram', 'range', 'ranger', 'rapid', 'rav4', 'rdx', 'regal', 'renault', 'renegade', 'rio', 'romeo', 'rover', 's', 's cross', 's10', 's60', 's90', 'sandero', 'santa', 'saveiro', 'scross', 's-cross', 'seat', 'sedan', 'sedan', 'sedona', 'sentra', 'sequoia', 'serie', 'sienna', 'sierra', 'silverado', 'slc', 'smart', 'sonata', 'sonic', 'sorento', 'soul', 'spark', 'sport', 'sport', 'sportage', 'sportback', 'sprinter', 'spur', 'spyder', 'st', 'starex', 'stelvio', 'stepway', 'sti', 'stinger', 'subaru', 'suburban', 'suzuki', 'swift', 'tacoma', 'tahoe', 'teramont', 'terrain', 'tiguan', 'tiida', 'tlx', 'toledo', 'tornado', 'touareg', 'toyota', 'transit', 'transporter', 'traverse', 'trax', 'tsuru', 'tt', 'tucson', 'tundra', 'turbo', 'twizy', 'uno', 'up!', 'urvan', 'v', 'v40', 'v6', 'variant', 'velar', 'vento', 'versa', 'vision', 'vitara', 'volkswagen', 'volt', 'volvo', 'wrangler', 'wrx', 'x trail', 'x1', 'x2', 'x25', 'x3', 'x35', 'x4', 'x5', 'x6', 'x65', 'xc40', 'xc60', 'xc90', 'xe', 'xf', 'xt4', 'xt5', 'xtrail', 'x-trail', 'xv', 'yaris', 'yukon', 'zoe', 'bora', 'xplorer', 'clasico', 'platina']
    for k in latest_pub_dict:
        all_tags_list = eval(k['pub_tags'])
        prim_tags_list = list()
        sec_tags_list = list()
        for j in all_tags_list:
            if str(j).lower() in makes_and_models_mx:
                prim_tags_list.append(str(j).lower())
            else:
                sec_tags_list.append(str(j).lower())
        new_dict = {
            'id': int(k['id']),
            'pub_title': k['pub_title'],
            'pub_date': k['pub_date'],
            'pub_author': k['pub_author'],
            'prim_tags_list':prim_tags_list,
            'sec_tags_list':sec_tags_list,
        }
        latest_publications.append(new_dict)

    return render(request, 'publications/list.html', {'latest_publications':latest_publications,})



def perform_search(request):
    query = request.GET.get('q', '')
    search_results_list = Publication.objects.filter(Q(pub_description__icontains=query) | Q(pub_title__icontains=query))
    return render(request, 'publications/search_results.html', {'search_results_list':search_results_list,})



def detail(request, pub_id):
    try:
        a = Publication.objects.get(id=pub_id)
    except:
        raise Http404("Anuncio no fue encontrado")

    latest_comments_list = a.comment_set.order_by('-id')

    tags = eval(a.pub_tags)

    return render(request, 'publications/details.html', {'publication': a, 'latest_comments_list': latest_comments_list, 'tags': tags})



def leave_comment(request, pub_id):
    try:
        a = Publication.objects.get(id=pub_id)
    except:
        raise Http404("Anuncio no fue encontrado")
    a.comment_set.create(comment_author = request.POST['name'], comment_text = request.POST['text'])
    return HttpResponseRedirect( reverse('publications:detail', args = (a.id,)) )





def create_publication(request):
    a = Publication(pub_title = str(request.POST['title'])[0:60], pub_author = request.POST['name'], pub_description = request.POST['text'], pub_date = timezone.now(), pub_objective = 0)

    input_text = str(a.pub_description).lower()

    # remove symbols and replaces üéúíóáñ letters
    clear_text = input_text.replace('1', ' ').replace('2', ' ').replace('3', ' ').replace('4', ' ').replace('5', ' ').replace('6', ' ').replace('7', ' ').replace('8', ' ').replace('9', ' ').replace('0', ' ').replace('!', ' ').replace('¡', ' ').replace('?', ' ').replace('¿', ' ').replace('#', ' ').replace('$', ' ').replace('%', ' ').replace('^', ' ').replace('&', ' ').replace('*', ' ').replace('(', ' ').replace(')', ' ').replace('_', ' ').replace('-', ' ').replace('+', ' ').replace('=', ' ').replace('/', ' ').replace('[', ' ').replace(']', ' ').replace('{', ' ').replace('}', ' ').replace('>', ' ').replace('<', ' ').replace(',', ' ').replace('.', ' ').replace('"', ' ').replace("'", ' ').replace('ü', 'u').replace('ú', 'u').replace('é', 'e').replace('á', 'a').replace('ó', 'o').replace('í', 'i').replace('ñ', 'n')

    # remove emojies
    output_text = []
    for item in clear_text:
        output_text.append(item.encode('ascii', 'ignore').decode('ascii'))
    almost_tags = ''.join(output_text)

    # remove unnecessary words
    unnecessary_words_set = ('busco', 'vendo', 'quien', 'tiene', 'tenga', 'con', 'para', 'de', 'y', 'o', 'se', 'en', 'alguna', 'alguien', 'un', 'uno', 'una', 'el', 'del', 'la', 'que', 'este', 'para', 'ocupo')
    pre_set = {i for i in almost_tags.split()}

    #remove all short words, when their lendth ==1
    tags_set = set()
    tags_set = {k for k in pre_set if not len(k) == 1 and not k in tags_set}
    tags_set.difference_update(unnecessary_words_set)
    a.pub_tags = list(tags_set)
    a.save()
    return HttpResponseRedirect(reverse('publications:index'))
