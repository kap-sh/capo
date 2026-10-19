"""Generated from Smithy shape ``com.amazonaws.mailmanager#CreateAddressListImportJobResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_mailmanager.types.job_id
    import capo_mailmanager.types.pre_signed_url


class CreateAddressListImportJobResponse(TypedDict, closed=True):
    job_id: "capo_mailmanager.types.job_id.JobId"
    """<p>The identifier of the created import job.</p>"""
    pre_signed_url: "capo_mailmanager.types.pre_signed_url.PreSignedUrl"
    """<p>The pre-signed URL target for uploading the input file.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CreateAddressListImportJobResponse) -> dict:
    out: dict = {}
    out["JobId"] = value["job_id"]
    out["PreSignedUrl"] = value["pre_signed_url"]
    return out


def deserialize_aws_json_1_0(data: dict) -> CreateAddressListImportJobResponse:
    out: CreateAddressListImportJobResponse = {}  # type: ignore[typeddict-item]
    if data.get("JobId") is not None:
        out["job_id"] = data["JobId"]
    else:
        out["job_id"] = ""
    if data.get("PreSignedUrl") is not None:
        out["pre_signed_url"] = data["PreSignedUrl"]
    else:
        out["pre_signed_url"] = ""
    return out


def redact_sensitive(value: CreateAddressListImportJobResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "pre_signed_url" in value:
        out["pre_signed_url"] = "*** Sensitive Data Redacted ***"
    return out
