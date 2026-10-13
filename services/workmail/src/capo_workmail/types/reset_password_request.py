"""Generated from Smithy shape ``com.amazonaws.workmail#ResetPasswordRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

from capo_workmail.errors import DeserializationError

if TYPE_CHECKING:
    import capo_workmail.types.organization_id
    import capo_workmail.types.password
    import capo_workmail.types.work_mail_identifier


class ResetPasswordRequest(TypedDict, closed=True):
    organization_id: "capo_workmail.types.organization_id.OrganizationId"
    """<p>The identifier of the organization that contains the user for which the password is reset.</p>"""
    user_id: "capo_workmail.types.work_mail_identifier.WorkMailIdentifier"
    """<p>The identifier of the user for whom the password is reset.</p>"""
    password: "capo_workmail.types.password.Password"
    """<p>The new password for the user.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ResetPasswordRequest) -> dict:
    out: dict = {}
    out["OrganizationId"] = value["organization_id"]
    out["UserId"] = value["user_id"]
    out["Password"] = value["password"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ResetPasswordRequest:
    out: ResetPasswordRequest = {}  # type: ignore[typeddict-item]
    if data.get("OrganizationId") is not None:
        out["organization_id"] = data["OrganizationId"]
    else:
        raise DeserializationError("ResetPasswordRequest.organization_id required")
    if data.get("UserId") is not None:
        out["user_id"] = data["UserId"]
    else:
        raise DeserializationError("ResetPasswordRequest.user_id required")
    if data.get("Password") is not None:
        out["password"] = data["Password"]
    else:
        raise DeserializationError("ResetPasswordRequest.password required")
    return out


def redact_sensitive(value: ResetPasswordRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "password" in value:
        out["password"] = "*** Sensitive Data Redacted ***"
    return out
