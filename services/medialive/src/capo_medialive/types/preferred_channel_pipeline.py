"""Generated from Smithy shape ``com.amazonaws.medialive#PreferredChannelPipeline``."""

from typing import Literal, TypeAlias, cast

r"""Indicates which pipeline is preferred by the multiplex for program ingest. If set to \"PIPELINE_0\" or \"PIPELINE_1\" and an unhealthy ingest causes the multiplex to switch to the non-preferred pipeline, it will switch back once that ingest is healthy again. If set to \"CURRENTLY_ACTIVE\", it will not switch back to the other pipeline based on it recovering to a healthy state, it will only switch if the active pipeline becomes unhealthy."""
PreferredChannelPipeline: TypeAlias = Literal[
    "CURRENTLY_ACTIVE",
    "PIPELINE_0",
    "PIPELINE_1",
]


# --- restJson1 ser/de ---
def serialize_json(value: PreferredChannelPipeline) -> str:
    return value


def deserialize_json(data: str) -> PreferredChannelPipeline:
    return cast(PreferredChannelPipeline, data)
