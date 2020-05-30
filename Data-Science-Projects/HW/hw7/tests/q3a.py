test = {   'name': 'q3a',
    'points': 2,
    'suites': [   {   'cases': [   {   'code': '>>> len(betas_used)\n21',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> len(betas_used) == '
                                               'len(losses_calculated) # beta '
                                               'history and loss history have '
                                               '21 items in them\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> betas_used[0].shape == '
                                               '(2,) # beta history contains '
                                               'beta values\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> '
                                               'np.isscalar(losses_calculated[0]) '
                                               '# loss history is a list of '
                                               'scalar values, not vector\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> '
                                               'np.isscalar(losses_calculated[0]) '
                                               '# loss is decreasing\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
