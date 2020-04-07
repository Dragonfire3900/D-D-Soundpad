#File Handling
import os

#Graphical setup
from tkinter import Frame, Button, Label, Scale, VERTICAL, GROOVE, Checkbutton, IntVar, DoubleVar, filedialog

#Audio handling
from pygame.mixer import Sound, Channel, get_init
from pygame import mixer

source = "C:\\Users\\Darkf\\Downloads\\soundfile.wav" #Some file source path that is going to be used for testing purposes

mixer.init()

class AudioHandle(object):
    def __init__(self, ch_id: int, file_path: str = ""):
        assert(get_init()), ValueError("The mixer has not been initialized yet")
        
        #Setting up the channel structure
        self.__channel = Channel(ch_id)

        #Setting up the sound path
        if file_path == '':
            self.__sound_path = ''
            self.__sound = '' #Once initialized this should become a pygame.mixer.Sound object
        else:
            self.setSound(file_path)

    #Accessors
    def getPlaying(self) -> bool:
        return self.__channel.get_busy()

    def getVolume(self) -> float:
        return self.__channel.get_volume()

    def getSoundPath(self) -> str:
        return self.__sound_path

    #Mutators
    def setVolume(self, value: float) -> bool:
        if value >= 0.0 and value <= 1.0:
            self.__channel.set_volume(value)
            return True
        else:
            return False

    def setSound(self, file_path: str) -> bool:
        try:
            self.__sound = Sound(file_path)
            self.__sound_path = file_path
            return True
        except FileNotFoundError as e:
            #print("The source file was not found. Recieved: {}".format(file_path))
            return False

    def clearSound(self):
        """Clears the currently set sound to just an empty string"""
        self.__sound = ''
        self.__sound_path = ''

    #Control flow
    def play(self, loops: int = 0) -> bool:
        """This plays the set sound file
        
        Keyword Arguments:
            loops {int} -- The number of times the file will be played. -1 is for forever (default: {0})
        
        Returns:
            bool -- Returns if the playing was successful or not
        """
        if isinstance(self.__sound, Sound):
            self.__channel.play(self.__sound, loops = loops)
            return True
        else:
            return False

    def pause(self) -> bool:
        """If the AudioHandler is playing something then it will pause it
        
        Returns:
            bool -- Returns true if the object was actually paused
        """
        if self.get_busy():
            self.__channel.pause()
            return True
        else:
            return False

    def unpause(self) -> bool:
        """If the AudioHandler is playing something then it will unpause it
        
        Returns:
            bool -- Returns true if the object was actually unpaused
        """
        if not self.get_busy():
            self.__channel.unpause()
            return True
        else:
            return False

    def stop(self) -> bool:
        """If the AudioHandler is playing something then it will stop it
        
        Returns:
            bool -- Returns if the audio feedback was stopped
        """
        if not self.get_busy():
            self.__channel.stop()
            return True
        else:
            return False

    #Default Functions
    def __str__(self):
        if self.getSoundPath() == '':
            return "Sound undefined for this channel"
        else:
            return "Sound Path: {}".format(self.getSoundPath())

a = AudioHandle(7, source)
print(a)
a.play()