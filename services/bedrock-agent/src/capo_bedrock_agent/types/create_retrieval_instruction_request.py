"""Generated from Smithy shape ``com.amazonaws.bedrockagent#CreateRetrievalInstructionRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_bedrock_agent.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock_agent.types.client_token
    import capo_bedrock_agent.types.kms_key_arn
    import capo_bedrock_agent.types.retrieval_instruction_content
    import capo_bedrock_agent.types.retrieval_instruction_description
    import capo_bedrock_agent.types.retrieval_instruction_name
    import capo_bedrock_agent.types.tags_map


class CreateRetrievalInstructionRequest(TypedDict, closed=True):
    client_token: NotRequired["capo_bedrock_agent.types.client_token.ClientToken"]
    """<p>A caller-supplied token that makes a retried create return the existing resource rather than a second one. The window is 8 hours.</p>"""
    name: "capo_bedrock_agent.types.retrieval_instruction_name.RetrievalInstructionName"
    """<p>Specifies the name of the retrieval instruction.</p>"""
    instruction: "capo_bedrock_agent.types.retrieval_instruction_content.RetrievalInstructionContent"
    """<p>The instruction content, as a set of named fields. Get does not return this field until the create review passes.</p>"""
    description: NotRequired[
        "capo_bedrock_agent.types.retrieval_instruction_description.RetrievalInstructionDescription"
    ]
    """<p>Specifies a description of the retrieval instruction.</p>"""
    customer_encryption_key_arn: NotRequired[
        "capo_bedrock_agent.types.kms_key_arn.KmsKeyArn"
    ]
    """<p>The Amazon Resource Name (ARN) of a customer managed AWS Key Management Service (AWS KMS) key used to encrypt the instruction content at rest. If you omit it, the service uses an AWS owned key. You fix the key at create and cannot change it later.</p>"""
    tags: NotRequired["capo_bedrock_agent.types.tags_map.TagsMap"]
    """<p>Tags for the retrieval instruction.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateRetrievalInstructionRequest) -> dict:
    out: dict = {}
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    out["name"] = value["name"]
    import capo_bedrock_agent.types.retrieval_instruction_content

    out["instruction"] = (
        capo_bedrock_agent.types.retrieval_instruction_content.serialize_json(
            value["instruction"]
        )
    )
    if "description" in value:
        out["description"] = value["description"]
    if "customer_encryption_key_arn" in value:
        out["customerEncryptionKeyArn"] = value["customer_encryption_key_arn"]
    if "tags" in value:
        import capo_bedrock_agent.types.tags_map

        out["tags"] = capo_bedrock_agent.types.tags_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> CreateRetrievalInstructionRequest:
    out: CreateRetrievalInstructionRequest = {}  # type: ignore[typeddict-item]
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("instruction") is not None:
        import capo_bedrock_agent.types.retrieval_instruction_content

        out["instruction"] = (
            capo_bedrock_agent.types.retrieval_instruction_content.deserialize_json(
                data["instruction"]
            )
        )
    else:
        raise DeserializationError(
            "CreateRetrievalInstructionRequest.instruction required"
        )
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("customerEncryptionKeyArn") is not None:
        out["customer_encryption_key_arn"] = data["customerEncryptionKeyArn"]
    if data.get("tags") is not None:
        import capo_bedrock_agent.types.tags_map

        out["tags"] = capo_bedrock_agent.types.tags_map.deserialize_json(data["tags"])
    return out


def redact_sensitive(value: CreateRetrievalInstructionRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "name" in value:
        out["name"] = "*** Sensitive Data Redacted ***"
    if "instruction" in value:
        out["instruction"] = "*** Sensitive Data Redacted ***"
    if "description" in value:
        out["description"] = "*** Sensitive Data Redacted ***"
    return out
