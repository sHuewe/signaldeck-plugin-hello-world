from signaldeck_sdk import DisplayProcessor

import logging

class HelloWorldProcessor(DisplayProcessor):
    def __init__(self,name,config,vP,collect_data):
        super().__init__(name,config,vP,collect_data)
        self.logger = logging.getLogger(__name__)

    def getTemplate(self,value):
        return "hello_world/hello_world.html"

