"""Generated from Smithy shape ``com.amazonaws.customerprofiles#ObjectAttribute``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_customer_profiles.types.comparison_operator
    import capo_customer_profiles.types.event_trigger_values
    import capo_customer_profiles.types.field_name
    import capo_customer_profiles.types.text


class ObjectAttribute(TypedDict, closed=True):
    source: NotRequired["capo_customer_profiles.types.text.text"]
    """<p>An attribute contained within a source object.</p>"""
    field_name: NotRequired["capo_customer_profiles.types.field_name.fieldName"]
    """<p>A field defined within an object type.</p>"""
    comparison_operator: (
        "capo_customer_profiles.types.comparison_operator.ComparisonOperator"
    )
    """<p>The operator used to compare an attribute against a list of values.</p>"""
    values: "capo_customer_profiles.types.event_trigger_values.EventTriggerValues"
    """<p>A list of attribute values used for comparison.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ObjectAttribute) -> dict:
    out: dict = {}
    if "source" in value:
        out["Source"] = value["source"]
    if "field_name" in value:
        out["FieldName"] = value["field_name"]
    import capo_customer_profiles.types.comparison_operator

    out["ComparisonOperator"] = (
        capo_customer_profiles.types.comparison_operator.serialize_json(
            value["comparison_operator"]
        )
    )
    import capo_customer_profiles.types.event_trigger_values

    out["Values"] = capo_customer_profiles.types.event_trigger_values.serialize_json(
        value["values"]
    )
    return out


def deserialize_json(data: dict) -> ObjectAttribute:
    out: ObjectAttribute = {}  # type: ignore[typeddict-item]
    if data.get("Source") is not None:
        out["source"] = data["Source"]
    if data.get("FieldName") is not None:
        out["field_name"] = data["FieldName"]
    if data.get("ComparisonOperator") is not None:
        import capo_customer_profiles.types.comparison_operator

        out["comparison_operator"] = (
            capo_customer_profiles.types.comparison_operator.deserialize_json(
                data["ComparisonOperator"]
            )
        )
    else:
        import typing

        out["comparison_operator"] = typing.cast(
            "capo_customer_profiles.types.comparison_operator.ComparisonOperator", ""
        )
    if data.get("Values") is not None:
        import capo_customer_profiles.types.event_trigger_values

        out["values"] = (
            capo_customer_profiles.types.event_trigger_values.deserialize_json(
                data["Values"]
            )
        )
    else:
        out["values"] = []
    return out
