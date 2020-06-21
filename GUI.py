"""
References:
- https://github.com/PySimpleGUI/PySimpleGUI/blob/master/DemoPrograms/Demo_Design_Pattern_Multiple_Windows3.py
"""

import PySimpleGUI as sg
import time

from src.SourceFiles import SourceFiles
from src.SimpleCopy import SimpleCopy

sg.theme('SystemDefault')
blue = '#005CAE'
today_date = time.strftime('%m-%d-%Y')


def generate_window2(directory):
    column_copy = [
        [sg.Text('I Fcked Up; Save Me', font=('Helvetica', 25), size=(40, 1), justification='center')],
        [sg.Text('* Backup Module Toolkit, @sonbyj01, MIT License, v0.1.')],
        [sg.Text('Date: {}'.format(today_date))],
        [sg.Text("Source Folder:", font=('Helvetica', 15), size=(40, 1), justification='center')],
        [sg.Text('{}'.format(directory), justification='center')],
        [sg.Button('Simple Copy', button_color=('white', blue))],
        [sg.Text('Status', justification='left')],
        [sg.Listbox(values=[], size=(80, 20), key='_STATUS_')]
    ]

    return [
        [sg.Column(column_copy, element_justification='center')],
        [sg.Button('Exit', button_color=('white', blue))]
    ]


class GUI:
    column_source = [
        [sg.Text('I Fcked Up; Save Me', font=('Helvetica', 25), size=(20, 1), justification='center')],
        [sg.Text('* Backup Module Toolkit, @sonbyj01, MIT License, v0.1.')],
        [sg.Text('Date: {}'.format(today_date))],
        [sg.Text('Source Folder', font=('Helvetica', 15), size=(20, 1), justification='center')],
        [sg.Button('Choose', button_color=('white', blue))]
    ]

    layout_source = [
        [
            sg.Column(column_source, element_justification='center')
        ],
        [
            sg.Button('Exit', button_color=('white', blue))
        ]
    ]

    def __init__(self):
        self.event_log = list()
        self.window = sg.Window('Backup Module GUI Source Selection', self.layout_source, element_padding=(5, 5))
        self.window2_active = False

        while True:
            if not self.window2_active:
                event1, values1 = self.window.read()
                if event1 is None or event1 == 'Exit':
                    break

                elif event1 == 'Choose':
                    self.window2_active = True
                    directory = sg.popup_get_folder('Source Folder: ',
                                                    title='Source',
                                                    button_color=('white', blue),
                                                    keep_on_top=True, )

                    if directory != '':
                        if directory is not None:
                            self.window.hide()
                            layout_copy = generate_window2(directory)
                            window2 = sg.Window('Backup Module GUI Copy',
                                                layout_copy,
                                                # resizable=True,
                                                finalize=True)
                            source_files = SourceFiles(directory)
                            self._update_status(window2.Element('_STATUS_'),
                                                custom_mes=True,
                                                message='Source File Object Initialized')

            if self.window2_active:
                event2, values2 = window2.read()
                print(event2)

                if event2 in (sg.WIN_CLOSED, 'Exit'):
                    self.window2_active = False
                    window2.close()
                    self.window.un_hide()

                if event2 == 'Simple Copy':
                    print('Simple Copy')
                    directory = sg.popup_get_folder('Target Folder: ',
                                                    title='Target',
                                                    button_color=('white', blue),
                                                    keep_on_top=True, )
                    self._update_status(window2.Element('_STATUS_'),
                                        start=True,
                                        command='Simple Copy')
                    SimpleCopy(source_files).simple_copy2(directory)
                    self._update_status(window2.Element('_STATUS_'),
                                        start=False,
                                        command='Simple Copy')

        self.window.close()

    def _update_status(self, status_window, start=False, command='', custom_mes=False, message=''):
        now = time.strftime('%Y-%m-%d %H:%M:%S')

        if custom_mes:
            self.event_log.append('{}:    {}'.format(now, message))
        elif start:
            self.event_log.append('{}:    {} started'.format(now, command))
        elif not start:
            self.event_log.append('{}:    {} finished'.format(now, command))
            self.event_log.append('')

        status_window.Update(values=self.event_log)



def main():
    GUI()


if __name__ == '__main__':
    main()
