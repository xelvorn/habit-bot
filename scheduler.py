from telegram.ext import JobQueue
import os
from datetime import time

def setup_scheduler(job_queue: JobQueue, callback, context):
    hour = int(os.getenv("REMIND_HOUR", 9))
    minute = int(os.getenv("REMIND_MINUTE", 0))
    job_queue.run_daily(callback, time(hour, minute), context=context, name=str(context))
