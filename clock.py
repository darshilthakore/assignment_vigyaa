def getTime(time):

	digits = {1: 'One', 2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five', \
             6: 'Six', 7: 'Seven', 8: 'Eight', 9: 'Nine', 10: 'Ten', \
            11: 'Eleven', 12: 'Twelve', 13: 'Thirteen', 14: 'Fourteen', \
            15: 'Fifteen', 16: 'Sixteen', 17: 'Seventeen', 18: 'Eighteen', \
            19: 'Nineteen', 20: 'Twenty', 30: 'Thirty', 40: 'Forty', \
            50: 'Fifty', 60: 'Sixty', 70: 'Seventy', 80: 'Eighty', \
            90: 'Ninety', 0: 'Zero'}


	hour, minutes = time.split(":")
	mins = int(minutes)

	if (int(hour) > 12) or (int(hour) < 1) or (mins < 0) or (mins > 59):
		return "ENter time in valid format 1-12 hour and 00-59 minutes"

	if mins == 0:
		return f"{digits[int(hour)]} o' clock"

	if (1 <= mins <= 30):
		if (mins <= 10):
			return f"{digits[int(hour)]} past {digits[mins]}"
		if (mins == 15):
			return f"quarter past {digits[int(hour)]}"
		if (mins == 30):
			return f"half past {digits[int(hour)]}"
		else:
			try:
				return f"{digits[mins]} minutes past {digits[int(hour)]}"
			except KeyError:
				return f"{digits[mins-mins%10]} {digits[mins%10]} minutes past {digits[int(hour)]}"


	if (31 <= mins <= 59):
		if (mins == 45):
			return f"quarter to {digits[int(hour) % 12 + 1]}"
		try:
			return f"{digits[60 - mins]} minutes to {digits[int(hour) % 12 + 1]}"
		except KeyError:
			return f"{digits[(60-mins)-(60-mins)%10]} {digits[(60-mins)%10]} minutes to {digits[int(hour) % 12 + 1]}"

print("Enter a time in format HH:MM")
time = str(input())
ans = getTime(time)
print(ans)