"""Generated from Smithy shape ``com.amazonaws.bedrock#ImplicitFilterConfiguration``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_bedrock.types.bedrock_model_arn
    import capo_bedrock.types.metadata_attribute_schema_list


class ImplicitFilterConfiguration(TypedDict, closed=True):
    metadata_attributes: (
        "capo_bedrock.types.metadata_attribute_schema_list.MetadataAttributeSchemaList"
    )
    """<p>A list of metadata attribute schemas that define the structure and properties of metadata fields used for implicit filtering. Each attribute defines a key, type, and optional description.</p>"""
    model_arn: "capo_bedrock.types.bedrock_model_arn.BedrockModelArn"
    """<p>The Amazon Resource Name (ARN) of the foundation model used for implicit filtering. This model processes the query to extract relevant filtering criteria.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ImplicitFilterConfiguration) -> dict:
    out: dict = {}
    import capo_bedrock.types.metadata_attribute_schema_list

    out["metadataAttributes"] = (
        capo_bedrock.types.metadata_attribute_schema_list.serialize_json(
            value["metadata_attributes"]
        )
    )
    out["modelArn"] = value["model_arn"]
    return out


def deserialize_json(data: dict) -> ImplicitFilterConfiguration:
    out: ImplicitFilterConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("metadataAttributes") is not None:
        import capo_bedrock.types.metadata_attribute_schema_list

        out["metadata_attributes"] = (
            capo_bedrock.types.metadata_attribute_schema_list.deserialize_json(
                data["metadataAttributes"]
            )
        )
    else:
        out["metadata_attributes"] = []
    if data.get("modelArn") is not None:
        out["model_arn"] = data["modelArn"]
    else:
        out["model_arn"] = ""
    return out


def redact_sensitive(value: ImplicitFilterConfiguration) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "metadata_attributes" in value:
        import capo_bedrock.types.metadata_attribute_schema_list

        out["metadata_attributes"] = (
            capo_bedrock.types.metadata_attribute_schema_list.redact_sensitive(
                value["metadata_attributes"]
            )
        )
    return out
