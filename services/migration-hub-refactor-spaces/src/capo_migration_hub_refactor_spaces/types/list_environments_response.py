"""Generated from Smithy shape ``com.amazonaws.migrationhubrefactorspaces#ListEnvironmentsResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_migration_hub_refactor_spaces.types.environment_summaries
    import capo_migration_hub_refactor_spaces.types.next_token


class ListEnvironmentsResponse(TypedDict, closed=True):
    environment_summary_list: NotRequired[
        "capo_migration_hub_refactor_spaces.types.environment_summaries.EnvironmentSummaries"
    ]
    """<p>The list of <code>EnvironmentSummary</code> objects. </p>"""
    next_token: NotRequired[
        "capo_migration_hub_refactor_spaces.types.next_token.NextToken"
    ]
    """<p>The token for the next page of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListEnvironmentsResponse) -> dict:
    out: dict = {}
    if "environment_summary_list" in value:
        import capo_migration_hub_refactor_spaces.types.environment_summaries

        out["EnvironmentSummaryList"] = (
            capo_migration_hub_refactor_spaces.types.environment_summaries.serialize_json(
                value["environment_summary_list"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListEnvironmentsResponse:
    out: ListEnvironmentsResponse = {}  # type: ignore[typeddict-item]
    if data.get("EnvironmentSummaryList") is not None:
        import capo_migration_hub_refactor_spaces.types.environment_summaries

        out["environment_summary_list"] = (
            capo_migration_hub_refactor_spaces.types.environment_summaries.deserialize_json(
                data["EnvironmentSummaryList"]
            )
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out


def redact_sensitive(value: ListEnvironmentsResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "environment_summary_list" in value:
        import capo_migration_hub_refactor_spaces.types.environment_summaries

        out["environment_summary_list"] = (
            capo_migration_hub_refactor_spaces.types.environment_summaries.redact_sensitive(
                value["environment_summary_list"]
            )
        )
    return out
