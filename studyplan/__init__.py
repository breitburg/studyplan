from argparse import ArgumentParser
from ics.icalendar import Calendar
from maya import when

from studyplan.scheduler import schedule


def main() -> None:
    parser = ArgumentParser(prog='studyplan')

    parser.add_argument(
        '-t', '--tasks', type=str,
        nargs='+',
        help='list of tasks to be done',
        required=True,
    )
    parser.add_argument('-pd', '--per-day', type=int,
                        default=3, help='unique tasks per day')
    parser.add_argument('-c', '--count', type=int,
                        default=5, help='each tasks goal per day')
    parser.add_argument('-f', '--finish', type=str,
                        default='in 1 month',
                        help='plan finish date')
    parser.add_argument('-b', '--begin', type=str,
                        default='now',
                        help='plan begin date')
    parser.add_argument('-o', '--output', type=str,
                        default='plan.ics',
                        help='output file path')

    args = parser.parse_args()
    calendar = Calendar()

    calendar.events = schedule(
        tasks=args.tasks,
        begin=when(args.begin),
        finish=when(args.finish),
        per_day=args.per_day,
        count=args.count,
    )

    open(file=args.output, mode='w').writelines(calendar)
    print('👓 Your study plan was saved at {}'.format(args.output))
