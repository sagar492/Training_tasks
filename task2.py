
l='''telemetry.navigation_event.test_tc1_navigation.TestNavigationForUpgrade.test_navigation	5 min 22 sec	1
telemetry.navigation_event.test_tc2_navigation.TestNavigationForUpgradeLater.test_navigation	2 min 30 sec	1
telemetry.navigation_event.test_tc3_navigation.TestNavigationForErrorScreen.test_navigation	2 min 28 sec	1
telemetry.startup_event.test_tc4_navigation.TestHomeLoadTime.test_navigation	2 min 26 sec	1
telemetry.startup_event.test_tc5_navigation.TestStartupEvent.test_navigation	2 min 30 sec	1'''

#type 1

l1 = l.split('\n')
for i in l1:
##    print((i.split('.'))[2] + '.py')
    l2 =[(item.split('.'))[2] + '.py' for item in l1] 
for i in l2:
    print(i)


#type 2

l1=l.split('.')
ul=[]
ext='.py'
for i in l1:
    if i.endswith('navigation'):
        ul.append(i)
for i in ul:
    print(i+ext)

    
