"""Generated from Smithy shape ``com.amazonaws.customerprofiles#SegmentDefinitionItem``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_customer_profiles.types.name
    import capo_customer_profiles.types.segment_definition_arn
    import capo_customer_profiles.types.segment_type
    import capo_customer_profiles.types.sensitive_string1_to4000
    import capo_customer_profiles.types.string1_to255
    import capo_customer_profiles.types.tag_map
    import capo_customer_profiles.types.timestamp


class SegmentDefinitionItem(TypedDict, closed=True):
    segment_definition_name: NotRequired["capo_customer_profiles.types.name.name"]
    """<p>Name of the segment definition.</p>"""
    display_name: NotRequired["capo_customer_profiles.types.string1_to255.string1To255"]
    """<p>Display name of the segment definition.</p>"""
    description: NotRequired[
        "capo_customer_profiles.types.sensitive_string1_to4000.sensitiveString1To4000"
    ]
    """<p>The description of the segment definition.</p>"""
    segment_definition_arn: NotRequired[
        "capo_customer_profiles.types.segment_definition_arn.SegmentDefinitionArn"
    ]
    """<p>The arn of the segment definition.</p>"""
    created_at: NotRequired["capo_customer_profiles.types.timestamp.timestamp"]
    """<p>When the segment definition was created.</p>"""
    tags: NotRequired["capo_customer_profiles.types.tag_map.TagMap"]
    """<p>The tags belonging to the segment definition.</p>"""
    segment_type: NotRequired["capo_customer_profiles.types.segment_type.SegmentType"]
    """<p>The segment type.</p> <p> Classic : Segments created using traditional SegmentGroup structure</p> <p> Enhanced : Segments created using SQL queries </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SegmentDefinitionItem) -> dict:
    out: dict = {}
    if "segment_definition_name" in value:
        out["SegmentDefinitionName"] = value["segment_definition_name"]
    if "display_name" in value:
        out["DisplayName"] = value["display_name"]
    if "description" in value:
        out["Description"] = value["description"]
    if "segment_definition_arn" in value:
        out["SegmentDefinitionArn"] = value["segment_definition_arn"]
    if "created_at" in value:
        import capo_customer_profiles.types.timestamp

        out["CreatedAt"] = capo_customer_profiles.types.timestamp.serialize_json(
            value["created_at"]
        )
    if "tags" in value:
        import capo_customer_profiles.types.tag_map

        out["Tags"] = capo_customer_profiles.types.tag_map.serialize_json(value["tags"])
    if "segment_type" in value:
        import capo_customer_profiles.types.segment_type

        out["SegmentType"] = capo_customer_profiles.types.segment_type.serialize_json(
            value["segment_type"]
        )
    return out


def deserialize_json(data: dict) -> SegmentDefinitionItem:
    out: SegmentDefinitionItem = {}  # type: ignore[typeddict-item]
    if data.get("SegmentDefinitionName") is not None:
        out["segment_definition_name"] = data["SegmentDefinitionName"]
    if data.get("DisplayName") is not None:
        out["display_name"] = data["DisplayName"]
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("SegmentDefinitionArn") is not None:
        out["segment_definition_arn"] = data["SegmentDefinitionArn"]
    if data.get("CreatedAt") is not None:
        import capo_customer_profiles.types.timestamp

        out["created_at"] = capo_customer_profiles.types.timestamp.deserialize_json(
            data["CreatedAt"]
        )
    if data.get("Tags") is not None:
        import capo_customer_profiles.types.tag_map

        out["tags"] = capo_customer_profiles.types.tag_map.deserialize_json(
            data["Tags"]
        )
    if data.get("SegmentType") is not None:
        import capo_customer_profiles.types.segment_type

        out["segment_type"] = (
            capo_customer_profiles.types.segment_type.deserialize_json(
                data["SegmentType"]
            )
        )
    return out


def redact_sensitive(value: SegmentDefinitionItem) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "description" in value:
        out["description"] = "*** Sensitive Data Redacted ***"
    return out
