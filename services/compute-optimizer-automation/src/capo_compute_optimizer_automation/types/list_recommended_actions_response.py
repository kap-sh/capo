"""Generated from Smithy shape ``com.amazonaws.computeoptimizerautomation#ListRecommendedActionsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_compute_optimizer_automation.types.next_token
    import capo_compute_optimizer_automation.types.recommended_actions


class ListRecommendedActionsResponse(TypedDict, closed=True):
    recommended_actions: NotRequired[
        "capo_compute_optimizer_automation.types.recommended_actions.RecommendedActions"
    ]
    """<p> The list of recommended actions that match the specified criteria. </p>"""
    next_token: NotRequired[
        "capo_compute_optimizer_automation.types.next_token.NextToken"
    ]
    """<p>A token used for pagination. If present, indicates there are more results available and can be used in subsequent requests.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListRecommendedActionsResponse) -> dict:
    out: dict = {}
    if "recommended_actions" in value:
        import capo_compute_optimizer_automation.types.recommended_actions

        out["recommendedActions"] = (
            capo_compute_optimizer_automation.types.recommended_actions.serialize_aws_json_1_0(
                value["recommended_actions"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ListRecommendedActionsResponse:
    out: ListRecommendedActionsResponse = {}  # type: ignore[typeddict-item]
    if data.get("recommendedActions") is not None:
        import capo_compute_optimizer_automation.types.recommended_actions

        out["recommended_actions"] = (
            capo_compute_optimizer_automation.types.recommended_actions.deserialize_aws_json_1_0(
                data["recommendedActions"]
            )
        )
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ListRecommendedActionsResponse) -> dict:
    out: dict = {}
    if "recommended_actions" in value:
        import capo_compute_optimizer_automation.types.recommended_actions

        out["recommendedActions"] = (
            capo_compute_optimizer_automation.types.recommended_actions.serialize_cbor(
                value["recommended_actions"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_cbor(data: dict) -> ListRecommendedActionsResponse:
    out: ListRecommendedActionsResponse = {}  # type: ignore[typeddict-item]
    if data.get("recommendedActions") is not None:
        import capo_compute_optimizer_automation.types.recommended_actions

        out["recommended_actions"] = (
            capo_compute_optimizer_automation.types.recommended_actions.deserialize_cbor(
                data["recommendedActions"]
            )
        )
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
