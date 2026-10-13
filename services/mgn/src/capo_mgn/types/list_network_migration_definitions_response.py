"""Generated from Smithy shape ``com.amazonaws.mgn#ListNetworkMigrationDefinitionsResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mgn.types.network_migration_definition_summaries_list
    import capo_mgn.types.pagination_token


class ListNetworkMigrationDefinitionsResponse(TypedDict, closed=True):
    items: NotRequired[
        "capo_mgn.types.network_migration_definition_summaries_list.NetworkMigrationDefinitionSummariesList"
    ]
    """<p>A list of network migration definition summaries.</p>"""
    next_token: NotRequired["capo_mgn.types.pagination_token.PaginationToken"]
    """<p>The token to use to retrieve the next page of results. This value is null when there are no more results to return.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListNetworkMigrationDefinitionsResponse) -> dict:
    out: dict = {}
    if "items" in value:
        import capo_mgn.types.network_migration_definition_summaries_list

        out["items"] = (
            capo_mgn.types.network_migration_definition_summaries_list.serialize_json(
                value["items"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListNetworkMigrationDefinitionsResponse:
    out: ListNetworkMigrationDefinitionsResponse = {}  # type: ignore[typeddict-item]
    if data.get("items") is not None:
        import capo_mgn.types.network_migration_definition_summaries_list

        out["items"] = (
            capo_mgn.types.network_migration_definition_summaries_list.deserialize_json(
                data["items"]
            )
        )
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out


def redact_sensitive(value: ListNetworkMigrationDefinitionsResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "items" in value:
        import capo_mgn.types.network_migration_definition_summaries_list

        out["items"] = (
            capo_mgn.types.network_migration_definition_summaries_list.redact_sensitive(
                value["items"]
            )
        )
    return out
