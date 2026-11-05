"""Generated from Smithy shape ``com.amazonaws.connectcontactlens#TagCondition``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connect_contact_lens.types.tag_comparison_type
    import capo_connect_contact_lens.types.tag_key
    import capo_connect_contact_lens.types.tag_value


class TagCondition(TypedDict, closed=True):
    tag_key: NotRequired["capo_connect_contact_lens.types.tag_key.TagKey"]
    """<p>The tag key in the tag condition.</p>"""
    tag_value: NotRequired["capo_connect_contact_lens.types.tag_value.TagValue"]
    """<p>The tag value in the tag condition.</p>"""
    comparison_type: NotRequired[
        "capo_connect_contact_lens.types.tag_comparison_type.TagComparisonType"
    ]
    """<p>The comparison operator for the tag condition. Valid values: <code>EQUALS</code> | <code>NOT_EQUALS</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TagCondition) -> dict:
    out: dict = {}
    if "tag_key" in value:
        out["TagKey"] = value["tag_key"]
    if "tag_value" in value:
        out["TagValue"] = value["tag_value"]
    if "comparison_type" in value:
        import capo_connect_contact_lens.types.tag_comparison_type

        out["ComparisonType"] = (
            capo_connect_contact_lens.types.tag_comparison_type.serialize_json(
                value["comparison_type"]
            )
        )
    return out


def deserialize_json(data: dict) -> TagCondition:
    out: TagCondition = {}  # type: ignore[typeddict-item]
    if data.get("TagKey") is not None:
        out["tag_key"] = data["TagKey"]
    if data.get("TagValue") is not None:
        out["tag_value"] = data["TagValue"]
    if data.get("ComparisonType") is not None:
        import capo_connect_contact_lens.types.tag_comparison_type

        out["comparison_type"] = (
            capo_connect_contact_lens.types.tag_comparison_type.deserialize_json(
                data["ComparisonType"]
            )
        )
    return out
