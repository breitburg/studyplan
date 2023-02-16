from random import randint
from threading import local
from maya import MayaDT
from typing import List
from ics.event import Event
from progress.bar import IncrementalBar


def schedule(tasks: List[str], begin: MayaDT, finish: MayaDT,
             per_day: int, count: int) -> List[Event]:
    delta_days = finish.subtract_date(dt=begin).days
    local_tasks = []
    events = []

    for day in IncrementalBar('🧠 Planning'.format(delta_days), suffix='%(percent)d%% (day %(index)d)',
                              max=delta_days).iter(range(delta_days)):
        if not local_tasks or len(local_tasks) < per_day:
            local_tasks = tasks.copy()

        today_tasks = [local_tasks.pop(randint(0, len(local_tasks) - 1))
                       for _ in range(per_day)]

        event = Event(
            name='Do tasks: {}'.format(', '.join(today_tasks)),
            begin=begin.add(days=day).datetime(),
            description='You need to do each task {} times.\n{} % of the plan, {} days remaining.'.format(
                count, round(day / delta_days * 100) + 1, delta_days - day),
        )
        event.make_all_day()
        events.append(event)

    return events
