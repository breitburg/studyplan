from random import shuffle
from time import sleep
from maya import MayaDT
from typing import List
from ics.event import Event
from math import ceil
from progress.bar import IncrementalBar


def schedule(tasks: List[str], begin: MayaDT, finish: MayaDT,
             per_day: int, count: int, plaid: bool = False) -> List[Event]:
    delta_days = finish.subtract_date(dt=begin).days
    tasks_sets = []
    for _ in range(per_day):
        task_set = tasks * ceil(delta_days / len(tasks))
        shuffle(task_set)
        tasks_sets.append(task_set)

    events = []
    for day in IncrementalBar('🧠 Planning'.format(delta_days), suffix='%(percent)d%% (day %(index)d)', max=delta_days).iter(range(delta_days)):
        today_tasks = [tasks_sets[index][day] for index in range(per_day)]
        event = Event(
            name='Do tasks: {}'.format(', '.join(today_tasks)),
            begin=begin.add(days=day).datetime(),
            description='You need to do {} of each task.\n{} % of the plan, {} days remaining.'.format(
                count, round(day / delta_days * 100) + 1, delta_days - day),
        )
        event.make_all_day()
        events.append(event)

        if not plaid:
            sleep(1 / delta_days)

    return events
