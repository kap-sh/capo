"""Generated from Smithy shape ``com.amazonaws.cloudcontrol#CreateResourceOutput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cloudcontrol.types.progress_event


class CreateResourceOutput(TypedDict, closed=True):
    progress_event: NotRequired["capo_cloudcontrol.types.progress_event.ProgressEvent"]
    """<p>Represents the current status of the resource creation request.</p> <p>After you have initiated a resource creation request, you can monitor the progress of your request by calling <a href="https://docs.aws.amazon.com/cloudcontrolapi/latest/APIReference/API_GetResourceRequestStatus.html">GetResourceRequestStatus</a> using the <code>RequestToken</code> of the <code>ProgressEvent</code> returned by <code>CreateResource</code>.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CreateResourceOutput) -> dict:
    out: dict = {}
    if "progress_event" in value:
        import capo_cloudcontrol.types.progress_event

        out["ProgressEvent"] = (
            capo_cloudcontrol.types.progress_event.serialize_aws_json_1_0(
                value["progress_event"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> CreateResourceOutput:
    out: CreateResourceOutput = {}  # type: ignore[typeddict-item]
    if data.get("ProgressEvent") is not None:
        import capo_cloudcontrol.types.progress_event

        out["progress_event"] = (
            capo_cloudcontrol.types.progress_event.deserialize_aws_json_1_0(
                data["ProgressEvent"]
            )
        )
    return out


def redact_sensitive(value: CreateResourceOutput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "progress_event" in value:
        import capo_cloudcontrol.types.progress_event

        out["progress_event"] = capo_cloudcontrol.types.progress_event.redact_sensitive(
            value["progress_event"]
        )
    return out
