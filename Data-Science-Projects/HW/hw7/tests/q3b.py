test = {   'name': 'q3b',
    'points': 2,
    'suites': [   {   'cases': [   {   'code': '>>> len(betas_used_decay) == '
                                               'len(losses_calculated_decay) '
                                               '== 21 # beta history and loss '
                                               'history are 20 items in them\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> betas_used_decay[0].shape '
                                               '== (2,) # beta history '
                                               'contains beta values\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> '
                                               'np.isscalar(losses_calculated_decay[0]) '
                                               '# loss history should be a '
                                               'list of values, not vector\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> losses_calculated_decay[1] '
                                               '- losses_calculated_decay[-1] '
                                               '> 0 # loss is decreasing\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
