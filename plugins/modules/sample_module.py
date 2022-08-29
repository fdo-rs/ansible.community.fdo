#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright: (c) 2022, XLAB Steampunk <steampunk@xlab.si>
#
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function

__metaclass__ = type


DOCUMENTATION = r"""
module: sample_module

author:
  - First Last (@firstlast)
short_description: Sample module
description:
  - TODO
version_added: 0.0.1
# extends_documentation_fragment:
#   - community.fdo.common_something
seealso: []
options:
  filename:
    description:
      - Filename for the message.
    type: str
    required: true
"""

EXAMPLES = r"""
"""

RETURN = r"""
"""


from ansible.module_utils.basic import AnsibleModule

from ..module_utils import errors


def run(module):
    filename = module.params["filename"]
    msg = "debug filename=%s" % filename
    return False, msg


def main():
    module = AnsibleModule(
        supports_check_mode=False,
        argument_spec=dict(
            filename=dict(
                type="str",
                required=True,
            ),
        ),
    )

    try:
        changed, msg = run(module)
        module.exit_json(changed=changed, msg=msg)
    except errors.FdoError as e:
        module.fail_json(msg=str(e))


if __name__ == "__main__":
    main()
