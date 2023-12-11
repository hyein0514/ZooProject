from queue import Queue
import subprocess

def main():
    # 10개의 리스트 생성
    bear = ["말레이곰", "불곰", "반달가슴곰", "아메리칸검정곰"]
    savage = ["호랑이", "표범"]
    south_america = ["나무늘보", "카피바라", "라마", "거북", "바다악어", "아나콘다", "개미핥기", "아카콘다"]
    deer = ["붉은사슴", "고라니", "큰뿔양", "다마사슴"]
    sea = ["참물범", "점박이물범", "바다사자"]
    camel = ["쌍봉낙타", "단봉낙타"]
    big = ["코끼리", "흰코뿔소", "코뿔소"]
    africa3_gwan = ["사자", "치타", "일런드", "세이블앤틸롭"]
    africa2_gwan = ["미어캣", "하마", "피그미하마", "흰오릭스", "돌산양", "바바리양"]
    africa1_gwan = ["기린", "얼룩말", "겜스복","타조", "사막여우", "검은꼬리프레리독"]

    # 딕셔너리 생성
    zoo_lists = {
        '제1 아프리카관': africa1_gwan,
        '제3 아프리카관': africa3_gwan,
        '제2 아프리카관': africa2_gwan,
        '대동물관': big,
        '낙타사': camel,
        '해양관': sea,
        '사슴사': deer,
        '남미관': south_america,
        '맹수사': savage,
        '곰사': bear
    }

    # 큐에 딕셔너리를 넣음
    queue1 = Queue()
    queue1.put(('제1 아프리카관', zoo_lists['제1 아프리카관']))
    queue1.put(('제3 아프리카관', zoo_lists['제3 아프리카관']))

    queue2 = Queue()
    queue2.put(('제2 아프리카관', zoo_lists['제2 아프리카관']))
    queue2.put(('대동물관', zoo_lists['대동물관']))
    queue2.put(('낙타사', zoo_lists['낙타사']))
    queue2.put(('해양관', zoo_lists['해양관']))
    queue2.put(('사슴사', zoo_lists['사슴사']))
    queue2.put(('곰사', zoo_lists['곰사']))
    queue2.put(('맹수사', zoo_lists['맹수사']))

    queue3 = Queue()
    queue3.put(('남미관', zoo_lists['남미관']))

    user_input = input("11월 이후 겨울이면 'cold'를, 봄~가을 이면 'hot'을 입력해주세요 : ")

    if user_input.lower() == 'hot':
        print("야외에서 볼 수 있는 동물들 목록입니다.")
        print_queue(queue1)
        print_queue(queue2)
        print_queue(queue3)
        print("경로 안내")
        subprocess.run(['python', 'hot_dijkstra.py'])
    elif user_input.lower() == 'cold':
        print("야외에서 볼 수 있는 동물들 목록입니다.")
        print_queue(queue2)
        print_queue(queue3)
        print("경로 안내")
        subprocess.run(['python', 'cold_dijkstra.py'])
    else:
        print("Invalid input. Please enter 'hot' or 'cold'.")



def print_queue(queue):
    while not queue.empty():
        list_info = queue.get()
        list_name = list_info[0]
        animal_list = list_info[1]
        print_lists(list_name, animal_list)

def print_lists(list_name, animal_list):
    print(f"{list_name}:")
    for animal in animal_list:
        print(f"- {animal}")

if __name__ == "__main__":
    main()
