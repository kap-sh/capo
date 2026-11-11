"""Generated from Smithy shape ``com.amazonaws.elasticsearchservice#ClonedBlueGreenScheduledActionType``."""

from typing import Literal, TypeAlias, cast

"""<p><code>AutomaticCutoverToPrimaryCluster</code> cuts the domain back over to the primary cluster if you haven't cut over by the scheduled time. <code>DeletePrimaryCluster</code> deletes the primary cluster when the retention period ends.</p>"""
ClonedBlueGreenScheduledActionType: TypeAlias = Literal[
    "AutomaticCutoverToPrimaryCluster",
    "DeletePrimaryCluster",
]


# --- restJson1 ser/de ---
def serialize_json(value: ClonedBlueGreenScheduledActionType) -> str:
    return value


def deserialize_json(data: str) -> ClonedBlueGreenScheduledActionType:
    return cast(ClonedBlueGreenScheduledActionType, data)
