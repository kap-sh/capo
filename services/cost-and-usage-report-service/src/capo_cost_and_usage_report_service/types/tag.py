"""Generated from Smithy shape ``com.amazonaws.costandusagereportservice#Tag``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_cost_and_usage_report_service.types.tag_key
    import capo_cost_and_usage_report_service.types.tag_value


class Tag(TypedDict, closed=True):
    key: "capo_cost_and_usage_report_service.types.tag_key.TagKey"
    """<p>The key of the tag. Tag keys are case sensitive. Each report definition can only have up to one tag with the same key. If you try to add an existing tag with the same key, the existing tag value will be updated to the new value.</p>"""
    value: "capo_cost_and_usage_report_service.types.tag_value.TagValue"
    """<p>The value of the tag. Tag values are case-sensitive. This can be an empty string.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Tag) -> dict:
    out: dict = {}
    out["Key"] = value["key"]
    out["Value"] = value["value"]
    return out


def deserialize_aws_json_1_1(data: dict) -> Tag:
    out: Tag = {}  # type: ignore[typeddict-item]
    if data.get("Key") is not None:
        out["key"] = data["Key"]
    else:
        out["key"] = ""
    if data.get("Value") is not None:
        out["value"] = data["Value"]
    else:
        out["value"] = ""
    return out
