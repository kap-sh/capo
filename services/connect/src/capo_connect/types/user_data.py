"""Generated from Smithy shape ``com.amazonaws.connect#UserData``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connect.types.agent_contact_reference_list
    import capo_connect.types.agent_status_name
    import capo_connect.types.agent_status_reference
    import capo_connect.types.channel_to_count_map
    import capo_connect.types.hierarchy_path_reference
    import capo_connect.types.routing_profile_reference
    import capo_connect.types.user_reference


class UserData(TypedDict, closed=True):
    user: NotRequired["capo_connect.types.user_reference.UserReference"]
    """<p>Information about the user for the data that is returned. It contains the <code>resourceId</code> and ARN of the user. </p>"""
    routing_profile: NotRequired[
        "capo_connect.types.routing_profile_reference.RoutingProfileReference"
    ]
    """<p>Information about the routing profile that is assigned to the user.</p>"""
    hierarchy_path: NotRequired[
        "capo_connect.types.hierarchy_path_reference.HierarchyPathReference"
    ]
    """<p>Contains information about the levels of a hierarchy group assigned to a user.</p>"""
    status: NotRequired[
        "capo_connect.types.agent_status_reference.AgentStatusReference"
    ]
    """<p>The status of the agent that they manually set in their Contact Control Panel (CCP), or that the supervisor manually changes in the real-time metrics report.</p>"""
    available_slots_by_channel: NotRequired[
        "capo_connect.types.channel_to_count_map.ChannelToCountMap"
    ]
    """<p>A map of available slots by channel. The key is a channel name. The value is an integer: the available number of slots. </p>"""
    max_slots_by_channel: NotRequired[
        "capo_connect.types.channel_to_count_map.ChannelToCountMap"
    ]
    """<p>A map of maximum slots by channel. The key is a channel name. The value is an integer: the maximum number of slots. This is calculated from <a href="https://docs.aws.amazon.com/connect/latest/APIReference/API_MediaConcurrency.html">MediaConcurrency</a> of the <code>RoutingProfile</code> assigned to the agent. </p>"""
    active_slots_by_channel: NotRequired[
        "capo_connect.types.channel_to_count_map.ChannelToCountMap"
    ]
    """<p> A map of active slots by channel. The key is a channel name. The value is an integer: the number of active slots. </p>"""
    contacts: NotRequired[
        "capo_connect.types.agent_contact_reference_list.AgentContactReferenceList"
    ]
    """<p>A list of contact reference information.</p>"""
    next_status: NotRequired["capo_connect.types.agent_status_name.AgentStatusName"]
    """<p>The Next status of the agent.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UserData) -> dict:
    out: dict = {}
    if "user" in value:
        import capo_connect.types.user_reference

        out["User"] = capo_connect.types.user_reference.serialize_json(value["user"])
    if "routing_profile" in value:
        import capo_connect.types.routing_profile_reference

        out["RoutingProfile"] = (
            capo_connect.types.routing_profile_reference.serialize_json(
                value["routing_profile"]
            )
        )
    if "hierarchy_path" in value:
        import capo_connect.types.hierarchy_path_reference

        out["HierarchyPath"] = (
            capo_connect.types.hierarchy_path_reference.serialize_json(
                value["hierarchy_path"]
            )
        )
    if "status" in value:
        import capo_connect.types.agent_status_reference

        out["Status"] = capo_connect.types.agent_status_reference.serialize_json(
            value["status"]
        )
    if "available_slots_by_channel" in value:
        import capo_connect.types.channel_to_count_map

        out["AvailableSlotsByChannel"] = (
            capo_connect.types.channel_to_count_map.serialize_json(
                value["available_slots_by_channel"]
            )
        )
    if "max_slots_by_channel" in value:
        import capo_connect.types.channel_to_count_map

        out["MaxSlotsByChannel"] = (
            capo_connect.types.channel_to_count_map.serialize_json(
                value["max_slots_by_channel"]
            )
        )
    if "active_slots_by_channel" in value:
        import capo_connect.types.channel_to_count_map

        out["ActiveSlotsByChannel"] = (
            capo_connect.types.channel_to_count_map.serialize_json(
                value["active_slots_by_channel"]
            )
        )
    if "contacts" in value:
        import capo_connect.types.agent_contact_reference_list

        out["Contacts"] = (
            capo_connect.types.agent_contact_reference_list.serialize_json(
                value["contacts"]
            )
        )
    if "next_status" in value:
        out["NextStatus"] = value["next_status"]
    return out


def deserialize_json(data: dict) -> UserData:
    out: UserData = {}  # type: ignore[typeddict-item]
    if data.get("User") is not None:
        import capo_connect.types.user_reference

        out["user"] = capo_connect.types.user_reference.deserialize_json(data["User"])
    if data.get("RoutingProfile") is not None:
        import capo_connect.types.routing_profile_reference

        out["routing_profile"] = (
            capo_connect.types.routing_profile_reference.deserialize_json(
                data["RoutingProfile"]
            )
        )
    if data.get("HierarchyPath") is not None:
        import capo_connect.types.hierarchy_path_reference

        out["hierarchy_path"] = (
            capo_connect.types.hierarchy_path_reference.deserialize_json(
                data["HierarchyPath"]
            )
        )
    if data.get("Status") is not None:
        import capo_connect.types.agent_status_reference

        out["status"] = capo_connect.types.agent_status_reference.deserialize_json(
            data["Status"]
        )
    if data.get("AvailableSlotsByChannel") is not None:
        import capo_connect.types.channel_to_count_map

        out["available_slots_by_channel"] = (
            capo_connect.types.channel_to_count_map.deserialize_json(
                data["AvailableSlotsByChannel"]
            )
        )
    if data.get("MaxSlotsByChannel") is not None:
        import capo_connect.types.channel_to_count_map

        out["max_slots_by_channel"] = (
            capo_connect.types.channel_to_count_map.deserialize_json(
                data["MaxSlotsByChannel"]
            )
        )
    if data.get("ActiveSlotsByChannel") is not None:
        import capo_connect.types.channel_to_count_map

        out["active_slots_by_channel"] = (
            capo_connect.types.channel_to_count_map.deserialize_json(
                data["ActiveSlotsByChannel"]
            )
        )
    if data.get("Contacts") is not None:
        import capo_connect.types.agent_contact_reference_list

        out["contacts"] = (
            capo_connect.types.agent_contact_reference_list.deserialize_json(
                data["Contacts"]
            )
        )
    if data.get("NextStatus") is not None:
        out["next_status"] = data["NextStatus"]
    return out
