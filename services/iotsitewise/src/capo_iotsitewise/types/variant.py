"""Generated from Smithy shape ``com.amazonaws.iotsitewise#Variant``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iotsitewise.types.property_value_boolean_value
    import capo_iotsitewise.types.property_value_double_value
    import capo_iotsitewise.types.property_value_integer_value
    import capo_iotsitewise.types.property_value_null_value
    import capo_iotsitewise.types.property_value_string_value


class Variant(TypedDict, closed=True):
    string_value: NotRequired[
        "capo_iotsitewise.types.property_value_string_value.PropertyValueStringValue"
    ]
    r"""<p> Asset property data of type string (sequence of characters). The allowed pattern: "^$|[^\u0000-\u001F\u007F]+". The max length is 1024. </p>"""
    integer_value: NotRequired[
        "capo_iotsitewise.types.property_value_integer_value.PropertyValueIntegerValue"
    ]
    """<p>Asset property data of type integer (whole number).</p>"""
    double_value: NotRequired[
        "capo_iotsitewise.types.property_value_double_value.PropertyValueDoubleValue"
    ]
    """<p> Asset property data of type double (floating point number). The min value is -10^10. The max value is 10^10. Double.NaN is allowed. </p>"""
    boolean_value: NotRequired[
        "capo_iotsitewise.types.property_value_boolean_value.PropertyValueBooleanValue"
    ]
    """<p>Asset property data of type Boolean (true or false).</p>"""
    null_value: NotRequired[
        "capo_iotsitewise.types.property_value_null_value.PropertyValueNullValue"
    ]
    """<p>The type of null asset property data with BAD and UNCERTAIN qualities.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Variant) -> dict:
    out: dict = {}
    if "string_value" in value:
        out["stringValue"] = value["string_value"]
    if "integer_value" in value:
        out["integerValue"] = value["integer_value"]
    if "double_value" in value:
        out["doubleValue"] = (
            "NaN"
            if value["double_value"] != value["double_value"]
            else "Infinity"
            if value["double_value"] == float("inf")
            else "-Infinity"
            if value["double_value"] == float("-inf")
            else value["double_value"]
        )
    if "boolean_value" in value:
        out["booleanValue"] = value["boolean_value"]
    if "null_value" in value:
        import capo_iotsitewise.types.property_value_null_value

        out["nullValue"] = (
            capo_iotsitewise.types.property_value_null_value.serialize_json(
                value["null_value"]
            )
        )
    return out


def deserialize_json(data: dict) -> Variant:
    out: Variant = {}  # type: ignore[typeddict-item]
    if data.get("stringValue") is not None:
        out["string_value"] = data["stringValue"]
    if data.get("integerValue") is not None:
        out["integer_value"] = data["integerValue"]
    if data.get("doubleValue") is not None:
        out["double_value"] = float(data["doubleValue"])
    if data.get("booleanValue") is not None:
        out["boolean_value"] = data["booleanValue"]
    if data.get("nullValue") is not None:
        import capo_iotsitewise.types.property_value_null_value

        out["null_value"] = (
            capo_iotsitewise.types.property_value_null_value.deserialize_json(
                data["nullValue"]
            )
        )
    return out
