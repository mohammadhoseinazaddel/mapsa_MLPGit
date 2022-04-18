https://stackoverflow.com/questions/14848274/git-log-to-get-commits-only-for-a-specific-branch

```git
git cherry -v develop UI-5636
```
https://stackoverflow.com/questions/38495989/how-to-get-git-parent-branch-name-from-current-branch
```git
git merge-base UI-5636 develop
```
## logging
```python
import logging

logging.basicConfig(filename='test.log', format='%(filename)s: %(message)s',
                    level=logging.DEBUG)

logging.debug('This is a debug message')
logging.info('This is an info message')
logging.warning('This is a warning message')
logging.error('This is an error message')
logging.critical('This is a critical message'

import logging.handlers
            file_handler = logging.FileHandler('/var/log/sab-ui-cmd.log')
            cmd_logger = logging.getLogger("ui-cmd")
            cmd_logger.addHandler(file_handler)
            cmd_logger.error('Monitoring:%s', str_command.cout)
            cmd_logger.removeHandler(file_handler)
            
import logging
import sys

logger = logging.getLogger()
logger.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s | %(levelname)s | %(message)s', 
                              '%m-%d-%Y %H:%M:%S')

stdout_handler = logging.StreamHandler(sys.stdout)
stdout_handler.setLevel(logging.DEBUG)
stdout_handler.setFormatter(formatter)

file_handler = logging.FileHandler('logs.log')
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)
logger.addHandler(stdout_handler)
```
