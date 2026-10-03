"""Generated from Smithy shape ``com.amazonaws.customerprofiles#Range``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_customer_profiles.types.string1_to255
    import capo_customer_profiles.types.unit
    import capo_customer_profiles.types.value
    import capo_customer_profiles.types.value_range


class Range(TypedDict, closed=True):
    value: "capo_customer_profiles.types.value.Value"
    """<p>The amount of time of the specified unit.</p>"""
    unit: "capo_customer_profiles.types.unit.Unit"
    """<p>The unit of time.</p>"""
    value_range: NotRequired["capo_customer_profiles.types.value_range.ValueRange"]
    """<p>A structure letting customers specify a relative time window over which over which data is included in the Calculated Attribute. Use positive numbers to indicate that the endpoint is in the past, and negative numbers to indicate it is in the future. ValueRange overrides Value.</p>"""
    timestamp_source: NotRequired[
        "capo_customer_profiles.types.string1_to255.string1To255"
    ]
    r"""<p>An expression specifying the field in your JSON object from which the date should be parsed. The expression should follow the structure of \"{ObjectTypeName.<Location of timestamp field in JSON pointer format>}\". E.g. if your object type is MyType and source JSON is {"generatedAt": {"timestamp": "1737587945945"}}, then TimestampSource should be "{MyType.generatedAt.timestamp}".</p>"""
    timestamp_format: NotRequired[
        "capo_customer_profiles.types.string1_to255.string1To255"
    ]
    """<p>The format the timestamp field in your JSON object is specified. This value should be one of EPOCHMILLI (for Unix epoch timestamps with second/millisecond level precision) or ISO_8601 (following ISO_8601 format with second/millisecond level precision, with an optional offset of Z or in the format HH:MM or HHMM.). E.g. if your object type is MyType and source JSON is {"generatedAt": {"timestamp": "2001-07-04T12:08:56.235-0700"}}, then TimestampFormat should be "ISO_8601".</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Range) -> dict:
    out: dict = {}
    out["Value"] = value.get("value", 0)
    import capo_customer_profiles.types.unit

    out["Unit"] = capo_customer_profiles.types.unit.serialize_json(
        value.get("unit", "DAYS")
    )
    if "value_range" in value:
        import capo_customer_profiles.types.value_range

        out["ValueRange"] = capo_customer_profiles.types.value_range.serialize_json(
            value["value_range"]
        )
    if "timestamp_source" in value:
        out["TimestampSource"] = value["timestamp_source"]
    if "timestamp_format" in value:
        out["TimestampFormat"] = value["timestamp_format"]
    return out


def deserialize_json(data: dict) -> Range:
    out: Range = {}  # type: ignore[typeddict-item]
    if data.get("Value") is not None:
        out["value"] = data["Value"]
    else:
        out["value"] = 0
    if data.get("Unit") is not None:
        import capo_customer_profiles.types.unit

        out["unit"] = capo_customer_profiles.types.unit.deserialize_json(data["Unit"])
    else:
        out["unit"] = "DAYS"
    if data.get("ValueRange") is not None:
        import capo_customer_profiles.types.value_range

        out["value_range"] = capo_customer_profiles.types.value_range.deserialize_json(
            data["ValueRange"]
        )
    if data.get("TimestampSource") is not None:
        out["timestamp_source"] = data["TimestampSource"]
    if data.get("TimestampFormat") is not None:
        out["timestamp_format"] = data["TimestampFormat"]
    return out
