from signaldeck_sdk import DisplayData
import json

class HelloWorldDisplayData(DisplayData):


    def getStatefullFields(self):
        return ["is_day","is_celsius","is_kelvin","temp","name"]


    def buttons(self):
        return {
            "submitFoo": {
                "name": "submitFoo",
                "text": "Submit Foo=bar",
                "params": {"foo": "bar"}
            },
            "submitNum": {
                "name": "submitNum",
                "text": "Submit a=11",
                "params": {"a": 11}
            },
            "isDay": {
                "name": "isDay",
                "text": "day",
                "toggleable": True,
                "button_active_condition": ("is_day", True),
                "params": {"is_day": True}
            },
            "isC": {
                "name": "isC",
                "text": "celsius",
                "button_active_condition": ("is_celsius", True),
                "params": {"is_celsius": True, "is_kelvin": False}
            },
            "isK": {
                "name": "isK",
                "text": "kelvin",
                "button_active_condition": ("is_kelvin", True),
                "params": {"is_celsius": False, "is_kelvin": True}
            },
            "setTemp10": {
                "name": "setTemp10",
                "text": "10°C",
                "button_active_condition": ("temp", 10),
                "params": {"temp": 10}
            },
            "setTemp15": {
                "name": "setTemp15",
                "text": "15°C",
                "button_active_condition": ("temp", 15),
                "params": {"temp": 15}
            },
            "setTemp20": {
                "name": "setTemp20",
                "text": "20°C",
                "button_active_condition": ("temp", 20),
                "params": {"temp": 20}
            },            
            "name": {
                "name": "name",
                "text": "Name senden",
                "params": {"name": "@name_field"}
            },            
            "datei": {
                "name": "datei",
                "text": "Datei hochladen",
                "params": {"datei": "@file_field"}
            }

        }