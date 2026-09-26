"""Generated from Smithy shape ``com.amazonaws.agentregistry#RecordType``."""

from typing import Literal, TypeAlias, cast

"""<p>Record type enum for registry record classification</p>"""
RecordType: TypeAlias = Literal[
    "MCP",
    "AGENT",
    "CUSTOM",
    "SKILL",
    "GATEWAY",
]


# --- restJson1 ser/de ---
def serialize_json(value: RecordType) -> str:
    return value


def deserialize_json(data: str) -> RecordType:
    return cast(RecordType, data)
