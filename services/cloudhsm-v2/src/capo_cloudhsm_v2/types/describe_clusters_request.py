"""Generated from Smithy shape ``com.amazonaws.cloudhsmv2#DescribeClustersRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cloudhsm_v2.types.clusters_max_size
    import capo_cloudhsm_v2.types.filters
    import capo_cloudhsm_v2.types.next_token


class DescribeClustersRequest(TypedDict, closed=True):
    filters: NotRequired["capo_cloudhsm_v2.types.filters.Filters"]
    """<p>One or more filters to limit the items returned in the response.</p> <p>Use the <code>clusterIds</code> filter to return only the specified clusters. Specify clusters by their cluster identifier (ID).</p> <p>Use the <code>vpcIds</code> filter to return only the clusters in the specified virtual private clouds (VPCs). Specify VPCs by their VPC identifier (ID).</p> <p>Use the <code>states</code> filter to return only clusters that match the specified state.</p>"""
    next_token: NotRequired["capo_cloudhsm_v2.types.next_token.NextToken"]
    """<p>The <code>NextToken</code> value that you received in the previous response. Use this value to get more clusters.</p>"""
    max_results: NotRequired["capo_cloudhsm_v2.types.clusters_max_size.ClustersMaxSize"]
    """<p>The maximum number of clusters to return in the response. When there are more clusters than the number you specify, the response contains a <code>NextToken</code> value.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeClustersRequest) -> dict:
    out: dict = {}
    if "filters" in value:
        import capo_cloudhsm_v2.types.filters

        out["Filters"] = capo_cloudhsm_v2.types.filters.serialize_aws_json_1_1(
            value["filters"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeClustersRequest:
    out: DescribeClustersRequest = {}  # type: ignore[typeddict-item]
    if data.get("Filters") is not None:
        import capo_cloudhsm_v2.types.filters

        out["filters"] = capo_cloudhsm_v2.types.filters.deserialize_aws_json_1_1(
            data["Filters"]
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    if data.get("MaxResults") is not None:
        out["max_results"] = data["MaxResults"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DescribeClustersRequest) -> dict:
    out: dict = {}
    if "filters" in value:
        import capo_cloudhsm_v2.types.filters

        out["Filters"] = capo_cloudhsm_v2.types.filters.serialize_cbor(value["filters"])
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    return out


def deserialize_cbor(data: dict) -> DescribeClustersRequest:
    out: DescribeClustersRequest = {}  # type: ignore[typeddict-item]
    if data.get("Filters") is not None:
        import capo_cloudhsm_v2.types.filters

        out["filters"] = capo_cloudhsm_v2.types.filters.deserialize_cbor(
            data["Filters"]
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    if data.get("MaxResults") is not None:
        out["max_results"] = data["MaxResults"]
    return out
