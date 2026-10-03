"""Generated from Smithy shape ``com.amazonaws.sagemaker#SearchTrainingPlanOfferingsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.training_plan_extension_offerings
    import capo_sagemaker.types.training_plan_offerings


class SearchTrainingPlanOfferingsResponse(TypedDict, closed=True):
    training_plan_offerings: NotRequired[
        "capo_sagemaker.types.training_plan_offerings.TrainingPlanOfferings"
    ]
    """<p>A list of training plan offerings that match the search criteria.</p>"""
    training_plan_extension_offerings: NotRequired[
        "capo_sagemaker.types.training_plan_extension_offerings.TrainingPlanExtensionOfferings"
    ]
    """<p>A list of extension offerings available for the specified training plan. These offerings can be used with the <code> <a href="https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ExtendTrainingPlan.html">ExtendTrainingPlan</a> </code> API to extend an existing training plan.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SearchTrainingPlanOfferingsResponse) -> dict:
    out: dict = {}
    if "training_plan_offerings" in value:
        import capo_sagemaker.types.training_plan_offerings

        out["TrainingPlanOfferings"] = (
            capo_sagemaker.types.training_plan_offerings.serialize_aws_json_1_1(
                value["training_plan_offerings"]
            )
        )
    if "training_plan_extension_offerings" in value:
        import capo_sagemaker.types.training_plan_extension_offerings

        out["TrainingPlanExtensionOfferings"] = (
            capo_sagemaker.types.training_plan_extension_offerings.serialize_aws_json_1_1(
                value["training_plan_extension_offerings"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> SearchTrainingPlanOfferingsResponse:
    out: SearchTrainingPlanOfferingsResponse = {}  # type: ignore[typeddict-item]
    if data.get("TrainingPlanOfferings") is not None:
        import capo_sagemaker.types.training_plan_offerings

        out["training_plan_offerings"] = (
            capo_sagemaker.types.training_plan_offerings.deserialize_aws_json_1_1(
                data["TrainingPlanOfferings"]
            )
        )
    if data.get("TrainingPlanExtensionOfferings") is not None:
        import capo_sagemaker.types.training_plan_extension_offerings

        out["training_plan_extension_offerings"] = (
            capo_sagemaker.types.training_plan_extension_offerings.deserialize_aws_json_1_1(
                data["TrainingPlanExtensionOfferings"]
            )
        )
    return out
