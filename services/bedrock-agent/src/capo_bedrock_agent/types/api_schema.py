"""Generated from Smithy shape ``com.amazonaws.bedrockagent#APISchema``."""

from typing import TYPE_CHECKING, Any, TypeAlias

from typing_extensions import TypedDict

from capo_bedrock_agent.errors import DeserializationError, SerializationError
from capo_bedrock_agent.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_bedrock_agent.types.payload
    import capo_bedrock_agent.types.s3_identifier


class _APISchema_s3(TypedDict, closed=True):
    s3: "capo_bedrock_agent.types.s3_identifier.S3Identifier"


class _APISchema_payload(TypedDict, closed=True):
    payload: "capo_bedrock_agent.types.payload.Payload"


APISchema: TypeAlias = _APISchema_s3 | _APISchema_payload | UnknownUnionMember


# --- restJson1 ser/de ---
def serialize_json(value: APISchema) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"APISchema: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "s3" in value:
        import capo_bedrock_agent.types.s3_identifier

        return {
            "s3": capo_bedrock_agent.types.s3_identifier.serialize_json(value["s3"])
        }
    elif "payload" in value:
        return {"payload": value["payload"]}
    else:
        raise SerializationError("APISchema: no variant present")


def deserialize_json(data: dict) -> APISchema:
    if data.get("s3") is not None:
        import capo_bedrock_agent.types.s3_identifier

        return {
            "s3": capo_bedrock_agent.types.s3_identifier.deserialize_json(data["s3"])
        }
    elif data.get("payload") is not None:
        return {"payload": data["payload"]}
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("APISchema: no recognized variant key")


def redact_sensitive(value: APISchema) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "payload" in value:
        out["payload"] = "*** Sensitive Data Redacted ***"
    return out
