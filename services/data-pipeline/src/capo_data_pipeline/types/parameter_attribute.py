"""Generated from Smithy shape ``com.amazonaws.datapipeline#ParameterAttribute``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_data_pipeline.types.attribute_name_string
    import capo_data_pipeline.types.attribute_value_string


class ParameterAttribute(TypedDict, closed=True):
    key: "capo_data_pipeline.types.attribute_name_string.attributeNameString"
    """<p>The field identifier.</p>"""
    string_value: "capo_data_pipeline.types.attribute_value_string.attributeValueString"
    """<p>The field value, expressed as a String.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ParameterAttribute) -> dict:
    out: dict = {}
    out["key"] = value["key"]
    out["stringValue"] = value["string_value"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ParameterAttribute:
    out: ParameterAttribute = {}  # type: ignore[typeddict-item]
    if data.get("key") is not None:
        out["key"] = data["key"]
    else:
        out["key"] = ""
    if data.get("stringValue") is not None:
        out["string_value"] = data["stringValue"]
    else:
        out["string_value"] = ""
    return out
