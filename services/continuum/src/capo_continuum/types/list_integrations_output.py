"""Generated from Smithy shape ``com.amazonaws.continuum#ListIntegrationsOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_continuum.types.integration_summaries
    import capo_continuum.types.next_token


class ListIntegrationsOutput(TypedDict, closed=True):
    items: "capo_continuum.types.integration_summaries.IntegrationSummaries"
    """The integrations in the account, ordered by integrationId descending."""
    next_token: NotRequired["capo_continuum.types.next_token.NextToken"]
    """A pagination token to retrieve the next page of results. Absent when there are no more results."""


# --- restJson1 ser/de ---
def serialize_json(value: ListIntegrationsOutput) -> dict:
    out: dict = {}
    import capo_continuum.types.integration_summaries

    out["items"] = capo_continuum.types.integration_summaries.serialize_json(
        value["items"]
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListIntegrationsOutput:
    out: ListIntegrationsOutput = {}  # type: ignore[typeddict-item]
    if data.get("items") is not None:
        import capo_continuum.types.integration_summaries

        out["items"] = capo_continuum.types.integration_summaries.deserialize_json(
            data["items"]
        )
    else:
        out["items"] = []
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
