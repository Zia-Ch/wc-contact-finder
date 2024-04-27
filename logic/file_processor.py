import datetime

from logic.constants import LINE_SPACER
from logic.performance_logger import log_performance
from logic.valid_email_counter import valid_email_counter
from logic.web_processor import process_websites


def file_processor(file_name,file_path, workers):
    print(LINE_SPACER)
    print(f"Processing {file_name}")
    print(f"{LINE_SPACER}\n")
    start_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    process_websites(file_path,workers)
    end_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    emails_found = valid_email_counter(file_path)
    log_performance(file_name, emails_found, workers, start_time, end_time)
    