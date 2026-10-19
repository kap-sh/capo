"""Generated from Smithy shape ``com.amazonaws.kendra#AdditionalResultAttribute``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_kendra.errors import DeserializationError

if TYPE_CHECKING:
    import capo_kendra.types.additional_result_attribute_value
    import capo_kendra.types.additional_result_attribute_value_type
    import capo_kendra.types.string


class AdditionalResultAttribute(TypedDict, closed=True):
    key: "capo_kendra.types.string.String"
    """<p>The key that identifies the attribute.</p>"""
    value_type: "capo_kendra.types.additional_result_attribute_value_type.AdditionalResultAttributeValueType"
    """<p>The data type of the <code>Value</code> property.</p>"""
    value: "capo_kendra.types.additional_result_attribute_value.AdditionalResultAttributeValue"
    """<p>An object that contains the attribute value.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AdditionalResultAttribute) -> dict:
    out: dict = {}
    out["Key"] = value["key"]
    import capo_kendra.types.additional_result_attribute_value_type

    out["ValueType"] = (
        capo_kendra.types.additional_result_attribute_value_type.serialize_aws_json_1_1(
            value["value_type"]
        )
    )
    import capo_kendra.types.additional_result_attribute_value

    out["Value"] = (
        capo_kendra.types.additional_result_attribute_value.serialize_aws_json_1_1(
            value["value"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> AdditionalResultAttribute:
    out: AdditionalResultAttribute = {}  # type: ignore[typeddict-item]
    if data.get("Key") is not None:
        out["key"] = data["Key"]
    else:
        out["key"] = ""
    if data.get("ValueType") is not None:
        import capo_kendra.types.additional_result_attribute_value_type

        out["value_type"] = (
            capo_kendra.types.additional_result_attribute_value_type.deserialize_aws_json_1_1(
                data["ValueType"]
            )
        )
    else:
        import typing

        out["value_type"] = typing.cast(
            "capo_kendra.types.additional_result_attribute_value_type.AdditionalResultAttributeValueType",
            "",
        )
    if data.get("Value") is not None:
        import capo_kendra.types.additional_result_attribute_value

        out["value"] = (
            capo_kendra.types.additional_result_attribute_value.deserialize_aws_json_1_1(
                data["Value"]
            )
        )
    else:
        raise DeserializationError("AdditionalResultAttribute.value required")
    return out
