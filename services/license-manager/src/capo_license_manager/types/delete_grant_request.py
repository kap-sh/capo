"""Generated from Smithy shape ``com.amazonaws.licensemanager#DeleteGrantRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_license_manager.types.arn
    import capo_license_manager.types.status_reason_message
    import capo_license_manager.types.string


class DeleteGrantRequest(TypedDict, closed=True):
    grant_arn: "capo_license_manager.types.arn.Arn"
    """<p>Amazon Resource Name (ARN) of the grant.</p>"""
    status_reason: NotRequired[
        "capo_license_manager.types.status_reason_message.StatusReasonMessage"
    ]
    """<p>The Status reason for the delete request.</p>"""
    version: "capo_license_manager.types.string.String"
    """<p>Current version of the grant.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteGrantRequest) -> dict:
    out: dict = {}
    out["GrantArn"] = value["grant_arn"]
    if "status_reason" in value:
        out["StatusReason"] = value["status_reason"]
    out["Version"] = value["version"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteGrantRequest:
    out: DeleteGrantRequest = {}  # type: ignore[typeddict-item]
    if data.get("GrantArn") is not None:
        out["grant_arn"] = data["GrantArn"]
    else:
        out["grant_arn"] = ""
    if data.get("StatusReason") is not None:
        out["status_reason"] = data["StatusReason"]
    if data.get("Version") is not None:
        out["version"] = data["Version"]
    else:
        out["version"] = ""
    return out
