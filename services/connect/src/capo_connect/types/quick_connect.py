"""Generated from Smithy shape ``com.amazonaws.connect#QuickConnect``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connect.types.arn
    import capo_connect.types.quick_connect_config
    import capo_connect.types.quick_connect_description
    import capo_connect.types.quick_connect_id
    import capo_connect.types.quick_connect_name
    import capo_connect.types.region_name
    import capo_connect.types.tag_map
    import capo_connect.types.timestamp


class QuickConnect(TypedDict, closed=True):
    quick_connect_arn: NotRequired["capo_connect.types.arn.ARN"]
    """<p>The Amazon Resource Name (ARN) of the quick connect.</p>"""
    quick_connect_id: NotRequired["capo_connect.types.quick_connect_id.QuickConnectId"]
    """<p>The identifier for the quick connect.</p>"""
    name: NotRequired["capo_connect.types.quick_connect_name.QuickConnectName"]
    """<p>The name of the quick connect.</p>"""
    description: NotRequired[
        "capo_connect.types.quick_connect_description.QuickConnectDescription"
    ]
    """<p>The description.</p>"""
    quick_connect_config: NotRequired[
        "capo_connect.types.quick_connect_config.QuickConnectConfig"
    ]
    """<p>Contains information about the quick connect.</p>"""
    tags: NotRequired["capo_connect.types.tag_map.TagMap"]
    """<p>The tags used to organize, track, or control access for this resource. For example, { "Tags": {"key1":"value1", "key2":"value2"} }.</p>"""
    last_modified_time: NotRequired["capo_connect.types.timestamp.Timestamp"]
    """<p>The timestamp when this resource was last modified.</p>"""
    last_modified_region: NotRequired["capo_connect.types.region_name.RegionName"]
    """<p>The Amazon Web Services Region where this resource was last modified.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: QuickConnect) -> dict:
    out: dict = {}
    if "quick_connect_arn" in value:
        out["QuickConnectARN"] = value["quick_connect_arn"]
    if "quick_connect_id" in value:
        out["QuickConnectId"] = value["quick_connect_id"]
    if "name" in value:
        out["Name"] = value["name"]
    if "description" in value:
        out["Description"] = value["description"]
    if "quick_connect_config" in value:
        import capo_connect.types.quick_connect_config

        out["QuickConnectConfig"] = (
            capo_connect.types.quick_connect_config.serialize_json(
                value["quick_connect_config"]
            )
        )
    if "tags" in value:
        import capo_connect.types.tag_map

        out["Tags"] = capo_connect.types.tag_map.serialize_json(value["tags"])
    if "last_modified_time" in value:
        import capo_connect.types.timestamp

        out["LastModifiedTime"] = capo_connect.types.timestamp.serialize_json(
            value["last_modified_time"]
        )
    if "last_modified_region" in value:
        out["LastModifiedRegion"] = value["last_modified_region"]
    return out


def deserialize_json(data: dict) -> QuickConnect:
    out: QuickConnect = {}  # type: ignore[typeddict-item]
    if data.get("QuickConnectARN") is not None:
        out["quick_connect_arn"] = data["QuickConnectARN"]
    if data.get("QuickConnectId") is not None:
        out["quick_connect_id"] = data["QuickConnectId"]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("QuickConnectConfig") is not None:
        import capo_connect.types.quick_connect_config

        out["quick_connect_config"] = (
            capo_connect.types.quick_connect_config.deserialize_json(
                data["QuickConnectConfig"]
            )
        )
    if data.get("Tags") is not None:
        import capo_connect.types.tag_map

        out["tags"] = capo_connect.types.tag_map.deserialize_json(data["Tags"])
    if data.get("LastModifiedTime") is not None:
        import capo_connect.types.timestamp

        out["last_modified_time"] = capo_connect.types.timestamp.deserialize_json(
            data["LastModifiedTime"]
        )
    if data.get("LastModifiedRegion") is not None:
        out["last_modified_region"] = data["LastModifiedRegion"]
    return out
