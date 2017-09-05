# -*- coding: utf-8 -*-
"""
/***************************************************************************
 TestLaunch
                                 A QGIS plugin
 Trying to launch a plugin from another plugin
                             -------------------
        begin                : 2017-08-24
        copyright            : (C) 2017 by Kasper Skjeggestad
        email                : kasper.skjeggestad@gmail.com
        git sha              : $Format:%H$
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load TestLaunch class from file TestLaunch.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .TestLaunch import TestLaunch
    return TestLaunch(iface)
