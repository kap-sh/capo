"""Generated from Smithy shape ``com.amazonaws.devicefarm#StopRunResult``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_device_farm.types.run


class StopRunResult(TypedDict, closed=True):
    run: NotRequired["capo_device_farm.types.run.Run"]
    """<p>The run that was stopped.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StopRunResult) -> dict:
    out: dict = {}
    if "run" in value:
        import capo_device_farm.types.run

        out["run"] = capo_device_farm.types.run.serialize_aws_json_1_1(value["run"])
    return out


def deserialize_aws_json_1_1(data: dict) -> StopRunResult:
    out: StopRunResult = {}  # type: ignore[typeddict-item]
    if data.get("run") is not None:
        import capo_device_farm.types.run

        out["run"] = capo_device_farm.types.run.deserialize_aws_json_1_1(data["run"])
    return out


def redact_sensitive(value: StopRunResult) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "run" in value:
        import capo_device_farm.types.run

        out["run"] = capo_device_farm.types.run.redact_sensitive(value["run"])
    return out
