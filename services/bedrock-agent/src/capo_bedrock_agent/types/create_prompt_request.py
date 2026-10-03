"""Generated from Smithy shape ``com.amazonaws.bedrockagent#CreatePromptRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_bedrock_agent.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock_agent.types.client_token
    import capo_bedrock_agent.types.kms_key_arn
    import capo_bedrock_agent.types.prompt_description
    import capo_bedrock_agent.types.prompt_name
    import capo_bedrock_agent.types.prompt_variant_list
    import capo_bedrock_agent.types.prompt_variant_name
    import capo_bedrock_agent.types.tags_map


class CreatePromptRequest(TypedDict, closed=True):
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
    client_token: NotRequired["capo_bedrock_agent.types.client_token.ClientToken"]
    """<p>A unique, case-sensitive identifier to ensure that the API request completes no more than one time. If this token matches a previous request, Amazon Bedrock ignores the request, but does not return an error. For more information, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html">Ensuring idempotency</a>.</p>"""
    tags: NotRequired["capo_bedrock_agent.types.tags_map.TagsMap"]
    """<p>Any tags that you want to attach to the prompt. For more information, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/tagging.html">Tagging resources in Amazon Bedrock</a>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreatePromptRequest) -> dict:
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
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    if "tags" in value:
        import capo_bedrock_agent.types.tags_map

        out["tags"] = capo_bedrock_agent.types.tags_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> CreatePromptRequest:
    out: CreatePromptRequest = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        raise DeserializationError("CreatePromptRequest.name required")
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
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    if data.get("tags") is not None:
        import capo_bedrock_agent.types.tags_map

        out["tags"] = capo_bedrock_agent.types.tags_map.deserialize_json(data["tags"])
    return out
