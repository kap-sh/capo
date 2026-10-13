"""Generated from Smithy shape ``com.amazonaws.migrationhubrefactorspaces#ListServicesResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_migration_hub_refactor_spaces.types.next_token
    import capo_migration_hub_refactor_spaces.types.service_summaries


class ListServicesResponse(TypedDict, closed=True):
    service_summary_list: NotRequired[
        "capo_migration_hub_refactor_spaces.types.service_summaries.ServiceSummaries"
    ]
    """<p> The list of <code>ServiceSummary</code> objects. </p>"""
    next_token: NotRequired[
        "capo_migration_hub_refactor_spaces.types.next_token.NextToken"
    ]
    """<p>The token for the next page of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListServicesResponse) -> dict:
    out: dict = {}
    if "service_summary_list" in value:
        import capo_migration_hub_refactor_spaces.types.service_summaries

        out["ServiceSummaryList"] = (
            capo_migration_hub_refactor_spaces.types.service_summaries.serialize_json(
                value["service_summary_list"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListServicesResponse:
    out: ListServicesResponse = {}  # type: ignore[typeddict-item]
    if data.get("ServiceSummaryList") is not None:
        import capo_migration_hub_refactor_spaces.types.service_summaries

        out["service_summary_list"] = (
            capo_migration_hub_refactor_spaces.types.service_summaries.deserialize_json(
                data["ServiceSummaryList"]
            )
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out


def redact_sensitive(value: ListServicesResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "service_summary_list" in value:
        import capo_migration_hub_refactor_spaces.types.service_summaries

        out["service_summary_list"] = (
            capo_migration_hub_refactor_spaces.types.service_summaries.redact_sensitive(
                value["service_summary_list"]
            )
        )
    return out
