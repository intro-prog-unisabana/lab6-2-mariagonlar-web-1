def trigger_alarm(temperatures, threshold):
    triggered_sensors = []
    for sensor in temperatures:
        if temperatures[sensor] > threshold:
            triggered_sensors.append(sensor)
    return triggered_sensors
