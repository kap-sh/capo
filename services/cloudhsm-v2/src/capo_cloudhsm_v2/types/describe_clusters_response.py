"""Generated from Smithy shape ``com.amazonaws.cloudhsmv2#DescribeClustersResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cloudhsm_v2.types.clusters
    import capo_cloudhsm_v2.types.next_token


class DescribeClustersResponse(TypedDict, closed=True):
    clusters: NotRequired["capo_cloudhsm_v2.types.clusters.Clusters"]
    """<p>A list of clusters.</p>"""
    next_token: NotRequired["capo_cloudhsm_v2.types.next_token.NextToken"]
    """<p>An opaque string that indicates that the response contains only a subset of clusters. Use this value in a subsequent <code>DescribeClusters</code> request to get more clusters.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeClustersResponse) -> dict:
    out: dict = {}
    if "clusters" in value:
        import capo_cloudhsm_v2.types.clusters

        out["Clusters"] = capo_cloudhsm_v2.types.clusters.serialize_aws_json_1_1(
            value["clusters"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeClustersResponse:
    out: DescribeClustersResponse = {}  # type: ignore[typeddict-item]
    if data.get("Clusters") is not None:
        import capo_cloudhsm_v2.types.clusters

        out["clusters"] = capo_cloudhsm_v2.types.clusters.deserialize_aws_json_1_1(
            data["Clusters"]
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DescribeClustersResponse) -> dict:
    out: dict = {}
    if "clusters" in value:
        import capo_cloudhsm_v2.types.clusters

        out["Clusters"] = capo_cloudhsm_v2.types.clusters.serialize_cbor(
            value["clusters"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_cbor(data: dict) -> DescribeClustersResponse:
    out: DescribeClustersResponse = {}  # type: ignore[typeddict-item]
    if data.get("Clusters") is not None:
        import capo_cloudhsm_v2.types.clusters

        out["clusters"] = capo_cloudhsm_v2.types.clusters.deserialize_cbor(
            data["Clusters"]
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
