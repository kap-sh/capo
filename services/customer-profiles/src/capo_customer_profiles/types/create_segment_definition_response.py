"""Generated from Smithy shape ``com.amazonaws.customerprofiles#CreateSegmentDefinitionResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_customer_profiles.errors import DeserializationError

if TYPE_CHECKING:
    import capo_customer_profiles.types.name
    import capo_customer_profiles.types.segment_definition_arn
    import capo_customer_profiles.types.sensitive_string1_to4000
    import capo_customer_profiles.types.string1_to255
    import capo_customer_profiles.types.tag_map
    import capo_customer_profiles.types.timestamp


class CreateSegmentDefinitionResponse(TypedDict, closed=True):
    segment_definition_name: "capo_customer_profiles.types.name.name"
    """<p>The name of the segment definition.</p>"""
    display_name: NotRequired["capo_customer_profiles.types.string1_to255.string1To255"]
    """<p>The display name of the segment definition.</p>"""
    description: NotRequired[
        "capo_customer_profiles.types.sensitive_string1_to4000.sensitiveString1To4000"
    ]
    """<p>The description of the segment definition.</p>"""
    created_at: NotRequired["capo_customer_profiles.types.timestamp.timestamp"]
    """<p>The timestamp of when the segment definition was created.</p>"""
    segment_definition_arn: NotRequired[
        "capo_customer_profiles.types.segment_definition_arn.SegmentDefinitionArn"
    ]
    """<p>The arn of the segment definition.</p>"""
    tags: NotRequired["capo_customer_profiles.types.tag_map.TagMap"]
    """<p>The tags used to organize, track, or control access for this resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateSegmentDefinitionResponse) -> dict:
    out: dict = {}
    out["SegmentDefinitionName"] = value["segment_definition_name"]
    if "display_name" in value:
        out["DisplayName"] = value["display_name"]
    if "description" in value:
        out["Description"] = value["description"]
    if "created_at" in value:
        import capo_customer_profiles.types.timestamp

        out["CreatedAt"] = capo_customer_profiles.types.timestamp.serialize_json(
            value["created_at"]
        )
    if "segment_definition_arn" in value:
        out["SegmentDefinitionArn"] = value["segment_definition_arn"]
    if "tags" in value:
        import capo_customer_profiles.types.tag_map

        out["Tags"] = capo_customer_profiles.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> CreateSegmentDefinitionResponse:
    out: CreateSegmentDefinitionResponse = {}  # type: ignore[typeddict-item]
    if data.get("SegmentDefinitionName") is not None:
        out["segment_definition_name"] = data["SegmentDefinitionName"]
    else:
        raise DeserializationError(
            "CreateSegmentDefinitionResponse.segment_definition_name required"
        )
    if data.get("DisplayName") is not None:
        out["display_name"] = data["DisplayName"]
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("CreatedAt") is not None:
        import capo_customer_profiles.types.timestamp

        out["created_at"] = capo_customer_profiles.types.timestamp.deserialize_json(
            data["CreatedAt"]
        )
    if data.get("SegmentDefinitionArn") is not None:
        out["segment_definition_arn"] = data["SegmentDefinitionArn"]
    if data.get("Tags") is not None:
        import capo_customer_profiles.types.tag_map

        out["tags"] = capo_customer_profiles.types.tag_map.deserialize_json(
            data["Tags"]
        )
    return out


def redact_sensitive(value: CreateSegmentDefinitionResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "description" in value:
        out["description"] = "*** Sensitive Data Redacted ***"
    return out
