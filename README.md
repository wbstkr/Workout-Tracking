# Workout-Tracking

[![Python][python-shield]][python-url]

A command line tool to extract workout data from markdown files.

## Features

- Handles isotonic, isometric, and body weight exercises.
- Able to track changes in weight for isotonic exercises.

## Installation

Clone the repository and install the package using pip:

```bash
git clone https://github.com/wbstkr/Workout-Tracking.git
cd Workout-Tracking
pip install .
```

## Usage

The CLI accepts one or more files or directories and outputs a compiled JSON dictionary of your workout history.

```bash
# Parse a single file
workout-tracking data/2026-09-28.md

# Parse a directory recursively
workout-tracking data/ -r

# Advanced filtering and custom headings
workout-tracking archive/ data/ -r --filter "2026-*" --heading "Workout"
```

### Options

* `paths` (required): One or more file or directory paths.
* `-r`, `--recursive`: Recursively scan any provided directories.
* `-f`, `--filter`: Filename pattern to match when scanning directories (default: `*`).
* `-H`, `--heading`: The markdown heading to extract data from (default: `Workout`).

### Expected Input

```md
# Gym
Dumbbell Curls 25lbs 12 10 8 20lbs 30
Pushups bw 20 15 10
Plank 60s 45s 30s
```

---

### Omar Faruque

[![GitHub][github-shield]][github-url]
[![LinkedIn][linkedin-shield]][linkedin-url]
[![Email][email-shield]][email-url]

<!-- Shields -->

[python-shield]: https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white
[python-url]: https://python.org

[github-shield]: https://img.shields.io/badge/GitHub-000000?style=for-the-badge&logo=github&logoColor=white
[github-url]: https://github.com/wbstkr

[linkedin-shield]: https://img.shields.io/badge/LinkedIn-0000FF?style=for-the-badge&logo=linkedin&logoColor=white
[linkedin-url]: https://linkedin.com/in/wbstkr

[email-shield]: https://img.shields.io/badge/Email-000000?style=for-the-badge&logo=gmail&logoColor=white
[email-url]: mailto:ofaruque245@gmail.com