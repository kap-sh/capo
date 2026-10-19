"""Generated from Smithy shape ``com.amazonaws.opensearchserverless#BatchGetVpcEndpointRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_opensearchserverless.types.vpc_endpoint_ids


class BatchGetVpcEndpointRequest(TypedDict, closed=True):
    ids: "capo_opensearchserverless.types.vpc_endpoint_ids.VpcEndpointIds"
    """<p>A list of VPC endpoint identifiers.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: BatchGetVpcEndpointRequest) -> dict:
    out: dict = {}
    import capo_opensearchserverless.types.vpc_endpoint_ids

    out["ids"] = (
        capo_opensearchserverless.types.vpc_endpoint_ids.serialize_aws_json_1_0(
            value["ids"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> BatchGetVpcEndpointRequest:
    out: BatchGetVpcEndpointRequest = {}  # type: ignore[typeddict-item]
    if data.get("ids") is not None:
        import capo_opensearchserverless.types.vpc_endpoint_ids

        out["ids"] = (
            capo_opensearchserverless.types.vpc_endpoint_ids.deserialize_aws_json_1_0(
                data["ids"]
            )
        )
    else:
        out["ids"] = []
    return out
