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
    """<p>The maximum length of the prefix used for routing decisions. Required when <code>RoutingStrategy</code> is <code>PREFIX_AWARE</code>.</p> <ul> <li> <p>For the SageMaker Runtime <code>InvokeEndpoint</code> and <code>InvokeEndpointWithResponseStream</code> APIs, this value specifies the number of bytes from the beginning of the request body.</p> </li> <li> <p>For OpenAI-compatible API, this value specifies the number of characters from the text content of the messages array.</p> </li> </ul> <p>The endpoint routes requests that share the same prefix to the same instance and, when that instance hosts more than one copy of the invoked inference component, to the same copy. Set this value to cover shared content (such as system prompts) plus enough unique content to distribute workloads across instances and copies.</p>"""
    concurrency_threshold: NotRequired[
        "capo_sagemaker.types.prefix_aware_routing_concurrency_threshold.PrefixAwareRoutingConcurrencyThreshold"
    ]
    """<p>The number of in-flight requests on the selected instance or inference component copy at which the endpoint routes a request to another copy or instance. Required when <code>RoutingStrategy</code> is <code>PREFIX_AWARE</code>.</p> <p>On an endpoint without inference components, the endpoint compares this threshold with the number of in-flight requests on the selected instance. When that number reaches the threshold, the endpoint routes the request to another instance.</p> <p>On an endpoint with inference components, the endpoint compares this threshold with the number of in-flight requests on the selected copy of the invoked inference component. Requests to other inference components on the same instance don't count. When the instance hosts more than one copy of the inference component, the endpoint routes requests that share a prefix to the same copy and, while that copy has reached the threshold, to another copy on the instance that is under the threshold. When every copy on the instance has reached the threshold, the endpoint routes the request to another instance.</p> <p>The threshold applies to every instance and every copy of every inference component in the production variant, so choose a value that suits the instance or copy that can serve the fewest concurrent requests.</p>"""


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
