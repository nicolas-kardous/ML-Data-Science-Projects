test = {   'name': 'q6',
    'points': 1,
    'suites': [   {   'cases': [   {   'code': ">>> 'Hour' in calls.columns\n"
                                               'True',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> set(calls["Hour"]) == '
                                               'set(range(24))\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> list(calls["Hour"][:5]) == '
                                               '[22, 21, 20, 8, 13]\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> '
                                               "np.allclose(calls['Hour'].mean(), "
                                               '13.35823)\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
