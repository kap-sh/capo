"""Generated from Smithy shape ``com.amazonaws.mgn#ListNetworkMigrationExecutionsResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mgn.types.network_migration_executions_list
    import capo_mgn.types.pagination_token


class ListNetworkMigrationExecutionsResponse(TypedDict, closed=True):
    items: NotRequired[
        "capo_mgn.types.network_migration_executions_list.NetworkMigrationExecutionsList"
    ]
    """<p>A list of network migration execution details.</p>"""
    next_token: NotRequired["capo_mgn.types.pagination_token.PaginationToken"]
    """<p>The token to use to retrieve the next page of results. This value is null when there are no more results to return.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListNetworkMigrationExecutionsResponse) -> dict:
    out: dict = {}
    if "items" in value:
        import capo_mgn.types.network_migration_executions_list

        out["items"] = capo_mgn.types.network_migration_executions_list.serialize_json(
            value["items"]
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListNetworkMigrationExecutionsResponse:
    out: ListNetworkMigrationExecutionsResponse = {}  # type: ignore[typeddict-item]
    if data.get("items") is not None:
        import capo_mgn.types.network_migration_executions_list

        out["items"] = (
            capo_mgn.types.network_migration_executions_list.deserialize_json(
                data["items"]
            )
        )
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out


def redact_sensitive(value: ListNetworkMigrationExecutionsResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "items" in value:
        import capo_mgn.types.network_migration_executions_list

        out["items"] = (
            capo_mgn.types.network_migration_executions_list.redact_sensitive(
                value["items"]
            )
        )
    return out
