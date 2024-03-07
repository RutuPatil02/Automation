from selenium.webdriver import Chrome


# def before_feature(context,feature):    ********** executes before given feature
# def before_scenario(context,scenario):   ********** executes before given scenario

# executes before all
def before_all(context):
    context.driver = Chrome()


def after_all(context):
    context.driver.close()
    