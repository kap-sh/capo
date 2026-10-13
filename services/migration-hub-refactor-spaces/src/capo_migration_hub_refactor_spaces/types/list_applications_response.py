"""Generated from Smithy shape ``com.amazonaws.migrationhubrefactorspaces#ListApplicationsResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_migration_hub_refactor_spaces.types.application_summaries
    import capo_migration_hub_refactor_spaces.types.next_token


class ListApplicationsResponse(TypedDict, closed=True):
    application_summary_list: NotRequired[
        "capo_migration_hub_refactor_spaces.types.application_summaries.ApplicationSummaries"
    ]
    """<p>The list of <code>ApplicationSummary</code> objects. </p>"""
    next_token: NotRequired[
        "capo_migration_hub_refactor_spaces.types.next_token.NextToken"
    ]
    """<p>The token for the next page of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListApplicationsResponse) -> dict:
    out: dict = {}
    if "application_summary_list" in value:
        import capo_migration_hub_refactor_spaces.types.application_summaries

        out["ApplicationSummaryList"] = (
            capo_migration_hub_refactor_spaces.types.application_summaries.serialize_json(
                value["application_summary_list"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListApplicationsResponse:
    out: ListApplicationsResponse = {}  # type: ignore[typeddict-item]
    if data.get("ApplicationSummaryList") is not None:
        import capo_migration_hub_refactor_spaces.types.application_summaries

        out["application_summary_list"] = (
            capo_migration_hub_refactor_spaces.types.application_summaries.deserialize_json(
                data["ApplicationSummaryList"]
            )
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out


def redact_sensitive(value: ListApplicationsResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "application_summary_list" in value:
        import capo_migration_hub_refactor_spaces.types.application_summaries

        out["application_summary_list"] = (
            capo_migration_hub_refactor_spaces.types.application_summaries.redact_sensitive(
                value["application_summary_list"]
            )
        )
    return out
