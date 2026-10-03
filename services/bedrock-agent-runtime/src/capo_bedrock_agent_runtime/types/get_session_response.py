"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#GetSessionResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_bedrock_agent_runtime.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock_agent_runtime.types.date_timestamp
    import capo_bedrock_agent_runtime.types.kms_key_arn
    import capo_bedrock_agent_runtime.types.session_arn
    import capo_bedrock_agent_runtime.types.session_metadata_map
    import capo_bedrock_agent_runtime.types.session_status
    import capo_bedrock_agent_runtime.types.uuid


class GetSessionResponse(TypedDict, closed=True):
    session_id: "capo_bedrock_agent_runtime.types.uuid.Uuid"
    """<p>The unique identifier for the session in UUID format.</p>"""
    session_arn: "capo_bedrock_agent_runtime.types.session_arn.SessionArn"
    """<p>The Amazon Resource Name (ARN) of the session.</p>"""
    session_status: "capo_bedrock_agent_runtime.types.session_status.SessionStatus"
    """<p>The current status of the session.</p>"""
    created_at: "capo_bedrock_agent_runtime.types.date_timestamp.DateTimestamp"
    """<p>The timestamp for when the session was created.</p>"""
    last_updated_at: "capo_bedrock_agent_runtime.types.date_timestamp.DateTimestamp"
    """<p>The timestamp for when the session was last modified.</p>"""
    session_metadata: NotRequired[
        "capo_bedrock_agent_runtime.types.session_metadata_map.SessionMetadataMap"
    ]
    """<p>A map of key-value pairs containing attributes persisted across the session.</p>"""
    encryption_key_arn: NotRequired[
        "capo_bedrock_agent_runtime.types.kms_key_arn.KmsKeyArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the Key Management Service key used to encrypt the session data. For more information, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/session-encryption.html">Amazon Bedrock session encryption</a>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetSessionResponse) -> dict:
    out: dict = {}
    out["sessionId"] = value["session_id"]
    out["sessionArn"] = value["session_arn"]
    import capo_bedrock_agent_runtime.types.session_status

    out["sessionStatus"] = (
        capo_bedrock_agent_runtime.types.session_status.serialize_json(
            value["session_status"]
        )
    )
    import capo_bedrock_agent_runtime.types.date_timestamp

    out["createdAt"] = capo_bedrock_agent_runtime.types.date_timestamp.serialize_json(
        value["created_at"]
    )
    import capo_bedrock_agent_runtime.types.date_timestamp

    out["lastUpdatedAt"] = (
        capo_bedrock_agent_runtime.types.date_timestamp.serialize_json(
            value["last_updated_at"]
        )
    )
    if "session_metadata" in value:
        import capo_bedrock_agent_runtime.types.session_metadata_map

        out["sessionMetadata"] = (
            capo_bedrock_agent_runtime.types.session_metadata_map.serialize_json(
                value["session_metadata"]
            )
        )
    if "encryption_key_arn" in value:
        out["encryptionKeyArn"] = value["encryption_key_arn"]
    return out


def deserialize_json(data: dict) -> GetSessionResponse:
    out: GetSessionResponse = {}  # type: ignore[typeddict-item]
    if data.get("sessionId") is not None:
        out["session_id"] = data["sessionId"]
    else:
        raise DeserializationError("GetSessionResponse.session_id required")
    if data.get("sessionArn") is not None:
        out["session_arn"] = data["sessionArn"]
    else:
        raise DeserializationError("GetSessionResponse.session_arn required")
    if data.get("sessionStatus") is not None:
        import capo_bedrock_agent_runtime.types.session_status

        out["session_status"] = (
            capo_bedrock_agent_runtime.types.session_status.deserialize_json(
                data["sessionStatus"]
            )
        )
    else:
        raise DeserializationError("GetSessionResponse.session_status required")
    if data.get("createdAt") is not None:
        import capo_bedrock_agent_runtime.types.date_timestamp

        out["created_at"] = (
            capo_bedrock_agent_runtime.types.date_timestamp.deserialize_json(
                data["createdAt"]
            )
        )
    else:
        raise DeserializationError("GetSessionResponse.created_at required")
    if data.get("lastUpdatedAt") is not None:
        import capo_bedrock_agent_runtime.types.date_timestamp

        out["last_updated_at"] = (
            capo_bedrock_agent_runtime.types.date_timestamp.deserialize_json(
                data["lastUpdatedAt"]
            )
        )
    else:
        raise DeserializationError("GetSessionResponse.last_updated_at required")
    if data.get("sessionMetadata") is not None:
        import capo_bedrock_agent_runtime.types.session_metadata_map

        out["session_metadata"] = (
            capo_bedrock_agent_runtime.types.session_metadata_map.deserialize_json(
                data["sessionMetadata"]
            )
        )
    if data.get("encryptionKeyArn") is not None:
        out["encryption_key_arn"] = data["encryptionKeyArn"]
    return out
