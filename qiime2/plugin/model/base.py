# ----------------------------------------------------------------------------
# Copyright (c) 2016-2018, QIIME 2 development team.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file LICENSE, distributed with this software.
# ----------------------------------------------------------------------------

from qiime2.core.format import FormatBase


__all__ = ['FormatBase', 'ValidationError', '_check_validation_level']


class ValidationError(Exception):
    pass


# TODO: once sniff is dropped, move this up into FormatBase as validate method
def _check_validation_level(level):
    if level not in ('min', 'max'):
        raise ValueError('Invalid validation level requested (%s), must '
                         'be \'min\' or \'max\'.' % level)
