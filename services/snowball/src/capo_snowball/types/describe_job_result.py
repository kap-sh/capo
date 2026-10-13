"""Generated from Smithy shape ``com.amazonaws.snowball#DescribeJobResult``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_snowball.types.job_metadata
    import capo_snowball.types.job_metadata_list


class DescribeJobResult(TypedDict, closed=True):
    job_metadata: NotRequired["capo_snowball.types.job_metadata.JobMetadata"]
    """<p>Information about a specific job, including shipping information, job status, and other important metadata.</p>"""
    sub_job_metadata: NotRequired[
        "capo_snowball.types.job_metadata_list.JobMetadataList"
    ]
    """<p>Information about a specific job part (in the case of an export job), including shipping information, job status, and other important metadata.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeJobResult) -> dict:
    out: dict = {}
    if "job_metadata" in value:
        import capo_snowball.types.job_metadata

        out["JobMetadata"] = capo_snowball.types.job_metadata.serialize_aws_json_1_1(
            value["job_metadata"]
        )
    if "sub_job_metadata" in value:
        import capo_snowball.types.job_metadata_list

        out["SubJobMetadata"] = (
            capo_snowball.types.job_metadata_list.serialize_aws_json_1_1(
                value["sub_job_metadata"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeJobResult:
    out: DescribeJobResult = {}  # type: ignore[typeddict-item]
    if data.get("JobMetadata") is not None:
        import capo_snowball.types.job_metadata

        out["job_metadata"] = capo_snowball.types.job_metadata.deserialize_aws_json_1_1(
            data["JobMetadata"]
        )
    if data.get("SubJobMetadata") is not None:
        import capo_snowball.types.job_metadata_list

        out["sub_job_metadata"] = (
            capo_snowball.types.job_metadata_list.deserialize_aws_json_1_1(
                data["SubJobMetadata"]
            )
        )
    return out


def redact_sensitive(value: DescribeJobResult) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "job_metadata" in value:
        import capo_snowball.types.job_metadata

        out["job_metadata"] = capo_snowball.types.job_metadata.redact_sensitive(
            value["job_metadata"]
        )
    if "sub_job_metadata" in value:
        import capo_snowball.types.job_metadata_list

        out["sub_job_metadata"] = (
            capo_snowball.types.job_metadata_list.redact_sensitive(
                value["sub_job_metadata"]
            )
        )
    return out
