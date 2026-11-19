"""Generated from Smithy shape ``com.amazonaws.computeoptimizerautomation#ListRecommendedActionSummariesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_compute_optimizer_automation.types.next_token
    import capo_compute_optimizer_automation.types.recommended_action_summaries


class ListRecommendedActionSummariesResponse(TypedDict, closed=True):
    recommended_action_summaries: NotRequired[
        "capo_compute_optimizer_automation.types.recommended_action_summaries.RecommendedActionSummaries"
    ]
    """<p> The summary of recommended actions that match the specified criteria. </p>"""
    next_token: NotRequired[
        "capo_compute_optimizer_automation.types.next_token.NextToken"
    ]
    """<p>A token used for pagination. If present, indicates there are more results available and can be used in subsequent requests.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListRecommendedActionSummariesResponse) -> dict:
    out: dict = {}
    if "recommended_action_summaries" in value:
        import capo_compute_optimizer_automation.types.recommended_action_summaries

        out["recommendedActionSummaries"] = (
            capo_compute_optimizer_automation.types.recommended_action_summaries.serialize_aws_json_1_0(
                value["recommended_action_summaries"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ListRecommendedActionSummariesResponse:
    out: ListRecommendedActionSummariesResponse = {}  # type: ignore[typeddict-item]
    if data.get("recommendedActionSummaries") is not None:
        import capo_compute_optimizer_automation.types.recommended_action_summaries

        out["recommended_action_summaries"] = (
            capo_compute_optimizer_automation.types.recommended_action_summaries.deserialize_aws_json_1_0(
                data["recommendedActionSummaries"]
            )
        )
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ListRecommendedActionSummariesResponse) -> dict:
    out: dict = {}
    if "recommended_action_summaries" in value:
        import capo_compute_optimizer_automation.types.recommended_action_summaries

        out["recommendedActionSummaries"] = (
            capo_compute_optimizer_automation.types.recommended_action_summaries.serialize_cbor(
                value["recommended_action_summaries"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_cbor(data: dict) -> ListRecommendedActionSummariesResponse:
    out: ListRecommendedActionSummariesResponse = {}  # type: ignore[typeddict-item]
    if data.get("recommendedActionSummaries") is not None:
        import capo_compute_optimizer_automation.types.recommended_action_summaries

        out["recommended_action_summaries"] = (
            capo_compute_optimizer_automation.types.recommended_action_summaries.deserialize_cbor(
                data["recommendedActionSummaries"]
            )
        )
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
