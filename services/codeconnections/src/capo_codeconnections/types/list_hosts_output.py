"""Generated from Smithy shape ``com.amazonaws.codeconnections#ListHostsOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codeconnections.types.host_list
    import capo_codeconnections.types.next_token


class ListHostsOutput(TypedDict, closed=True):
    hosts: NotRequired["capo_codeconnections.types.host_list.HostList"]
    """<p>A list of hosts and the details for each host, such as status, endpoint, and provider type.</p>"""
    next_token: NotRequired["capo_codeconnections.types.next_token.NextToken"]
    """<p>A token that can be used in the next <code>ListHosts</code> call. To view all items in the list, continue to call this operation with each subsequent token until no more <code>nextToken</code> values are returned.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListHostsOutput) -> dict:
    out: dict = {}
    if "hosts" in value:
        import capo_codeconnections.types.host_list

        out["Hosts"] = capo_codeconnections.types.host_list.serialize_aws_json_1_0(
            value["hosts"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ListHostsOutput:
    out: ListHostsOutput = {}  # type: ignore[typeddict-item]
    if data.get("Hosts") is not None:
        import capo_codeconnections.types.host_list

        out["hosts"] = capo_codeconnections.types.host_list.deserialize_aws_json_1_0(
            data["Hosts"]
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ListHostsOutput) -> dict:
    out: dict = {}
    if "hosts" in value:
        import capo_codeconnections.types.host_list

        out["Hosts"] = capo_codeconnections.types.host_list.serialize_cbor(
            value["hosts"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_cbor(data: dict) -> ListHostsOutput:
    out: ListHostsOutput = {}  # type: ignore[typeddict-item]
    if data.get("Hosts") is not None:
        import capo_codeconnections.types.host_list

        out["hosts"] = capo_codeconnections.types.host_list.deserialize_cbor(
            data["Hosts"]
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
