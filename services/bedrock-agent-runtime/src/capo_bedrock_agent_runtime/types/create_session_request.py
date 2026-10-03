"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#CreateSessionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agent_runtime.types.kms_key_arn
    import capo_bedrock_agent_runtime.types.session_metadata_map
    import capo_bedrock_agent_runtime.types.tags_map


class CreateSessionRequest(TypedDict, closed=True):
    session_metadata: NotRequired[
        "capo_bedrock_agent_runtime.types.session_metadata_map.SessionMetadataMap"
    ]
    """<p>A map of key-value pairs containing attributes to be persisted across the session. For example, the user's ID, their language preference, and the type of device they are using.</p>"""
    encryption_key_arn: NotRequired[
        "capo_bedrock_agent_runtime.types.kms_key_arn.KmsKeyArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the KMS key to use to encrypt the session data. The user or role creating the session must have permission to use the key. For more information, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/session-encryption.html">Amazon Bedrock session encryption</a>. </p>"""
    tags: NotRequired["capo_bedrock_agent_runtime.types.tags_map.TagsMap"]
    """<p>Specify the key-value pairs for the tags that you want to attach to the session.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateSessionRequest) -> dict:
    out: dict = {}
    if "session_metadata" in value:
        import capo_bedrock_agent_runtime.types.session_metadata_map

        out["sessionMetadata"] = (
            capo_bedrock_agent_runtime.types.session_metadata_map.serialize_json(
                value["session_metadata"]
            )
        )
    if "encryption_key_arn" in value:
        out["encryptionKeyArn"] = value["encryption_key_arn"]
    if "tags" in value:
        import capo_bedrock_agent_runtime.types.tags_map

        out["tags"] = capo_bedrock_agent_runtime.types.tags_map.serialize_json(
            value["tags"]
        )
    return out


def deserialize_json(data: dict) -> CreateSessionRequest:
    out: CreateSessionRequest = {}  # type: ignore[typeddict-item]
    if data.get("sessionMetadata") is not None:
        import capo_bedrock_agent_runtime.types.session_metadata_map

        out["session_metadata"] = (
            capo_bedrock_agent_runtime.types.session_metadata_map.deserialize_json(
                data["sessionMetadata"]
            )
        )
    if data.get("encryptionKeyArn") is not None:
        out["encryption_key_arn"] = data["encryptionKeyArn"]
    if data.get("tags") is not None:
        import capo_bedrock_agent_runtime.types.tags_map

        out["tags"] = capo_bedrock_agent_runtime.types.tags_map.deserialize_json(
            data["tags"]
        )
    return out
