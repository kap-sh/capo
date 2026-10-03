"""Generated from Smithy shape ``com.amazonaws.resiliencehub#AppAssessmentSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_resiliencehub.errors import DeserializationError

if TYPE_CHECKING:
    import capo_resiliencehub.types.arn
    import capo_resiliencehub.types.assessment_invoker
    import capo_resiliencehub.types.assessment_status
    import capo_resiliencehub.types.compliance_status
    import capo_resiliencehub.types.cost
    import capo_resiliencehub.types.double
    import capo_resiliencehub.types.drift_status
    import capo_resiliencehub.types.entity_name
    import capo_resiliencehub.types.entity_version
    import capo_resiliencehub.types.string500
    import capo_resiliencehub.types.time_stamp


class AppAssessmentSummary(TypedDict, closed=True):
    app_arn: NotRequired["capo_resiliencehub.types.arn.Arn"]
    """<p>Amazon Resource Name (ARN) of the Resilience Hub application. The format for this ARN is: arn:<code>partition</code>:resiliencehub:<code>region</code>:<code>account</code>:app/<code>app-id</code>. For more information about ARNs, see <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html"> Amazon Resource Names (ARNs)</a> in the <i>Amazon Web Services General Reference</i> guide.</p>"""
    app_version: NotRequired["capo_resiliencehub.types.entity_version.EntityVersion"]
    """<p>Version of an application.</p>"""
    assessment_status: "capo_resiliencehub.types.assessment_status.AssessmentStatus"
    """<p>Current status of the assessment for the resiliency policy.</p>"""
    invoker: NotRequired[
        "capo_resiliencehub.types.assessment_invoker.AssessmentInvoker"
    ]
    """<p>Entity that invoked the assessment.</p>"""
    start_time: NotRequired["capo_resiliencehub.types.time_stamp.TimeStamp"]
    """<p>Starting time for the action.</p>"""
    end_time: NotRequired["capo_resiliencehub.types.time_stamp.TimeStamp"]
    """<p>End time for the action.</p>"""
    message: NotRequired["capo_resiliencehub.types.string500.String500"]
    """<p>Message from the assessment run.</p>"""
    assessment_name: NotRequired["capo_resiliencehub.types.entity_name.EntityName"]
    """<p>Name of the assessment.</p>"""
    assessment_arn: "capo_resiliencehub.types.arn.Arn"
    """<p>Amazon Resource Name (ARN) of the assessment. The format for this ARN is: arn:<code>partition</code>:resiliencehub:<code>region</code>:<code>account</code>:app-assessment/<code>app-id</code>. For more information about ARNs, see <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html"> Amazon Resource Names (ARNs)</a> in the <i>Amazon Web Services General Reference</i> guide.</p>"""
    compliance_status: NotRequired[
        "capo_resiliencehub.types.compliance_status.ComplianceStatus"
    ]
    """<p>Current status of compliance for the resiliency policy.</p>"""
    cost: NotRequired["capo_resiliencehub.types.cost.Cost"]
    """<p>Cost for an application.</p>"""
    resiliency_score: "capo_resiliencehub.types.double.Double"
    """<p>Current resiliency score for the application.</p>"""
    version_name: NotRequired["capo_resiliencehub.types.entity_version.EntityVersion"]
    """<p>Name of an application version.</p>"""
    drift_status: NotRequired["capo_resiliencehub.types.drift_status.DriftStatus"]
    """<p>Indicates if compliance drifts (deviations) were detected while running an assessment for your application.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AppAssessmentSummary) -> dict:
    out: dict = {}
    if "app_arn" in value:
        out["appArn"] = value["app_arn"]
    if "app_version" in value:
        out["appVersion"] = value["app_version"]
    import capo_resiliencehub.types.assessment_status

    out["assessmentStatus"] = capo_resiliencehub.types.assessment_status.serialize_json(
        value["assessment_status"]
    )
    if "invoker" in value:
        import capo_resiliencehub.types.assessment_invoker

        out["invoker"] = capo_resiliencehub.types.assessment_invoker.serialize_json(
            value["invoker"]
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
    if "compliance_status" in value:
        import capo_resiliencehub.types.compliance_status

        out["complianceStatus"] = (
            capo_resiliencehub.types.compliance_status.serialize_json(
                value["compliance_status"]
            )
        )
    if "cost" in value:
        import capo_resiliencehub.types.cost

        out["cost"] = capo_resiliencehub.types.cost.serialize_json(value["cost"])
    out["resiliencyScore"] = (
        "NaN"
        if value.get("resiliency_score", 0) != value.get("resiliency_score", 0)
        else "Infinity"
        if value.get("resiliency_score", 0) == float("inf")
        else "-Infinity"
        if value.get("resiliency_score", 0) == float("-inf")
        else value.get("resiliency_score", 0)
    )
    if "version_name" in value:
        out["versionName"] = value["version_name"]
    if "drift_status" in value:
        import capo_resiliencehub.types.drift_status

        out["driftStatus"] = capo_resiliencehub.types.drift_status.serialize_json(
            value["drift_status"]
        )
    return out


def deserialize_json(data: dict) -> AppAssessmentSummary:
    out: AppAssessmentSummary = {}  # type: ignore[typeddict-item]
    if data.get("appArn") is not None:
        out["app_arn"] = data["appArn"]
    if data.get("appVersion") is not None:
        out["app_version"] = data["appVersion"]
    if data.get("assessmentStatus") is not None:
        import capo_resiliencehub.types.assessment_status

        out["assessment_status"] = (
            capo_resiliencehub.types.assessment_status.deserialize_json(
                data["assessmentStatus"]
            )
        )
    else:
        raise DeserializationError("AppAssessmentSummary.assessment_status required")
    if data.get("invoker") is not None:
        import capo_resiliencehub.types.assessment_invoker

        out["invoker"] = capo_resiliencehub.types.assessment_invoker.deserialize_json(
            data["invoker"]
        )
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
        raise DeserializationError("AppAssessmentSummary.assessment_arn required")
    if data.get("complianceStatus") is not None:
        import capo_resiliencehub.types.compliance_status

        out["compliance_status"] = (
            capo_resiliencehub.types.compliance_status.deserialize_json(
                data["complianceStatus"]
            )
        )
    if data.get("cost") is not None:
        import capo_resiliencehub.types.cost

        out["cost"] = capo_resiliencehub.types.cost.deserialize_json(data["cost"])
    if data.get("resiliencyScore") is not None:
        out["resiliency_score"] = float(data["resiliencyScore"])
    else:
        out["resiliency_score"] = 0
    if data.get("versionName") is not None:
        out["version_name"] = data["versionName"]
    if data.get("driftStatus") is not None:
        import capo_resiliencehub.types.drift_status

        out["drift_status"] = capo_resiliencehub.types.drift_status.deserialize_json(
            data["driftStatus"]
        )
    return out
