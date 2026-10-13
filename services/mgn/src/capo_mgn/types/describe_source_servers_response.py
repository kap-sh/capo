"""Generated from Smithy shape ``com.amazonaws.mgn#DescribeSourceServersResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mgn.types.pagination_token
    import capo_mgn.types.source_servers_list


class DescribeSourceServersResponse(TypedDict, closed=True):
    items: NotRequired["capo_mgn.types.source_servers_list.SourceServersList"]
    """<p>The list of returned Source Servers.</p>"""
    next_token: NotRequired["capo_mgn.types.pagination_token.PaginationToken"]
    """<p>The token of the next Source Server to retrieve.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeSourceServersResponse) -> dict:
    out: dict = {}
    if "items" in value:
        import capo_mgn.types.source_servers_list

        out["items"] = capo_mgn.types.source_servers_list.serialize_json(value["items"])
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> DescribeSourceServersResponse:
    out: DescribeSourceServersResponse = {}  # type: ignore[typeddict-item]
    if data.get("items") is not None:
        import capo_mgn.types.source_servers_list

        out["items"] = capo_mgn.types.source_servers_list.deserialize_json(
            data["items"]
        )
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out


def redact_sensitive(value: DescribeSourceServersResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "items" in value:
        import capo_mgn.types.source_servers_list

        out["items"] = capo_mgn.types.source_servers_list.redact_sensitive(
            value["items"]
        )
    return out
