"""Generated from Smithy shape ``com.amazonaws.drs#ListExtensibleSourceServersResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_drs.types.pagination_token
    import capo_drs.types.staging_source_servers_list


class ListExtensibleSourceServersResponse(TypedDict, closed=True):
    items: NotRequired[
        "capo_drs.types.staging_source_servers_list.StagingSourceServersList"
    ]
    """<p>A list of source servers on a staging Account that are extensible.</p>"""
    next_token: NotRequired["capo_drs.types.pagination_token.PaginationToken"]
    """<p>The token of the next extensible source server to retrieve.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListExtensibleSourceServersResponse) -> dict:
    out: dict = {}
    if "items" in value:
        import capo_drs.types.staging_source_servers_list

        out["items"] = capo_drs.types.staging_source_servers_list.serialize_json(
            value["items"]
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListExtensibleSourceServersResponse:
    out: ListExtensibleSourceServersResponse = {}  # type: ignore[typeddict-item]
    if data.get("items") is not None:
        import capo_drs.types.staging_source_servers_list

        out["items"] = capo_drs.types.staging_source_servers_list.deserialize_json(
            data["items"]
        )
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out


def redact_sensitive(value: ListExtensibleSourceServersResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "items" in value:
        import capo_drs.types.staging_source_servers_list

        out["items"] = capo_drs.types.staging_source_servers_list.redact_sensitive(
            value["items"]
        )
    return out
