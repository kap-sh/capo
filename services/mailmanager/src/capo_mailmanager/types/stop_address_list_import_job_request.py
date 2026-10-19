"""Generated from Smithy shape ``com.amazonaws.mailmanager#StopAddressListImportJobRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_mailmanager.types.job_id


class StopAddressListImportJobRequest(TypedDict, closed=True):
    job_id: "capo_mailmanager.types.job_id.JobId"
    """<p>The identifier of the import job that needs to be stopped.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: StopAddressListImportJobRequest) -> dict:
    out: dict = {}
    out["JobId"] = value["job_id"]
    return out


def deserialize_aws_json_1_0(data: dict) -> StopAddressListImportJobRequest:
    out: StopAddressListImportJobRequest = {}  # type: ignore[typeddict-item]
    if data.get("JobId") is not None:
        out["job_id"] = data["JobId"]
    else:
        out["job_id"] = ""
    return out
