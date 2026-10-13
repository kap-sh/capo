"""Generated from Smithy shape ``com.amazonaws.quicksight#Dashboard``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.arn
    import capo_quicksight.types.dashboard_name
    import capo_quicksight.types.dashboard_version
    import capo_quicksight.types.link_entity_arn_list
    import capo_quicksight.types.short_restrictive_resource_id
    import capo_quicksight.types.timestamp


class Dashboard(TypedDict, closed=True):
    dashboard_id: NotRequired[
        "capo_quicksight.types.short_restrictive_resource_id.ShortRestrictiveResourceId"
    ]
    """<p>Dashboard ID.</p>"""
    arn: NotRequired["capo_quicksight.types.arn.Arn"]
    """<p>The Amazon Resource Name (ARN) of the resource.</p>"""
    name: NotRequired["capo_quicksight.types.dashboard_name.DashboardName"]
    """<p>A display name for the dashboard.</p>"""
    version: NotRequired["capo_quicksight.types.dashboard_version.DashboardVersion"]
    """<p>Version.</p>"""
    created_time: NotRequired["capo_quicksight.types.timestamp.Timestamp"]
    """<p>The time that this dashboard was created.</p>"""
    last_published_time: NotRequired["capo_quicksight.types.timestamp.Timestamp"]
    """<p>The last time that this dashboard was published.</p>"""
    last_updated_time: NotRequired["capo_quicksight.types.timestamp.Timestamp"]
    """<p>The last time that this dashboard was updated.</p>"""
    link_entities: NotRequired[
        "capo_quicksight.types.link_entity_arn_list.LinkEntityArnList"
    ]
    """<p>A list of analysis Amazon Resource Names (ARNs) to be linked to the dashboard.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Dashboard) -> dict:
    out: dict = {}
    if "dashboard_id" in value:
        out["DashboardId"] = value["dashboard_id"]
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "name" in value:
        out["Name"] = value["name"]
    if "version" in value:
        import capo_quicksight.types.dashboard_version

        out["Version"] = capo_quicksight.types.dashboard_version.serialize_json(
            value["version"]
        )
    if "created_time" in value:
        import capo_quicksight.types.timestamp

        out["CreatedTime"] = capo_quicksight.types.timestamp.serialize_json(
            value["created_time"]
        )
    if "last_published_time" in value:
        import capo_quicksight.types.timestamp

        out["LastPublishedTime"] = capo_quicksight.types.timestamp.serialize_json(
            value["last_published_time"]
        )
    if "last_updated_time" in value:
        import capo_quicksight.types.timestamp

        out["LastUpdatedTime"] = capo_quicksight.types.timestamp.serialize_json(
            value["last_updated_time"]
        )
    if "link_entities" in value:
        import capo_quicksight.types.link_entity_arn_list

        out["LinkEntities"] = capo_quicksight.types.link_entity_arn_list.serialize_json(
            value["link_entities"]
        )
    return out


def deserialize_json(data: dict) -> Dashboard:
    out: Dashboard = {}  # type: ignore[typeddict-item]
    if data.get("DashboardId") is not None:
        out["dashboard_id"] = data["DashboardId"]
    if data.get("Arn") is not None:
        out["arn"] = data["Arn"]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("Version") is not None:
        import capo_quicksight.types.dashboard_version

        out["version"] = capo_quicksight.types.dashboard_version.deserialize_json(
            data["Version"]
        )
    if data.get("CreatedTime") is not None:
        import capo_quicksight.types.timestamp

        out["created_time"] = capo_quicksight.types.timestamp.deserialize_json(
            data["CreatedTime"]
        )
    if data.get("LastPublishedTime") is not None:
        import capo_quicksight.types.timestamp

        out["last_published_time"] = capo_quicksight.types.timestamp.deserialize_json(
            data["LastPublishedTime"]
        )
    if data.get("LastUpdatedTime") is not None:
        import capo_quicksight.types.timestamp

        out["last_updated_time"] = capo_quicksight.types.timestamp.deserialize_json(
            data["LastUpdatedTime"]
        )
    if data.get("LinkEntities") is not None:
        import capo_quicksight.types.link_entity_arn_list

        out["link_entities"] = (
            capo_quicksight.types.link_entity_arn_list.deserialize_json(
                data["LinkEntities"]
            )
        )
    return out


def redact_sensitive(value: Dashboard) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "version" in value:
        import capo_quicksight.types.dashboard_version

        out["version"] = capo_quicksight.types.dashboard_version.redact_sensitive(
            value["version"]
        )
    return out
