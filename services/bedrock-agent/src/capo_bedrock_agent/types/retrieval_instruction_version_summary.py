"""Generated from Smithy shape ``com.amazonaws.bedrockagent#RetrievalInstructionVersionSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agent.types.date_timestamp
    import capo_bedrock_agent.types.retrieval_instruction_numerical_version


class RetrievalInstructionVersionSummary(TypedDict, closed=True):
    version: "capo_bedrock_agent.types.retrieval_instruction_numerical_version.RetrievalInstructionNumericalVersion"
    """<p>The version number.</p>"""
    created_at: "capo_bedrock_agent.types.date_timestamp.DateTimestamp"
    """<p>When this version was created.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RetrievalInstructionVersionSummary) -> dict:
    out: dict = {}
    out["version"] = value["version"]
    import capo_bedrock_agent.types.date_timestamp

    out["createdAt"] = capo_bedrock_agent.types.date_timestamp.serialize_json(
        value["created_at"]
    )
    return out


def deserialize_json(data: dict) -> RetrievalInstructionVersionSummary:
    out: RetrievalInstructionVersionSummary = {}  # type: ignore[typeddict-item]
    if data.get("version") is not None:
        out["version"] = data["version"]
    else:
        out["version"] = ""
    if data.get("createdAt") is not None:
        import capo_bedrock_agent.types.date_timestamp

        out["created_at"] = capo_bedrock_agent.types.date_timestamp.deserialize_json(
            data["createdAt"]
        )
    else:
        import datetime

        out["created_at"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    return out
