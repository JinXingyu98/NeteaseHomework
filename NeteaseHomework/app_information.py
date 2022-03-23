desired_caps = {
  'platformName': 'Android', # 被测手机是安卓
  'platformVersion': '5.1', # 手机安卓版本
  'deviceName': 'xxx', # 设备名，安卓手机可以随意填写
  'appPackage': 'com.netease.cloudmusic', # 启动APP Package名称
  'appActivity': '.activity.LoadingActivity', # 启动Activity名称
  'unicodeKeyboard': True, # 使用自带输入法，输入中文时填True
  'resetKeyboard': True, # 执行完程序恢复原来输入法
  'noReset': True,       # 不要重置App
  'newCommandTimeout': 6000,
  'automationName': 'UiAutomator2'
  # 'app': r'd:\apk\bili.apk',
}