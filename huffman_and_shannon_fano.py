from math import log
from operator import itemgetter
import pandas as pd
######################################################################
st = "каменного здания мимо которого мы проходим оборудование слишком незнакомое чтобы можно было его опознать несколько  человек за столами у одного в руках пробирка ха химические опыты в  виртуальном пространстве чтото новое имеет смысл лишь если работа ведется  над очень ядовитыми веществами или с бактериальными средами возьмем на  заметку куда вы меня ведете  интересуюсь у охранника лысина не оборачивается но  отвечает к директору корпорации имени он не называет но и без того сказано многое алькабар   транснациональная корпорация специализирующаяся на производстве лекарств  телефонной связи кажется  еще на добыче нефти несмотря на весь арабский  антураж контролируется она из швейцарии директор ее фридрих урман  личность  слишком значительная чтобы беседовать с каждым посетителем теплая готовится встреча мы останавливаемся у маленькой увитой виноградом деревянной беседки сзади меня  подталкивают и я вхожу охранники остаются за порогом внутри помещение куда больше чем снаружи огромный павильон в центре бассейн демедленно плавают сонные блестящие рыбы рядом столик с двумя креслами очень много цветов я даже начинаю чувствовать запахи и никого что ж подождем сажусь в кресло легкая муть перед глазами что и следовало ожидать сейчас прощупывают мой  канал связи пытаются определить откуда я пришел объем информации которую  могу принимать и передавать за секунду присутствующие при мне программы давайте работайте шесть арендованных на раз роутеров через которые  пробегает сигнал и все достаточно стойкие к взлому а под конец  платный  интернетовский гейт в австрии через который я и вошел в виртуальность следы останутся но никуда не приведут можно в любой момент оборвать связь вышвырнуть меня из квартала только что  им это даст все вещичкипрограммки что находятся при мне немедленно сработают мало что останется для изучения а я им очень интересен сомнений нет отслежен первый роутер  сообщает виндоусхоум быстро качаю головой  и в этот момент кресло напротив перестает быть пустым господин фридрих урман пренебрегает арабским колоритом он в шортах цветастой рубашке пожилой сухопарый серьезный добрый день дайвер  произносит он порусски голос неестественный  пропущенный через программупереводчик вот и причина столь высокой чести боюсь что вы ошибаетесь господин директор когда полгода назад мы создали мост это преследовало лишь одну цель господин дайвер обнаружить вас человек находящийся в виртуальности не смог бы его преодолеть  урман скупо улыбается  я первый раз вижу настоящего дайвера одинноль не в мою пользу а я первый раз вижу настоящего мультимиллионера вот видите наша встреча уже принесла первые плоды виндоусхоум шепчет отслежен второй роутер уран хмурится  похоже и ему чтото сообщают потом интересуется простите через сколько компьютеров вы прошли на пути сюда к сожалению я не помню урман пожимает плечами как я могу вас называть иванцаревич секундная пауза  потом улыбка ему объяснили о русский сказочный герой а вы сами  русский разве это имеет значение да вы совершенно правы господин дайвер как я понимаю вы проникли в наш  квартал незаконно разве  поражаюсь я  честно говоря просто искал работу прочитал ваше  объявление прошел по мосту подчинился этим странноватым охранникам одинодин фридрих урман всплескивает руками да действительно но у нас и нет претензий в ваш адрес господин дайвер разве что странные вещи которые вы носите с собой медленно демонстративно вытаскиваю все из карманов расческа носовой платок маленькое зеркальце вот отдать вам меч урман машет руками господи к чему мы же не собираемся устраивать потасовок верно давайте  поговорим отслежен третий роутер как жаль что времени на беседу остается все меньше и меньше  вздыхаю я да но времени всегда не хватает итак господин дайвер у меня есть основания полагать что некоторые лица хотели бы получить ряд наших разработок и даже ухитрились нанять дайвера чтобы пожать чужие плоды яблочки  уточняю я да именно у нас работает хороший русский программист он сделал красивую  форму для хранения информации  урман хлопает в ладоши и рядом с нами воздух  начинает мутнеть сгущаться миг  и возникает маленькое деревце усыпанное плодами  полагаю что наибольший интерес вызывает вон то маленькое зеленое яблочко на нижней ветке я смотрю на вожделенный плод он мелкий незрелый и червивый как вы думаете дайвер сколько могли бы заплатить наши конкуренты за этот файл тысяч десять  несколько завышаю цену урман недоуменно смотрит на меня уточняет десять тысяч долларов да честно говоря даже сто тысяч были бы невысокой наградой хорошо допустим я предлагаю человеку пытавшемуся украсть файл сто пятьдесят тысяч при  условии что он начнет сотрудничать с нами за нормальную хорошую плату это что лекарство от рака  спрашиваю я урман качает головой нет тогда бы оно не имело цены это лишь средство от простуды но очень очень действенное мы готовимся начать его производство но лишь после того как будут распроданы запасы менее действенных лекарств так что вы скажете о моем предложении"
h1 = 4.352982602 # H(X) (лаб.1)
h2 = 3.120147 # H(Y/X) (лаб.2)

st = st.replace("  ", " ")
st = st.replace("ё", "е")
st = st.replace("ъ", "ь")

