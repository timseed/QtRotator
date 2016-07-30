import subprocess


class RumLogNg(object):

    def __init__(self):

        self.heading_script = '''tell application "RUMlogNG"
          return headingToCountry
          end tell
        '''

    def get_heading(self):
        try:
            proc = subprocess.Popen(['osascript', '-'],
                                stdin=subprocess.PIPE,
                                stdout=subprocess.PIPE)
            stdout_output = proc.communicate(self.script.encode('utf-8'))[0]
            heading=int(stdout_output)
            print(str.format('Heading is {}  Object Type is  {}',heading,type(proc)))
            return heading
        except Exception as err:
            print(str.format('Error Occurred in RumLogNG error {}',str(err)))
            return -1
