# *-* coding: utf-8 *-*

import ctypes, os
from ctypes import *

import speech

class NVDASupport(speech.SpeechSupport):
	nvdaLibrary = None
	
	def __init__(self):
		path = os.path.join(os.getcwd(), "nvdaControllerClient.dll")
		self.nvdaLibrary = windll.LoadLibrary(path)
		ret = self.nvdaLibrary.nvdaController_testIfRunning()
		if ret == 0:
			self.active = True

	def isActive(self):
		return self.active
	
	def speak(self, message):
		if self.active is False:
			return
		self.nvdaLibrary.nvdaController_speakText(message)
		
	def cancelSpeech(self):
		if self.active is False:
			return
		self.nvdaLibrary.nvdaController_cancelSpeech()
