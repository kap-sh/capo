"""Generated from Smithy shape ``com.amazonaws.lambdaweb#AutoDeploymentMode``."""

from typing import Literal, TypeAlias, cast

"""<p>The auto-deployment mode for a web function endpoint. Possible values: <code>LatestRevision</code> (endpoint automatically serves the newest revision), <code>Disabled</code> (revision routing is fixed until explicitly changed).</p>"""
AutoDeploymentMode: TypeAlias = Literal[
    "LatestRevision",
    "Disabled",
]


# --- restJson1 ser/de ---
def serialize_json(value: AutoDeploymentMode) -> str:
    return value


def deserialize_json(data: str) -> AutoDeploymentMode:
    return cast(AutoDeploymentMode, data)
