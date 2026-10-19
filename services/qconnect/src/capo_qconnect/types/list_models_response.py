"""Generated from Smithy shape ``com.amazonaws.qconnect#ListModelsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_qconnect.types.model_summary_list
    import capo_qconnect.types.next_token


class ListModelsResponse(TypedDict, closed=True):
    model_summaries: "capo_qconnect.types.model_summary_list.ModelSummaryList"
    """<p>The summaries of the models available to the assistant.</p>"""
    next_token: NotRequired["capo_qconnect.types.next_token.NextToken"]
    """<p>If there are additional results, this is the token for the next set of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListModelsResponse) -> dict:
    out: dict = {}
    import capo_qconnect.types.model_summary_list

    out["modelSummaries"] = capo_qconnect.types.model_summary_list.serialize_json(
        value["model_summaries"]
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListModelsResponse:
    out: ListModelsResponse = {}  # type: ignore[typeddict-item]
    if data.get("modelSummaries") is not None:
        import capo_qconnect.types.model_summary_list

        out["model_summaries"] = (
            capo_qconnect.types.model_summary_list.deserialize_json(
                data["modelSummaries"]
            )
        )
    else:
        out["model_summaries"] = []
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
