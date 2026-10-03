"""Generated from Smithy shape ``com.amazonaws.ecs#PutClusterCapacityProvidersRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_ecs.errors import DeserializationError

if TYPE_CHECKING:
    import capo_ecs.types.capacity_provider_strategy
    import capo_ecs.types.string
    import capo_ecs.types.string_list


class PutClusterCapacityProvidersRequest(TypedDict, closed=True):
    cluster: "capo_ecs.types.string.String"
    """<p>The short name or full Amazon Resource Name (ARN) of the cluster to modify the capacity provider settings for. If you don't specify a cluster, the default cluster is assumed.</p>"""
    capacity_providers: "capo_ecs.types.string_list.StringList"
    """<p>The name of one or more capacity providers to associate with the cluster.</p> <p>If specifying a capacity provider that uses an Auto Scaling group, the capacity provider must already be created. New capacity providers can be created with the <a href="https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_CreateCapacityProvider.html">CreateCapacityProvider</a> API operation.</p> <p>To use a Fargate capacity provider, specify either the <code>FARGATE</code> or <code>FARGATE_SPOT</code> capacity providers. The Fargate capacity providers are available to all accounts and only need to be associated with a cluster to be used.</p>"""
    default_capacity_provider_strategy: (
        "capo_ecs.types.capacity_provider_strategy.CapacityProviderStrategy"
    )
    """<p>The capacity provider strategy to use by default for the cluster.</p> <p>When creating a service or running a task on a cluster, if no capacity provider or launch type is specified then the default capacity provider strategy for the cluster is used.</p> <p>A capacity provider strategy consists of one or more capacity providers along with the <code>base</code> and <code>weight</code> to assign to them. A capacity provider must be associated with the cluster to be used in a capacity provider strategy. The <a href="https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_PutClusterCapacityProviders.html">PutClusterCapacityProviders</a> API is used to associate a capacity provider with a cluster. Only capacity providers with an <code>ACTIVE</code> or <code>UPDATING</code> status can be used.</p> <p>If specifying a capacity provider that uses an Auto Scaling group, the capacity provider must already be created. New capacity providers can be created with the <a href="https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_CreateCapacityProvider.html">CreateCapacityProvider</a> API operation.</p> <p>To use a Fargate capacity provider, specify either the <code>FARGATE</code> or <code>FARGATE_SPOT</code> capacity providers. The Fargate capacity providers are available to all accounts and only need to be associated with a cluster to be used.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PutClusterCapacityProvidersRequest) -> dict:
    out: dict = {}
    out["cluster"] = value["cluster"]
    import capo_ecs.types.string_list

    out["capacityProviders"] = capo_ecs.types.string_list.serialize_aws_json_1_1(
        value["capacity_providers"]
    )
    import capo_ecs.types.capacity_provider_strategy

    out["defaultCapacityProviderStrategy"] = (
        capo_ecs.types.capacity_provider_strategy.serialize_aws_json_1_1(
            value["default_capacity_provider_strategy"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> PutClusterCapacityProvidersRequest:
    out: PutClusterCapacityProvidersRequest = {}  # type: ignore[typeddict-item]
    if data.get("cluster") is not None:
        out["cluster"] = data["cluster"]
    else:
        raise DeserializationError(
            "PutClusterCapacityProvidersRequest.cluster required"
        )
    if data.get("capacityProviders") is not None:
        import capo_ecs.types.string_list

        out["capacity_providers"] = capo_ecs.types.string_list.deserialize_aws_json_1_1(
            data["capacityProviders"]
        )
    else:
        raise DeserializationError(
            "PutClusterCapacityProvidersRequest.capacity_providers required"
        )
    if data.get("defaultCapacityProviderStrategy") is not None:
        import capo_ecs.types.capacity_provider_strategy

        out["default_capacity_provider_strategy"] = (
            capo_ecs.types.capacity_provider_strategy.deserialize_aws_json_1_1(
                data["defaultCapacityProviderStrategy"]
            )
        )
    else:
        raise DeserializationError(
            "PutClusterCapacityProvidersRequest.default_capacity_provider_strategy required"
        )
    return out
