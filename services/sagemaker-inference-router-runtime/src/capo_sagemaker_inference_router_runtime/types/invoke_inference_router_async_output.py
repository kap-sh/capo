"""Generated from Smithy shape ``com.amazonaws.sagemakerinferencerouterruntime#InvokeInferenceRouterAsyncOutput``."""

from typing_extensions import NotRequired, TypedDict


class InvokeInferenceRouterAsyncOutput(TypedDict, closed=True):
    inference_id: NotRequired["str"]
    """<p>The identifier for the inference request. This is the <code>InferenceId</code> that you provided, or the one that SageMaker AI generated.</p>"""
    output_location: NotRequired["str"]
    """<p>The Amazon S3 URI where the inference response is written. The location doesn't change if the router moves the request to another destination.</p>"""
    failure_location: NotRequired["str"]
    """<p>The Amazon S3 URI where the failure details are written if the inference fails.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: InvokeInferenceRouterAsyncOutput) -> dict:
    out: dict = {}
    if "inference_id" in value:
        out["InferenceId"] = value["inference_id"]
    return out


def deserialize_json(data: dict) -> InvokeInferenceRouterAsyncOutput:
    out: InvokeInferenceRouterAsyncOutput = {}  # type: ignore[typeddict-item]
    if data.get("InferenceId") is not None:
        out["inference_id"] = data["InferenceId"]
    return out
