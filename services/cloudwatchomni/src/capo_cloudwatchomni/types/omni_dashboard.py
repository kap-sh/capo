"""Generated from Smithy shape ``com.amazonaws.cloudwatchomni#OmniDashboard``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_cloudwatchomni.types.arn
    import capo_cloudwatchomni.types.dashboard_id
    import capo_cloudwatchomni.types.tag_map


class OmniDashboard(TypedDict, closed=True):
    dashboard_id: "capo_cloudwatchomni.types.dashboard_id.DashboardId"
    """The unique ID of the dashboard."""
    arn: "capo_cloudwatchomni.types.arn.Arn"
    """The Amazon Resource Name (ARN) of the dashboard."""
    name: "str"
    """A name that identifies the dashboard."""
    body: "str"
    """The dashboard definition."""
    created_by: "str"
    """The principal that created the dashboard."""
    description: NotRequired["str"]
    """An optional description of the dashboard."""
    tags: NotRequired["capo_cloudwatchomni.types.tag_map.TagMap"]
    """The tags associated with the dashboard."""
    created_at: "datetime.datetime"
    """The timestamp when the dashboard was created."""
    updated_at: "datetime.datetime"
    """The timestamp when the dashboard was last updated."""


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: OmniDashboard) -> dict:
    out: dict = {}
    out["dashboardId"] = value["dashboard_id"]
    out["arn"] = value["arn"]
    out["name"] = value["name"]
    out["body"] = value["body"]
    out["createdBy"] = value["created_by"]
    if "description" in value:
        out["description"] = value["description"]
    if "tags" in value:
        import capo_cloudwatchomni.types.tag_map

        out["tags"] = capo_cloudwatchomni.types.tag_map.serialize_cbor(value["tags"])
    import capo_cloudwatchomni.types._prelude.timestamp

    out["createdAt"] = capo_cloudwatchomni.types._prelude.timestamp.serialize_cbor(
        value["created_at"]
    )
    import capo_cloudwatchomni.types._prelude.timestamp

    out["updatedAt"] = capo_cloudwatchomni.types._prelude.timestamp.serialize_cbor(
        value["updated_at"]
    )
    return out


def deserialize_cbor(data: dict) -> OmniDashboard:
    out: OmniDashboard = {}  # type: ignore[typeddict-item]
    if data.get("dashboardId") is not None:
        out["dashboard_id"] = data["dashboardId"]
    else:
        out["dashboard_id"] = ""
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    else:
        out["arn"] = ""
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("body") is not None:
        out["body"] = data["body"]
    else:
        out["body"] = ""
    if data.get("createdBy") is not None:
        out["created_by"] = data["createdBy"]
    else:
        out["created_by"] = ""
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("tags") is not None:
        import capo_cloudwatchomni.types.tag_map

        out["tags"] = capo_cloudwatchomni.types.tag_map.deserialize_cbor(data["tags"])
    if data.get("createdAt") is not None:
        import capo_cloudwatchomni.types._prelude.timestamp

        out["created_at"] = (
            capo_cloudwatchomni.types._prelude.timestamp.deserialize_cbor(
                data["createdAt"]
            )
        )
    else:
        import datetime

        out["created_at"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    if data.get("updatedAt") is not None:
        import capo_cloudwatchomni.types._prelude.timestamp

        out["updated_at"] = (
            capo_cloudwatchomni.types._prelude.timestamp.deserialize_cbor(
                data["updatedAt"]
            )
        )
    else:
        import datetime

        out["updated_at"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    return out
