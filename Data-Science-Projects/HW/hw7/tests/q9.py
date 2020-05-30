test = {   'name': 'q9',
    'points': 2,
    'suites': [   {   'cases': [   {   'code': '>>> X_new = np.hstack([X,\n'
                                               '...                  '
                                               'np.ones([len(X), 1])]) # This '
                                               'is adding a coefficient of 1 '
                                               'for the intercept term;\n'
                                               '>>> '
                                               'np.isclose(lr_loss(np.array([0, '
                                               '0]), X_new, Y), '
                                               '0.69314718055994529)\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> beta = '
                                               'np.array([lr.coef_[0][0],\n'
                                               '...                   '
                                               'lr.intercept_[0]]);\n'
                                               '>>> np.isclose(lr_loss(beta, '
                                               'X_new, Y), '
                                               '0.34566168837055461)\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
