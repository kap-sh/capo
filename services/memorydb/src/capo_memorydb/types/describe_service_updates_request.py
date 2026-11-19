"""Generated from Smithy shape ``com.amazonaws.memorydb#DescribeServiceUpdatesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_memorydb.types.cluster_name_list
    import capo_memorydb.types.integer_optional
    import capo_memorydb.types.service_update_status_list
    import capo_memorydb.types.string


class DescribeServiceUpdatesRequest(TypedDict, closed=True):
    service_update_name: NotRequired["capo_memorydb.types.string.String"]
    """<p>The unique ID of the service update to describe.</p>"""
    cluster_names: NotRequired["capo_memorydb.types.cluster_name_list.ClusterNameList"]
    """<p>The list of cluster names to identify service updates to apply.</p>"""
    status: NotRequired[
        "capo_memorydb.types.service_update_status_list.ServiceUpdateStatusList"
    ]
    """<p>The status(es) of the service updates to filter on.</p>"""
    max_results: NotRequired["capo_memorydb.types.integer_optional.IntegerOptional"]
    """<p>The maximum number of records to include in the response. If more records exist than the specified MaxResults value, a token is included in the response so that the remaining results can be retrieved.</p>"""
    next_token: NotRequired["capo_memorydb.types.string.String"]
    """<p>An optional argument to pass in case the total number of records exceeds the value of MaxResults. If nextToken is returned, there are more results available. The value of nextToken is a unique pagination token for each page. Make the call again using the returned token to retrieve the next page. Keep all other arguments unchanged. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeServiceUpdatesRequest) -> dict:
    out: dict = {}
    if "service_update_name" in value:
        out["ServiceUpdateName"] = value["service_update_name"]
    if "cluster_names" in value:
        import capo_memorydb.types.cluster_name_list

        out["ClusterNames"] = (
            capo_memorydb.types.cluster_name_list.serialize_aws_json_1_1(
                value["cluster_names"]
            )
        )
    if "status" in value:
        import capo_memorydb.types.service_update_status_list

        out["Status"] = (
            capo_memorydb.types.service_update_status_list.serialize_aws_json_1_1(
                value["status"]
            )
        )
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeServiceUpdatesRequest:
    out: DescribeServiceUpdatesRequest = {}  # type: ignore[typeddict-item]
    if data.get("ServiceUpdateName") is not None:
        out["service_update_name"] = data["ServiceUpdateName"]
    if data.get("ClusterNames") is not None:
        import capo_memorydb.types.cluster_name_list

        out["cluster_names"] = (
            capo_memorydb.types.cluster_name_list.deserialize_aws_json_1_1(
                data["ClusterNames"]
            )
        )
    if data.get("Status") is not None:
        import capo_memorydb.types.service_update_status_list

        out["status"] = (
            capo_memorydb.types.service_update_status_list.deserialize_aws_json_1_1(
                data["Status"]
            )
        )
    if data.get("MaxResults") is not None:
        out["max_results"] = data["MaxResults"]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DescribeServiceUpdatesRequest) -> dict:
    out: dict = {}
    if "service_update_name" in value:
        out["ServiceUpdateName"] = value["service_update_name"]
    if "cluster_names" in value:
        import capo_memorydb.types.cluster_name_list

        out["ClusterNames"] = capo_memorydb.types.cluster_name_list.serialize_cbor(
            value["cluster_names"]
        )
    if "status" in value:
        import capo_memorydb.types.service_update_status_list

        out["Status"] = capo_memorydb.types.service_update_status_list.serialize_cbor(
            value["status"]
        )
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_cbor(data: dict) -> DescribeServiceUpdatesRequest:
    out: DescribeServiceUpdatesRequest = {}  # type: ignore[typeddict-item]
    if data.get("ServiceUpdateName") is not None:
        out["service_update_name"] = data["ServiceUpdateName"]
    if data.get("ClusterNames") is not None:
        import capo_memorydb.types.cluster_name_list

        out["cluster_names"] = capo_memorydb.types.cluster_name_list.deserialize_cbor(
            data["ClusterNames"]
        )
    if data.get("Status") is not None:
        import capo_memorydb.types.service_update_status_list

        out["status"] = capo_memorydb.types.service_update_status_list.deserialize_cbor(
            data["Status"]
        )
    if data.get("MaxResults") is not None:
        out["max_results"] = data["MaxResults"]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
