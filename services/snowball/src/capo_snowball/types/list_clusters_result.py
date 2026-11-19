"""Generated from Smithy shape ``com.amazonaws.snowball#ListClustersResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_snowball.types.cluster_list_entry_list
    import capo_snowball.types.string


class ListClustersResult(TypedDict, closed=True):
    cluster_list_entries: NotRequired[
        "capo_snowball.types.cluster_list_entry_list.ClusterListEntryList"
    ]
    """<p>Each <code>ClusterListEntry</code> object contains a cluster's state, a cluster's ID, and other important status information.</p>"""
    next_token: NotRequired["capo_snowball.types.string.String"]
    """<p>HTTP requests are stateless. If you use the automatically generated <code>NextToken</code> value in your next <code>ClusterListEntry</code> call, your list of returned clusters will start from this point in the array.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListClustersResult) -> dict:
    out: dict = {}
    if "cluster_list_entries" in value:
        import capo_snowball.types.cluster_list_entry_list

        out["ClusterListEntries"] = (
            capo_snowball.types.cluster_list_entry_list.serialize_aws_json_1_1(
                value["cluster_list_entries"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListClustersResult:
    out: ListClustersResult = {}  # type: ignore[typeddict-item]
    if data.get("ClusterListEntries") is not None:
        import capo_snowball.types.cluster_list_entry_list

        out["cluster_list_entries"] = (
            capo_snowball.types.cluster_list_entry_list.deserialize_aws_json_1_1(
                data["ClusterListEntries"]
            )
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ListClustersResult) -> dict:
    out: dict = {}
    if "cluster_list_entries" in value:
        import capo_snowball.types.cluster_list_entry_list

        out["ClusterListEntries"] = (
            capo_snowball.types.cluster_list_entry_list.serialize_cbor(
                value["cluster_list_entries"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_cbor(data: dict) -> ListClustersResult:
    out: ListClustersResult = {}  # type: ignore[typeddict-item]
    if data.get("ClusterListEntries") is not None:
        import capo_snowball.types.cluster_list_entry_list

        out["cluster_list_entries"] = (
            capo_snowball.types.cluster_list_entry_list.deserialize_cbor(
                data["ClusterListEntries"]
            )
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
