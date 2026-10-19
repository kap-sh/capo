"""Generated from Smithy shape ``com.amazonaws.glue#TransformConfigParameter``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_glue.types.boxed_boolean
    import capo_glue.types.enclosed_in_string_properties
    import capo_glue.types.enclosed_in_string_property
    import capo_glue.types.param_type


class TransformConfigParameter(TypedDict, closed=True):
    name: "capo_glue.types.enclosed_in_string_property.EnclosedInStringProperty"
    """<p>Specifies the name of the parameter in the config file of the dynamic transform.</p>"""
    type: "capo_glue.types.param_type.ParamType"
    """<p>Specifies the parameter type in the config file of the dynamic transform.</p>"""
    validation_rule: NotRequired[
        "capo_glue.types.enclosed_in_string_property.EnclosedInStringProperty"
    ]
    """<p>Specifies the validation rule in the config file of the dynamic transform.</p>"""
    validation_message: NotRequired[
        "capo_glue.types.enclosed_in_string_property.EnclosedInStringProperty"
    ]
    """<p>Specifies the validation message in the config file of the dynamic transform.</p>"""
    value: NotRequired[
        "capo_glue.types.enclosed_in_string_properties.EnclosedInStringProperties"
    ]
    """<p>Specifies the value of the parameter in the config file of the dynamic transform.</p>"""
    list_type: NotRequired["capo_glue.types.param_type.ParamType"]
    """<p>Specifies the list type of the parameter in the config file of the dynamic transform.</p>"""
    is_optional: NotRequired["capo_glue.types.boxed_boolean.BoxedBoolean"]
    """<p>Specifies whether the parameter is optional or not in the config file of the dynamic transform.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TransformConfigParameter) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    import capo_glue.types.param_type

    out["Type"] = capo_glue.types.param_type.serialize_aws_json_1_1(value["type"])
    if "validation_rule" in value:
        out["ValidationRule"] = value["validation_rule"]
    if "validation_message" in value:
        out["ValidationMessage"] = value["validation_message"]
    if "value" in value:
        import capo_glue.types.enclosed_in_string_properties

        out["Value"] = (
            capo_glue.types.enclosed_in_string_properties.serialize_aws_json_1_1(
                value["value"]
            )
        )
    if "list_type" in value:
        import capo_glue.types.param_type

        out["ListType"] = capo_glue.types.param_type.serialize_aws_json_1_1(
            value["list_type"]
        )
    if "is_optional" in value:
        out["IsOptional"] = value["is_optional"]
    return out


def deserialize_aws_json_1_1(data: dict) -> TransformConfigParameter:
    out: TransformConfigParameter = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        out["name"] = ""
    if data.get("Type") is not None:
        import capo_glue.types.param_type

        out["type"] = capo_glue.types.param_type.deserialize_aws_json_1_1(data["Type"])
    else:
        import typing

        out["type"] = typing.cast("capo_glue.types.param_type.ParamType", "")
    if data.get("ValidationRule") is not None:
        out["validation_rule"] = data["ValidationRule"]
    if data.get("ValidationMessage") is not None:
        out["validation_message"] = data["ValidationMessage"]
    if data.get("Value") is not None:
        import capo_glue.types.enclosed_in_string_properties

        out["value"] = (
            capo_glue.types.enclosed_in_string_properties.deserialize_aws_json_1_1(
                data["Value"]
            )
        )
    if data.get("ListType") is not None:
        import capo_glue.types.param_type

        out["list_type"] = capo_glue.types.param_type.deserialize_aws_json_1_1(
            data["ListType"]
        )
    if data.get("IsOptional") is not None:
        out["is_optional"] = data["IsOptional"]
    return out
