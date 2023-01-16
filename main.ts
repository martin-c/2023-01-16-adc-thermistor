function calc_temp (adc_count: number) {
    // Calculate the temperature in deg C of an NTC
    // thermistor given an ADC count using the Beta equation.
    // Thermistor r0 is 10kOhm, thermistor Beta is 3988.
    r_therm = 10000 * (1023 / adc_count - 1)
    t_kelvin = 1 / (1 / (273.15 + 25) + 1 / 3988 * Math.log(r_therm / 10E3))
    return t_kelvin - 273.15
}
let t_kelvin = 0
let r_therm = 0
basic.showIcon(IconNames.Yes)
basic.forever(function () {
    serial.writeValue("temp", calc_temp(pins.analogReadPin(AnalogPin.P0)))
    basic.pause(100)
})
