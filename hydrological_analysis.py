# -*- coding: utf-8 -*-

"""
/***************************************************************************
                                 A QGIS plugin
 Hydrological Analysis Stream Network
                              -------------------
        begin                : 2026-01-13
        copyright            : (C) 2026 by Giuseppe Cosentino
        email                : giuseppe.cosentino@cnr.it
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""

__author__ = 'Giuseppe Cosentino, Francesco Pennnica'
__date__ = '2026-01-13'
__copyright__ = '(C) 2026 by Giuseppe Cosentino, Francesco Pennnica'

# This will get replaced with a git SHA1 when you do a git archive

import os
from qgis.PyQt.QtWidgets import QAction, QToolBar
from qgis.PyQt.QtGui import QIcon
from qgis.core import QgsApplication
from .hydrological_analysis_provider import HydrologyProvider


class HydrologyPlugin:

    def __init__(self, iface):
        self.iface = iface
        self.provider = None
        self.toolbar = None
        self.action = None

    def initProcessing(self):
        """Inizializza e registra il provider nel Processing Framework."""
        self.provider = HydrologyProvider()
        QgsApplication.processingRegistry().addProvider(self.provider)

    def initGui(self):
        """Chiamato da QGIS quando il plugin viene caricato nell'interfaccia."""
        self.initProcessing()

        # --- Icona nella barra degli strumenti ---
        icon_path = os.path.join(os.path.dirname(__file__), 'icon.png')
        icon = QIcon(icon_path)

        # Crea il QAction con icona e tooltip
        self.action = QAction(icon, 'Hydrology Analysis', self.iface.mainWindow())
        self.action.setToolTip('Open Hydrology Analysis')
        self.action.triggered.connect(self.run)

        # Aggiunge l'azione alla barra degli strumenti dei plugin (quella di QGIS)
        self.iface.addToolBarIcon(self.action)

        # (Opzionale) Crea una toolbar DEDICATA al plugin invece di usare quella comune
        # Decommenta le righe seguenti se preferisci una toolbar separata:
        #
        # self.toolbar = self.iface.addToolBar('Hydrology Analysis')
        # self.toolbar.setObjectName('HydrologyAnalysisToolbar')
        # self.toolbar.addAction(self.action)

        # Aggiunge anche la voce nel menu "Plugins" (opzionale ma consigliato)
        self.iface.addPluginToMenu('Hydrology Analysis', self.action)

    def unload(self):
        """Chiamato quando il plugin viene disattivato: rimuove tutti gli elementi GUI."""
        # Rimuove l'icona dalla toolbar
        self.iface.removeToolBarIcon(self.action)

        # Rimuove la voce dal menu Plugins
        self.iface.removePluginMenu('Hydrology Analysis', self.action)

        # Dealloca l'action
        del self.action

        # (Se hai usato toolbar dedicata, decommentare):
        # if self.toolbar:
        #     self.toolbar.deleteLater()

        # Rimuove il provider dal Processing Framework
        QgsApplication.processingRegistry().removeProvider(self.provider)

    def run(self):
        """
        Trova dinamicamente il primo algoritmo del provider e apre la sua
        finestra di dialogo. Nessun ID hardcoded: funziona sempre.
        """
        from qgis import processing

        # Recupera il provider tramite il suo id()
        provider = QgsApplication.processingRegistry().providerById(
            self.provider.id()
        )

        if not provider:
            self.iface.messageBar().pushWarning(
                'Hydrology', 'Provider non trovato nel registro Processing.'
            )
            return

        algorithms = provider.algorithms()
        if not algorithms:
            self.iface.messageBar().pushWarning(
                'Hydrology', 'Nessun algoritmo trovato nel provider.'
            )
            return

        # Apre la dialog del primo (o unico) algoritmo
        processing.execAlgorithmDialog(algorithms[0].id())