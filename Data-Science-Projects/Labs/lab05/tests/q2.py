test = {   'name': 'q2',
    'points': 1,
    'suites': [   {   'cases': [   {   'code': '>>> isinstance(answer2, list)\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> all([isinstance(elt, str) '
                                               'for elt in answer2])\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> all([elt in '
                                               "calls['CVLEGEND'].values for "
                                               'elt in answer2])\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> set(answer2) == '
                                               "set(['LARCENY', 'BURGLARY - "
                                               "VEHICLE', 'VANDALISM', "
                                               "'DISORDERLY CONDUCT', "
                                               "'ASSAULT'])\n"
                                               'True',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
