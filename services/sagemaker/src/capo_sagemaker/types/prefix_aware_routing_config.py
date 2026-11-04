"""Generated from Smithy shape ``com.amazonaws.sagemaker#PrefixAwareRoutingConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.prefix_aware_routing_concurrency_threshold
    import capo_sagemaker.types.prefix_aware_routing_prefix_length


class PrefixAwareRoutingConfig(TypedDict, closed=True):
    prefix_length: NotRequired[
        "capo_sagemaker.types.prefix_aware_routing_prefix_length.PrefixAwareRoutingPrefixLength"
    ]
    """<p>The maximum length of the prefix used for routing decisions. Required when <code>RoutingStrategy</code> is <code>PREFIX_AWARE</code>.</p> <ul> <li> <p>For the SageMaker Runtime <code>InvokeEndpoint</code> and <code>InvokeEndpointWithResponseStream</code> APIs, this value specifies the number of bytes from the beginning of the request body.</p> </li> <li> <p>For OpenAI-compatible API, this value specifies the number of characters from the text content of the messages array.</p> </li> </ul> <p>The endpoint routes requests that share the same prefix to the same instance. Set this value to cover shared content (such as system prompts) plus enough unique content to distribute workloads across instances.</p>"""
    concurrency_threshold: NotRequired[
        "capo_sagemaker.types.prefix_aware_routing_concurrency_threshold.PrefixAwareRoutingConcurrencyThreshold"
    ]
    """<p>The maximum number of in-flight requests on the target instance before the endpoint routes to another instance. Required when <code>RoutingStrategy</code> is <code>PREFIX_AWARE</code>. When in-flight requests on the prefix-selected instance reach this threshold, the endpoint routes the request to an instance with more available capacity.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PrefixAwareRoutingConfig) -> dict:
    out: dict = {}
    if "prefix_length" in value:
        out["PrefixLength"] = value["prefix_length"]
    if "concurrency_threshold" in value:
        out["ConcurrencyThreshold"] = value["concurrency_threshold"]
    return out


def deserialize_aws_json_1_1(data: dict) -> PrefixAwareRoutingConfig:
    out: PrefixAwareRoutingConfig = {}  # type: ignore[typeddict-item]
    if data.get("PrefixLength") is not None:
        out["prefix_length"] = data["PrefixLength"]
    if data.get("ConcurrencyThreshold") is not None:
        out["concurrency_threshold"] = data["ConcurrencyThreshold"]
    return out
