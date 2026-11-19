"""Generated from Smithy shape ``com.amazonaws.securityhub#GcpScopeType``."""

from typing import Literal, TypeAlias, cast

"""<p>The type of scope for a GCP connector. Valid values are <code>ORGANIZATION</code> (monitor all projects in the organization) and <code>PROJECT</code> (monitor specific projects).</p>"""
GcpScopeType: TypeAlias = Literal[
    "PROJECT",
    "ORGANIZATION",
]


# --- restJson1 ser/de ---
def serialize_json(value: GcpScopeType) -> str:
    return value


def deserialize_json(data: str) -> GcpScopeType:
    return cast(GcpScopeType, data)
