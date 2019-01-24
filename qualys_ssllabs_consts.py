# --
# File: qualys_ssllabs_consts.py
#
# Copyright (c) 2016-2019 Splunk Inc.
#
# SPLUNK CONFIDENTIAL - Use or disclosure of this material in whole or in part
# without a valid written license from Splunk Inc. is PROHIBITED.
#
# --

QUALYS_SSLLABS_ERR_API_INITIALIZATION = "API Initialization failed"
ERR_CONNECTIVITY_TEST = "Connectivity test failed"
SUCC_CONNECTIVITY_TEST = "Connectivity test passed"
ERR_SERVER_CONNECTION = "Connection failed"
ERR_FROM_SERVER = "API failed, Status code: {status}, Detail: {detail}"
ERR_EMPTY_FIELDS = "The fields dictionary was detected to be empty"
ERR_API_UNSUPPORTED_METHOD = "Unsupported method"

USING_BASE_URL = "Using url: {base_url}/{api_uri}/{endpoint}"
ERR_JSON_PARSE = "Unable to parse reply as a Json, raw string reply: '{raw_text}'"
QUALYS_SSLLABS_BASE_URL = "https://api.ssllabs.com/"
QUALYS_SSLLABS_BASE_API = "/api/v2"
QUALYS_SSLLABS_TICKET_FOOTNOTE = "Added by Phantom for container id: "
QUALYS_SSLLABS_MSG_GET_INFO = "Querying API availability info"
QUALYS_SSLLABS_MAX_AGE = "12"
MSG_REPORT_PENDING = "Report Pending"
MSG_MAX_POLLS_REACHED = "Reached max polling attempts."

POLL_TIMEOUT_MINS = 10
MAX_TIMEOUT_DEF = 10
SLEEP_SECS = 10
