# studyplan

A tiny utility that schedules your exams preparation routines. You only need to specify the tasks and the deadline. App will output a iCal file, that you can than import to your calendar application or website.

```console
$ studyplan --finish "in 3 month" --output "English Exam.ics" --tasks "essey" "describe a picture" "write a letter" "compare two pictures"
```

![](https://i.imgur.com/QojYhoy.png)

## Installation

Use `pip` to install the package:

```console
$ pip install studyplan
```

Or you can install directly from source. Clone the repository and execute the following command:

```console
$ python setup.py install
```