import sys
from PyQt6.QtWidgets import *
from PyQt6 import uic
from PyQt6.QtCore import *
import openai
from APIKEY import APIKEY

# api key
openai.api_key = APIKEY.OPENAI_KEY.value

#UI파일 연결
#단, UI파일은 Python 코드 파일과 같은 디렉토리에 위치해야한다.
form_class = uic.loadUiType("app/prototype.ui")[0]

#화면을 띄우는데 사용되는 Class 선언
class WindowClass(QMainWindow, form_class):
    def __init__(self) :
        super().__init__()
        self.setupUi(self)

        self.btn_submit.clicked.connect(self.submit)


    def submit(self):
        self.browserAnswer.clear()
        question = self.textQuestion.toPlainText()
        answer = myGPT(question)
        self.browserAnswer.insertPlainText(answer)



def myGPT(question):
    messages = [
    {"role": "user", "content": """복부 CT 검사.
     
  복부 CT 검사(전산회단층촬영)는 배 속의 장기를 X선으로 관찰하는 검사예요. 일반 X선 촬영과는 달리 김밥 자르듯이 가로 방향으로 촬영해 자세히 관찰할 수 있다는 장점이 있어요. 또 통증은 없고 조사되는 방사선의 양은 적어 안전해요.

  복부 CT 검사는 복부 통증이 있을 때, 배 속 장기인 소장, 대장, 간, 담낭, 췌장, 비장, 신장의 질병을 진단할 때 검사해요. 특히 췌장은 다른 장기들로 감춰져 있어 복부 CT 검사로 자세히 관찰할 수 있어요. 또 암을 진단할 때 도움이 돼요. 그 외 응급상황에 장기가 손상입었는지 신속하게 알 수 있어요.

  검사 전 준비 사항이 있어요. 당뇨병 약인 메포민을 먹고 있다면 24~48시간 전부터 중단해주세요. 검사 시 투여하는 조영제와 상호작용을 일으켜 신장에 이상이 생길 수 있기 때문이죠. 이전 조영제 알레르기가 있거나 신장이 약하다면 알려주세요. 검사를 안전하게 받기 위해 추가로 주사를 맞을 수 있어요. 또 CT 검사의 방사선이 태아에게 해가 될 가능성이 높아 임신 중이면 알려주세요. 
     
  검사 전 4~6시간 금식을 하고 검사 동의서를 작성해요. 안경, 틀니, 머리핀과 같은 금속물품은 보호자에게 맡겨주세요. 검사 시행 직전 물을 500cc 마시고 조영제를 주사한 뒤 복부를 촬영해요. 검사 중 움직이지 마시고 안내에 잘 따라주세요. 검사 소요 시간은 10분~15분이에요. 소아는 진정제를 투여할 수 있어요.

  검사 후 조영제 투여로 몸 전체가 화끈거리지만, 곧 가라앉을 거예요. 만일 피부가 가렵거나 숨쉬기 힘들고 가슴이 두근거리면 의료진에게 알려주세요. 검사 후 의료진의 특별한 안내가 없다면 식사를 해도 괜찮아요. 또 몸에서 조영제를 배출하기 위해 물을 충분히 마셔주세요. 운전도 할 수 있어요. 

  검사 결과는 응급이라면 바로 알 수 있고 그 외는 3~7일 후 나와요. 의사는 결과를 확인하고 다음 계획에 대해 안내할 거예요.
     
     

     병실 이동.
     
     환자 분이 원하신다면 병실 이동이 가능합니다. 1인실 또는 2인실을 원한다면 간호사에게 말씀해주세요.

     다만, 병실 이동은 오전 11시 이전에는 말씀해주셔야 하며, 이후에는 병실 이동이 힘들 수 있습니다.



     편의점 위치.
     
     편의점: GS25
     위치 : 본관 3층, 암병원 지하 1층, 치과대학병원 2층
     영업시간 : 
     본관, 암병원 00:00~24:00(연중무휴)
     치과대학병원 평일 08:00~ 18:00, 토요일 08:00~13:00 / 일요일, 공휴일 휴무

     """},

    {"role": "user", "content": """Please answer the question below based on the text above.
     
     Question: CT 검사 후에도 뭐 못먹나요?

     All answers should be printed in Korean.
     
     If the question is irrelevant with the text above, please print the text below as it is without modifying anything.
     
     '죄송합니다. 해당 질문은 답변이 어렵습니다. 의사 또는 간호사에게 질문해주세요!"""},  

    {"role": "assistant", "content": "CT 검사 후 의료진의 특별한 안내가 없다면 식사를 해도 괜찮습니다."},

    {"role": "user", "content": """Please answer the question below based on the text above.
     
     Question: 옆 침대 환자 이름이 무엇인가요?

     All answers should be printed in Korean.
     
     If the question is irrelevant with the text above, please print the text below as it is without modifying anything.
     
     '죄송합니다. 해당 질문은 답변이 어렵습니다. 의사 또는 간호사에게 질문해주세요!"""},

    {"role": "assistant", "content": "죄송합니다. 해당 질문은 답변이 어렵습니다. 의사 또는 간호사에게 질문해주세요!"}, 

    {"role": "user", "content": """Please answer the question below based on the text above.
     
     Question: 복부 CT 결과는 언제쯤 알 수 있나요?

     All answers should be printed in Korean.
     
     If the question is irrelevant with the text above, please print the text below as it is without modifying anything.
     
     '죄송합니다. 해당 질문은 답변이 어렵습니다. 의사 또는 간호사에게 질문해주세요!"""},

    {"role": "assistant", "content": "검사 결과는 응급이라면 바로 알 수 있습니다. 응급이 아니라면 3~7일 후 알 수 있습니다."},

    {"role": "user", "content": """Please answer the question below based on the text above.
     
     Question: MRI 검사 전에 금식해야하나요?

     All answers should be printed in Korean.
     
     If the question is irrelevant with the text above, please print the text below as it is without modifying anything.
     
     '죄송합니다. 해당 질문은 답변이 어렵습니다. 의사 또는 간호사에게 질문해주세요!"""},

    {"role": "assistant", "content": "죄송합니다. 해당 질문은 답변이 어렵습니다. 의사 또는 간호사에게 질문해주세요!"}, 

    {"role": "user", "content": """Please answer the question below based on the text above.
     
     Question: 계속 기침이 나오는데, 괜찮은건가요?

     All answers should be printed in Korean.
     
     If the question is irrelevant with the text above, please print the text below as it is without modifying anything.
     
     '죄송합니다. 해당 질문은 답변이 어렵습니다. 의사 또는 간호사에게 질문해주세요!"""},

    {"role": "assistant", "content": "죄송합니다. 해당 질문은 답변이 어렵습니다. 의사 또는 간호사에게 질문해주세요!"}, 

    {"role": "user", "content": """Please answer the question below based on the text above.
     
     Question: 암병동 편의점이 어디에 있어요?

     All answers should be printed in Korean.
     
     If the question is irrelevant with the text above, please print the text below as it is without modifying anything.
     
     '죄송합니다. 해당 질문은 답변이 어렵습니다. 의사 또는 간호사에게 질문해주세요!"""},

    {"role": "assistant", "content": "암병원 편의점은 암병원 건물 지하 1층에 있습니다."},

    {"role": "user", "content": """Please answer the question below based on the text above.
     
     Question: 기분이 우울한데, 우울증 약을 받을 수 있을까요?

     All answers should be printed in Korean.
     
     If the question is irrelevant with the text above, please print the text below as it is without modifying anything.
     
     '죄송합니다. 해당 질문은 답변이 어렵습니다. 의사 또는 간호사에게 질문해주세요!"""},

    {"role": "assistant", "content": "죄송합니다. 해당 질문은 답변이 어렵습니다. 의사 또는 간호사에게 질문해주세요!"},     

    {"role": "user", "content": f"""Please answer the question below based on the text above.
     
     Question: {question}

     All answers should be printed in Korean.
     
     If the question is irrelevant with the text above, please print the text below as it is without modifying anything.
     
     '죄송합니다. 해당 질문은 답변이 어렵습니다. 의사 또는 간호사에게 질문해주세요!"""},
]
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo-16k",
        messages = messages
    )    
    answer = response['choices'][0]['message']['content']

    return answer


if __name__ == "__main__" :
    app = QApplication(sys.argv) 
    myWindow = WindowClass() 
    myWindow.show()
    app.exec()