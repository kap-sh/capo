"""Generated from Smithy shape ``com.amazonaws.healthlake#DescribeDataTransformationJobRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_healthlake.types.data_transformation_job_id


class DescribeDataTransformationJobRequest(TypedDict, closed=True):
    job_id: "capo_healthlake.types.data_transformation_job_id.DataTransformationJobId"
    """<p>The unique identifier of the data transformation job to describe.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DescribeDataTransformationJobRequest) -> dict:
    out: dict = {}
    out["JobId"] = value["job_id"]
    return out


def deserialize_aws_json_1_0(data: dict) -> DescribeDataTransformationJobRequest:
    out: DescribeDataTransformationJobRequest = {}  # type: ignore[typeddict-item]
    if data.get("JobId") is not None:
        out["job_id"] = data["JobId"]
    else:
        out["job_id"] = ""
    return out
