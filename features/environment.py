import json
import os
from utils.browsers import browsers
from utils.rp_driver import (start_launcher, start_feature_test, timestamp, start_scenario_test,
                             log_step_result, finish_launcher, terminate_service,
                             finish_scenario_test, finish_feature, start_step_test, finish_step_test)
from utils.paths import project_path
from utils.general import get_browser_name


def before_all(context):
    pass


def before_feature(context, feature):
    pass


def before_scenario(context, scenario):
    default_browser = get_browser_name()
    context.browser = browsers(context, context.config.userdata.get("browser", default_browser))
    #context.browser = browsers(context, context.config.userdata.get("browser", 'Chrome'))


def before_step(context, step):
    pass


def after_step(context, step):
    pass


def after_scenario(context, scenario):
    if scenario.status.name != 'passed':
        if not os.path.isdir(project_path.join("screenshots").strpath):
            os.mkdir(project_path.join("screenshots").strpath)
        context.browser.save_screenshot(project_path.join("screenshots",
                                                          f"{context.scenario.name}_screenshot.png").strpath)
    context.browser.quit()


def after_feature(context, feature):
    pass


def after_all(context):
    pass