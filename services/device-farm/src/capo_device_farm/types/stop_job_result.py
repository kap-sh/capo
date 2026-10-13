"""Generated from Smithy shape ``com.amazonaws.devicefarm#StopJobResult``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_device_farm.types.job


class StopJobResult(TypedDict, closed=True):
    job: NotRequired["capo_device_farm.types.job.Job"]
    """<p>The job that was stopped.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StopJobResult) -> dict:
    out: dict = {}
    if "job" in value:
        import capo_device_farm.types.job

        out["job"] = capo_device_farm.types.job.serialize_aws_json_1_1(value["job"])
    return out


def deserialize_aws_json_1_1(data: dict) -> StopJobResult:
    out: StopJobResult = {}  # type: ignore[typeddict-item]
    if data.get("job") is not None:
        import capo_device_farm.types.job

        out["job"] = capo_device_farm.types.job.deserialize_aws_json_1_1(data["job"])
    return out


def redact_sensitive(value: StopJobResult) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "job" in value:
        import capo_device_farm.types.job

        out["job"] = capo_device_farm.types.job.redact_sensitive(value["job"])
    return out
