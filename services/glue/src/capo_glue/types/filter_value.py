"""Generated from Smithy shape ``com.amazonaws.glue#FilterValue``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_glue.types.enclosed_in_string_properties
    import capo_glue.types.filter_value_type


class FilterValue(TypedDict, closed=True):
    type: "capo_glue.types.filter_value_type.FilterValueType"
    """<p>The type of filter value.</p>"""
    value: "capo_glue.types.enclosed_in_string_properties.EnclosedInStringProperties"
    """<p>The value to be associated.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FilterValue) -> dict:
    out: dict = {}
    import capo_glue.types.filter_value_type

    out["Type"] = capo_glue.types.filter_value_type.serialize_aws_json_1_1(
        value["type"]
    )
    import capo_glue.types.enclosed_in_string_properties

    out["Value"] = capo_glue.types.enclosed_in_string_properties.serialize_aws_json_1_1(
        value["value"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> FilterValue:
    out: FilterValue = {}  # type: ignore[typeddict-item]
    if data.get("Type") is not None:
        import capo_glue.types.filter_value_type

        out["type"] = capo_glue.types.filter_value_type.deserialize_aws_json_1_1(
            data["Type"]
        )
    else:
        import typing

        out["type"] = typing.cast(
            "capo_glue.types.filter_value_type.FilterValueType", ""
        )
    if data.get("Value") is not None:
        import capo_glue.types.enclosed_in_string_properties

        out["value"] = (
            capo_glue.types.enclosed_in_string_properties.deserialize_aws_json_1_1(
                data["Value"]
            )
        )
    else:
        out["value"] = []
    return out
