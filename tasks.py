from invoke import task


@task
def run(context, browser="", tags="", resolution=""):
    behave_cmd = "behave"
    if browser != "":
        behave_cmd = f"{behave_cmd} -D browser={browser}"
    if tags != "":
        behave_cmd = f"{behave_cmd} --tags={tags}"
    if resolution != "":
        behave_cmd = f"{behave_cmd} -D resolution={resolution}"
    context.run(behave_cmd)


@task
def run_with_allure(context, browser="", tags="", resolution=""):
    behave_cmd = "behave -f allure_behave.formatter:AllureFormatter -o artifacts -f pretty"
    if browser != "":
        behave_cmd = f"{behave_cmd} -D browser={browser}"
    if tags != "":
        behave_cmd = f"{behave_cmd} --tags={tags}"
    if resolution != "":
        behave_cmd = f"{behave_cmd} -D resolution={resolution}"
    context.run(behave_cmd)
