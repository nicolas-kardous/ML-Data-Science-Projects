test = {   'name': 'q3b',
    'points': 2,
    'suites': [   {   'cases': [   {   'code': '>>> df_1972_to_2016.shape\n'
                                               '(51, 12)',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> '
                                               'df_1972_to_2016.index.name\n'
                                               "'State'",
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> '
                                               'all(df_1972_to_2016.columns == '
                                               '[str(x) for x in '
                                               'np.arange(1972, 2017, 4)])\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> df_1972_to_2016.index[-1]\n'
                                               "'Wyoming'",
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> '
                                               'np.all(df_1972_to_2016.applymap(lambda '
                                               "x: str(x) in ['D', 'R']))\n"
                                               'True',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
