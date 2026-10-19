"""Generated from Smithy shape ``com.amazonaws.opensearchserverless#BatchGetLifecyclePolicyRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_opensearchserverless.types.lifecycle_policy_identifiers


class BatchGetLifecyclePolicyRequest(TypedDict, closed=True):
    identifiers: "capo_opensearchserverless.types.lifecycle_policy_identifiers.LifecyclePolicyIdentifiers"
    """<p>The unique identifiers of policy types and policy names.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: BatchGetLifecyclePolicyRequest) -> dict:
    out: dict = {}
    import capo_opensearchserverless.types.lifecycle_policy_identifiers

    out["identifiers"] = (
        capo_opensearchserverless.types.lifecycle_policy_identifiers.serialize_aws_json_1_0(
            value["identifiers"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> BatchGetLifecyclePolicyRequest:
    out: BatchGetLifecyclePolicyRequest = {}  # type: ignore[typeddict-item]
    if data.get("identifiers") is not None:
        import capo_opensearchserverless.types.lifecycle_policy_identifiers

        out["identifiers"] = (
            capo_opensearchserverless.types.lifecycle_policy_identifiers.deserialize_aws_json_1_0(
                data["identifiers"]
            )
        )
    else:
        out["identifiers"] = []
    return out
