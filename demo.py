from US_Visa_Approval_Prediction.logger import logging
from US_Visa_Approval_Prediction.exception import USvisaException
import sys


logging.info("Welcome to custom log")

try:
    a = 2/0
except Exception as e:
    raise USvisaException(e, sys)