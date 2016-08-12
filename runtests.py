import os
import sys


def runtests(tests_to_run):
    test_dir = os.path.dirname(__file__)
    sys.path.insert(0, test_dir)
    os.environ['DJANGO_SETTINGS_MODULE'] = 'tests.settings'

    import django
    from django.test.utils import get_runner
    from django.conf import settings

    django.setup()

    TestRunner = get_runner(settings)
    test_runner = TestRunner(verbosity=1, interactive=True)
    failures = test_runner.run_tests(tests_to_run or ['.'])
    sys.exit(failures)


if __name__ == '__main__':
    runtests(sys.argv[1:])
