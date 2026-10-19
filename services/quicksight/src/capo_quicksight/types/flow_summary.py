"""Generated from Smithy shape ``com.amazonaws.quicksight#FlowSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.flow_description
    import capo_quicksight.types.flow_id
    import capo_quicksight.types.flow_publish_state
    import capo_quicksight.types.integer
    import capo_quicksight.types.timestamp
    import capo_quicksight.types.title


class FlowSummary(TypedDict, closed=True):
    arn: "str"
    """<p>The Amazon Resource Name (ARN) of the flow.</p>"""
    flow_id: "capo_quicksight.types.flow_id.FlowId"
    """<p>The unique identifier of the flow.</p>"""
    name: "capo_quicksight.types.title.Title"
    """<p>The display name of the flow.</p>"""
    description: NotRequired["capo_quicksight.types.flow_description.FlowDescription"]
    """<p>The description of the flow.</p>"""
    created_time: "capo_quicksight.types.timestamp.Timestamp"
    """<p>The time this flow was created.</p>"""
    created_by: NotRequired["str"]
    """<p>The identifier of the principal who created the flow.</p>"""
    last_updated_time: NotRequired["capo_quicksight.types.timestamp.Timestamp"]
    """<p>The last time this flow was modified.</p>"""
    last_updated_by: NotRequired["str"]
    """<p>The identifier of the last principal who updated the flow.</p>"""
    publish_state: NotRequired[
        "capo_quicksight.types.flow_publish_state.FlowPublishState"
    ]
    """<p>The publish state for the flow. The valid values are <code>DRAFT</code>, <code>PUBLISHED</code>, or <code>PENDING_APPROVAL</code>.</p>"""
    run_count: "capo_quicksight.types.integer.Integer"
    """<p>The number of runs done for the flow.</p>"""
    user_count: "capo_quicksight.types.integer.Integer"
    """<p>The number of users who have used the flow.</p>"""
    last_published_by: NotRequired["str"]
    """<p>The identifier of the last principal who published the flow.</p>"""
    last_published_at: NotRequired["capo_quicksight.types.timestamp.Timestamp"]
    """<p>The last time this flow was published.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FlowSummary) -> dict:
    out: dict = {}
    out["Arn"] = value["arn"]
    out["FlowId"] = value["flow_id"]
    out["Name"] = value["name"]
    if "description" in value:
        out["Description"] = value["description"]
    import capo_quicksight.types.timestamp

    out["CreatedTime"] = capo_quicksight.types.timestamp.serialize_json(
        value["created_time"]
    )
    if "created_by" in value:
        out["CreatedBy"] = value["created_by"]
    if "last_updated_time" in value:
        import capo_quicksight.types.timestamp

        out["LastUpdatedTime"] = capo_quicksight.types.timestamp.serialize_json(
            value["last_updated_time"]
        )
    if "last_updated_by" in value:
        out["LastUpdatedBy"] = value["last_updated_by"]
    if "publish_state" in value:
        import capo_quicksight.types.flow_publish_state

        out["PublishState"] = capo_quicksight.types.flow_publish_state.serialize_json(
            value["publish_state"]
        )
    out["RunCount"] = value.get("run_count", 0)
    out["UserCount"] = value.get("user_count", 0)
    if "last_published_by" in value:
        out["LastPublishedBy"] = value["last_published_by"]
    if "last_published_at" in value:
        import capo_quicksight.types.timestamp

        out["LastPublishedAt"] = capo_quicksight.types.timestamp.serialize_json(
            value["last_published_at"]
        )
    return out


def deserialize_json(data: dict) -> FlowSummary:
    out: FlowSummary = {}  # type: ignore[typeddict-item]
    if data.get("Arn") is not None:
        out["arn"] = data["Arn"]
    else:
        out["arn"] = ""
    if data.get("FlowId") is not None:
        out["flow_id"] = data["FlowId"]
    else:
        out["flow_id"] = ""
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        out["name"] = ""
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("CreatedTime") is not None:
        import capo_quicksight.types.timestamp

        out["created_time"] = capo_quicksight.types.timestamp.deserialize_json(
            data["CreatedTime"]
        )
    else:
        import datetime

        out["created_time"] = datetime.datetime.fromtimestamp(
            0, tz=datetime.timezone.utc
        )
    if data.get("CreatedBy") is not None:
        out["created_by"] = data["CreatedBy"]
    if data.get("LastUpdatedTime") is not None:
        import capo_quicksight.types.timestamp

        out["last_updated_time"] = capo_quicksight.types.timestamp.deserialize_json(
            data["LastUpdatedTime"]
        )
    if data.get("LastUpdatedBy") is not None:
        out["last_updated_by"] = data["LastUpdatedBy"]
    if data.get("PublishState") is not None:
        import capo_quicksight.types.flow_publish_state

        out["publish_state"] = (
            capo_quicksight.types.flow_publish_state.deserialize_json(
                data["PublishState"]
            )
        )
    if data.get("RunCount") is not None:
        out["run_count"] = data["RunCount"]
    else:
        out["run_count"] = 0
    if data.get("UserCount") is not None:
        out["user_count"] = data["UserCount"]
    else:
        out["user_count"] = 0
    if data.get("LastPublishedBy") is not None:
        out["last_published_by"] = data["LastPublishedBy"]
    if data.get("LastPublishedAt") is not None:
        import capo_quicksight.types.timestamp

        out["last_published_at"] = capo_quicksight.types.timestamp.deserialize_json(
            data["LastPublishedAt"]
        )
    return out
