import os
import signal
import subprocess


class RumLogNg(object):

    def __init__(self):

        self.heading_script = '''tell application "RUMlogNG"
          return headingToCountry
          end tell
        '''

    def get_heading(self):


        rv = -1
        try:
            proc = subprocess.Popen(['osascript', '-'],
                                stdin=subprocess.PIPE,
                                stdout=subprocess.PIPE)
            stdout_output = proc.communicate(self.heading_script.encode('utf-8'))[0]
            rv =int(stdout_output)

            # The os.setsid() is passed in the argument preexec_fn so
            # it's run after the fork() and before  exec() to run the shell.

            #os.killpg(os.getpgid(proc.pid), signal.SIGTERM)
        except Exception as err:
            print(str.format('Error Occurred in RumLogNG error {}',str(err)))

        return rv