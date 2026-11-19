"""Generated from Smithy shape ``com.amazonaws.backupgateway#ListGatewaysInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_backup_gateway.types.max_results
    import capo_backup_gateway.types.next_token


class ListGatewaysInput(TypedDict, closed=True):
    max_results: NotRequired["capo_backup_gateway.types.max_results.MaxResults"]
    """<p>The maximum number of gateways to list.</p>"""
    next_token: NotRequired["capo_backup_gateway.types.next_token.NextToken"]
    """<p>The next item following a partial list of returned resources. For example, if a request is made to return <code>MaxResults</code> number of resources, <code>NextToken</code> allows you to return more items in your list starting at the location pointed to by the next token.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListGatewaysInput) -> dict:
    out: dict = {}
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ListGatewaysInput:
    out: ListGatewaysInput = {}  # type: ignore[typeddict-item]
    if data.get("MaxResults") is not None:
        out["max_results"] = data["MaxResults"]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ListGatewaysInput) -> dict:
    out: dict = {}
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_cbor(data: dict) -> ListGatewaysInput:
    out: ListGatewaysInput = {}  # type: ignore[typeddict-item]
    if data.get("MaxResults") is not None:
        out["max_results"] = data["MaxResults"]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
