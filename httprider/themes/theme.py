import logging

from PyQt5.QtWidgets import QProxyStyle, qApp

from httprider.core.pygment_styles import styles_from_file


class Theme(QProxyStyle):
    def __init__(self):
        super(Theme, self).__init__()

    def load_palette(self, palette):
        qApp.setPalette(palette)

    def load_stylesheet(self, theme_mode):
        filename = ":/themes/{}.qss".format(theme_mode)

        styles = styles_from_file(filename)
        qApp.setStyleSheet(styles) if styles else self.log_error(filename)

    def log_error(self, styles_file):
        logging.error(f"Unable to read file from {styles_file}")
