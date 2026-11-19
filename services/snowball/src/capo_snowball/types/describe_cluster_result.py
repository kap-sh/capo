"""Generated from Smithy shape ``com.amazonaws.snowball#DescribeClusterResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_snowball.types.cluster_metadata


class DescribeClusterResult(TypedDict, closed=True):
    cluster_metadata: NotRequired[
        "capo_snowball.types.cluster_metadata.ClusterMetadata"
    ]
    """<p>Information about a specific cluster, including shipping information, cluster status, and other important metadata.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeClusterResult) -> dict:
    out: dict = {}
    if "cluster_metadata" in value:
        import capo_snowball.types.cluster_metadata

        out["ClusterMetadata"] = (
            capo_snowball.types.cluster_metadata.serialize_aws_json_1_1(
                value["cluster_metadata"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeClusterResult:
    out: DescribeClusterResult = {}  # type: ignore[typeddict-item]
    if data.get("ClusterMetadata") is not None:
        import capo_snowball.types.cluster_metadata

        out["cluster_metadata"] = (
            capo_snowball.types.cluster_metadata.deserialize_aws_json_1_1(
                data["ClusterMetadata"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DescribeClusterResult) -> dict:
    out: dict = {}
    if "cluster_metadata" in value:
        import capo_snowball.types.cluster_metadata

        out["ClusterMetadata"] = capo_snowball.types.cluster_metadata.serialize_cbor(
            value["cluster_metadata"]
        )
    return out


def deserialize_cbor(data: dict) -> DescribeClusterResult:
    out: DescribeClusterResult = {}  # type: ignore[typeddict-item]
    if data.get("ClusterMetadata") is not None:
        import capo_snowball.types.cluster_metadata

        out["cluster_metadata"] = capo_snowball.types.cluster_metadata.deserialize_cbor(
            data["ClusterMetadata"]
        )
    return out
