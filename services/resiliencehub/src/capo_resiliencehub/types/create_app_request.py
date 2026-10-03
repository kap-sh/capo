"""Generated from Smithy shape ``com.amazonaws.resiliencehub#CreateAppRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_resiliencehub.errors import DeserializationError

if TYPE_CHECKING:
    import capo_resiliencehub.types.app_assessment_schedule_type
    import capo_resiliencehub.types.arn
    import capo_resiliencehub.types.client_token
    import capo_resiliencehub.types.entity_description
    import capo_resiliencehub.types.entity_name
    import capo_resiliencehub.types.event_subscription_list
    import capo_resiliencehub.types.permission_model
    import capo_resiliencehub.types.tag_map


class CreateAppRequest(TypedDict, closed=True):
    name: "capo_resiliencehub.types.entity_name.EntityName"
    """<p>Name of the application.</p>"""
    description: NotRequired[
        "capo_resiliencehub.types.entity_description.EntityDescription"
    ]
    """<p>The optional description for an app.</p>"""
    policy_arn: NotRequired["capo_resiliencehub.types.arn.Arn"]
    """<p>Amazon Resource Name (ARN) of the resiliency policy. The format for this ARN is: arn:<code>partition</code>:resiliencehub:<code>region</code>:<code>account</code>:resiliency-policy/<code>policy-id</code>. For more information about ARNs, see <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html"> Amazon Resource Names (ARNs)</a> in the <i>Amazon Web Services General Reference</i> guide.</p>"""
    tags: NotRequired["capo_resiliencehub.types.tag_map.TagMap"]
    """<p>Tags assigned to the resource. A tag is a label that you assign to an Amazon Web Services resource. Each tag consists of a key/value pair.</p>"""
    client_token: NotRequired["capo_resiliencehub.types.client_token.ClientToken"]
    """<p>Used for an idempotency token. A client token is a unique, case-sensitive string of up to 64 ASCII characters. You should not reuse the same client token for other API requests.</p>"""
    assessment_schedule: NotRequired[
        "capo_resiliencehub.types.app_assessment_schedule_type.AppAssessmentScheduleType"
    ]
    """<p> Assessment execution schedule with 'Daily' or 'Disabled' values. </p>"""
    permission_model: NotRequired[
        "capo_resiliencehub.types.permission_model.PermissionModel"
    ]
    """<p>Defines the roles and credentials that Resilience Hub would use while creating the application, importing its resources, and running an assessment.</p>"""
    event_subscriptions: NotRequired[
        "capo_resiliencehub.types.event_subscription_list.EventSubscriptionList"
    ]
    """<p>The list of events you would like to subscribe and get notification for. Currently, Resilience Hub supports only <b>Drift detected</b> and <b>Scheduled assessment failure</b> events notification.</p>"""
    aws_application_arn: NotRequired["capo_resiliencehub.types.arn.Arn"]
    """<p>Amazon Resource Name (ARN) of Resource Groups group that is integrated with an AppRegistry application. For more information about ARNs, see <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html"> Amazon Resource Names (ARNs)</a> in the <i>Amazon Web Services General Reference</i> guide.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateAppRequest) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    if "policy_arn" in value:
        out["policyArn"] = value["policy_arn"]
    if "tags" in value:
        import capo_resiliencehub.types.tag_map

        out["tags"] = capo_resiliencehub.types.tag_map.serialize_json(value["tags"])
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    if "assessment_schedule" in value:
        import capo_resiliencehub.types.app_assessment_schedule_type

        out["assessmentSchedule"] = (
            capo_resiliencehub.types.app_assessment_schedule_type.serialize_json(
                value["assessment_schedule"]
            )
        )
    if "permission_model" in value:
        import capo_resiliencehub.types.permission_model

        out["permissionModel"] = (
            capo_resiliencehub.types.permission_model.serialize_json(
                value["permission_model"]
            )
        )
    if "event_subscriptions" in value:
        import capo_resiliencehub.types.event_subscription_list

        out["eventSubscriptions"] = (
            capo_resiliencehub.types.event_subscription_list.serialize_json(
                value["event_subscriptions"]
            )
        )
    if "aws_application_arn" in value:
        out["awsApplicationArn"] = value["aws_application_arn"]
    return out


def deserialize_json(data: dict) -> CreateAppRequest:
    out: CreateAppRequest = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        raise DeserializationError("CreateAppRequest.name required")
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("policyArn") is not None:
        out["policy_arn"] = data["policyArn"]
    if data.get("tags") is not None:
        import capo_resiliencehub.types.tag_map

        out["tags"] = capo_resiliencehub.types.tag_map.deserialize_json(data["tags"])
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    if data.get("assessmentSchedule") is not None:
        import capo_resiliencehub.types.app_assessment_schedule_type

        out["assessment_schedule"] = (
            capo_resiliencehub.types.app_assessment_schedule_type.deserialize_json(
                data["assessmentSchedule"]
            )
        )
    if data.get("permissionModel") is not None:
        import capo_resiliencehub.types.permission_model

        out["permission_model"] = (
            capo_resiliencehub.types.permission_model.deserialize_json(
                data["permissionModel"]
            )
        )
    if data.get("eventSubscriptions") is not None:
        import capo_resiliencehub.types.event_subscription_list

        out["event_subscriptions"] = (
            capo_resiliencehub.types.event_subscription_list.deserialize_json(
                data["eventSubscriptions"]
            )
        )
    if data.get("awsApplicationArn") is not None:
        out["aws_application_arn"] = data["awsApplicationArn"]
    return out
