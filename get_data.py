import os 
import sys
import json

from dotenv import load_dotenv

import certifi
import pandas as pd
import numpy as np
import pymongo

from network_security.exception.exception import NetworkSecurityException
from network_security.logger.logger import logging

class network_data_extraction():
    def __init__(self):
        try:
            pass
        except Exception as e:
            raise NetworkSecurityException(e,sys)
        
    def csv_tojoin_converter(self):
        try:
            pass
        except Exception as e:
            raise Network_Security_Exception(e,sys)
        
    def pushing_data_to_mongodb(self):
        try:
            pass
        except Exception as e:
            raise Network_Security_Exception(e,self)
        
    if __name__ == '__main__':
        pass
