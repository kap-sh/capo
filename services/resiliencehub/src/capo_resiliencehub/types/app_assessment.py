"""Generated from Smithy shape ``com.amazonaws.resiliencehub#AppAssessment``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_resiliencehub.errors import DeserializationError

if TYPE_CHECKING:
    import capo_resiliencehub.types.arn
    import capo_resiliencehub.types.assessment_compliance
    import capo_resiliencehub.types.assessment_invoker
    import capo_resiliencehub.types.assessment_status
    import capo_resiliencehub.types.assessment_summary
    import capo_resiliencehub.types.compliance_status
    import capo_resiliencehub.types.cost
    import capo_resiliencehub.types.drift_status
    import capo_resiliencehub.types.entity_name
    import capo_resiliencehub.types.entity_version
    import capo_resiliencehub.types.resiliency_policy
    import capo_resiliencehub.types.resiliency_score
    import capo_resiliencehub.types.resource_errors_details
    import capo_resiliencehub.types.string500
    import capo_resiliencehub.types.tag_map
    import capo_resiliencehub.types.time_stamp


class AppAssessment(TypedDict, closed=True):
    app_arn: NotRequired["capo_resiliencehub.types.arn.Arn"]
    """<p>Amazon Resource Name (ARN) of the Resilience Hub application. The format for this ARN is: arn:<code>partition</code>:resiliencehub:<code>region</code>:<code>account</code>:app/<code>app-id</code>. For more information about ARNs, see <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html"> Amazon Resource Names (ARNs)</a> in the <i>Amazon Web Services General Reference</i> guide.</p>"""
    app_version: NotRequired["capo_resiliencehub.types.entity_version.EntityVersion"]
    """<p>Version of an application.</p>"""
    invoker: "capo_resiliencehub.types.assessment_invoker.AssessmentInvoker"
    """<p>The entity that invoked the assessment.</p>"""
    cost: NotRequired["capo_resiliencehub.types.cost.Cost"]
    """<p>Cost for the application.</p>"""
    resiliency_score: NotRequired[
        "capo_resiliencehub.types.resiliency_score.ResiliencyScore"
    ]
    """<p>Current resiliency score for an application.</p>"""
    compliance: NotRequired[
        "capo_resiliencehub.types.assessment_compliance.AssessmentCompliance"
    ]
    """<p>Application compliance against the resiliency policy.</p>"""
    compliance_status: NotRequired[
        "capo_resiliencehub.types.compliance_status.ComplianceStatus"
    ]
    """<p>Current status of the compliance for the resiliency policy.</p>"""
    assessment_status: "capo_resiliencehub.types.assessment_status.AssessmentStatus"
    """<p>Current status of the assessment for the resiliency policy.</p>"""
    start_time: NotRequired["capo_resiliencehub.types.time_stamp.TimeStamp"]
    """<p>Starting time for the action.</p>"""
    end_time: NotRequired["capo_resiliencehub.types.time_stamp.TimeStamp"]
    """<p>End time for the action.</p>"""
    message: NotRequired["capo_resiliencehub.types.string500.String500"]
    """<p>Error or warning message from the assessment execution</p>"""
    assessment_name: NotRequired["capo_resiliencehub.types.entity_name.EntityName"]
    """<p>Name of the assessment.</p>"""
    assessment_arn: "capo_resiliencehub.types.arn.Arn"
    """<p>Amazon Resource Name (ARN) of the assessment. The format for this ARN is: arn:<code>partition</code>:resiliencehub:<code>region</code>:<code>account</code>:app-assessment/<code>app-id</code>. For more information about ARNs, see <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html"> Amazon Resource Names (ARNs)</a> in the <i>Amazon Web Services General Reference</i> guide.</p>"""
    policy: NotRequired["capo_resiliencehub.types.resiliency_policy.ResiliencyPolicy"]
    """<p>Resiliency policy of an application.</p>"""
    tags: NotRequired["capo_resiliencehub.types.tag_map.TagMap"]
    """<p>Tags assigned to the resource. A tag is a label that you assign to an Amazon Web Services resource. Each tag consists of a key/value pair.</p>"""
    resource_errors_details: NotRequired[
        "capo_resiliencehub.types.resource_errors_details.ResourceErrorsDetails"
    ]
    """<p> A resource error object containing a list of errors retrieving an application's resources. </p>"""
    version_name: NotRequired["capo_resiliencehub.types.entity_version.EntityVersion"]
    """<p>Version name of the published application.</p>"""
    drift_status: NotRequired["capo_resiliencehub.types.drift_status.DriftStatus"]
    """<p>Indicates if compliance drifts (deviations) were detected while running an assessment for your application.</p>"""
    summary: NotRequired[
        "capo_resiliencehub.types.assessment_summary.AssessmentSummary"
    ]
    """<p>Indicates the AI-generated summary for the Resilience Hub assessment, providing a concise overview that highlights the top risks and recommendations.</p> <note> <p>This property is available only in the US East (N. Virginia) Region.</p> </note>"""


