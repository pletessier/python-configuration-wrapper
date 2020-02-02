import unittest

from python_configuration_wrapper import config


class TestCase(unittest.TestCase):
    def test(self):
        self.assertEqual(config.database.host, "my-dh-host.com")
        self.assertEqual(config.database.port, 5432)
        self.assertEqual(config.logging.level, "INFO")
        self.assertEqual(config.database.name, "postgres")
        self.assertEqual(config.database.user, "root")
        self.assertEqual(config.database.password, "123456")


if __name__ == '__main__':

    config.pprint()

    TestCase().test()
