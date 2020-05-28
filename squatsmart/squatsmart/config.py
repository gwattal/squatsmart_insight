# config.py

from pathlib import Path  # pathlib is seriously awesome!

data_dir = Path('/path/to/some/logical/parent/dir')
data_path = data_dir / 'my_file.csv'  # use feather files if possible!!!

customer_db_url = 'sql:///customer/db/url'
purchases_db_url = 'sql:///purchases/db/url'