# --- restJson1 ser/de ---
def serialize_json(value: AppAssessment) -> dict:
    out: dict = {}
    if "app_arn" in value:
        out["appArn"] = value["app_arn"]
    if "app_version" in value:
        out["appVersion"] = value["app_version"]
    import capo_resiliencehub.types.assessment_invoker

    out["invoker"] = capo_resiliencehub.types.assessment_invoker.serialize_json(
        value["invoker"]
    )
    if "cost" in value:
        import capo_resiliencehub.types.cost

        out["cost"] = capo_resiliencehub.types.cost.serialize_json(value["cost"])
    if "resiliency_score" in value:
        import capo_resiliencehub.types.resiliency_score

        out["resiliencyScore"] = (
            capo_resiliencehub.types.resiliency_score.serialize_json(
                value["resiliency_score"]
            )
        )
    if "compliance" in value:
        import capo_resiliencehub.types.assessment_compliance

        out["compliance"] = (
            capo_resiliencehub.types.assessment_compliance.serialize_json(
                value["compliance"]
            )
        )
    if "compliance_status" in value:
        import capo_resiliencehub.types.compliance_status

        out["complianceStatus"] = (
            capo_resiliencehub.types.compliance_status.serialize_json(
                value["compliance_status"]
            )
        )
    import capo_resiliencehub.types.assessment_status

    out["assessmentStatus"] = capo_resiliencehub.types.assessment_status.serialize_json(
        value["assessment_status"]
    )
    if "start_time" in value:
        import capo_resiliencehub.types.time_stamp

        out["startTime"] = capo_resiliencehub.types.time_stamp.serialize_json(
            value["start_time"]
        )
    if "end_time" in value:
        import capo_resiliencehub.types.time_stamp

        out["endTime"] = capo_resiliencehub.types.time_stamp.serialize_json(
            value["end_time"]
        )
    if "message" in value:
        out["message"] = value["message"]
    if "assessment_name" in value:
        out["assessmentName"] = value["assessment_name"]
    out["assessmentArn"] = value["assessment_arn"]
    if "policy" in value:
        import capo_resiliencehub.types.resiliency_policy

        out["policy"] = capo_resiliencehub.types.resiliency_policy.serialize_json(
            value["policy"]
        )
    if "tags" in value:
        import capo_resiliencehub.types.tag_map

        out["tags"] = capo_resiliencehub.types.tag_map.serialize_json(value["tags"])
    if "resource_errors_details" in value:
        import capo_resiliencehub.types.resource_errors_details

        out["resourceErrorsDetails"] = (
            capo_resiliencehub.types.resource_errors_details.serialize_json(
                value["resource_errors_details"]
            )
        )
    if "version_name" in value:
        out["versionName"] = value["version_name"]
    if "drift_status" in value:
        import capo_resiliencehub.types.drift_status

        out["driftStatus"] = capo_resiliencehub.types.drift_status.serialize_json(
            value["drift_status"]
        )
    if "summary" in value:
        import capo_resiliencehub.types.assessment_summary

        out["summary"] = capo_resiliencehub.types.assessment_summary.serialize_json(
            value["summary"]
        )
    return out


