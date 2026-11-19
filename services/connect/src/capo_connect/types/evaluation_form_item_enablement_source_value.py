"""Generated from Smithy shape ``com.amazonaws.connect#EvaluationFormItemEnablementSourceValue``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connect.types.evaluation_form_enablement_boolean_value
    import capo_connect.types.evaluation_form_enablement_numeric_value
    import capo_connect.types.evaluation_form_enablement_string_value
    import capo_connect.types.evaluation_form_item_enablement_source_value_type
    import capo_connect.types.reference_id
    import capo_connect.types.timestamp


class EvaluationFormItemEnablementSourceValue(TypedDict, closed=True):
    type: "capo_connect.types.evaluation_form_item_enablement_source_value_type.EvaluationFormItemEnablementSourceValueType"
    """<p>A type of source item value. Valid values: <code>OPTION_REF_ID</code> | <code>STRING_VALUE</code> | <code>NUMERIC_VALUE</code> | <code>BOOLEAN_VALUE</code> | <code>DATETIME_VALUE</code>.</p>"""
    ref_id: NotRequired["capo_connect.types.reference_id.ReferenceId"]
    """<p>A referenceId of the source value. Use when <code>Type</code> is <code>OPTION_REF_ID</code>.</p>"""
    string_value: NotRequired[
        "capo_connect.types.evaluation_form_enablement_string_value.EvaluationFormEnablementStringValue"
    ]
    """<p>A string value to compare against the source. Use when <code>Type</code> is <code>STRING_VALUE</code>.</p>"""
    numeric_value: NotRequired[
        "capo_connect.types.evaluation_form_enablement_numeric_value.EvaluationFormEnablementNumericValue"
    ]
    """<p>A numeric value to compare against the source. Use when <code>Type</code> is <code>NUMERIC_VALUE</code>.</p>"""
    boolean_value: NotRequired[
        "capo_connect.types.evaluation_form_enablement_boolean_value.EvaluationFormEnablementBooleanValue"
    ]
    """<p>A Boolean value to compare against the source. Use when <code>Type</code> is <code>BOOLEAN_VALUE</code>.</p>"""
    date_time_value: NotRequired["capo_connect.types.timestamp.Timestamp"]
    """<p>A date and time value to compare against the source. Use when <code>Type</code> is <code>DATETIME_VALUE</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EvaluationFormItemEnablementSourceValue) -> dict:
    out: dict = {}
    import capo_connect.types.evaluation_form_item_enablement_source_value_type

    out["Type"] = (
        capo_connect.types.evaluation_form_item_enablement_source_value_type.serialize_json(
            value["type"]
        )
    )
    if "ref_id" in value:
        out["RefId"] = value["ref_id"]
    if "string_value" in value:
        out["StringValue"] = value["string_value"]
    if "numeric_value" in value:
        out["NumericValue"] = (
            "NaN"
            if value["numeric_value"] != value["numeric_value"]
            else "Infinity"
            if value["numeric_value"] == float("inf")
            else "-Infinity"
            if value["numeric_value"] == float("-inf")
            else value["numeric_value"]
        )
    if "boolean_value" in value:
        out["BooleanValue"] = value["boolean_value"]
    if "date_time_value" in value:
        import capo_connect.types.timestamp

        out["DateTimeValue"] = capo_connect.types.timestamp.serialize_json(
            value["date_time_value"]
        )
    return out


def deserialize_json(data: dict) -> EvaluationFormItemEnablementSourceValue:
    out: EvaluationFormItemEnablementSourceValue = {}  # type: ignore[typeddict-item]
    if data.get("Type") is not None:
        import capo_connect.types.evaluation_form_item_enablement_source_value_type

        out["type"] = (
            capo_connect.types.evaluation_form_item_enablement_source_value_type.deserialize_json(
                data["Type"]
            )
        )
    else:
        import typing

        out["type"] = typing.cast(
            "capo_connect.types.evaluation_form_item_enablement_source_value_type.EvaluationFormItemEnablementSourceValueType",
            "",
        )
    if data.get("RefId") is not None:
        out["ref_id"] = data["RefId"]
    if data.get("StringValue") is not None:
        out["string_value"] = data["StringValue"]
    if data.get("NumericValue") is not None:
        out["numeric_value"] = float(data["NumericValue"])
    if data.get("BooleanValue") is not None:
        out["boolean_value"] = data["BooleanValue"]
    if data.get("DateTimeValue") is not None:
        import capo_connect.types.timestamp

        out["date_time_value"] = capo_connect.types.timestamp.deserialize_json(
            data["DateTimeValue"]
        )
    return out
