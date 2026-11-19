"""Generated from Smithy shape ``com.amazonaws.wellarchitected#RemediationType``."""

from typing import Literal, TypeAlias, cast

"""<p>The method by which a recommendation is remediated.</p>"""
RemediationType: TypeAlias = Literal[
    "AUTO_REMEDIATION",
    "CONSOLE",
    "CLI",
    "SDK",
    "IAC",
    "MCP",
]


# --- restJson1 ser/de ---
def serialize_json(value: RemediationType) -> str:
    return value


def deserialize_json(data: str) -> RemediationType:
    return cast(RemediationType, data)
