"""Generated from Smithy shape ``com.amazonaws.datapipeline#ParameterObject``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_data_pipeline.types.field_name_string
    import capo_data_pipeline.types.parameter_attribute_list


class ParameterObject(TypedDict, closed=True):
    id: "capo_data_pipeline.types.field_name_string.fieldNameString"
    """<p>The ID of the parameter object. </p>"""
    attributes: (
        "capo_data_pipeline.types.parameter_attribute_list.ParameterAttributeList"
    )
    """<p>The attributes of the parameter object.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ParameterObject) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    import capo_data_pipeline.types.parameter_attribute_list

    out["attributes"] = (
        capo_data_pipeline.types.parameter_attribute_list.serialize_aws_json_1_1(
            value["attributes"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> ParameterObject:
    out: ParameterObject = {}  # type: ignore[typeddict-item]
    if data.get("id") is not None:
        out["id"] = data["id"]
    else:
        out["id"] = ""
    if data.get("attributes") is not None:
        import capo_data_pipeline.types.parameter_attribute_list

        out["attributes"] = (
            capo_data_pipeline.types.parameter_attribute_list.deserialize_aws_json_1_1(
                data["attributes"]
            )
        )
    else:
        out["attributes"] = []
    return out
