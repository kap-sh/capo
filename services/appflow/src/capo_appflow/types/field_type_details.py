"""Generated from Smithy shape ``com.amazonaws.appflow#FieldTypeDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_appflow.errors import DeserializationError

if TYPE_CHECKING:
    import capo_appflow.types.field_type
    import capo_appflow.types.filter_operator_list
    import capo_appflow.types.range
    import capo_appflow.types.string
    import capo_appflow.types.supported_value_list


class FieldTypeDetails(TypedDict, closed=True):
    field_type: "capo_appflow.types.field_type.FieldType"
    """<p> The type of field, such as string, integer, date, and so on. </p>"""
    filter_operators: "capo_appflow.types.filter_operator_list.FilterOperatorList"
    """<p> The list of operators supported by a field. </p>"""
    supported_values: NotRequired[
        "capo_appflow.types.supported_value_list.SupportedValueList"
    ]
    """<p> The list of values that a field can contain. For example, a Boolean <code>fieldType</code> can have two values: "true" and "false". </p>"""
    value_regex_pattern: NotRequired["capo_appflow.types.string.String"]
    """<p>The regular expression pattern for the field name.</p>"""
    supported_date_format: NotRequired["capo_appflow.types.string.String"]
    """<p>The date format that the field supports.</p>"""
    field_value_range: NotRequired["capo_appflow.types.range.Range"]
    """<p>The range of values this field can hold.</p>"""
    field_length_range: NotRequired["capo_appflow.types.range.Range"]
    """<p>This is the allowable length range for this field's value.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FieldTypeDetails) -> dict:
    out: dict = {}
    out["fieldType"] = value["field_type"]
    import capo_appflow.types.filter_operator_list

    out["filterOperators"] = capo_appflow.types.filter_operator_list.serialize_json(
        value["filter_operators"]
    )
    if "supported_values" in value:
        import capo_appflow.types.supported_value_list

        out["supportedValues"] = capo_appflow.types.supported_value_list.serialize_json(
            value["supported_values"]
        )
    if "value_regex_pattern" in value:
        out["valueRegexPattern"] = value["value_regex_pattern"]
    if "supported_date_format" in value:
        out["supportedDateFormat"] = value["supported_date_format"]
    if "field_value_range" in value:
        import capo_appflow.types.range

        out["fieldValueRange"] = capo_appflow.types.range.serialize_json(
            value["field_value_range"]
        )
    if "field_length_range" in value:
        import capo_appflow.types.range

        out["fieldLengthRange"] = capo_appflow.types.range.serialize_json(
            value["field_length_range"]
        )
    return out


def deserialize_json(data: dict) -> FieldTypeDetails:
    out: FieldTypeDetails = {}  # type: ignore[typeddict-item]
    if data.get("fieldType") is not None:
        out["field_type"] = data["fieldType"]
    else:
        raise DeserializationError("FieldTypeDetails.field_type required")
    if data.get("filterOperators") is not None:
        import capo_appflow.types.filter_operator_list

        out["filter_operators"] = (
            capo_appflow.types.filter_operator_list.deserialize_json(
                data["filterOperators"]
            )
        )
    else:
        raise DeserializationError("FieldTypeDetails.filter_operators required")
    if data.get("supportedValues") is not None:
        import capo_appflow.types.supported_value_list

        out["supported_values"] = (
            capo_appflow.types.supported_value_list.deserialize_json(
                data["supportedValues"]
            )
        )
    if data.get("valueRegexPattern") is not None:
        out["value_regex_pattern"] = data["valueRegexPattern"]
    if data.get("supportedDateFormat") is not None:
        out["supported_date_format"] = data["supportedDateFormat"]
    if data.get("fieldValueRange") is not None:
        import capo_appflow.types.range

        out["field_value_range"] = capo_appflow.types.range.deserialize_json(
            data["fieldValueRange"]
        )
    if data.get("fieldLengthRange") is not None:
        import capo_appflow.types.range

        out["field_length_range"] = capo_appflow.types.range.deserialize_json(
            data["fieldLengthRange"]
        )
    return out