alphabet = ''.join(set(st))
alphabet_size = 32
text_size = len(st)
hmax = log(alphabet_size, 2)
######################################################################
print("ЗАДАНИЕ 1")
dp = 1 - (h1 / hmax)
print("Избыточность заданного текста, вызванная неравновероятностью появления символов в сообщении Dp:", dp)
ds = 1 - (h2/h1)
print("Избыточность заданного текста, вызванная статистической связью между соседними символами Ds:", ds)
d = ds + dp - ds*dp
print("Полная информационная избыточность:", d)
print("")
######################################################################
def divide(code):
    sum_total = 0
    for i in range(len(code)):
        sum_total += code[i][1]
    minimal_difference, sum, division_point = 1000000000000000, 0, 0
    for i in range(len(code)):
        sum += code[i][1]
        if abs(sum_total - sum * 2) < minimal_difference:
            minimal_difference = abs(sum_total - sum * 2)
            division_point = i + 1
    
    return code[:division_point], code[division_point:]

def assign_label(code):
    if len(code) > 1:
        part1, part2 = divide(code)
        for i in range(len(part1)):
            part1[i][2] += "0"
        for i in range(len(part2)):
            part2[i][2] += "1"
        if len(part1) == 1 and len(part2) == 1:
            return 
        assign_label(part1)
        assign_label(part2)

def encode_shannon(text):
    frequencies = {}
    for letter in text:
        if letter in frequencies:
            frequencies[letter] += 1
        else:
            frequencies[letter] = 1
    code = []
    # Представляет собой вложенный список: [["а", 473, "1101"], ["б", 273, "1100"], ...]
    for key in frequencies:
        code.append([key, frequencies[key], ''])
    code = sorted(code, key=itemgetter(1), reverse=True)
    assign_label(code)

    encoded = ''
    coded_letters = {}
    for letter in code:
        coded_letters[letter[0]] = letter[2]
    for letter in text:
        encoded += coded_letters[letter]
    return encoded, code

def decode_shannon(encoded, code):
    decoded_letters = {}
    for letter in code:
        decoded_letters[letter[2]] = letter[0]
    decoded = ""
    coded_letter = ""
    for letter in encoded:
        coded_letter += letter
        if decoded_letters.get(coded_letter):
            decoded += decoded_letters[coded_letter]
            coded_letter = ""
    return decoded
######################################################################
class NodeTree(object):
    def __init__(self, left=None, right=None):
        self.left = left
        self.right = right

    def children(self):
        return self.left, self.right


def huffman_code_tree(node, binString=''):
    if type(node) is str:
        return {node: binString}
    (l, r) = node.children()
    d = dict()
    d.update(huffman_code_tree(l, binString + '0'))
    d.update(huffman_code_tree(r, binString + '1'))
    return d

def make_tree(nodes):
    while len(nodes) > 1:
        (key1, c1) = nodes[-1]
        (key2, c2) = nodes[-2]
        nodes = nodes[:-2]
        node = NodeTree(key1, key2)
        nodes.append((node, c1 + c2))
        nodes = sorted(nodes, key=lambda x: x[1], reverse=True)
    return nodes[0][0]


def encode_huffman(text):
    frequencies = {}
    for letter in text:
        if letter in frequencies:
            frequencies[letter] += 1
        else:
            frequencies[letter] = 1
    frequencies = sorted(frequencies.items(), key=lambda x: x[1], reverse=True)
    node = make_tree(frequencies)
    coded_letters = huffman_code_tree(node)

    encoded = ""
    for letter in text:
        encoded += coded_letters[letter]
    return encoded, coded_letters

def decode_huffman(encoded, coded_letters):
    decoded_letters = {}
    for letter, code in coded_letters.items():
        decoded_letters[code] = letter

    decoded = ""
    coded_letter = ""
    for letter in encoded:
        coded_letter += letter
        if decoded_letters.get(coded_letter):
            decoded += decoded_letters[coded_letter]
            coded_letter = ""
    return decoded
######################################################################
print("ЗАДАНИЕ 2")
encoded1, code1 = encode_shannon(st)
print("Текст, закодированный с помощью метода Шеннона-Фано:", encoded1[:200])
decoded1 = decode_shannon(encoded1, code1)
print("Декодированный текст:", decoded1[:50])
code1 = sorted(code1, key=itemgetter(0))
dictionary1 = {}
for item in code1:
    dictionary1[item[0]] = [item[2]]
df1 = pd.DataFrame.from_dict(dictionary1)
df1.to_excel("ShannonFano.xlsx")
print("")

encoded2, code2 = encode_huffman(st)
print("Текст, закодированный с помощью метода Хаффмана:", encoded2[:200])
decoded2 = decode_huffman(encoded2, code2)
print("Декодированный текст:", decoded2[:50])
code2 = dict(sorted(code2.items()))
dictionary2 = {}
for letter, code in code2.items():
    dictionary2[letter] = [code]
df2 = pd.DataFrame.from_dict(dictionary2)
df2.to_excel("Huffman.xlsx")
print("")
######################################################################
print("ЗАДАНИЕ 3")
print("Метод Шеннона-Фано:")
frequencies1 = {}
for letter in alphabet:
    frequencies1[letter] = 0
for letter in st:
    frequencies1[letter] += 1
l1 = 0
for letter in alphabet:
    l1 += (frequencies1[letter]/text_size)*len(dictionary1[letter][0])
print("Средняя длина кода:", l1)
kcc1 = hmax/l1
print("Коэффициент статистического сжатия:", kcc1)
koe1 = h1/l1
print("Коэффициент относительной эффективности:", koe1)
print(" ")

print("Метод Хаффмана:")
frequencies2 = {}
for letter in alphabet:
    frequencies2[letter] = 0
for letter in st:
    frequencies2[letter] += 1
l2 = 0
for letter in alphabet:
    l2 += (frequencies2[letter]/text_size)*len(dictionary2[letter][0])
print("Средняя длина кода:", l2)
kcc2 = hmax/l2
print("Коэффициент статистического сжатия:", kcc2)
koe2 = h1/l2
print("Коэффициент относительной эффективности:", koe2)