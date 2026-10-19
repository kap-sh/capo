"""Generated from Smithy shape ``com.amazonaws.customerprofiles#GetSegmentDefinitionResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_customer_profiles.types.name
    import capo_customer_profiles.types.segment_definition_arn
    import capo_customer_profiles.types.segment_group
    import capo_customer_profiles.types.segment_sort
    import capo_customer_profiles.types.segment_type
    import capo_customer_profiles.types.sensitive_string1_to4000
    import capo_customer_profiles.types.sensitive_string1_to50000
    import capo_customer_profiles.types.string1_to255
    import capo_customer_profiles.types.tag_map
    import capo_customer_profiles.types.timestamp


class GetSegmentDefinitionResponse(TypedDict, closed=True):
    segment_definition_name: NotRequired["capo_customer_profiles.types.name.name"]
    """<p>The name of the segment definition.</p>"""
    display_name: NotRequired["capo_customer_profiles.types.string1_to255.string1To255"]
    """<p>The display name of the segment definition.</p>"""
    description: NotRequired[
        "capo_customer_profiles.types.sensitive_string1_to4000.sensitiveString1To4000"
    ]
    """<p>The description of the segment definition.</p>"""
    segment_groups: NotRequired[
        "capo_customer_profiles.types.segment_group.SegmentGroup"
    ]
    """<p>The segment criteria associated with this definition.</p>"""
    segment_sort: NotRequired["capo_customer_profiles.types.segment_sort.SegmentSort"]
    """<p>The segment sort.</p>"""
    segment_definition_arn: (
        "capo_customer_profiles.types.segment_definition_arn.SegmentDefinitionArn"
    )
    """<p>The arn of the segment definition.</p>"""
    created_at: NotRequired["capo_customer_profiles.types.timestamp.timestamp"]
    """<p>The timestamp of when the segment definition was created.</p>"""
    tags: NotRequired["capo_customer_profiles.types.tag_map.TagMap"]
    """<p>The tags used to organize, track, or control access for this resource.</p>"""
    segment_sql_query: NotRequired[
        "capo_customer_profiles.types.sensitive_string1_to50000.sensitiveString1To50000"
    ]
    """<p>The segment SQL query.</p>"""
    segment_type: NotRequired["capo_customer_profiles.types.segment_type.SegmentType"]
    """<p>The segment type.</p> <p> Classic : Segments created using traditional SegmentGroup structure</p> <p> Enhanced : Segments created using SQL queries </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetSegmentDefinitionResponse) -> dict:
    out: dict = {}
    if "segment_definition_name" in value:
        out["SegmentDefinitionName"] = value["segment_definition_name"]
    if "display_name" in value:
        out["DisplayName"] = value["display_name"]
    if "description" in value:
        out["Description"] = value["description"]
    if "segment_groups" in value:
        import capo_customer_profiles.types.segment_group

        out["SegmentGroups"] = (
            capo_customer_profiles.types.segment_group.serialize_json(
                value["segment_groups"]
            )
        )
    if "segment_sort" in value:
        import capo_customer_profiles.types.segment_sort

        out["SegmentSort"] = capo_customer_profiles.types.segment_sort.serialize_json(
            value["segment_sort"]
        )
    out["SegmentDefinitionArn"] = value["segment_definition_arn"]
    if "created_at" in value:
        import capo_customer_profiles.types.timestamp

        out["CreatedAt"] = capo_customer_profiles.types.timestamp.serialize_json(
            value["created_at"]
        )
    if "tags" in value:
        import capo_customer_profiles.types.tag_map

        out["Tags"] = capo_customer_profiles.types.tag_map.serialize_json(value["tags"])
    if "segment_sql_query" in value:
        out["SegmentSqlQuery"] = value["segment_sql_query"]
    if "segment_type" in value:
        import capo_customer_profiles.types.segment_type

        out["SegmentType"] = capo_customer_profiles.types.segment_type.serialize_json(
            value["segment_type"]
        )
    return out


def deserialize_json(data: dict) -> GetSegmentDefinitionResponse:
    out: GetSegmentDefinitionResponse = {}  # type: ignore[typeddict-item]
    if data.get("SegmentDefinitionName") is not None:
        out["segment_definition_name"] = data["SegmentDefinitionName"]
    if data.get("DisplayName") is not None:
        out["display_name"] = data["DisplayName"]
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("SegmentGroups") is not None:
        import capo_customer_profiles.types.segment_group

        out["segment_groups"] = (
            capo_customer_profiles.types.segment_group.deserialize_json(
                data["SegmentGroups"]
            )
        )
    if data.get("SegmentSort") is not None:
        import capo_customer_profiles.types.segment_sort

        out["segment_sort"] = (
            capo_customer_profiles.types.segment_sort.deserialize_json(
                data["SegmentSort"]
            )
        )
    if data.get("SegmentDefinitionArn") is not None:
        out["segment_definition_arn"] = data["SegmentDefinitionArn"]
    else:
        out["segment_definition_arn"] = ""
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
    if data.get("SegmentSqlQuery") is not None:
        out["segment_sql_query"] = data["SegmentSqlQuery"]
    if data.get("SegmentType") is not None:
        import capo_customer_profiles.types.segment_type

        out["segment_type"] = (
            capo_customer_profiles.types.segment_type.deserialize_json(
                data["SegmentType"]
            )
        )
    return out


def redact_sensitive(value: GetSegmentDefinitionResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "description" in value:
        out["description"] = "*** Sensitive Data Redacted ***"
    if "segment_groups" in value:
        out["segment_groups"] = "*** Sensitive Data Redacted ***"
    if "segment_sort" in value:
        out["segment_sort"] = "*** Sensitive Data Redacted ***"
    if "segment_sql_query" in value:
        out["segment_sql_query"] = "*** Sensitive Data Redacted ***"
    return out
