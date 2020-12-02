def add_time(start, duration, start_day = None):
  
  # Splitting the start time string
  start_time_s, start_am_or_pm = start.split()
  start_hour, start_minute = map(int, start_time_s.split(':'))

  # Splitting the duration time string
  dur_hour, dur_minute = map(int, duration.split(':'))

  # Adding the start and duration minutes
  end_minute = (start_minute + dur_minute) % 60

  # Number of days
  n = (dur_hour // 24)
  days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']

  # Adding the start and duration hours
  carry_hour = (start_minute + dur_minute) // 60
  end_hour = start_hour + dur_hour + carry_hour
  end_am_or_pm = start_am_or_pm 
  if end_hour >= 12:
    # If the end hour is a multiple of 12
    if end_hour % 12 == 0:
      end_hour = 12
    elif end_hour % 12 != 0:
      end_hour = end_hour % 12
    # If only hours in terms of days are added
    if (dur_hour % 24 == 0 and dur_minute == 0):
      end_am_or_pm = start_am_or_pm
    elif (dur_hour % 24 != 0 or dur_minute != 0):
      if start_am_or_pm == 'AM':
        end_am_or_pm = 'PM'
      elif start_am_or_pm == 'PM':
        end_am_or_pm = 'AM'
        n += 1
  
  # Building the end time string
  end_hour_s, end_minute_s = str(end_hour), str(end_minute)
  if len(end_minute_s) == 1:
    end_minute_s = '0' + end_minute_s
  end_time = end_hour_s + ':' + end_minute_s + ' ' + end_am_or_pm

  # Determining the additional number of days
  if n == 1:
    num_days = "(next day)"
  elif n > 1:
    num_days = "({} days later)".format(n)

  # Determining the end day
  if start_day != None:
    start_day_idx = days.index(start_day.lower())
    end_day_idx = (start_day_idx + n) % (len(days))
    end_day = days[end_day_idx].capitalize()
  
  # Building the new time string
  new_time = end_time
  if start_day != None:
    new_time += ', ' + end_day
  if n > 0:
    new_time += ' ' + num_days

  return new_time