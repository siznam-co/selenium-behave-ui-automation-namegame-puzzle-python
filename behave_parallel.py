import os
import argparse
import multiprocessing

BROWSER_NUM = 3
FORMATTER = "allure_behave.formatter:AllureFormatter"


def parse_arguments():
    parser = argparse.ArgumentParser('Running in parallel mode.')
    parser.add_argument('--feature', '-f', help='Please specify feature you want to run.')
    parser.add_argument('--processes', '-p', type=int, help='Maximum number of processes. Default = 5', default=3)
    parser.add_argument('--tags', '-t', help='Please specify behave tags to run')
    return parser.parse_args()


def get_browser_type(n):
    return {
        0: "chrome",
        1: "firefox",
        # 2: "safari",
    }.get(n, "chrome")


def clear_json_reports(path="reports"):
    cur_dir = os.getcwd()
    for root, dirs, files in os.walk("{}/{}".format(cur_dir, path)):
        for f in files:
            if f.endswith(".json"):
                file_path = "{}/{}/{}".format(cur_dir, path, f)
                os.remove(file_path)


def generate_cmd(num, args):
    browser_type = get_browser_type(num % BROWSER_NUM)
    cmd = ("behave --define browser={} -f {} -o reports/ ".format(browser_type, FORMATTER))
    if args.tags:
        tags = args.tags.split(",")
        cmd = "{} --tags ".format(cmd)
        for tag in tags:
            cmd = "{}@{},".format(cmd, tag)
        cmd = cmd[:-1]

    if args.feature:
        features = args.feature.split(",")
        for feature in features:
            cmd = "{} ./features/{} ".format(cmd, feature.strip())
    else:
        cmd = "{} ./features".format(cmd)

    return cmd.strip()


def run(number, args):
    os.system(generate_cmd(number, args))


def main():
    args = parse_arguments()
    procs = []
    try:
        for i in range(args.processes-1):
            p = multiprocessing.Process(target=run, args=(i, args,))
            procs.append(p)
            p.start()
        [p.join() for p in procs]
    except Exception as e:
        print(e)
        pass
    finally:
        [p.close() for p in procs]
        procs.clear()


if __name__ == "__main__":
    clear_json_reports("reports")
    main()
