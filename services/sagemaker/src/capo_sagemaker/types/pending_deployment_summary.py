"""Generated from Smithy shape ``com.amazonaws.sagemaker#PendingDeploymentSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.endpoint_config_name
    import capo_sagemaker.types.pending_production_variant_summary_list
    import capo_sagemaker.types.timestamp


class PendingDeploymentSummary(TypedDict, closed=True):
    endpoint_config_name: NotRequired[
        "capo_sagemaker.types.endpoint_config_name.EndpointConfigName"
    ]
    """<p>The name of the endpoint configuration used in the deployment. </p>"""
    production_variants: NotRequired[
        "capo_sagemaker.types.pending_production_variant_summary_list.PendingProductionVariantSummaryList"
    ]
    """<p>An array of <a href="https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_PendingProductionVariantSummary.html">PendingProductionVariantSummary</a> objects, one for each model hosted behind this endpoint for the in-progress deployment.</p>"""
    start_time: NotRequired["capo_sagemaker.types.timestamp.Timestamp"]
    """<p>The start time of the deployment.</p>"""
    shadow_production_variants: NotRequired[
        "capo_sagemaker.types.pending_production_variant_summary_list.PendingProductionVariantSummaryList"
    ]
    """<p>An array of <a href="https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_PendingProductionVariantSummary.html">PendingProductionVariantSummary</a> objects, one for each model hosted behind this endpoint in shadow mode with production traffic replicated from the model specified on <code>ProductionVariants</code> for the in-progress deployment.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PendingDeploymentSummary) -> dict:
    out: dict = {}
    if "endpoint_config_name" in value:
        out["EndpointConfigName"] = value["endpoint_config_name"]
    if "production_variants" in value:
        import capo_sagemaker.types.pending_production_variant_summary_list

        out["ProductionVariants"] = (
            capo_sagemaker.types.pending_production_variant_summary_list.serialize_aws_json_1_1(
                value["production_variants"]
            )
        )
    if "start_time" in value:
        import capo_sagemaker.types.timestamp

        out["StartTime"] = capo_sagemaker.types.timestamp.serialize_aws_json_1_1(
            value["start_time"]
        )
    if "shadow_production_variants" in value:
        import capo_sagemaker.types.pending_production_variant_summary_list

        out["ShadowProductionVariants"] = (
            capo_sagemaker.types.pending_production_variant_summary_list.serialize_aws_json_1_1(
                value["shadow_production_variants"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> PendingDeploymentSummary:
    out: PendingDeploymentSummary = {}  # type: ignore[typeddict-item]
    if data.get("EndpointConfigName") is not None:
        out["endpoint_config_name"] = data["EndpointConfigName"]
    if data.get("ProductionVariants") is not None:
        import capo_sagemaker.types.pending_production_variant_summary_list

        out["production_variants"] = (
            capo_sagemaker.types.pending_production_variant_summary_list.deserialize_aws_json_1_1(
                data["ProductionVariants"]
            )
        )
    if data.get("StartTime") is not None:
        import capo_sagemaker.types.timestamp

        out["start_time"] = capo_sagemaker.types.timestamp.deserialize_aws_json_1_1(
            data["StartTime"]
        )
    if data.get("ShadowProductionVariants") is not None:
        import capo_sagemaker.types.pending_production_variant_summary_list

        out["shadow_production_variants"] = (
            capo_sagemaker.types.pending_production_variant_summary_list.deserialize_aws_json_1_1(
                data["ShadowProductionVariants"]
            )
        )
    return out
