"""Generated from Smithy shape ``com.amazonaws.inspector2#Filter``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_inspector2.errors import DeserializationError

if TYPE_CHECKING:
    import capo_inspector2.types.date_time_timestamp
    import capo_inspector2.types.filter_action
    import capo_inspector2.types.filter_arn
    import capo_inspector2.types.filter_criteria
    import capo_inspector2.types.filter_description
    import capo_inspector2.types.filter_name
    import capo_inspector2.types.filter_reason
    import capo_inspector2.types.owner_id
    import capo_inspector2.types.tag_map


class Filter(TypedDict, closed=True):
    arn: "capo_inspector2.types.filter_arn.FilterArn"
    """<p>The Amazon Resource Number (ARN) associated with this filter.</p>"""
    owner_id: "capo_inspector2.types.owner_id.OwnerId"
    """<p>The Amazon Web Services account ID of the account that created the filter.</p>"""
    name: "capo_inspector2.types.filter_name.FilterName"
    """<p>The name of the filter.</p>"""
    criteria: "capo_inspector2.types.filter_criteria.FilterCriteria"
    """<p>Details on the filter criteria associated with this filter.</p>"""
    action: "capo_inspector2.types.filter_action.FilterAction"
    """<p>The action that is to be applied to the findings that match the filter.</p>"""
    created_at: "capo_inspector2.types.date_time_timestamp.DateTimeTimestamp"
    """<p>The date and time this filter was created at.</p>"""
    updated_at: "capo_inspector2.types.date_time_timestamp.DateTimeTimestamp"
    """<p>The date and time the filter was last updated at.</p>"""
    description: NotRequired[
        "capo_inspector2.types.filter_description.FilterDescription"
    ]
    """<p>A description of the filter.</p>"""
    reason: NotRequired["capo_inspector2.types.filter_reason.FilterReason"]
    """<p>The reason for the filter.</p>"""
    tags: NotRequired["capo_inspector2.types.tag_map.TagMap"]
    """<p>The tags attached to the filter.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Filter) -> dict:
    out: dict = {}
    out["arn"] = value["arn"]
    out["ownerId"] = value["owner_id"]
    out["name"] = value["name"]
    import capo_inspector2.types.filter_criteria

    out["criteria"] = capo_inspector2.types.filter_criteria.serialize_json(
        value["criteria"]
    )
    out["action"] = value["action"]
    import capo_inspector2.types.date_time_timestamp

    out["createdAt"] = capo_inspector2.types.date_time_timestamp.serialize_json(
        value["created_at"]
    )
    import capo_inspector2.types.date_time_timestamp

    out["updatedAt"] = capo_inspector2.types.date_time_timestamp.serialize_json(
        value["updated_at"]
    )
    if "description" in value:
        out["description"] = value["description"]
    if "reason" in value:
        out["reason"] = value["reason"]
    if "tags" in value:
        import capo_inspector2.types.tag_map

        out["tags"] = capo_inspector2.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> Filter:
    out: Filter = {}  # type: ignore[typeddict-item]
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    else:
        out["arn"] = ""
    if data.get("ownerId") is not None:
        out["owner_id"] = data["ownerId"]
    else:
        out["owner_id"] = ""
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("criteria") is not None:
        import capo_inspector2.types.filter_criteria

        out["criteria"] = capo_inspector2.types.filter_criteria.deserialize_json(
            data["criteria"]
        )
    else:
        raise DeserializationError("Filter.criteria required")
    if data.get("action") is not None:
        out["action"] = data["action"]
    else:
        out["action"] = ""
    if data.get("createdAt") is not None:
        import capo_inspector2.types.date_time_timestamp

        out["created_at"] = capo_inspector2.types.date_time_timestamp.deserialize_json(
            data["createdAt"]
        )
    else:
        import datetime

        out["created_at"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    if data.get("updatedAt") is not None:
        import capo_inspector2.types.date_time_timestamp

        out["updated_at"] = capo_inspector2.types.date_time_timestamp.deserialize_json(
            data["updatedAt"]
        )
    else:
        import datetime

        out["updated_at"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("reason") is not None:
        out["reason"] = data["reason"]
    if data.get("tags") is not None:
        import capo_inspector2.types.tag_map

        out["tags"] = capo_inspector2.types.tag_map.deserialize_json(data["tags"])
    return out
