"""Generated from Smithy shape ``com.amazonaws.ssmincidents#StartIncidentInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ssm_incidents.errors import DeserializationError

if TYPE_CHECKING:
    import capo_ssm_incidents.types.arn
    import capo_ssm_incidents.types.client_token
    import capo_ssm_incidents.types.impact
    import capo_ssm_incidents.types.incident_title
    import capo_ssm_incidents.types.related_item_list
    import capo_ssm_incidents.types.trigger_details


class StartIncidentInput(TypedDict, closed=True):
    client_token: NotRequired["capo_ssm_incidents.types.client_token.ClientToken"]
    """<p>A token ensuring that the operation is called only once with the specified details.</p>"""
    response_plan_arn: "capo_ssm_incidents.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) of the response plan that pre-defines summary, chat channels, Amazon SNS topics, runbooks, title, and impact of the incident. </p>"""
    title: NotRequired["capo_ssm_incidents.types.incident_title.IncidentTitle"]
    """<p>Provide a title for the incident. Providing a title overwrites the title provided by the response plan. </p>"""
    impact: NotRequired["capo_ssm_incidents.types.impact.Impact"]
    """<p>Defines the impact to the customers. Providing an impact overwrites the impact provided by a response plan.</p> <p class="title"> <b>Supported impact codes</b> </p> <ul> <li> <p> <code>1</code> - Critical</p> </li> <li> <p> <code>2</code> - High</p> </li> <li> <p> <code>3</code> - Medium</p> </li> <li> <p> <code>4</code> - Low</p> </li> <li> <p> <code>5</code> - No Impact</p> </li> </ul>"""
    trigger_details: NotRequired[
        "capo_ssm_incidents.types.trigger_details.TriggerDetails"
    ]
    """<p>Details of what created the incident record in Incident Manager.</p>"""
    related_items: NotRequired[
        "capo_ssm_incidents.types.related_item_list.RelatedItemList"
    ]
    """<p>Add related items to the incident for other responders to use. Related items are Amazon Web Services resources, external links, or files uploaded to an Amazon S3 bucket. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartIncidentInput) -> dict:
    out: dict = {}
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    out["responsePlanArn"] = value["response_plan_arn"]
    if "title" in value:
        out["title"] = value["title"]
    if "impact" in value:
        out["impact"] = value["impact"]
    if "trigger_details" in value:
        import capo_ssm_incidents.types.trigger_details

        out["triggerDetails"] = capo_ssm_incidents.types.trigger_details.serialize_json(
            value["trigger_details"]
        )
    if "related_items" in value:
        import capo_ssm_incidents.types.related_item_list

        out["relatedItems"] = capo_ssm_incidents.types.related_item_list.serialize_json(
            value["related_items"]
        )
    return out


def deserialize_json(data: dict) -> StartIncidentInput:
    out: StartIncidentInput = {}  # type: ignore[typeddict-item]
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    if data.get("responsePlanArn") is not None:
        out["response_plan_arn"] = data["responsePlanArn"]
    else:
        raise DeserializationError("StartIncidentInput.response_plan_arn required")
    if data.get("title") is not None:
        out["title"] = data["title"]
    if data.get("impact") is not None:
        out["impact"] = data["impact"]
    if data.get("triggerDetails") is not None:
        import capo_ssm_incidents.types.trigger_details

        out["trigger_details"] = (
            capo_ssm_incidents.types.trigger_details.deserialize_json(
                data["triggerDetails"]
            )
        )
    if data.get("relatedItems") is not None:
        import capo_ssm_incidents.types.related_item_list

        out["related_items"] = (
            capo_ssm_incidents.types.related_item_list.deserialize_json(
                data["relatedItems"]
            )
        )
    return out
