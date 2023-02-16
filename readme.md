# studyplan

This app will help you plan and schedule your exam preparation routines. You just need to specify the tasks and the deadline. The app will output an iCal file, which you can then import into your calendar app or website.

```console
$ studyplan --finish "in 2 month" --output "IELTS.ics" --tasks "speaking" "listening" "reading" "writing"
```

![Example of the Generated Plan](https://user-images.githubusercontent.com/25728414/219512527-7be91cc1-7e69-4a6b-9224-96f40c7ae730.png)

## Installation

Use `pip` to install the package:

```console
$ pip install studyplan
```

Or you can install directly from source. Clone the repository and execute the following command:

```console
$ python setup.py install
```