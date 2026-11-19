"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#LambdaEffectiveRecommendationPreferences``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_compute_optimizer.types.lambda_savings_estimation_mode


class LambdaEffectiveRecommendationPreferences(TypedDict, closed=True):
    savings_estimation_mode: NotRequired[
        "capo_compute_optimizer.types.lambda_savings_estimation_mode.LambdaSavingsEstimationMode"
    ]
    """<p> Describes the savings estimation mode applied for calculating savings opportunity for Lambda functions. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: LambdaEffectiveRecommendationPreferences) -> dict:
    out: dict = {}
    if "savings_estimation_mode" in value:
        import capo_compute_optimizer.types.lambda_savings_estimation_mode

        out["savingsEstimationMode"] = (
            capo_compute_optimizer.types.lambda_savings_estimation_mode.serialize_aws_json_1_0(
                value["savings_estimation_mode"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> LambdaEffectiveRecommendationPreferences:
    out: LambdaEffectiveRecommendationPreferences = {}  # type: ignore[typeddict-item]
    if data.get("savingsEstimationMode") is not None:
        import capo_compute_optimizer.types.lambda_savings_estimation_mode

        out["savings_estimation_mode"] = (
            capo_compute_optimizer.types.lambda_savings_estimation_mode.deserialize_aws_json_1_0(
                data["savingsEstimationMode"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: LambdaEffectiveRecommendationPreferences) -> dict:
    out: dict = {}
    if "savings_estimation_mode" in value:
        import capo_compute_optimizer.types.lambda_savings_estimation_mode

        out["savingsEstimationMode"] = (
            capo_compute_optimizer.types.lambda_savings_estimation_mode.serialize_cbor(
                value["savings_estimation_mode"]
            )
        )
    return out


def deserialize_cbor(data: dict) -> LambdaEffectiveRecommendationPreferences:
    out: LambdaEffectiveRecommendationPreferences = {}  # type: ignore[typeddict-item]
    if data.get("savingsEstimationMode") is not None:
        import capo_compute_optimizer.types.lambda_savings_estimation_mode

        out["savings_estimation_mode"] = (
            capo_compute_optimizer.types.lambda_savings_estimation_mode.deserialize_cbor(
                data["savingsEstimationMode"]
            )
        )
    return out
