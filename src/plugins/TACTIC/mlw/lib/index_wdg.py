###########################################################
#
# Copyright (c) 2020, Southpaw Technology
#                     All Rights Reserved
#
# PROPRIETARY INFORMATION.  This software is proprietary to
# Southpaw Technology, and is not to be reproduced, transmitted,
# or disclosed in any way without written permission.
#
#
#
from pyasm.web import DivWdg, HtmlElement
from pyasm.biz import Project, ProjectSetting
from pyasm.search import Search
from pyasm.common import Environment
from pyasm.web import DivWdg

from tactic.ui.bootstrap_app import BootstrapIndexWdg, BootstrapTopNavWdg



__all__ = ['MLWIndexWdg', 'MLWTopNavWdg']

class MLWIndexWdg(BootstrapIndexWdg):

    def _get_tab_save_state(self):
        return "mlw_main_body_tab_state"


    def get_start_link(self):
        return "/dashboard"

    def _get_top_nav_xml(self):

        class_name = 'TACTIC.mlw.MLWTopNavWdg'

        return """
            <element name="top_nav">
              <display class="%s">
              </display>
            </element>""" % class_name


class MLWTopNavWdg(BootstrapTopNavWdg):
   
    def get_logo_div(self):

        div = super(MLWTopNavWdg, self).get_logo_div()

        div.add(''' <div style="margin-left: 10px; font-size: 22px")>MLW</div>''')

        return div
