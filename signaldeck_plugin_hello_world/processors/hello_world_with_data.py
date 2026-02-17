from signaldeck_sdk import DisplayData
from signaldeck_sdk import DisplayProcessor
from .hello_world_displaydata import HelloWorldDisplayData

import logging

class HelloWorldWithDataProcessor(DisplayProcessor):
    def __init__(self,name,config,vP,collect_data):
        super().__init__(name,config,vP,collect_data)
        self.logger = logging.getLogger(__name__)

    def getTemplate(self,value):
        return "hello_world/hello_world_data.html"

    def getDisplayData(self,value,actionHash,**kwargs) -> DisplayData:
        if self._uploaded_file is not None:
            kwargs["file_name"] = self._uploaded_file.filename
            kwargs["file_size"] = self._uploaded_file.content_length
            kwargs["file_type"] = self._uploaded_file.content_type
        self.logger.info(kwargs)
        return HelloWorldDisplayData(actionHash).withData(kwargs)
    
    def getBoolParams(self):
        return ["is_day","is_celsius","is_kelvin"]
    
    def getFloatParams(self):
        return ["temp"]
    
    def accecptUploadedFile(self,value,actionHash,**kwargs):
        return True
    
    def getUploadPath(self,value,file,actionHash,**kwargs):
        return "hello_world_upload/"+file.filename