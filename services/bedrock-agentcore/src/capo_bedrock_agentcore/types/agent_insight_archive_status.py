"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#AgentInsightArchiveStatus``."""

from typing import Literal, TypeAlias, cast

"""<p>Specifies whether an Agent Insight is active or archived. Valid values:</p> <ul> <li> <p> <code>ACTIVE</code> - The insight is currently active.</p> </li> <li> <p> <code>ARCHIVED</code> - The insight has been archived.</p> </li> </ul>"""
AgentInsightArchiveStatus: TypeAlias = Literal[
    "ACTIVE",
    "ARCHIVED",
]


# --- restJson1 ser/de ---
def serialize_json(value: AgentInsightArchiveStatus) -> str:
    return value


def deserialize_json(data: str) -> AgentInsightArchiveStatus:
    return cast(AgentInsightArchiveStatus, data)
