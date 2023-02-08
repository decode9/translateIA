import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QTextEdit, QPushButton
from .openai_helper import OpenAI

class Qt5Application():

    def __init__(self):
        self.app = QApplication(sys.argv)
        self.window = QWidget()
        self.layout = QVBoxLayout()
        self.openai_helper = OpenAI()

    def __declareSpanishToEnglishContent(self):
        label = QLabel('Traductor / Translator')
        spanishEnglish = QLabel('Traducir de espanol a ingles / Translate from spanish to english')
        inputSpanish = QTextEdit()
        buttonTranslateEnglish = QPushButton('Traducir / Translate')
        spanishEnglishResult = QLabel('Resultado de traduccion / Translate Result')
        textEnglish = QLabel()
        self.textEnglish = textEnglish
        self.inputSpanish = inputSpanish
        self.buttonTranslateEnglish = buttonTranslateEnglish
        self.layout.addWidget(label)
        self.layout.addWidget(spanishEnglish)
        self.layout.addWidget(inputSpanish)
        self.layout.addWidget(buttonTranslateEnglish)
        self.layout.addWidget(spanishEnglishResult)
        self.layout.addWidget(textEnglish)
        
    def __declareEnglishToSpanishContent(self):
        spanishEnglish = QLabel('Traducir de ingles a espanol / Translate from english to spanish')
        inputEnglish = QTextEdit()
        buttonTranslateSpanish = QPushButton('Traducir / Translate')
        spanishEnglishResult = QLabel('Resultado de traduccion / Translate Result')
        textSpanish = QLabel()
        self.textSpanish = textSpanish
        self.inputEnglish = inputEnglish
        self.buttonTranslateSpanish = buttonTranslateSpanish
        self.layout.addWidget(spanishEnglish)
        self.layout.addWidget(inputEnglish)
        self.layout.addWidget(buttonTranslateSpanish)
        self.layout.addWidget(spanishEnglishResult)
        self.layout.addWidget(textSpanish)

    def __translateSpanishToEnglish(self):
        text = self.inputSpanish.toPlainText()
        translation = self.openai_helper.translate('Spanish','English', text)
        if(translation == 'error'):
            return self.textEnglish.setText('Ha ocurrido un error intente de nuevo / an error has ocurred try again')
        self.textEnglish.setText(translation)
    
    def __translateEnglishToSpanish(self):
        text = self.inputEnglish.toPlainText()
        translation = self.openai_helper.translate('English','Spanish', text)
        if(translation == 'error'):
            return self.textEnglish.setText('Ha ocurrido un error intente de nuevo / an error has ocurred try again')
        self.textSpanish.setText(translation)
    
    def __buildInterface(self):
        self.__declareSpanishToEnglishContent()
        self.buttonTranslateEnglish.clicked.connect(self.__translateSpanishToEnglish)
        self.__declareEnglishToSpanishContent()
        self.buttonTranslateSpanish.clicked.connect(self.__translateEnglishToSpanish)
        self.window.setLayout(self.layout)
    
    def start_app(self):
        self.__buildInterface()
        self.window.setFixedWidth(800)
        self.window.show()
        self.app.exec()
        
        