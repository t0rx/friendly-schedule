# friendly-schedule
Python library for parsing human-friendly schedule strings, e.g.:
```
Mon-Fri: 11:00-12:30, 14:00-15:00
```

More detailed notes to follow.

Basic env setup
---------------

```bash
python3 -m venv ~/friendly-schedule
cd friendly-schedule
git clone https://github.com/t0rx/friendly-schedule.git .
pip3 install pytest pylint flake8
```

Use `script/lint` and `script/test` to check changes before committing.
