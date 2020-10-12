import win32com.client as wincl
speak =wincl.Dispatch("SAPI.SpVoice")


speak.Speak(" Hey Khushi, How are you doing??")


speak.Speak(" What are  you doing, Now??")
