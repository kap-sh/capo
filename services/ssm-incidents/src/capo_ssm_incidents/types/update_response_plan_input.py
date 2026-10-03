"""Generated from Smithy shape ``com.amazonaws.ssmincidents#UpdateResponsePlanInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ssm_incidents.errors import DeserializationError

if TYPE_CHECKING:
    import capo_ssm_incidents.types.actions_list
    import capo_ssm_incidents.types.arn
    import capo_ssm_incidents.types.chat_channel
    import capo_ssm_incidents.types.client_token
    import capo_ssm_incidents.types.dedupe_string
    import capo_ssm_incidents.types.engagement_set
    import capo_ssm_incidents.types.impact
    import capo_ssm_incidents.types.incident_summary
    import capo_ssm_incidents.types.incident_title
    import capo_ssm_incidents.types.integrations
    import capo_ssm_incidents.types.notification_target_set
    import capo_ssm_incidents.types.response_plan_display_name
    import capo_ssm_incidents.types.tag_map_update


class UpdateResponsePlanInput(TypedDict, closed=True):
    client_token: NotRequired["capo_ssm_incidents.types.client_token.ClientToken"]
    """<p>A token ensuring that the operation is called only once with the specified details.</p>"""
    arn: "capo_ssm_incidents.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) of the response plan.</p>"""
    display_name: NotRequired[
        "capo_ssm_incidents.types.response_plan_display_name.ResponsePlanDisplayName"
    ]
    """<p>The long format name of the response plan. The display name can't contain spaces.</p>"""
    incident_template_title: NotRequired[
        "capo_ssm_incidents.types.incident_title.IncidentTitle"
    ]
    """<p>The short format name of the incident. The title can't contain spaces.</p>"""
    incident_template_impact: NotRequired["capo_ssm_incidents.types.impact.Impact"]
    """<p>Defines the impact to the customers. Providing an impact overwrites the impact provided by a response plan.</p> <p class="title"> <b>Supported impact codes</b> </p> <ul> <li> <p> <code>1</code> - Critical</p> </li> <li> <p> <code>2</code> - High</p> </li> <li> <p> <code>3</code> - Medium</p> </li> <li> <p> <code>4</code> - Low</p> </li> <li> <p> <code>5</code> - No Impact</p> </li> </ul>"""
    incident_template_summary: NotRequired[
        "capo_ssm_incidents.types.incident_summary.IncidentSummary"
    ]
    """<p>A brief summary of the incident. This typically contains what has happened, what's currently happening, and next steps.</p>"""
    incident_template_dedupe_string: NotRequired[
        "capo_ssm_incidents.types.dedupe_string.DedupeString"
    ]
    """<p>The string Incident Manager uses to prevent duplicate incidents from being created by the same incident in the same account.</p>"""
    incident_template_notification_targets: NotRequired[
        "capo_ssm_incidents.types.notification_target_set.NotificationTargetSet"
    ]
    """<p>The Amazon SNS targets that are notified when updates are made to an incident.</p>"""
    chat_channel: NotRequired["capo_ssm_incidents.types.chat_channel.ChatChannel"]
    """<p>The Chatbot chat channel used for collaboration during an incident.</p> <p>Use the empty structure to remove the chat channel from the response plan.</p>"""
    engagements: NotRequired["capo_ssm_incidents.types.engagement_set.EngagementSet"]
    """<p>The Amazon Resource Name (ARN) for the contacts and escalation plans that the response plan engages during an incident.</p>"""
    actions: NotRequired["capo_ssm_incidents.types.actions_list.ActionsList"]
    """<p>The actions that this response plan takes at the beginning of an incident.</p>"""
    incident_template_tags: NotRequired[
        "capo_ssm_incidents.types.tag_map_update.TagMapUpdate"
    ]
    """<p>Tags to assign to the template. When the <code>StartIncident</code> API action is called, Incident Manager assigns the tags specified in the template to the incident. To call this action, you must also have permission to call the <code>TagResource</code> API action for the incident record resource.</p>"""
    integrations: NotRequired["capo_ssm_incidents.types.integrations.Integrations"]
    """<p>Information about third-party services integrated into the response plan.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateResponsePlanInput) -> dict:
    out: dict = {}
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    out["arn"] = value["arn"]
    if "display_name" in value:
        out["displayName"] = value["display_name"]
    if "incident_template_title" in value:
        out["incidentTemplateTitle"] = value["incident_template_title"]
    if "incident_template_impact" in value:
        out["incidentTemplateImpact"] = value["incident_template_impact"]
    if "incident_template_summary" in value:
        out["incidentTemplateSummary"] = value["incident_template_summary"]
    if "incident_template_dedupe_string" in value:
        out["incidentTemplateDedupeString"] = value["incident_template_dedupe_string"]
    if "incident_template_notification_targets" in value:
        import capo_ssm_incidents.types.notification_target_set

        out["incidentTemplateNotificationTargets"] = (
            capo_ssm_incidents.types.notification_target_set.serialize_json(
                value["incident_template_notification_targets"]
            )
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
    if "incident_template_tags" in value:
        import capo_ssm_incidents.types.tag_map_update

        out["incidentTemplateTags"] = (
            capo_ssm_incidents.types.tag_map_update.serialize_json(
                value["incident_template_tags"]
            )
        )
    if "integrations" in value:
        import capo_ssm_incidents.types.integrations

        out["integrations"] = capo_ssm_incidents.types.integrations.serialize_json(
            value["integrations"]
        )
    return out


def deserialize_json(data: dict) -> UpdateResponsePlanInput:
    out: UpdateResponsePlanInput = {}  # type: ignore[typeddict-item]
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    else:
        raise DeserializationError("UpdateResponsePlanInput.arn required")
    if data.get("displayName") is not None:
        out["display_name"] = data["displayName"]
    if data.get("incidentTemplateTitle") is not None:
        out["incident_template_title"] = data["incidentTemplateTitle"]
    if data.get("incidentTemplateImpact") is not None:
        out["incident_template_impact"] = data["incidentTemplateImpact"]
    if data.get("incidentTemplateSummary") is not None:
        out["incident_template_summary"] = data["incidentTemplateSummary"]
    if data.get("incidentTemplateDedupeString") is not None:
        out["incident_template_dedupe_string"] = data["incidentTemplateDedupeString"]
    if data.get("incidentTemplateNotificationTargets") is not None:
        import capo_ssm_incidents.types.notification_target_set

        out["incident_template_notification_targets"] = (
            capo_ssm_incidents.types.notification_target_set.deserialize_json(
                data["incidentTemplateNotificationTargets"]
            )
        )
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
    if data.get("incidentTemplateTags") is not None:
        import capo_ssm_incidents.types.tag_map_update

        out["incident_template_tags"] = (
            capo_ssm_incidents.types.tag_map_update.deserialize_json(
                data["incidentTemplateTags"]
            )
        )
    if data.get("integrations") is not None:
        import capo_ssm_incidents.types.integrations

        out["integrations"] = capo_ssm_incidents.types.integrations.deserialize_json(
            data["integrations"]
        )
    return out
