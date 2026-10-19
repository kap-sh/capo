"""Generated from Smithy shape ``com.amazonaws.securityagent#ApplicationSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityagent.types.application_domain
    import capo_securityagent.types.application_id
    import capo_securityagent.types.default_kms_key_id


class ApplicationSummary(TypedDict, closed=True):
    application_id: "capo_securityagent.types.application_id.ApplicationId"
    """<p>The unique identifier of the application.</p>"""
    application_name: "str"
    """<p>The name of the application.</p>"""
    domain: "capo_securityagent.types.application_domain.ApplicationDomain"
    """<p>The domain associated with the application.</p>"""
    default_kms_key_id: NotRequired[
        "capo_securityagent.types.default_kms_key_id.DefaultKmsKeyId"
    ]
    """<p>The identifier of the default AWS KMS key used to encrypt data for the application.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ApplicationSummary) -> dict:
    out: dict = {}
    out["applicationId"] = value["application_id"]
    out["applicationName"] = value["application_name"]
    out["domain"] = value["domain"]
    if "default_kms_key_id" in value:
        out["defaultKmsKeyId"] = value["default_kms_key_id"]
    return out


def deserialize_json(data: dict) -> ApplicationSummary:
    out: ApplicationSummary = {}  # type: ignore[typeddict-item]
    if data.get("applicationId") is not None:
        out["application_id"] = data["applicationId"]
    else:
        out["application_id"] = ""
    if data.get("applicationName") is not None:
        out["application_name"] = data["applicationName"]
    else:
        out["application_name"] = ""
    if data.get("domain") is not None:
        out["domain"] = data["domain"]
    else:
        out["domain"] = ""
    if data.get("defaultKmsKeyId") is not None:
        out["default_kms_key_id"] = data["defaultKmsKeyId"]
    return out
