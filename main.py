def calc_temp(adc_count: number):
    global r_therm, t_kelvin
    # Calculate the temperature in deg C of an NTC
    # thermistor given an ADC count using the Beta equation.
    # Thermistor r0 is 10kOhm, thermistor Beta is 3988.
    r_therm = 10000 * (1023 / adc_count - 1)
    t_kelvin = 1 / (1 / (273.15 + 25) + 1 / 3988 * Math.log(r_therm / 10E3))
    return t_kelvin - 273.15
t_kelvin = 0
r_therm = 0
basic.show_icon(IconNames.YES)

def on_forever():
    serial.write_value("temp", calc_temp(pins.analog_read_pin(AnalogPin.P0)))
    basic.pause(100)
basic.forever(on_forever)
