"""Generated from Smithy shape ``com.amazonaws.ssmincidents#CreateResponsePlanInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ssm_incidents.errors import DeserializationError

if TYPE_CHECKING:
    import capo_ssm_incidents.types.actions_list
    import capo_ssm_incidents.types.chat_channel
    import capo_ssm_incidents.types.client_token
    import capo_ssm_incidents.types.engagement_set
    import capo_ssm_incidents.types.incident_template
    import capo_ssm_incidents.types.integrations
    import capo_ssm_incidents.types.response_plan_display_name
    import capo_ssm_incidents.types.response_plan_name
    import capo_ssm_incidents.types.tag_map


class CreateResponsePlanInput(TypedDict, closed=True):
    client_token: NotRequired["capo_ssm_incidents.types.client_token.ClientToken"]
    """<p>A token ensuring that the operation is called only once with the specified details.</p>"""
    name: "capo_ssm_incidents.types.response_plan_name.ResponsePlanName"
    """<p>The short format name of the response plan. Can't include spaces.</p>"""
    display_name: NotRequired[
        "capo_ssm_incidents.types.response_plan_display_name.ResponsePlanDisplayName"
    ]
    """<p>The long format of the response plan name. This field can contain spaces.</p>"""
    incident_template: "capo_ssm_incidents.types.incident_template.IncidentTemplate"
    """<p>Details used to create an incident when using this response plan.</p>"""
    chat_channel: NotRequired["capo_ssm_incidents.types.chat_channel.ChatChannel"]
    """<p>The Chatbot chat channel used for collaboration during an incident.</p>"""
    engagements: NotRequired["capo_ssm_incidents.types.engagement_set.EngagementSet"]
    """<p>The Amazon Resource Name (ARN) for the contacts and escalation plans that the response plan engages during an incident.</p>"""
    actions: NotRequired["capo_ssm_incidents.types.actions_list.ActionsList"]
    """<p>The actions that the response plan starts at the beginning of an incident.</p>"""
    tags: NotRequired["capo_ssm_incidents.types.tag_map.TagMap"]
    """<p>A list of tags that you are adding to the response plan.</p>"""
    integrations: NotRequired["capo_ssm_incidents.types.integrations.Integrations"]
    """<p>Information about third-party services integrated into the response plan.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateResponsePlanInput) -> dict:
    out: dict = {}
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    out["name"] = value["name"]
    if "display_name" in value:
        out["displayName"] = value["display_name"]
    import capo_ssm_incidents.types.incident_template

    out["incidentTemplate"] = capo_ssm_incidents.types.incident_template.serialize_json(
        value["incident_template"]
    )
    if "chat_channel" in value:
        import capo_ssm_incidents.types.chat_channel

        out["chatChannel"] = capo_ssm_incidents.types.chat_channel.serialize_json(
            value["chat_channel"]
        )
    if "engagements" in value:
        import capo_ssm_incidents.types.engagement_set

        out["engagements"] = capo_ssm_incidents.types.engagement_set.serialize_json(
            value["engagements"]
        )
    if "actions" in value:
        import capo_ssm_incidents.types.actions_list

        out["actions"] = capo_ssm_incidents.types.actions_list.serialize_json(
            value["actions"]
        )
    if "tags" in value:
        import capo_ssm_incidents.types.tag_map

        out["tags"] = capo_ssm_incidents.types.tag_map.serialize_json(value["tags"])
    if "integrations" in value:
        import capo_ssm_incidents.types.integrations

        out["integrations"] = capo_ssm_incidents.types.integrations.serialize_json(
            value["integrations"]
        )
    return out


def deserialize_json(data: dict) -> CreateResponsePlanInput:
    out: CreateResponsePlanInput = {}  # type: ignore[typeddict-item]
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("displayName") is not None:
        out["display_name"] = data["displayName"]
    if data.get("incidentTemplate") is not None:
        import capo_ssm_incidents.types.incident_template

        out["incident_template"] = (
            capo_ssm_incidents.types.incident_template.deserialize_json(
                data["incidentTemplate"]
            )
        )
    else:
        raise DeserializationError("CreateResponsePlanInput.incident_template required")
    if data.get("chatChannel") is not None:
        import capo_ssm_incidents.types.chat_channel

        out["chat_channel"] = capo_ssm_incidents.types.chat_channel.deserialize_json(
            data["chatChannel"]
        )
    if data.get("engagements") is not None:
        import capo_ssm_incidents.types.engagement_set

        out["engagements"] = capo_ssm_incidents.types.engagement_set.deserialize_json(
            data["engagements"]
        )
    if data.get("actions") is not None:
        import capo_ssm_incidents.types.actions_list

        out["actions"] = capo_ssm_incidents.types.actions_list.deserialize_json(
            data["actions"]
        )
    if data.get("tags") is not None:
        import capo_ssm_incidents.types.tag_map

        out["tags"] = capo_ssm_incidents.types.tag_map.deserialize_json(data["tags"])
    if data.get("integrations") is not None:
        import capo_ssm_incidents.types.integrations

        out["integrations"] = capo_ssm_incidents.types.integrations.deserialize_json(
            data["integrations"]
        )
    return out
