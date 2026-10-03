"""Generated from Smithy shape ``com.amazonaws.costoptimizationhub#UpdatePreferencesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cost_optimization_hub.types.member_account_discount_visibility
    import capo_cost_optimization_hub.types.preferred_commitment
    import capo_cost_optimization_hub.types.savings_estimation_mode


class UpdatePreferencesResponse(TypedDict, closed=True):
    savings_estimation_mode: NotRequired[
        "capo_cost_optimization_hub.types.savings_estimation_mode.SavingsEstimationMode"
    ]
    """<p>Shows the status of the "savings estimation mode" preference.</p>"""
    member_account_discount_visibility: NotRequired[
        "capo_cost_optimization_hub.types.member_account_discount_visibility.MemberAccountDiscountVisibility"
    ]
    """<p>Shows the status of the "member account discount visibility" preference.</p>"""
    preferred_commitment: NotRequired[
        "capo_cost_optimization_hub.types.preferred_commitment.PreferredCommitment"
    ]
    """<p>Shows the updated preferences for how Reserved Instances and Savings Plans cost-saving opportunities are prioritized in terms of payment option and term length.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: UpdatePreferencesResponse) -> dict:
    out: dict = {}
    if "savings_estimation_mode" in value:
        import capo_cost_optimization_hub.types.savings_estimation_mode

        out["savingsEstimationMode"] = (
            capo_cost_optimization_hub.types.savings_estimation_mode.serialize_aws_json_1_0(
                value["savings_estimation_mode"]
            )
        )
    if "member_account_discount_visibility" in value:
        import capo_cost_optimization_hub.types.member_account_discount_visibility

        out["memberAccountDiscountVisibility"] = (
            capo_cost_optimization_hub.types.member_account_discount_visibility.serialize_aws_json_1_0(
                value["member_account_discount_visibility"]
            )
        )
    if "preferred_commitment" in value:
        import capo_cost_optimization_hub.types.preferred_commitment

        out["preferredCommitment"] = (
            capo_cost_optimization_hub.types.preferred_commitment.serialize_aws_json_1_0(
                value["preferred_commitment"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> UpdatePreferencesResponse:
    out: UpdatePreferencesResponse = {}  # type: ignore[typeddict-item]
    if data.get("savingsEstimationMode") is not None:
        import capo_cost_optimization_hub.types.savings_estimation_mode

        out["savings_estimation_mode"] = (
            capo_cost_optimization_hub.types.savings_estimation_mode.deserialize_aws_json_1_0(
                data["savingsEstimationMode"]
            )
        )
    if data.get("memberAccountDiscountVisibility") is not None:
        import capo_cost_optimization_hub.types.member_account_discount_visibility

        out["member_account_discount_visibility"] = (
            capo_cost_optimization_hub.types.member_account_discount_visibility.deserialize_aws_json_1_0(
                data["memberAccountDiscountVisibility"]
            )
        )
    if data.get("preferredCommitment") is not None:
        import capo_cost_optimization_hub.types.preferred_commitment

        out["preferred_commitment"] = (
            capo_cost_optimization_hub.types.preferred_commitment.deserialize_aws_json_1_0(
                data["preferredCommitment"]
            )
        )
    return out
