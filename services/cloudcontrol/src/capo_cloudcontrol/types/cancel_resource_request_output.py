"""Generated from Smithy shape ``com.amazonaws.cloudcontrol#CancelResourceRequestOutput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cloudcontrol.types.progress_event


class CancelResourceRequestOutput(TypedDict, closed=True):
    progress_event: NotRequired["capo_cloudcontrol.types.progress_event.ProgressEvent"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CancelResourceRequestOutput) -> dict:
    out: dict = {}
    if "progress_event" in value:
        import capo_cloudcontrol.types.progress_event

        out["ProgressEvent"] = (
            capo_cloudcontrol.types.progress_event.serialize_aws_json_1_0(
                value["progress_event"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> CancelResourceRequestOutput:
    out: CancelResourceRequestOutput = {}  # type: ignore[typeddict-item]
    if data.get("ProgressEvent") is not None:
        import capo_cloudcontrol.types.progress_event

        out["progress_event"] = (
            capo_cloudcontrol.types.progress_event.deserialize_aws_json_1_0(
                data["ProgressEvent"]
            )
        )
    return out


def redact_sensitive(value: CancelResourceRequestOutput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "progress_event" in value:
        import capo_cloudcontrol.types.progress_event

        out["progress_event"] = capo_cloudcontrol.types.progress_event.redact_sensitive(
            value["progress_event"]
        )
    return out
