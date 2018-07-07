import os
apk = {'j': 'com.seckawijoki.androidtest',
       'h': 'com.miniteck.miniworld'}
print 'enter \'j\' to test com.seckawijoki.androidtest'
print 'enter \'h\' to test com.miniteck.miniworld'
#choose apk
while True:
    test_apk = raw_input('which apk do you want to test?\n(\'h\' or \'j\'):')
    try:
        apk_name = apk[test_apk]
    except KeyError:
        print 'Please enter \'j\' or \'h\'! - -#'
    else:
        break
#check the input value
while True:
    event_num = raw_input('How many pseudo random events(-v) do you want?\nenter int num(>0):')
    if event_num.isdigit() and int(event_num) > 0:
        print 'OK, your events are ' + event_num
        break
    else:
        print 'Please enter a number and the number > 0'
#check the input value
while True:
    for_time = raw_input('How many times monkey test do you want?\ntimes(>1):')
    if for_time.isdigit() and int(for_time) > 1:
        print 'OK, you want to loop ' + for_time + ' times monkey test'
        break
    else:
        print 'Please enter a number and the number > 1'
#the log path
log_path = 'F:\\monkey_log\\'
#the log name
log_name = 'monkeytestlog.txt'
#monkey shell script
monkey_shell = 'adb shell monkey -v -v -v -p '+ apk_name+ ' -v ' + event_num + ' >'+log_path

def monkeytest():
    print 'now let\'s check your phone'
    phonedevice = os.popen('adb devices').read()
    if phonedevice.strip().endswith('device'):
        print 'OK, your phone get ready,let\'s start moneky test!'
        for i in range(1, int(for_time)+1):
            print 'The', i, 'monkey test starting...'
            os.system(monkey_shell+str(i)+log_name)
            print i, 'complete!'
        print 'OK, moneky test all complete! The log is in ' + log_path
    else:
        print 'please check your phone has linked your computer well'

#find 'adb' command at your os
sysPath = os.environ.get('PATH')
if not sysPath.find('platform-tools'):
    print '''please install the android-sdk and put the 'platform-tools' dir in your system PATH'''
else:

    #kill the 'tadb.exe'
    tadb = os.popen('tasklist').read()
    if tadb.find('tadb.exe') != -1:
        print 'Find \'tadb.exe\', it must be killed!!!!!!'
        os.system('taskkill /im tadb.exe /F')
        print 'OK,the \'tadb.exe\' has been killed, let\'s go on'
        monkeytest()
    else:
        print 'not find \'tadb.exe\',great! go on!'
        monkeytest()