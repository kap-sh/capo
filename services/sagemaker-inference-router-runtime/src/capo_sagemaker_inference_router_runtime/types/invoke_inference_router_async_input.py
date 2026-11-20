"""Generated from Smithy shape ``com.amazonaws.sagemakerinferencerouterruntime#InvokeInferenceRouterAsyncInput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker_inference_router_runtime.types.custom_attributes_header


class InvokeInferenceRouterAsyncInput(TypedDict, closed=True):
    inference_router_name: "str"
    """<p>The name of the inference router to invoke.</p>"""
    routing_target_name: "str"
    """<p>The name of the routing target in the inference router. The routing target must be configured for asynchronous inference.</p>"""
    content_type: NotRequired["str"]
    """<p>The MIME type of the input data in Amazon S3. The router passes it to the destination.</p>"""
    accept: NotRequired["str"]
    """<p>The MIME type that you want for the inference response. The router passes it to the destination.</p>"""
    custom_attributes: NotRequired[
        "capo_sagemaker_inference_router_runtime.types.custom_attributes_header.CustomAttributesHeader"
    ]
    """<p>Provides additional information about the inference request. The value is an opaque string that the router passes, unchanged, to the model container of the destination that serves the request. The value can contain up to 1,024 visible US-ASCII characters.</p>"""
    inference_id: NotRequired["str"]
    """<p>An identifier for the inference request. If you don't provide one, SageMaker AI generates one and returns it in the response.</p>"""
    input_location: "str"
    """<p>The Amazon S3 URI of the object that contains the input data for the inference. The bucket must be in the inference router's Amazon Web Services Region and owned by the router's account. The destination endpoint's execution role reads the object, and the destination's asynchronous inference limits apply to it.</p>"""
    s3_output_path_extension: NotRequired["str"]
    """<p>The path extension that is appended to the routing target's Amazon S3 output path where the inference response is stored.</p>"""
    filename: NotRequired["str"]
    """<p>The file name of the inference response stored in Amazon S3. If you don't provide one, SageMaker AI generates one.</p>"""
    request_ttl_seconds: NotRequired["int"]
    """<p>The time to live of the request, in seconds, measured from when the router accepts it. If no destination starts the request in this time, the request fails. The default is 21,600 seconds (6 hours).</p>"""
    invocation_timeout_seconds: NotRequired["int"]
    """<p>The maximum time, in seconds, that a destination can spend processing the request before the request is marked as expired. The default is 900 seconds (15 minutes).</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: InvokeInferenceRouterAsyncInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> InvokeInferenceRouterAsyncInput:
    out: InvokeInferenceRouterAsyncInput = {}  # type: ignore[typeddict-item]
    return out


def redact_sensitive(value: InvokeInferenceRouterAsyncInput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "custom_attributes" in value:
        out["custom_attributes"] = "*** Sensitive Data Redacted ***"
    return out
