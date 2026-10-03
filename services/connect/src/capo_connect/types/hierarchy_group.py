"""Generated from Smithy shape ``com.amazonaws.connect#HierarchyGroup``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connect.types.arn
    import capo_connect.types.hierarchy_group_id
    import capo_connect.types.hierarchy_group_name
    import capo_connect.types.hierarchy_level_id
    import capo_connect.types.hierarchy_path
    import capo_connect.types.region_name
    import capo_connect.types.tag_map
    import capo_connect.types.timestamp


class HierarchyGroup(TypedDict, closed=True):
    id: NotRequired["capo_connect.types.hierarchy_group_id.HierarchyGroupId"]
    """<p>The identifier of the hierarchy group.</p>"""
    arn: NotRequired["capo_connect.types.arn.ARN"]
    """<p>The Amazon Resource Name (ARN) of the hierarchy group.</p>"""
    name: NotRequired["capo_connect.types.hierarchy_group_name.HierarchyGroupName"]
    """<p>The name of the hierarchy group.</p>"""
    level_id: NotRequired["capo_connect.types.hierarchy_level_id.HierarchyLevelId"]
    """<p>The identifier of the level in the hierarchy group.</p>"""
    hierarchy_path: NotRequired["capo_connect.types.hierarchy_path.HierarchyPath"]
    """<p>Information about the levels in the hierarchy group.</p>"""
    tags: NotRequired["capo_connect.types.tag_map.TagMap"]
    """<p>The tags used to organize, track, or control access for this resource. For example, { "Tags": {"key1":"value1", "key2":"value2"} }.</p>"""
    last_modified_time: NotRequired["capo_connect.types.timestamp.Timestamp"]
    """<p>The timestamp when this resource was last modified.</p>"""
    last_modified_region: NotRequired["capo_connect.types.region_name.RegionName"]
    """<p>The Amazon Web Services Region where this resource was last modified.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: HierarchyGroup) -> dict:
    out: dict = {}
    if "id" in value:
        out["Id"] = value["id"]
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "name" in value:
        out["Name"] = value["name"]
    if "level_id" in value:
        out["LevelId"] = value["level_id"]
    if "hierarchy_path" in value:
        import capo_connect.types.hierarchy_path

        out["HierarchyPath"] = capo_connect.types.hierarchy_path.serialize_json(
            value["hierarchy_path"]
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


def deserialize_json(data: dict) -> HierarchyGroup:
    out: HierarchyGroup = {}  # type: ignore[typeddict-item]
    if data.get("Id") is not None:
        out["id"] = data["Id"]
    if data.get("Arn") is not None:
        out["arn"] = data["Arn"]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("LevelId") is not None:
        out["level_id"] = data["LevelId"]
    if data.get("HierarchyPath") is not None:
        import capo_connect.types.hierarchy_path

        out["hierarchy_path"] = capo_connect.types.hierarchy_path.deserialize_json(
            data["HierarchyPath"]
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
