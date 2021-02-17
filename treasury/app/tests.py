from django.test import TestCase

# Create your tests here.


from TQapis.TQTest import run_test_all, run_test_single


def test_all():
    email = "test.account@treasuryquants.com"  # <- this is your active email account
    target_url = "http://operations.treasuryquants.com"  # <-this is your target url
    # target_url = "http://192.168.1.80:8080"# this is for shahram's local server

    folder = "./test_files"  # <- test all files for reporting
    report = dict()

    #
    # run all the files inside a folder
    #
    report = run_test_all(folder, email, target_url)

    #
    # run a single test file
    #
    # single_file_name = "test_account_ip_change"  # <- test a single file for debugging
    # report = run_test_single(folder, single_file_name, email,  target_url)

    is_success = True
    for key, value in report.items():
        if value.lower() != 'ok':
            is_success = False
            #print("Failed on {}".format(key))
    return is_success

print(test_all()) # the return of this function is a single bollean dictating whether the test as passed or failed.