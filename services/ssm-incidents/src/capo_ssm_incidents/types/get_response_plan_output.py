"""Generated from Smithy shape ``com.amazonaws.ssmincidents#GetResponsePlanOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ssm_incidents.errors import DeserializationError

if TYPE_CHECKING:
    import capo_ssm_incidents.types.actions_list
    import capo_ssm_incidents.types.arn
    import capo_ssm_incidents.types.chat_channel
    import capo_ssm_incidents.types.engagement_set
    import capo_ssm_incidents.types.incident_template
    import capo_ssm_incidents.types.integrations
    import capo_ssm_incidents.types.response_plan_display_name
    import capo_ssm_incidents.types.response_plan_name


class GetResponsePlanOutput(TypedDict, closed=True):
    arn: "capo_ssm_incidents.types.arn.Arn"
    """<p>The ARN of the response plan.</p>"""
    name: "capo_ssm_incidents.types.response_plan_name.ResponsePlanName"
    """<p>The short format name of the response plan. The name can't contain spaces.</p>"""
    display_name: NotRequired[
        "capo_ssm_incidents.types.response_plan_display_name.ResponsePlanDisplayName"
    ]
    """<p>The long format name of the response plan. Can contain spaces.</p>"""
    incident_template: "capo_ssm_incidents.types.incident_template.IncidentTemplate"
    """<p>Details used to create the incident when using this response plan.</p>"""
    chat_channel: NotRequired["capo_ssm_incidents.types.chat_channel.ChatChannel"]
    """<p>The Chatbot chat channel used for collaboration during an incident.</p>"""
    engagements: NotRequired["capo_ssm_incidents.types.engagement_set.EngagementSet"]
    """<p>The Amazon Resource Name (ARN) for the contacts and escalation plans that the response plan engages during an incident.</p>"""
    actions: NotRequired["capo_ssm_incidents.types.actions_list.ActionsList"]
    """<p>The actions that this response plan takes at the beginning of the incident.</p>"""
    integrations: NotRequired["capo_ssm_incidents.types.integrations.Integrations"]
    """<p>Information about third-party services integrated into the Incident Manager response plan.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetResponsePlanOutput) -> dict:
    out: dict = {}
    out["arn"] = value["arn"]
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
    if "integrations" in value:
        import capo_ssm_incidents.types.integrations

        out["integrations"] = capo_ssm_incidents.types.integrations.serialize_json(
            value["integrations"]
        )
    return out


def deserialize_json(data: dict) -> GetResponsePlanOutput:
    out: GetResponsePlanOutput = {}  # type: ignore[typeddict-item]
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    else:
        out["arn"] = ""
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
        raise DeserializationError("GetResponsePlanOutput.incident_template required")
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
    if data.get("integrations") is not None:
        import capo_ssm_incidents.types.integrations

        out["integrations"] = capo_ssm_incidents.types.integrations.deserialize_json(
            data["integrations"]
        )
    return out
