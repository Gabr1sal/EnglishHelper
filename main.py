import random as rand
import copy

def paragraph_order(passage_list):
    print(f"몇 개의 문단으로 나누고 싶습니까? (최대: {len(passage_list)})")
    num_sentence = int(input('> '))
    quotient = len(passage_list) // num_sentence
    remainder = len(passage_list) % num_sentence
    num_array = [quotient] * num_sentence
    for i in range(remainder):
        num_array[i] += 1

    cumu = 0
    paragraphs = []
    for j in range(num_sentence):
        paragraphs.append(" ".join(passage_list[cumu:cumu+num_array[j]]))
        cumu += num_array[j]
    order_array = []
    for k in range(1, num_sentence+1):
        order_array.append(k)
    random_order = copy.copy(order_array)
    rand.shuffle(random_order)
    paragraph_random = []
    for a in range(1, num_sentence+1):
        paragraph_random.append('(' + str(a) + ') ' + paragraphs[random_order[a-1]-1])

    for paragraph in paragraph_random:
        print(paragraph)
    order_dict = {random_order[i] : order_array[i] for i in range(len(random_order))}
    sorted_order = [order_dict[i] for i in order_array]
    input('엔터 눌러 정답 확인')
    print(sorted_order)



def main():
    passage = input("지문을 입력해주세요: ")
    passage = passage.replace("!", ".")
    passage = passage.replace("?", ".")
    passage_list = passage.split(". ")
    passage_list = [sentence + "." for sentence in passage_list]
    new_list = [''] * len(passage_list)
    separated = False
    i = 0
    j = 0
    while not separated:
        if (len(passage_list[j].split()) < 8) or ("Mr." in passage_list[j]) or ("Ms." in passage_list[j]) or ("Mrs." in passage_list[j]):
            new_list[i] = passage_list[j] + ' '
        else:
            new_list[i] += passage_list[j]
            i += 1
        if j == len(passage_list) - 1:
            separated = True
        j += 1
    new_list[-1] = new_list[-1][:-1]
    refined = False
    while not refined:
        if new_list[-1] == "":
            new_list.pop()
        else:
            refined = True

    paragraph_order(new_list)


main()
