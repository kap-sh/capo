"""Generated from Smithy shape ``com.amazonaws.glue#GetJobResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_glue.types.job


class GetJobResponse(TypedDict, closed=True):
    job: NotRequired["capo_glue.types.job.Job"]
    """<p>The requested job definition.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetJobResponse) -> dict:
    out: dict = {}
    if "job" in value:
        import capo_glue.types.job

        out["Job"] = capo_glue.types.job.serialize_aws_json_1_1(value["job"])
    return out


def deserialize_aws_json_1_1(data: dict) -> GetJobResponse:
    out: GetJobResponse = {}  # type: ignore[typeddict-item]
    if data.get("Job") is not None:
        import capo_glue.types.job

        out["job"] = capo_glue.types.job.deserialize_aws_json_1_1(data["Job"])
    return out


def redact_sensitive(value: GetJobResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "job" in value:
        import capo_glue.types.job

        out["job"] = capo_glue.types.job.redact_sensitive(value["job"])
    return out
