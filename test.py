import unittest

import readFiles
import specifications


class Tines(unittest.TestCase):
    events = {}
    events['location'] = {'ip': '2a02:8084:2160:4400:4994:d7c2:a1f0:339e',
                          'success': True,
                          'type': 'IPv4',
                          'continent': 'Europe',
                          'continent_code': 'EU',
                          'country': 'Ireland',
                          'country_capital': 'Dublin',
                          'latitude': '53.3165322',
                          'longitude': '-6.3425318',
                          'currency': 'Euro',
                          'currency_code': 'EUR',
                          'currency_symbol': '€',
                          'currency_rates': '0.924078',
                          'currency_plural': 'euros',
                          }
    events['sunset'] = {'results': {'solar_noon': '8:22:20 AM'},
                        'status': 'OK'}
    events["foo"] = {"bar": "World"}
    events["test"] = {"testing": "unit testing"}
    events["convert"] = {"me": "converted"}
    events["dot"] = {"not": "ation"}

    options = (("https://www.robmcelhinney.com/?continent={{location.continent}}&money={{location.currency_plural}}",
                "https://www.robmcelhinney.com/?continent=Europe&money=euros"),
               ("https://www.robmcelhinney.com/?noon={{sunset.results.solar_noon}}&ipType={{location.type}}",
                "https://www.robmcelhinney.com/?noon=8:22:20 AM&ipType=IPv4"),
               ("Hello {{foo.bar}}!", "Hello World!"),
               ("Hello {{foo.bar}!", "Hello {{foo.bar}!"),
               ("Hello {{foo.bar}} }}!", "Hello World }}!"),
               ("Hello {{ {{foo.bar}}!", "Hello {{ World!"),
               ("Hello {{foo.qux}}!", "Hello !"))

    def test_interpolate_option(self):
        for option, result in self.options:
            result_inter = specifications.interpolate_option(self.events, option)
            self.assertEqual(result, result_inter)

    bracket_values = ((["test.testing"], [["test", "testing"]]),
                      (["dot.notation", "convert.me"], [["dot", "notation"], ["convert", "me"]]))

    def test_dot_to_paran(self):
        for value, result in self.bracket_values:
            parantheses_result = specifications.dot_to_paran(value)
            self.assertEqual(result, parantheses_result)

    converted_options = (([['test', 'testing']], "domain/?a={{test.testing}}", "domain/?a=unit testing"),
                         ([['convert', 'me'], ["dot", "not"]], "domain/?a={{convert.me}}&b={{dot.not}}",
                          "domain/?a=converted&b=ation"),
                         )

    def test_get_conv(self):
        for conv_values, value_str, result in self.converted_options:
            conv_result = specifications.get_conv(conv_values, value_str,
                                                  self.events)
            self.assertEqual(result, conv_result)

    def test_fakefile(self):
        result = readFiles.read({"json": "xyz.json"})
        self.assertEqual("IOError. Error reading file.", result)


if __name__ == '__main__':
    unittest.main()
