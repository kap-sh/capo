"""Generated from Smithy shape ``com.amazonaws.bedrock#CustomModelSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_bedrock.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock.types.account_id
    import capo_bedrock.types.custom_model_arn
    import capo_bedrock.types.custom_model_name
    import capo_bedrock.types.customization_type
    import capo_bedrock.types.model_arn
    import capo_bedrock.types.model_name
    import capo_bedrock.types.model_status
    import capo_bedrock.types.timestamp


class CustomModelSummary(TypedDict, closed=True):
    model_arn: "capo_bedrock.types.custom_model_arn.CustomModelArn"
    """<p>The Amazon Resource Name (ARN) of the custom model.</p>"""
    model_name: "capo_bedrock.types.custom_model_name.CustomModelName"
    """<p>The name of the custom model.</p>"""
    creation_time: "capo_bedrock.types.timestamp.Timestamp"
    """<p>Creation time of the model.</p>"""
    base_model_arn: "capo_bedrock.types.model_arn.ModelArn"
    """<p>The base model Amazon Resource Name (ARN).</p>"""
    base_model_name: "capo_bedrock.types.model_name.ModelName"
    """<p>The base model name.</p>"""
    customization_type: NotRequired[
        "capo_bedrock.types.customization_type.CustomizationType"
    ]
    """<p>Specifies whether to carry out continued pre-training of a model or whether to fine-tune it. For more information, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/custom-models.html">Custom models</a>.</p>"""
    owner_account_id: NotRequired["capo_bedrock.types.account_id.AccountId"]
    """<p>The unique identifier of the account that owns the model.</p>"""
    model_status: NotRequired["capo_bedrock.types.model_status.ModelStatus"]
    """<p>The current status of the custom model. Possible values include:</p> <ul> <li> <p> <code>Creating</code> - The model is being created and validated.</p> </li> <li> <p> <code>Active</code> - The model has been successfully created and is ready for use.</p> </li> <li> <p> <code>Failed</code> - The model creation process failed.</p> </li> </ul>"""


# --- restJson1 ser/de ---
def serialize_json(value: CustomModelSummary) -> dict:
    out: dict = {}
    out["modelArn"] = value["model_arn"]
    out["modelName"] = value["model_name"]
    import capo_bedrock.types.timestamp

    out["creationTime"] = capo_bedrock.types.timestamp.serialize_json(
        value["creation_time"]
    )
    out["baseModelArn"] = value["base_model_arn"]
    out["baseModelName"] = value["base_model_name"]
    if "customization_type" in value:
        import capo_bedrock.types.customization_type

        out["customizationType"] = capo_bedrock.types.customization_type.serialize_json(
            value["customization_type"]
        )
    if "owner_account_id" in value:
        out["ownerAccountId"] = value["owner_account_id"]
    if "model_status" in value:
        import capo_bedrock.types.model_status

        out["modelStatus"] = capo_bedrock.types.model_status.serialize_json(
            value["model_status"]
        )
    return out


def deserialize_json(data: dict) -> CustomModelSummary:
    out: CustomModelSummary = {}  # type: ignore[typeddict-item]
    if data.get("modelArn") is not None:
        out["model_arn"] = data["modelArn"]
    else:
        raise DeserializationError("CustomModelSummary.model_arn required")
    if data.get("modelName") is not None:
        out["model_name"] = data["modelName"]
    else:
        raise DeserializationError("CustomModelSummary.model_name required")
    if data.get("creationTime") is not None:
        import capo_bedrock.types.timestamp

        out["creation_time"] = capo_bedrock.types.timestamp.deserialize_json(
            data["creationTime"]
        )
    else:
        raise DeserializationError("CustomModelSummary.creation_time required")
    if data.get("baseModelArn") is not None:
        out["base_model_arn"] = data["baseModelArn"]
    else:
        raise DeserializationError("CustomModelSummary.base_model_arn required")
    if data.get("baseModelName") is not None:
        out["base_model_name"] = data["baseModelName"]
    else:
        raise DeserializationError("CustomModelSummary.base_model_name required")
    if data.get("customizationType") is not None:
        import capo_bedrock.types.customization_type

        out["customization_type"] = (
            capo_bedrock.types.customization_type.deserialize_json(
                data["customizationType"]
            )
        )
    if data.get("ownerAccountId") is not None:
        out["owner_account_id"] = data["ownerAccountId"]
    if data.get("modelStatus") is not None:
        import capo_bedrock.types.model_status

        out["model_status"] = capo_bedrock.types.model_status.deserialize_json(
            data["modelStatus"]
        )
    return out
