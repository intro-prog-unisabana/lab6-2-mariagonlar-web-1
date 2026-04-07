def trigger_alarm(temperatures, threshold=80):
    triggered_sensors = []
    for sensor in temperatures:
        if temperatures[sensor] > threshold:
            triggered_sensors.append(sensor)
    return triggered_sensors
