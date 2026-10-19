"""Generated from Smithy shape ``com.amazonaws.securityagent#UpdateApplicationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityagent.types.application_id
    import capo_securityagent.types.default_kms_key_id
    import capo_securityagent.types.role_arn


class UpdateApplicationRequest(TypedDict, closed=True):
    application_id: "capo_securityagent.types.application_id.ApplicationId"
    """<p>The unique identifier of the application to update.</p>"""
    role_arn: NotRequired["capo_securityagent.types.role_arn.RoleArn"]
    """<p>The updated Amazon Resource Name (ARN) of the IAM role for the application.</p>"""
    default_kms_key_id: NotRequired[
        "capo_securityagent.types.default_kms_key_id.DefaultKmsKeyId"
    ]
    """<p>The updated identifier of the default AWS KMS key for the application.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateApplicationRequest) -> dict:
    out: dict = {}
    out["applicationId"] = value["application_id"]
    if "role_arn" in value:
        out["roleArn"] = value["role_arn"]
    if "default_kms_key_id" in value:
        out["defaultKmsKeyId"] = value["default_kms_key_id"]
    return out


def deserialize_json(data: dict) -> UpdateApplicationRequest:
    out: UpdateApplicationRequest = {}  # type: ignore[typeddict-item]
    if data.get("applicationId") is not None:
        out["application_id"] = data["applicationId"]
    else:
        out["application_id"] = ""
    if data.get("roleArn") is not None:
        out["role_arn"] = data["roleArn"]
    if data.get("defaultKmsKeyId") is not None:
        out["default_kms_key_id"] = data["defaultKmsKeyId"]
    return out
