"""Generated from Smithy shape ``com.amazonaws.bedrockagent#UpdatePromptResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_bedrock_agent.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock_agent.types.date_timestamp
    import capo_bedrock_agent.types.kms_key_arn
    import capo_bedrock_agent.types.prompt_arn
    import capo_bedrock_agent.types.prompt_description
    import capo_bedrock_agent.types.prompt_id
    import capo_bedrock_agent.types.prompt_name
    import capo_bedrock_agent.types.prompt_variant_list
    import capo_bedrock_agent.types.prompt_variant_name
    import capo_bedrock_agent.types.version


class UpdatePromptResponse(TypedDict, closed=True):
    name: "capo_bedrock_agent.types.prompt_name.PromptName"
    """<p>The name of the prompt.</p>"""
    description: NotRequired[
        "capo_bedrock_agent.types.prompt_description.PromptDescription"
    ]
    """<p>The description of the prompt.</p>"""
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
    id: "capo_bedrock_agent.types.prompt_id.PromptId"
    """<p>The unique identifier of the prompt.</p>"""
    arn: "capo_bedrock_agent.types.prompt_arn.PromptArn"
    """<p>The Amazon Resource Name (ARN) of the prompt.</p>"""
    version: "capo_bedrock_agent.types.version.Version"
    """<p>The version of the prompt. When you update a prompt, the version updated is the <code>DRAFT</code> version.</p>"""
    created_at: "capo_bedrock_agent.types.date_timestamp.DateTimestamp"
    """<p>The time at which the prompt was created.</p>"""
    updated_at: "capo_bedrock_agent.types.date_timestamp.DateTimestamp"
    """<p>The time at which the prompt was last updated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdatePromptResponse) -> dict:
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
    out["id"] = value["id"]
    out["arn"] = value["arn"]
    out["version"] = value["version"]
    import capo_bedrock_agent.types.date_timestamp

    out["createdAt"] = capo_bedrock_agent.types.date_timestamp.serialize_json(
        value["created_at"]
    )
    import capo_bedrock_agent.types.date_timestamp

    out["updatedAt"] = capo_bedrock_agent.types.date_timestamp.serialize_json(
        value["updated_at"]
    )
    return out


def deserialize_json(data: dict) -> UpdatePromptResponse:
    out: UpdatePromptResponse = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        raise DeserializationError("UpdatePromptResponse.name required")
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
    if data.get("id") is not None:
        out["id"] = data["id"]
    else:
        raise DeserializationError("UpdatePromptResponse.id required")
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    else:
        raise DeserializationError("UpdatePromptResponse.arn required")
    if data.get("version") is not None:
        out["version"] = data["version"]
    else:
        raise DeserializationError("UpdatePromptResponse.version required")
    if data.get("createdAt") is not None:
        import capo_bedrock_agent.types.date_timestamp

        out["created_at"] = capo_bedrock_agent.types.date_timestamp.deserialize_json(
            data["createdAt"]
        )
    else:
        raise DeserializationError("UpdatePromptResponse.created_at required")
    if data.get("updatedAt") is not None:
        import capo_bedrock_agent.types.date_timestamp

        out["updated_at"] = capo_bedrock_agent.types.date_timestamp.deserialize_json(
            data["updatedAt"]
        )
    else:
        raise DeserializationError("UpdatePromptResponse.updated_at required")
    return out
