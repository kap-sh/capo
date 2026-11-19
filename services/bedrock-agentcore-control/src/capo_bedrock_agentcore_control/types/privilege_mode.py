"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#PrivilegeMode``."""

from typing import Literal, TypeAlias, cast

"""<p>The privilege mode of the agents, either <code>STANDARD</code> (the default) or <code>PRIVILEGED</code>.</p>"""
PrivilegeMode: TypeAlias = Literal[
    "STANDARD",
    "PRIVILEGED",
]


# --- restJson1 ser/de ---
def serialize_json(value: PrivilegeMode) -> str:
    return value


def deserialize_json(data: str) -> PrivilegeMode:
    return cast(PrivilegeMode, data)
