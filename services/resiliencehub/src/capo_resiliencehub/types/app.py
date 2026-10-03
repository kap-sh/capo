"""Generated from Smithy shape ``com.amazonaws.resiliencehub#App``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_resiliencehub.errors import DeserializationError

if TYPE_CHECKING:
    import capo_resiliencehub.types.app_assessment_schedule_type
    import capo_resiliencehub.types.app_compliance_status_type
    import capo_resiliencehub.types.app_drift_status_type
    import capo_resiliencehub.types.app_status_type
    import capo_resiliencehub.types.arn
    import capo_resiliencehub.types.double
    import capo_resiliencehub.types.entity_description
    import capo_resiliencehub.types.entity_name
    import capo_resiliencehub.types.event_subscription_list
    import capo_resiliencehub.types.integer_optional
    import capo_resiliencehub.types.permission_model
    import capo_resiliencehub.types.tag_map
    import capo_resiliencehub.types.time_stamp


class App(TypedDict, closed=True):
    app_arn: "capo_resiliencehub.types.arn.Arn"
    """<p>Amazon Resource Name (ARN) of the Resilience Hub application. The format for this ARN is: arn:<code>partition</code>:resiliencehub:<code>region</code>:<code>account</code>:app/<code>app-id</code>. For more information about ARNs, see <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html"> Amazon Resource Names (ARNs)</a> in the <i>Amazon Web Services General Reference</i> guide.</p>"""
    name: "capo_resiliencehub.types.entity_name.EntityName"
    """<p>Name for the application.</p>"""
    description: NotRequired[
        "capo_resiliencehub.types.entity_description.EntityDescription"
    ]
    """<p>Optional description for an application.</p>"""
    policy_arn: NotRequired["capo_resiliencehub.types.arn.Arn"]
    """<p>Amazon Resource Name (ARN) of the resiliency policy. The format for this ARN is: arn:<code>partition</code>:resiliencehub:<code>region</code>:<code>account</code>:resiliency-policy/<code>policy-id</code>. For more information about ARNs, see <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html"> Amazon Resource Names (ARNs)</a> in the <i>Amazon Web Services General Reference</i> guide.</p>"""
    creation_time: "capo_resiliencehub.types.time_stamp.TimeStamp"
    """<p>Date and time when the application was created.</p>"""
    status: NotRequired["capo_resiliencehub.types.app_status_type.AppStatusType"]
    """<p>Status of the application.</p>"""
    compliance_status: NotRequired[
        "capo_resiliencehub.types.app_compliance_status_type.AppComplianceStatusType"
    ]
    """<p>Current status of compliance for the resiliency policy.</p>"""
    last_app_compliance_evaluation_time: NotRequired[
        "capo_resiliencehub.types.time_stamp.TimeStamp"
    ]
    """<p>Date and time the most recent compliance evaluation.</p>"""
    resiliency_score: "capo_resiliencehub.types.double.Double"
    """<p>Current resiliency score for the application.</p>"""
    last_resiliency_score_evaluation_time: NotRequired[
        "capo_resiliencehub.types.time_stamp.TimeStamp"
    ]
    """<p>Date and time the most recent resiliency score evaluation.</p>"""
    tags: NotRequired["capo_resiliencehub.types.tag_map.TagMap"]
    """<p>Tags assigned to the resource. A tag is a label that you assign to an Amazon Web Services resource. Each tag consists of a key/value pair.</p>"""
    assessment_schedule: NotRequired[
        "capo_resiliencehub.types.app_assessment_schedule_type.AppAssessmentScheduleType"
    ]
    """<p>Assessment execution schedule with 'Daily' or 'Disabled' values. </p>"""
    permission_model: NotRequired[
        "capo_resiliencehub.types.permission_model.PermissionModel"
    ]
    """<p>Defines the roles and credentials that Resilience Hub would use while creating the application, importing its resources, and running an assessment.</p>"""
    event_subscriptions: NotRequired[
        "capo_resiliencehub.types.event_subscription_list.EventSubscriptionList"
    ]
    """<p>The list of events you would like to subscribe and get notification for. Currently, Resilience Hub supports notifications only for <b>Drift detected</b> and <b>Scheduled assessment failure</b> events.</p>"""
    drift_status: NotRequired[
        "capo_resiliencehub.types.app_drift_status_type.AppDriftStatusType"
    ]
    """<p>Indicates if compliance drifts (deviations) were detected while running an assessment for your application.</p>"""
    last_drift_evaluation_time: NotRequired[
        "capo_resiliencehub.types.time_stamp.TimeStamp"
    ]
    """<p>Indicates the last time that a drift was evaluated.</p>"""
    rto_in_secs: NotRequired[
        "capo_resiliencehub.types.integer_optional.IntegerOptional"
    ]
    """<p>Recovery Time Objective (RTO) in seconds.</p>"""
    rpo_in_secs: NotRequired[
        "capo_resiliencehub.types.integer_optional.IntegerOptional"
    ]
    """<p>Recovery Point Objective (RPO) in seconds.</p>"""
    aws_application_arn: NotRequired["capo_resiliencehub.types.arn.Arn"]
    """<p>Amazon Resource Name (ARN) of Resource Groups group that is integrated with an AppRegistry application. For more information about ARNs, see <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html"> Amazon Resource Names (ARNs)</a> in the <i>Amazon Web Services General Reference</i> guide.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: App) -> dict:
    out: dict = {}
    out["appArn"] = value["app_arn"]
    out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    if "policy_arn" in value:
        out["policyArn"] = value["policy_arn"]
    import capo_resiliencehub.types.time_stamp

    out["creationTime"] = capo_resiliencehub.types.time_stamp.serialize_json(
        value["creation_time"]
    )
    if "status" in value:
        import capo_resiliencehub.types.app_status_type

        out["status"] = capo_resiliencehub.types.app_status_type.serialize_json(
            value["status"]
        )
    if "compliance_status" in value:
        import capo_resiliencehub.types.app_compliance_status_type

        out["complianceStatus"] = (
            capo_resiliencehub.types.app_compliance_status_type.serialize_json(
                value["compliance_status"]
            )
        )
    if "last_app_compliance_evaluation_time" in value:
        import capo_resiliencehub.types.time_stamp

        out["lastAppComplianceEvaluationTime"] = (
            capo_resiliencehub.types.time_stamp.serialize_json(
                value["last_app_compliance_evaluation_time"]
            )
        )
    out["resiliencyScore"] = (
        "NaN"
        if value.get("resiliency_score", 0) != value.get("resiliency_score", 0)
        else "Infinity"
        if value.get("resiliency_score", 0) == float("inf")
        else "-Infinity"
        if value.get("resiliency_score", 0) == float("-inf")
        else value.get("resiliency_score", 0)
    )
    if "last_resiliency_score_evaluation_time" in value:
        import capo_resiliencehub.types.time_stamp

        out["lastResiliencyScoreEvaluationTime"] = (
            capo_resiliencehub.types.time_stamp.serialize_json(
                value["last_resiliency_score_evaluation_time"]
            )
        )
    if "tags" in value:
        import capo_resiliencehub.types.tag_map

        out["tags"] = capo_resiliencehub.types.tag_map.serialize_json(value["tags"])
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
    if "drift_status" in value:
        import capo_resiliencehub.types.app_drift_status_type

        out["driftStatus"] = (
            capo_resiliencehub.types.app_drift_status_type.serialize_json(
                value["drift_status"]
            )
        )
    if "last_drift_evaluation_time" in value:
        import capo_resiliencehub.types.time_stamp

        out["lastDriftEvaluationTime"] = (
            capo_resiliencehub.types.time_stamp.serialize_json(
                value["last_drift_evaluation_time"]
            )
        )
    if "rto_in_secs" in value:
        out["rtoInSecs"] = value["rto_in_secs"]
    if "rpo_in_secs" in value:
        out["rpoInSecs"] = value["rpo_in_secs"]
    if "aws_application_arn" in value:
        out["awsApplicationArn"] = value["aws_application_arn"]
    return out


def deserialize_json(data: dict) -> App:
    out: App = {}  # type: ignore[typeddict-item]
    if data.get("appArn") is not None:
        out["app_arn"] = data["appArn"]
    else:
        raise DeserializationError("App.app_arn required")
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        raise DeserializationError("App.name required")
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("policyArn") is not None:
        out["policy_arn"] = data["policyArn"]
    if data.get("creationTime") is not None:
        import capo_resiliencehub.types.time_stamp

        out["creation_time"] = capo_resiliencehub.types.time_stamp.deserialize_json(
            data["creationTime"]
        )
    else:
        raise DeserializationError("App.creation_time required")
    if data.get("status") is not None:
        import capo_resiliencehub.types.app_status_type

        out["status"] = capo_resiliencehub.types.app_status_type.deserialize_json(
            data["status"]
        )
    if data.get("complianceStatus") is not None:
        import capo_resiliencehub.types.app_compliance_status_type

        out["compliance_status"] = (
            capo_resiliencehub.types.app_compliance_status_type.deserialize_json(
                data["complianceStatus"]
            )
        )
    if data.get("lastAppComplianceEvaluationTime") is not None:
        import capo_resiliencehub.types.time_stamp

        out["last_app_compliance_evaluation_time"] = (
            capo_resiliencehub.types.time_stamp.deserialize_json(
                data["lastAppComplianceEvaluationTime"]
            )
        )
    if data.get("resiliencyScore") is not None:
        out["resiliency_score"] = float(data["resiliencyScore"])
    else:
        out["resiliency_score"] = 0
    if data.get("lastResiliencyScoreEvaluationTime") is not None:
        import capo_resiliencehub.types.time_stamp

        out["last_resiliency_score_evaluation_time"] = (
            capo_resiliencehub.types.time_stamp.deserialize_json(
                data["lastResiliencyScoreEvaluationTime"]
            )
        )
    if data.get("tags") is not None:
        import capo_resiliencehub.types.tag_map

        out["tags"] = capo_resiliencehub.types.tag_map.deserialize_json(data["tags"])
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
    if data.get("driftStatus") is not None:
        import capo_resiliencehub.types.app_drift_status_type

        out["drift_status"] = (
            capo_resiliencehub.types.app_drift_status_type.deserialize_json(
                data["driftStatus"]
            )
        )
    if data.get("lastDriftEvaluationTime") is not None:
        import capo_resiliencehub.types.time_stamp

        out["last_drift_evaluation_time"] = (
            capo_resiliencehub.types.time_stamp.deserialize_json(
                data["lastDriftEvaluationTime"]
            )
        )
    if data.get("rtoInSecs") is not None:
        out["rto_in_secs"] = data["rtoInSecs"]
    if data.get("rpoInSecs") is not None:
        out["rpo_in_secs"] = data["rpoInSecs"]
    if data.get("awsApplicationArn") is not None:
        out["aws_application_arn"] = data["awsApplicationArn"]
    return out
