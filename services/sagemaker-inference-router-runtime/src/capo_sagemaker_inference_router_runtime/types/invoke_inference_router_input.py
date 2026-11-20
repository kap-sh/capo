"""Generated from Smithy shape ``com.amazonaws.sagemakerinferencerouterruntime#InvokeInferenceRouterInput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker_inference_router_runtime.types.custom_attributes_header
    import capo_sagemaker_inference_router_runtime.types.inference_router_body_blob


class InvokeInferenceRouterInput(TypedDict, closed=True):
    inference_router_name: "str"
    """<p>The name of the inference router to invoke.</p>"""
    routing_target_name: "str"
    """<p>The name of the routing target in the inference router. The routing target lists the destinations that can serve the request.</p>"""
    content_type: NotRequired["str"]
    """<p>The MIME type of the input data in the request body. The router passes it to the destination.</p>"""
    accept: NotRequired["str"]
    """<p>The MIME type that you want for the inference response. The router passes it to the destination.</p>"""
    inference_id: NotRequired["str"]
    """<p>An identifier for the inference request. The router passes it to the destination.</p>"""
    prefix_aware_id: NotRequired["str"]
    """<p>An optional, stable identifier that serves as a routing hint for prefix-aware routing. The router passes it to the destination that serves the request. Within that destination, requests with the same prefix and the same identifier go to the same instance. If requests from different applications might have the same prompt prefix, set a different identifier for each application to differentiate their routing decisions.</p> <p>Applies only to destination endpoints configured with a <code>RoutingStrategy</code> of <code>PREFIX_AWARE</code>.</p>"""
    custom_attributes: NotRequired[
        "capo_sagemaker_inference_router_runtime.types.custom_attributes_header.CustomAttributesHeader"
    ]
    """<p>Provides additional information about the inference request. The value is an opaque string that the router passes, unchanged, to the model container of the destination that serves the request. The value can contain up to 1,024 visible US-ASCII characters.</p>"""
    body: "capo_sagemaker_inference_router_runtime.types.inference_router_body_blob.InferenceRouterBodyBlob"
    """<p>The input data for the inference, in the format that your model expects. The body can't be empty.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: InvokeInferenceRouterInput) -> dict:
    out: dict = {}
    import capo_sagemaker_inference_router_runtime.types.inference_router_body_blob

    out["Body"] = (
        capo_sagemaker_inference_router_runtime.types.inference_router_body_blob.serialize_json(
            value["body"]
        )
    )
    return out


def deserialize_json(data: dict) -> InvokeInferenceRouterInput:
    out: InvokeInferenceRouterInput = {}  # type: ignore[typeddict-item]
    if data.get("Body") is not None:
        import capo_sagemaker_inference_router_runtime.types.inference_router_body_blob

        out["body"] = (
            capo_sagemaker_inference_router_runtime.types.inference_router_body_blob.deserialize_json(
                data["Body"]
            )
        )
    else:
        out["body"] = b""
    return out


def redact_sensitive(value: InvokeInferenceRouterInput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "custom_attributes" in value:
        out["custom_attributes"] = "*** Sensitive Data Redacted ***"
    if "body" in value:
        out["body"] = "*** Sensitive Data Redacted ***"
    return out
