import traceback


class Logger:

    def error(self, error):
        print("[ERROR]: {0}".format(error))
        traceback.print_exc()