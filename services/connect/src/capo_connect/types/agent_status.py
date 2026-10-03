"""Generated from Smithy shape ``com.amazonaws.connect#AgentStatus``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connect.types.agent_status_description
    import capo_connect.types.agent_status_id
    import capo_connect.types.agent_status_name
    import capo_connect.types.agent_status_order_number
    import capo_connect.types.agent_status_state
    import capo_connect.types.agent_status_type
    import capo_connect.types.arn
    import capo_connect.types.region_name
    import capo_connect.types.tag_map
    import capo_connect.types.timestamp


class AgentStatus(TypedDict, closed=True):
    agent_status_arn: NotRequired["capo_connect.types.arn.ARN"]
    """<p>The Amazon Resource Name (ARN) of the agent status.</p>"""
    agent_status_id: NotRequired["capo_connect.types.agent_status_id.AgentStatusId"]
    """<p>The identifier of the agent status.</p>"""
    name: NotRequired["capo_connect.types.agent_status_name.AgentStatusName"]
    """<p>The name of the agent status.</p>"""
    description: NotRequired[
        "capo_connect.types.agent_status_description.AgentStatusDescription"
    ]
    """<p>The description of the agent status.</p>"""
    type: NotRequired["capo_connect.types.agent_status_type.AgentStatusType"]
    """<p>The type of agent status.</p>"""
    display_order: NotRequired[
        "capo_connect.types.agent_status_order_number.AgentStatusOrderNumber"
    ]
    """<p>The display order of the agent status.</p>"""
    state: NotRequired["capo_connect.types.agent_status_state.AgentStatusState"]
    """<p>The state of the agent status.</p>"""
    tags: NotRequired["capo_connect.types.tag_map.TagMap"]
    """<p>The tags used to organize, track, or control access for this resource. For example, { "Tags": {"key1":"value1", "key2":"value2"} }.</p>"""
    last_modified_time: NotRequired["capo_connect.types.timestamp.Timestamp"]
    """<p>The timestamp when this resource was last modified.</p>"""
    last_modified_region: NotRequired["capo_connect.types.region_name.RegionName"]
    """<p>The Amazon Web Services Region where this resource was last modified.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AgentStatus) -> dict:
    out: dict = {}
    if "agent_status_arn" in value:
        out["AgentStatusARN"] = value["agent_status_arn"]
    if "agent_status_id" in value:
        out["AgentStatusId"] = value["agent_status_id"]
    if "name" in value:
        out["Name"] = value["name"]
    if "description" in value:
        out["Description"] = value["description"]
    if "type" in value:
        import capo_connect.types.agent_status_type

        out["Type"] = capo_connect.types.agent_status_type.serialize_json(value["type"])
    if "display_order" in value:
        out["DisplayOrder"] = value["display_order"]
    if "state" in value:
        import capo_connect.types.agent_status_state

        out["State"] = capo_connect.types.agent_status_state.serialize_json(
            value["state"]
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


def deserialize_json(data: dict) -> AgentStatus:
    out: AgentStatus = {}  # type: ignore[typeddict-item]
    if data.get("AgentStatusARN") is not None:
        out["agent_status_arn"] = data["AgentStatusARN"]
    if data.get("AgentStatusId") is not None:
        out["agent_status_id"] = data["AgentStatusId"]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("Type") is not None:
        import capo_connect.types.agent_status_type

        out["type"] = capo_connect.types.agent_status_type.deserialize_json(
            data["Type"]
        )
    if data.get("DisplayOrder") is not None:
        out["display_order"] = data["DisplayOrder"]
    if data.get("State") is not None:
        import capo_connect.types.agent_status_state

        out["state"] = capo_connect.types.agent_status_state.deserialize_json(
            data["State"]
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
