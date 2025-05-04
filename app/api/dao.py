from datetime import date, timedelta, datetime, time, timezone
from typing import List
from fastapi import HTTPException
from loguru import logger
from sqlalchemy import select, and_, func 
from sqlalchemy.exc import 