"""Generated from Smithy shape ``com.amazonaws.observabilityadmin#ListDatasetIntegrationsOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_observabilityadmin.types.dataset_integration_summaries
    import capo_observabilityadmin.types.next_token


class ListDatasetIntegrationsOutput(TypedDict, closed=True):
    dataset_integration_summaries: "capo_observabilityadmin.types.dataset_integration_summaries.DatasetIntegrationSummaries"
    """<p>The dataset integrations in your account.</p>"""
    next_token: NotRequired["capo_observabilityadmin.types.next_token.NextToken"]
    """<p>A token to resume pagination of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListDatasetIntegrationsOutput) -> dict:
    out: dict = {}
    import capo_observabilityadmin.types.dataset_integration_summaries

    out["DatasetIntegrationSummaries"] = (
        capo_observabilityadmin.types.dataset_integration_summaries.serialize_json(
            value["dataset_integration_summaries"]
        )
    )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListDatasetIntegrationsOutput:
    out: ListDatasetIntegrationsOutput = {}  # type: ignore[typeddict-item]
    if data.get("DatasetIntegrationSummaries") is not None:
        import capo_observabilityadmin.types.dataset_integration_summaries

        out["dataset_integration_summaries"] = (
            capo_observabilityadmin.types.dataset_integration_summaries.deserialize_json(
                data["DatasetIntegrationSummaries"]
            )
        )
    else:
        out["dataset_integration_summaries"] = []
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
