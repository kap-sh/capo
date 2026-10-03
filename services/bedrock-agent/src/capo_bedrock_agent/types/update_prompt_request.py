"""Generated from Smithy shape ``com.amazonaws.bedrockagent#UpdatePromptRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_bedrock_agent.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock_agent.types.kms_key_arn
    import capo_bedrock_agent.types.prompt_description
    import capo_bedrock_agent.types.prompt_identifier
    import capo_bedrock_agent.types.prompt_name
    import capo_bedrock_agent.types.prompt_variant_list
    import capo_bedrock_agent.types.prompt_variant_name


class UpdatePromptRequest(TypedDict, closed=True):
    name: "capo_bedrock_agent.types.prompt_name.PromptName"
    """<p>A name for the prompt.</p>"""
    description: NotRequired[
        "capo_bedrock_agent.types.prompt_description.PromptDescription"
    ]
    """<p>A description for the prompt.</p>"""
    customer_encryption_key_arn: NotRequired[
        "capo_bedrock_agent.types.kms_key_arn.KmsKeyArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the KMS key to encrypt the prompt.</p>"""
    default_variant: NotRequired[
        "capo_bedrock_agent.types.prompt_variant_name.PromptVariantName"
    ]
    """<p>The name of the default variant for the prompt. This value must match the <code>name</code> field in the relevant <a href="https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent_PromptVariant.html">PromptVariant</a> object.</p>"""
    variants: NotRequired[
        "capo_bedrock_agent.types.prompt_variant_list.PromptVariantList"
    ]
    """<p>A list of objects, each containing details about a variant of the prompt.</p>"""
    prompt_identifier: "capo_bedrock_agent.types.prompt_identifier.PromptIdentifier"
    """<p>The unique identifier of the prompt.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdatePromptRequest) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    if "customer_encryption_key_arn" in value:
        out["customerEncryptionKeyArn"] = value["customer_encryption_key_arn"]
    if "default_variant" in value:
        out["defaultVariant"] = value["default_variant"]
    if "variants" in value:
        import capo_bedrock_agent.types.prompt_variant_list

        out["variants"] = capo_bedrock_agent.types.prompt_variant_list.serialize_json(
            value["variants"]
        )
    return out


def deserialize_json(data: dict) -> UpdatePromptRequest:
    out: UpdatePromptRequest = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        raise DeserializationError("UpdatePromptRequest.name required")
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("customerEncryptionKeyArn") is not None:
        out["customer_encryption_key_arn"] = data["customerEncryptionKeyArn"]
    if data.get("defaultVariant") is not None:
        out["default_variant"] = data["defaultVariant"]
    if data.get("variants") is not None:
        import capo_bedrock_agent.types.prompt_variant_list

        out["variants"] = capo_bedrock_agent.types.prompt_variant_list.deserialize_json(
            data["variants"]
        )
    return out
