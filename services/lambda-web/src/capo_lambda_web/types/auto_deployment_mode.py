"""Generated from Smithy shape ``com.amazonaws.lambdaweb#AutoDeploymentMode``."""

from typing import Literal, TypeAlias, cast

"""<p>The auto-deployment mode for a web function endpoint.</p> <p>Valid values:</p> <ul> <li> <p> <code>LatestRevision</code> – The endpoint automatically serves the newest revision.</p> </li> <li> <p> <code>Disabled</code> – Revision routing stays fixed until you change it.</p> </li> </ul>"""
AutoDeploymentMode: TypeAlias = Literal[
    "LatestRevision",
    "Disabled",
]


# --- restJson1 ser/de ---
def serialize_json(value: AutoDeploymentMode) -> str:
    return value


def deserialize_json(data: str) -> AutoDeploymentMode:
    return cast(AutoDeploymentMode, data)
