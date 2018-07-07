#!/usr/bin/env python3

import urllib.request
from datetime import datetime

from bs4 import BeautifulSoup
from icalendar import Calendar, Event, vDate

CALENDAR_URL = "https://www.seiyu.co.jp/service/5off/"

if __name__ == '__main__':
  html = urllib.request.urlopen(CALENDAR_URL).read().decode("utf-8")
  bs = BeautifulSoup(html, "lxml")

  c = Calendar()
  c.add("version", "2.0")

  year = datetime.today().year

  items = bs.find_all("ul", class_="off_calendar_list")
  for item in items:
    month = int(item.find("span", class_="off_calendar_month").text.strip("/"))
    for i in item.find_all("span", class_="off_calendar_day"):
      day = int(i.text)

      e = Event()
      e.add("summary", "西友 5% OFF 開催日")
      e.add("dtstart", vDate(datetime(year, month, day)))
      c.add_component(e)

  print(c.to_ical().decode("utf-8").strip())
