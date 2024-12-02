from src.interceptor_pre.create_pre_intercept_success_response import update_credential_type
from src.utils.configure_logger import logger


def perform(data, token, traceparent, metadata):

    logger.info("Sending to modification")
    return update_credential_type(data)