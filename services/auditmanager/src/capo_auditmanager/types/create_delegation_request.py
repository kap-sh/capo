"""Generated from Smithy shape ``com.amazonaws.auditmanager#CreateDelegationRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_auditmanager.types.control_set_id
    import capo_auditmanager.types.delegation_comment
    import capo_auditmanager.types.iam_arn
    import capo_auditmanager.types.role_type


class CreateDelegationRequest(TypedDict, closed=True):
    comment: NotRequired["capo_auditmanager.types.delegation_comment.DelegationComment"]
    """<p> A comment that's related to the delegation request. </p>"""
    control_set_id: NotRequired["capo_auditmanager.types.control_set_id.ControlSetId"]
    """<p> The unique identifier for the control set. </p>"""
    role_arn: NotRequired["capo_auditmanager.types.iam_arn.IamArn"]
    """<p> The Amazon Resource Name (ARN) of the IAM role. </p>"""
    role_type: NotRequired["capo_auditmanager.types.role_type.RoleType"]
    """<p> The type of customer persona. </p> <note> <p>In <code>CreateAssessment</code>, <code>roleType</code> can only be <code>PROCESS_OWNER</code>. </p> <p>In <code>UpdateSettings</code>, <code>roleType</code> can only be <code>PROCESS_OWNER</code>.</p> <p>In <code>BatchCreateDelegationByAssessment</code>, <code>roleType</code> can only be <code>RESOURCE_OWNER</code>.</p> </note>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateDelegationRequest) -> dict:
    out: dict = {}
    if "comment" in value:
        out["comment"] = value["comment"]
    if "control_set_id" in value:
        out["controlSetId"] = value["control_set_id"]
    if "role_arn" in value:
        out["roleArn"] = value["role_arn"]
    if "role_type" in value:
        import capo_auditmanager.types.role_type

        out["roleType"] = capo_auditmanager.types.role_type.serialize_json(
            value["role_type"]
        )
    return out


def deserialize_json(data: dict) -> CreateDelegationRequest:
    out: CreateDelegationRequest = {}  # type: ignore[typeddict-item]
    if data.get("comment") is not None:
        out["comment"] = data["comment"]
    if data.get("controlSetId") is not None:
        out["control_set_id"] = data["controlSetId"]
    if data.get("roleArn") is not None:
        out["role_arn"] = data["roleArn"]
    if data.get("roleType") is not None:
        import capo_auditmanager.types.role_type

        out["role_type"] = capo_auditmanager.types.role_type.deserialize_json(
            data["roleType"]
        )
    return out


def redact_sensitive(value: CreateDelegationRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "comment" in value:
        out["comment"] = "*** Sensitive Data Redacted ***"
    return out
