"""Generated from Smithy shape ``com.amazonaws.opensearchserverless#BatchGetEffectiveLifecyclePolicyRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_opensearchserverless.types.lifecycle_policy_resource_identifiers


class BatchGetEffectiveLifecyclePolicyRequest(TypedDict, closed=True):
    resource_identifiers: "capo_opensearchserverless.types.lifecycle_policy_resource_identifiers.LifecyclePolicyResourceIdentifiers"
    """<p>The unique identifiers of policy types and resource names.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: BatchGetEffectiveLifecyclePolicyRequest) -> dict:
    out: dict = {}
    import capo_opensearchserverless.types.lifecycle_policy_resource_identifiers

    out["resourceIdentifiers"] = (
        capo_opensearchserverless.types.lifecycle_policy_resource_identifiers.serialize_aws_json_1_0(
            value["resource_identifiers"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> BatchGetEffectiveLifecyclePolicyRequest:
    out: BatchGetEffectiveLifecyclePolicyRequest = {}  # type: ignore[typeddict-item]
    if data.get("resourceIdentifiers") is not None:
        import capo_opensearchserverless.types.lifecycle_policy_resource_identifiers

        out["resource_identifiers"] = (
            capo_opensearchserverless.types.lifecycle_policy_resource_identifiers.deserialize_aws_json_1_0(
                data["resourceIdentifiers"]
            )
        )
    else:
        out["resource_identifiers"] = []
    return out
