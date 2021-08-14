import string
from typing import DefaultDict
import PySimpleGUI as sg
from PySimpleGUI import popup_get_text

AlphabetToRuneDict = {
    "A": "ᚪ",    "B": "ᛒ",    "C": "ᚳ",    "D": "ᛞ",    "E": "ᛖ",
    "F": "ᚠ",    "G": "ᚷ",    "H": "ᚻ",    "I": "ᛁ",    "J": "ᛄ",
    "K": "ᛣ",    "L": "ᛚ",    "M": "ᛗ",    "N": "ᚾ",    "O": "ᚩ",
    "P": "ᛈ",    "Q": "ᚴ",    "R": "ᚱ",    "S": "ᛋ",    "T": "ᛏ",
    "U": "ᚢ",    "V": "ᛓ",    "W": "ᚹ",    "X": "ᛣ",    "Y": "ᚣ",
    "Z": "ᛉ"
}

def AlphabetToRune(s):
    answer = ""
    for letter in range(len(s)):
        answer += AlphabetToRuneDict.get(s[letter].upper(), s[letter])
    return answer

def RuneToAlphabet(s):
    answer = ""
    for letter in range(len(s)):
        keys = [k for k, v in AlphabetToRuneDict.items() if v == s[letter]]
        if keys:
            answer += keys[0]
        else:
            answer += s[letter]
    return answer

class MainDisplay:
    def __init__(self):
        sg.theme("DefaultNoMoreNagging")
        self.layout = [ [sg.Image(filename="AssaultLilyLogo.png"), sg.Text("ルーン文字変換機",font=("IPAゴシック", 18))],
                        [sg.Multiline(size=(70,10),key="txt")],
                        [sg.Button("アルファベットに変換",border_width=2), sg.Button("ルーン文字に変換",border_width=2)]]
        self.window = sg.Window("RuneConverter", self.layout, icon="icon.ico")

    def MakeSubDisplay(self, s):
        disp2 = SubDisplay(s)
        disp2.main()
        del disp2

    def main(self):
        while True:
            event, values = self.window.read()
            if event == sg.WIN_CLOSED:
                break
            elif event == "アルファベットに変換":
                answer = RuneToAlphabet(values["txt"])
                self.MakeSubDisplay(answer)
            else:
                answer = AlphabetToRune(values["txt"])
                self.MakeSubDisplay(answer)
        self.window.close()

class SubDisplay:
    def __init__(self, s):
        sg.theme("DefaultNoMoreNagging")
        self.layout = [ [sg.Multiline(size=(50,8),default_text=s)],
                        [sg.Button("閉じる",border_width=2)] ]
        self.window = sg.Window("Converted", self.layout, icon="icon.ico", keep_on_top=True)

    def main(self):
        while True:
            event, values = self.window.read()
            if event == "閉じる" or event == sg.WIN_CLOSED:
                break
        self.window.close()

if __name__ == "__main__":
    disp1 = MainDisplay()
    disp1.main()