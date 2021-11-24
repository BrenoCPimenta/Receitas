from datetime import datetime
from pylint import epylint as lint
import os
import env

try:
    with open("log_linter.txt", "a+") as f:
        # Log control statement
        today = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        entrance = f"[LOG] {today}\n"

        # Get packages that will be ANALIZED
        packages = os.environ.get('LINTER_PACKAGES')
        if packages == '':
            raise ValueError("No packages specifed")

        # Get files to be ignored by the analyses
        ignored_files = os.environ.get('LINTER_IGNORED_FILES')
        if ignored_files != '':
            ignored_files = '--ignore='+ignored_files

        # j=0 is to check availability of CPUs to run the analyze
        command = f"{packages} -j 0 {ignored_files}"
        (pylint_stdout, pylint_stderr) = lint.py_run(command, return_std=True)

        # Verifying for execution errors:
        if pylint_stderr.getvalue() != '':
            raise SystemError(pylint_stderr.getvalue())

        # Appending analyses into log file:
        f.write(f"{entrance}\n{pylint_stdout.getvalue()}\n\n\n")
        print("Analysis performed successfully")


except Exception as e:
    print("Well... there was a problem:\n\n" + str(e))
