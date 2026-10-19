"""Generated from Smithy shape ``com.amazonaws.iotsitewise#ListComputationModelDataBindingUsagesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iotsitewise.types.computation_model_data_binding_usage_summaries
    import capo_iotsitewise.types.next_token


class ListComputationModelDataBindingUsagesResponse(TypedDict, closed=True):
    data_binding_usage_summaries: "capo_iotsitewise.types.computation_model_data_binding_usage_summaries.ComputationModelDataBindingUsageSummaries"
    """<p>A list of summaries describing the data binding usages across computation models. Each summary includes the computation model IDs and the matched data binding details.</p>"""
    next_token: NotRequired["capo_iotsitewise.types.next_token.NextToken"]
    """<p>The token for the next set of paginated results, or null if there are no additional results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListComputationModelDataBindingUsagesResponse) -> dict:
    out: dict = {}
    import capo_iotsitewise.types.computation_model_data_binding_usage_summaries

    out["dataBindingUsageSummaries"] = (
        capo_iotsitewise.types.computation_model_data_binding_usage_summaries.serialize_json(
            value["data_binding_usage_summaries"]
        )
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListComputationModelDataBindingUsagesResponse:
    out: ListComputationModelDataBindingUsagesResponse = {}  # type: ignore[typeddict-item]
    if data.get("dataBindingUsageSummaries") is not None:
        import capo_iotsitewise.types.computation_model_data_binding_usage_summaries

        out["data_binding_usage_summaries"] = (
            capo_iotsitewise.types.computation_model_data_binding_usage_summaries.deserialize_json(
                data["dataBindingUsageSummaries"]
            )
        )
    else:
        out["data_binding_usage_summaries"] = []
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
