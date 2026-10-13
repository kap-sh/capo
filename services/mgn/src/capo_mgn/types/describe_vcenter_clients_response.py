"""Generated from Smithy shape ``com.amazonaws.mgn#DescribeVcenterClientsResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mgn.types.pagination_token
    import capo_mgn.types.vcenter_client_list


class DescribeVcenterClientsResponse(TypedDict, closed=True):
    items: NotRequired["capo_mgn.types.vcenter_client_list.VcenterClientList"]
    """<p>List of items returned by DescribeVcenterClients.</p>"""
    next_token: NotRequired["capo_mgn.types.pagination_token.PaginationToken"]
    """<p>Next pagination token returned from DescribeVcenterClients.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeVcenterClientsResponse) -> dict:
    out: dict = {}
    if "items" in value:
        import capo_mgn.types.vcenter_client_list

        out["items"] = capo_mgn.types.vcenter_client_list.serialize_json(value["items"])
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> DescribeVcenterClientsResponse:
    out: DescribeVcenterClientsResponse = {}  # type: ignore[typeddict-item]
    if data.get("items") is not None:
        import capo_mgn.types.vcenter_client_list

        out["items"] = capo_mgn.types.vcenter_client_list.deserialize_json(
            data["items"]
        )
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out


def redact_sensitive(value: DescribeVcenterClientsResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "items" in value:
        import capo_mgn.types.vcenter_client_list

        out["items"] = capo_mgn.types.vcenter_client_list.redact_sensitive(
            value["items"]
        )
    return out
