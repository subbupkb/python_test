#!/bin/env python
###################################################################
#

###################################################################
##-----------------------  IMPORT section ----------------------###
###################################################################
import sys, os, time
import subprocess
import logging
from os import path
from datetime import datetime, timedelta
import argparse
import datetime

from kivy.app import App
from kivy.uix.button import Button

###################################################################


class langLearnApp(App):
	def build(self):
		return Button(text = "Hello Subbu")


###################################################################

if __name__ == "__main__" :
	langLearnApp().run()

###################################################################
