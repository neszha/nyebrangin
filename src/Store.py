import json
import src.state as state
from os import path, mkdir

class Store: 
    
    def __init__(self):
        self.__dir = './__temp/'
        self.__checkpoints = 'checkpoints.json'

    def __create_checkpoints(self):
        full_path = f'{self.__dir}{self.__checkpoints}'
        if not path.exists(self.__dir): mkdir(self.__dir)
        if not path.exists(full_path): self.__save_checkpoints()

    def __save_checkpoints(self):
        full_path = f'{self.__dir}{self.__checkpoints}'
        file = open(full_path, 'w')
        file.write(json.dumps(state.CHECKPOINTS))
        file.close()

    def load_checkpoints(self):
        self.__create_checkpoints()
        full_path = f'{self.__dir}{self.__checkpoints}'
        file = open(full_path, 'r')
        checkpoints = json.loads(file.read())
        state.CHECKPOINTS = checkpoints
        for data in checkpoints:
            if data['opened'] or state.OPEN_ALL_LEVEL:
                state.CURRENT_LEVEL = data['level']
            else: return

    def save_checkpoint(self, time_left, thropy):
        level = state.LEVEL_RUNNING - 1
        next_level = level + 1
        state.CHECKPOINTS[level]['thropy'] = int(thropy)
        state.CHECKPOINTS[level]['time_left'] = str(time_left)
        if next_level > state.MAX_LEVEL: next_level = state.MAX_LEVEL
        state.CHECKPOINTS[next_level]['opened'] = True
        self.__save_checkpoints()

