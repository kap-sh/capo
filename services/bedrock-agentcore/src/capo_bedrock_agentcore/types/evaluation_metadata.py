"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#EvaluationMetadata``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_bedrock_agentcore.errors import DeserializationError, SerializationError
from capo_bedrock_agentcore.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_bedrock_agentcore.types.session_metadata_list


class _EvaluationMetadata_sessionMetadata(TypedDict, closed=True):
    sessionMetadata: (
        "capo_bedrock_agentcore.types.session_metadata_list.SessionMetadataList"
    )


EvaluationMetadata: TypeAlias = _EvaluationMetadata_sessionMetadata | UnknownUnionMember


# --- restJson1 ser/de ---
def serialize_json(value: EvaluationMetadata) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"EvaluationMetadata: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "sessionMetadata" in value:
        import capo_bedrock_agentcore.types.session_metadata_list

        return {
            "sessionMetadata": capo_bedrock_agentcore.types.session_metadata_list.serialize_json(
                value["sessionMetadata"]
            )
        }
    else:
        raise SerializationError("EvaluationMetadata: no variant present")


def deserialize_json(data: dict) -> EvaluationMetadata:
    if data.get("sessionMetadata") is not None:
        import capo_bedrock_agentcore.types.session_metadata_list

        return {
            "sessionMetadata": capo_bedrock_agentcore.types.session_metadata_list.deserialize_json(
                data["sessionMetadata"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("EvaluationMetadata: no recognized variant key")
