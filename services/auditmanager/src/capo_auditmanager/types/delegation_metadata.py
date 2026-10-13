"""Generated from Smithy shape ``com.amazonaws.auditmanager#DelegationMetadata``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_auditmanager.types.assessment_name
    import capo_auditmanager.types.delegation_status
    import capo_auditmanager.types.iam_arn
    import capo_auditmanager.types.non_empty_string
    import capo_auditmanager.types.timestamp
    import capo_auditmanager.types.uuid


class DelegationMetadata(TypedDict, closed=True):
    id: NotRequired["capo_auditmanager.types.uuid.UUID"]
    """<p> The unique identifier for the delegation. </p>"""
    assessment_name: NotRequired[
        "capo_auditmanager.types.assessment_name.AssessmentName"
    ]
    """<p> The name of the associated assessment. </p>"""
    assessment_id: NotRequired["capo_auditmanager.types.uuid.UUID"]
    """<p> The unique identifier for the assessment. </p>"""
    status: NotRequired["capo_auditmanager.types.delegation_status.DelegationStatus"]
    """<p> The current status of the delegation. </p>"""
    role_arn: NotRequired["capo_auditmanager.types.iam_arn.IamArn"]
    """<p> The Amazon Resource Name (ARN) of the IAM role. </p>"""
    creation_time: NotRequired["capo_auditmanager.types.timestamp.Timestamp"]
    """<p> Specifies when the delegation was created. </p>"""
    control_set_name: NotRequired[
        "capo_auditmanager.types.non_empty_string.NonEmptyString"
    ]
    """<p> Specifies the name of the control set that was delegated for review. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DelegationMetadata) -> dict:
    out: dict = {}
    if "id" in value:
        out["id"] = value["id"]
    if "assessment_name" in value:
        out["assessmentName"] = value["assessment_name"]
    if "assessment_id" in value:
        out["assessmentId"] = value["assessment_id"]
    if "status" in value:
        import capo_auditmanager.types.delegation_status

        out["status"] = capo_auditmanager.types.delegation_status.serialize_json(
            value["status"]
        )
    if "role_arn" in value:
        out["roleArn"] = value["role_arn"]
    if "creation_time" in value:
        import capo_auditmanager.types.timestamp

        out["creationTime"] = capo_auditmanager.types.timestamp.serialize_json(
            value["creation_time"]
        )
    if "control_set_name" in value:
        out["controlSetName"] = value["control_set_name"]
    return out


def deserialize_json(data: dict) -> DelegationMetadata:
    out: DelegationMetadata = {}  # type: ignore[typeddict-item]
    if data.get("id") is not None:
        out["id"] = data["id"]
    if data.get("assessmentName") is not None:
        out["assessment_name"] = data["assessmentName"]
    if data.get("assessmentId") is not None:
        out["assessment_id"] = data["assessmentId"]
    if data.get("status") is not None:
        import capo_auditmanager.types.delegation_status

        out["status"] = capo_auditmanager.types.delegation_status.deserialize_json(
            data["status"]
        )
    if data.get("roleArn") is not None:
        out["role_arn"] = data["roleArn"]
    if data.get("creationTime") is not None:
        import capo_auditmanager.types.timestamp

        out["creation_time"] = capo_auditmanager.types.timestamp.deserialize_json(
            data["creationTime"]
        )
    if data.get("controlSetName") is not None:
        out["control_set_name"] = data["controlSetName"]
    return out


def redact_sensitive(value: DelegationMetadata) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "assessment_name" in value:
        out["assessment_name"] = "*** Sensitive Data Redacted ***"
    return out
