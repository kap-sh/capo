"""Generated from Smithy shape ``com.amazonaws.migrationhubrefactorspaces#ListRoutesResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_migration_hub_refactor_spaces.types.next_token
    import capo_migration_hub_refactor_spaces.types.route_summaries


class ListRoutesResponse(TypedDict, closed=True):
    route_summary_list: NotRequired[
        "capo_migration_hub_refactor_spaces.types.route_summaries.RouteSummaries"
    ]
    """<p>The list of <code>RouteSummary</code> objects. </p>"""
    next_token: NotRequired[
        "capo_migration_hub_refactor_spaces.types.next_token.NextToken"
    ]
    """<p>The token for the next page of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListRoutesResponse) -> dict:
    out: dict = {}
    if "route_summary_list" in value:
        import capo_migration_hub_refactor_spaces.types.route_summaries

        out["RouteSummaryList"] = (
            capo_migration_hub_refactor_spaces.types.route_summaries.serialize_json(
                value["route_summary_list"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListRoutesResponse:
    out: ListRoutesResponse = {}  # type: ignore[typeddict-item]
    if data.get("RouteSummaryList") is not None:
        import capo_migration_hub_refactor_spaces.types.route_summaries

        out["route_summary_list"] = (
            capo_migration_hub_refactor_spaces.types.route_summaries.deserialize_json(
                data["RouteSummaryList"]
            )
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out


def redact_sensitive(value: ListRoutesResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "route_summary_list" in value:
        import capo_migration_hub_refactor_spaces.types.route_summaries

        out["route_summary_list"] = (
            capo_migration_hub_refactor_spaces.types.route_summaries.redact_sensitive(
                value["route_summary_list"]
            )
        )
    return out
