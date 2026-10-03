"""Generated from Smithy shape ``com.amazonaws.connect#CreateAgentStatusRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_connect.errors import DeserializationError

if TYPE_CHECKING:
    import capo_connect.types.agent_status_description
    import capo_connect.types.agent_status_name
    import capo_connect.types.agent_status_order_number
    import capo_connect.types.agent_status_state
    import capo_connect.types.instance_id
    import capo_connect.types.tag_map


class CreateAgentStatusRequest(TypedDict, closed=True):
    instance_id: "capo_connect.types.instance_id.InstanceId"
    """<p>The identifier of the Connect Customer instance. You can <a href="https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html">find the instance ID</a> in the Amazon Resource Name (ARN) of the instance.</p>"""
    name: "capo_connect.types.agent_status_name.AgentStatusName"
    """<p>The name of the status.</p>"""
    description: NotRequired[
        "capo_connect.types.agent_status_description.AgentStatusDescription"
    ]
    """<p>The description of the status.</p>"""
    state: "capo_connect.types.agent_status_state.AgentStatusState"
    """<p>The state of the status.</p>"""
    display_order: NotRequired[
        "capo_connect.types.agent_status_order_number.AgentStatusOrderNumber"
    ]
    """<p>The display order of the status.</p>"""
    tags: NotRequired["capo_connect.types.tag_map.TagMap"]
    """<p>The tags used to organize, track, or control access for this resource. For example, { "Tags": {"key1":"value1", "key2":"value2"} }.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateAgentStatusRequest) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    if "description" in value:
        out["Description"] = value["description"]
    import capo_connect.types.agent_status_state

    out["State"] = capo_connect.types.agent_status_state.serialize_json(value["state"])
    if "display_order" in value:
        out["DisplayOrder"] = value["display_order"]
    if "tags" in value:
        import capo_connect.types.tag_map

        out["Tags"] = capo_connect.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> CreateAgentStatusRequest:
    out: CreateAgentStatusRequest = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("CreateAgentStatusRequest.name required")
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("State") is not None:
        import capo_connect.types.agent_status_state

        out["state"] = capo_connect.types.agent_status_state.deserialize_json(
            data["State"]
        )
    else:
        raise DeserializationError("CreateAgentStatusRequest.state required")
    if data.get("DisplayOrder") is not None:
        out["display_order"] = data["DisplayOrder"]
    if data.get("Tags") is not None:
        import capo_connect.types.tag_map

        out["tags"] = capo_connect.types.tag_map.deserialize_json(data["Tags"])
    return out
