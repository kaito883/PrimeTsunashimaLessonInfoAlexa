
#from datetime import datetime, timedelta, timezone
import datetime
import calendar
#print(soup)


def getTargetTimeFromMap(day, lesson_name):
	group_power_map = { 'Monday':'14:50-15:35と21:20-22:05', 'Tuesday':'15:20', 'Wednesday':'21:25-22:25', 'Thursday':'', 'Friday':'', 'Saturday':'15:20-16:20', 'Sunday':'16:20-17:20'}
	group_blast_map = { 'Monday':'22:15-23:00', 'Tuesday':'13:40-14:40', 'Wednesday':'', 'Thursday':'', 'Friday':'', 'Saturday':'16:35-17:35', 'Sunday':''}
	timeString = ''
	if lesson_name == 'groupPower':
		timeString = group_power_map[day]
	if lesson_name == 'groupBlast':
		timeString = group_blast_map[day]
	else:
		timeString == ''

	return timeString

def createGroupPowerText(day):
	if getTargetTimeFromMap(day, 'groupPower') == '':
		text = '本日、グループパワーはありません。'
	else:
		text = 'グループパワーは、' + getTargetTimeFromMap(day, 'groupPower') + 'です。' 
	return text

def createGroupBlastText(day):
	if getTargetTimeFromMap(day, 'groupBlast') == '':
		text = '本日、グループブラストはありません。'
	else:
		text = 'グループブラストは、' + getTargetTimeFromMap(day, 'groupBlast') + 'です。'
	return text

def createText():
	text = '情報を取得できませんでした。'
	day = ''
	weekday = datetime.date.today().weekday()
	day = calendar.day_name[weekday]
	print(day)
	text = '本日のプライム綱島のレッスン情報です。' + \
			createGroupPowerText(day) + \
			createGroupBlastText(day)
	return text

def createResponse():
	text = createText()

	response = {
       'version': '1.0',
       'response': {
           'outputSpeech': {
               'type': 'PlainText',
               'text': text
           }
       }
   }
	return response


#lambdaのmain処理
def lambda_handler(event, context):
	response = createResponse()
	return response


#デバッグ用
print(createResponse())
#print(lambda_handler())
