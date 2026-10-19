"""Generated from Smithy shape ``com.amazonaws.snowball#GetSoftwareUpdatesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_snowball.types.job_id


class GetSoftwareUpdatesRequest(TypedDict, closed=True):
    job_id: "capo_snowball.types.job_id.JobId"
    """<p>The ID for a job that you want to get the software update file for, for example <code>JID123e4567-e89b-12d3-a456-426655440000</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetSoftwareUpdatesRequest) -> dict:
    out: dict = {}
    out["JobId"] = value["job_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetSoftwareUpdatesRequest:
    out: GetSoftwareUpdatesRequest = {}  # type: ignore[typeddict-item]
    if data.get("JobId") is not None:
        out["job_id"] = data["JobId"]
    else:
        out["job_id"] = ""
    return out