def deserialize_json(data: dict) -> AppAssessment:
    out: AppAssessment = {}  # type: ignore[typeddict-item]
    if data.get("appArn") is not None:
        out["app_arn"] = data["appArn"]
    if data.get("appVersion") is not None:
        out["app_version"] = data["appVersion"]
    if data.get("invoker") is not None:
        import capo_resiliencehub.types.assessment_invoker

        out["invoker"] = capo_resiliencehub.types.assessment_invoker.deserialize_json(
            data["invoker"]
        )
    else:
        raise DeserializationError("AppAssessment.invoker required")
    if data.get("cost") is not None:
        import capo_resiliencehub.types.cost

        out["cost"] = capo_resiliencehub.types.cost.deserialize_json(data["cost"])
    if data.get("resiliencyScore") is not None:
        import capo_resiliencehub.types.resiliency_score

        out["resiliency_score"] = (
            capo_resiliencehub.types.resiliency_score.deserialize_json(
                data["resiliencyScore"]
            )
        )
    if data.get("compliance") is not None:
        import capo_resiliencehub.types.assessment_compliance

        out["compliance"] = (
            capo_resiliencehub.types.assessment_compliance.deserialize_json(
                data["compliance"]
            )
        )
    if data.get("complianceStatus") is not None:
        import capo_resiliencehub.types.compliance_status

        out["compliance_status"] = (
            capo_resiliencehub.types.compliance_status.deserialize_json(
                data["complianceStatus"]
            )
        )
    if data.get("assessmentStatus") is not None:
        import capo_resiliencehub.types.assessment_status

        out["assessment_status"] = (
            capo_resiliencehub.types.assessment_status.deserialize_json(
                data["assessmentStatus"]
            )
        )
    else:
        raise DeserializationError("AppAssessment.assessment_status required")
    if data.get("startTime") is not None:
        import capo_resiliencehub.types.time_stamp

        out["start_time"] = capo_resiliencehub.types.time_stamp.deserialize_json(
            data["startTime"]
        )
    if data.get("endTime") is not None:
        import capo_resiliencehub.types.time_stamp

        out["end_time"] = capo_resiliencehub.types.time_stamp.deserialize_json(
            data["endTime"]
        )
    if data.get("message") is not None:
        out["message"] = data["message"]
    if data.get("assessmentName") is not None:
        out["assessment_name"] = data["assessmentName"]
    if data.get("assessmentArn") is not None:
        out["assessment_arn"] = data["assessmentArn"]
    else:
        raise DeserializationError("AppAssessment.assessment_arn required")
    if data.get("policy") is not None:
        import capo_resiliencehub.types.resiliency_policy

        out["policy"] = capo_resiliencehub.types.resiliency_policy.deserialize_json(
            data["policy"]
        )
    if data.get("tags") is not None:
        import capo_resiliencehub.types.tag_map

        out["tags"] = capo_resiliencehub.types.tag_map.deserialize_json(data["tags"])
    if data.get("resourceErrorsDetails") is not None:
        import capo_resiliencehub.types.resource_errors_details

        out["resource_errors_details"] = (
            capo_resiliencehub.types.resource_errors_details.deserialize_json(
                data["resourceErrorsDetails"]
            )
        )
    if data.get("versionName") is not None:
        out["version_name"] = data["versionName"]
    if data.get("driftStatus") is not None:
        import capo_resiliencehub.types.drift_status

        out["drift_status"] = capo_resiliencehub.types.drift_status.deserialize_json(
            data["driftStatus"]
        )
    if data.get("summary") is not None:
        import capo_resiliencehub.types.assessment_summary

        out["summary"] = capo_resiliencehub.types.assessment_summary.deserialize_json(
            data["summary"]
        )
    return out
