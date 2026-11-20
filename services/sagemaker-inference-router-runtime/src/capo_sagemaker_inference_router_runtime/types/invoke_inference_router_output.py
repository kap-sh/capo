"""Generated from Smithy shape ``com.amazonaws.sagemakerinferencerouterruntime#InvokeInferenceRouterOutput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker_inference_router_runtime.types.custom_attributes_header
    import capo_sagemaker_inference_router_runtime.types.inference_router_body_blob


class InvokeInferenceRouterOutput(TypedDict, closed=True):
    body: NotRequired[
        "capo_sagemaker_inference_router_runtime.types.inference_router_body_blob.InferenceRouterBodyBlob"
    ]
    """<p>The inference that the model returned.</p>"""
    content_type: NotRequired["str"]
    """<p>The MIME type of the inference returned in the response body.</p>"""
    invoked_routed_resource_arn: NotRequired["str"]
    """<p>The Amazon Resource Name (ARN) of the endpoint or inference component that served the request.</p>"""
    routing_reason: NotRequired["str"]
    """<p>The reason that the router chose the destination that served the request. Possible values:</p> <ul> <li> <p> <code>local-preferred</code> – The destination is a healthy destination in the router's Region.</p> </li> <li> <p> <code>capacity-available</code> – No destination in the router's Region could take the request, and two or more destinations in other Regions could.</p> </li> <li> <p> <code>only-healthy</code> – No destination in the router's Region could take the request, and exactly one destination in another Region could.</p> </li> <li> <p> <code>failover</code> – The router moved the request away from destinations in its Region because they were overloaded or returning errors. You also see this value when the router can't assess destination health, and when no destination is healthy and the router tries one anyway.</p> </li> </ul>"""
    invoked_production_variant: NotRequired["str"]
    """<p>The production variant of the destination endpoint that served the request.</p>"""
    custom_attributes: NotRequired[
        "capo_sagemaker_inference_router_runtime.types.custom_attributes_header.CustomAttributesHeader"
    ]
    """<p>Provides additional information in the response about the inference. This is the value that the model container of the destination returned, unchanged.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: InvokeInferenceRouterOutput) -> dict:
    out: dict = {}
    if "body" in value:
        import capo_sagemaker_inference_router_runtime.types.inference_router_body_blob

        out["Body"] = (
            capo_sagemaker_inference_router_runtime.types.inference_router_body_blob.serialize_json(
                value["body"]
            )
        )
    return out


def deserialize_json(data: dict) -> InvokeInferenceRouterOutput:
    out: InvokeInferenceRouterOutput = {}  # type: ignore[typeddict-item]
    if data.get("Body") is not None:
        import capo_sagemaker_inference_router_runtime.types.inference_router_body_blob

        out["body"] = (
            capo_sagemaker_inference_router_runtime.types.inference_router_body_blob.deserialize_json(
                data["Body"]
            )
        )
    return out


def redact_sensitive(value: InvokeInferenceRouterOutput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "body" in value:
        out["body"] = "*** Sensitive Data Redacted ***"
    if "custom_attributes" in value:
        out["custom_attributes"] = "*** Sensitive Data Redacted ***"
    return out
