"""Generated from Smithy shape ``com.amazonaws.sagemaker#DescribeEndpointOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.async_inference_config
    import capo_sagemaker.types.data_capture_config_summary
    import capo_sagemaker.types.deployment_config
    import capo_sagemaker.types.endpoint_arn
    import capo_sagemaker.types.endpoint_config_name
    import capo_sagemaker.types.endpoint_name
    import capo_sagemaker.types.endpoint_status
    import capo_sagemaker.types.explainer_config
    import capo_sagemaker.types.failure_reason
    import capo_sagemaker.types.metrics_config
    import capo_sagemaker.types.pending_deployment_summary
    import capo_sagemaker.types.production_variant_summary_list
    import capo_sagemaker.types.timestamp


class DescribeEndpointOutput(TypedDict, closed=True):
    endpoint_name: NotRequired["capo_sagemaker.types.endpoint_name.EndpointName"]
    """<p>Name of the endpoint.</p>"""
    endpoint_arn: NotRequired["capo_sagemaker.types.endpoint_arn.EndpointArn"]
    """<p>The Amazon Resource Name (ARN) of the endpoint.</p>"""
    endpoint_config_name: NotRequired[
        "capo_sagemaker.types.endpoint_config_name.EndpointConfigName"
    ]
    """<p>The name of the endpoint configuration associated with this endpoint.</p>"""
    production_variants: NotRequired[
        "capo_sagemaker.types.production_variant_summary_list.ProductionVariantSummaryList"
    ]
    """<p>An array of <a href="https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ProductionVariantSummary.html">ProductionVariantSummary</a> objects, one for each model hosted behind this endpoint.</p>"""
    data_capture_config: NotRequired[
        "capo_sagemaker.types.data_capture_config_summary.DataCaptureConfigSummary"
    ]
    endpoint_status: NotRequired["capo_sagemaker.types.endpoint_status.EndpointStatus"]
    """<p>The status of the endpoint.</p> <ul> <li> <p> <code>OutOfService</code>: Endpoint is not available to take incoming requests.</p> </li> <li> <p> <code>Creating</code>: <a href="https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateEndpoint.html">CreateEndpoint</a> is executing.</p> </li> <li> <p> <code>Updating</code>: <a href="https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_UpdateEndpoint.html">UpdateEndpoint</a> or <a href="https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_UpdateEndpointWeightsAndCapacities.html">UpdateEndpointWeightsAndCapacities</a> is executing.</p> </li> <li> <p> <code>SystemUpdating</code>: Endpoint is undergoing maintenance and cannot be updated or deleted or re-scaled until it has completed. This maintenance operation does not change any customer-specified values such as VPC config, KMS encryption, model, instance type, or instance count.</p> </li> <li> <p> <code>RollingBack</code>: Endpoint fails to scale up or down or change its variant weight and is in the process of rolling back to its previous configuration. Once the rollback completes, endpoint returns to an <code>InService</code> status. This transitional status only applies to an endpoint that has autoscaling enabled and is undergoing variant weight or capacity changes as part of an <a href="https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_UpdateEndpointWeightsAndCapacities.html">UpdateEndpointWeightsAndCapacities</a> call or when the <a href="https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_UpdateEndpointWeightsAndCapacities.html">UpdateEndpointWeightsAndCapacities</a> operation is called explicitly.</p> </li> <li> <p> <code>InService</code>: Endpoint is available to process incoming requests.</p> </li> <li> <p> <code>Deleting</code>: <a href="https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DeleteEndpoint.html">DeleteEndpoint</a> is executing.</p> </li> <li> <p> <code>Failed</code>: Endpoint could not be created, updated, or re-scaled. Use the <code>FailureReason</code> value returned by <a href="https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DescribeEndpoint.html">DescribeEndpoint</a> for information about the failure. <a href="https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DeleteEndpoint.html">DeleteEndpoint</a> is the only operation that can be performed on a failed endpoint.</p> </li> <li> <p> <code>UpdateRollbackFailed</code>: Both the rolling deployment and auto-rollback failed. Your endpoint is in service with a mix of the old and new endpoint configurations. For information about how to remedy this issue and restore the endpoint's status to <code>InService</code>, see <a href="https://docs.aws.amazon.com/sagemaker/latest/dg/deployment-guardrails-rolling.html">Rolling Deployments</a>.</p> </li> </ul>"""
    failure_reason: NotRequired["capo_sagemaker.types.failure_reason.FailureReason"]
    """<p>If the status of the endpoint is <code>Failed</code>, the reason why it failed. </p>"""
    creation_time: NotRequired["capo_sagemaker.types.timestamp.Timestamp"]
    """<p>A timestamp that shows when the endpoint was created.</p>"""
    last_modified_time: NotRequired["capo_sagemaker.types.timestamp.Timestamp"]
    """<p>A timestamp that shows when the endpoint was last modified.</p>"""
    last_deployment_config: NotRequired[
        "capo_sagemaker.types.deployment_config.DeploymentConfig"
    ]
    """<p>The most recent deployment configuration for the endpoint.</p>"""
    async_inference_config: NotRequired[
        "capo_sagemaker.types.async_inference_config.AsyncInferenceConfig"
    ]
    """<p>Returns the description of an endpoint configuration created using the <a href="https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateEndpointConfig.html"> <code>CreateEndpointConfig</code> </a> API.</p>"""
    pending_deployment_summary: NotRequired[
        "capo_sagemaker.types.pending_deployment_summary.PendingDeploymentSummary"
    ]
    """<p>Returns the summary of an in-progress deployment. This field is only returned when the endpoint is creating or updating with a new endpoint configuration.</p>"""
    explainer_config: NotRequired[
        "capo_sagemaker.types.explainer_config.ExplainerConfig"
    ]
    """<p>The configuration parameters for an explainer.</p>"""
    shadow_production_variants: NotRequired[
        "capo_sagemaker.types.production_variant_summary_list.ProductionVariantSummaryList"
    ]
    """<p>An array of <a href="https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ProductionVariantSummary.html">ProductionVariantSummary</a> objects, one for each model that you want to host at this endpoint in shadow mode with production traffic replicated from the model specified on <code>ProductionVariants</code>.</p>"""
    metrics_config: NotRequired["capo_sagemaker.types.metrics_config.MetricsConfig"]
    """<p>The configuration parameters for utilization metrics.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeEndpointOutput) -> dict:
    out: dict = {}
    if "endpoint_name" in value:
        out["EndpointName"] = value["endpoint_name"]
    if "endpoint_arn" in value:
        out["EndpointArn"] = value["endpoint_arn"]
    if "endpoint_config_name" in value:
        out["EndpointConfigName"] = value["endpoint_config_name"]
    if "production_variants" in value:
        import capo_sagemaker.types.production_variant_summary_list

        out["ProductionVariants"] = (
            capo_sagemaker.types.production_variant_summary_list.serialize_aws_json_1_1(
                value["production_variants"]
            )
        )
    if "data_capture_config" in value:
        import capo_sagemaker.types.data_capture_config_summary

        out["DataCaptureConfig"] = (
            capo_sagemaker.types.data_capture_config_summary.serialize_aws_json_1_1(
                value["data_capture_config"]
            )
        )
    if "endpoint_status" in value:
        import capo_sagemaker.types.endpoint_status

        out["EndpointStatus"] = (
            capo_sagemaker.types.endpoint_status.serialize_aws_json_1_1(
                value["endpoint_status"]
            )
        )
    if "failure_reason" in value:
        out["FailureReason"] = value["failure_reason"]
    if "creation_time" in value:
        import capo_sagemaker.types.timestamp

        out["CreationTime"] = capo_sagemaker.types.timestamp.serialize_aws_json_1_1(
            value["creation_time"]
        )
    if "last_modified_time" in value:
        import capo_sagemaker.types.timestamp

        out["LastModifiedTime"] = capo_sagemaker.types.timestamp.serialize_aws_json_1_1(
            value["last_modified_time"]
        )
    if "last_deployment_config" in value:
        import capo_sagemaker.types.deployment_config

        out["LastDeploymentConfig"] = (
            capo_sagemaker.types.deployment_config.serialize_aws_json_1_1(
                value["last_deployment_config"]
            )
        )
    if "async_inference_config" in value:
        import capo_sagemaker.types.async_inference_config

        out["AsyncInferenceConfig"] = (
            capo_sagemaker.types.async_inference_config.serialize_aws_json_1_1(
                value["async_inference_config"]
            )
        )
    if "pending_deployment_summary" in value:
        import capo_sagemaker.types.pending_deployment_summary

        out["PendingDeploymentSummary"] = (
            capo_sagemaker.types.pending_deployment_summary.serialize_aws_json_1_1(
                value["pending_deployment_summary"]
            )
        )
    if "explainer_config" in value:
        import capo_sagemaker.types.explainer_config

        out["ExplainerConfig"] = (
            capo_sagemaker.types.explainer_config.serialize_aws_json_1_1(
                value["explainer_config"]
            )
        )
    if "shadow_production_variants" in value:
        import capo_sagemaker.types.production_variant_summary_list

        out["ShadowProductionVariants"] = (
            capo_sagemaker.types.production_variant_summary_list.serialize_aws_json_1_1(
                value["shadow_production_variants"]
            )
        )
    if "metrics_config" in value:
        import capo_sagemaker.types.metrics_config

        out["MetricsConfig"] = (
            capo_sagemaker.types.metrics_config.serialize_aws_json_1_1(
                value["metrics_config"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeEndpointOutput:
    out: DescribeEndpointOutput = {}  # type: ignore[typeddict-item]
    if data.get("EndpointName") is not None:
        out["endpoint_name"] = data["EndpointName"]
    if data.get("EndpointArn") is not None:
        out["endpoint_arn"] = data["EndpointArn"]
    if data.get("EndpointConfigName") is not None:
        out["endpoint_config_name"] = data["EndpointConfigName"]
    if data.get("ProductionVariants") is not None:
        import capo_sagemaker.types.production_variant_summary_list

        out["production_variants"] = (
            capo_sagemaker.types.production_variant_summary_list.deserialize_aws_json_1_1(
                data["ProductionVariants"]
            )
        )
    if data.get("DataCaptureConfig") is not None:
        import capo_sagemaker.types.data_capture_config_summary

        out["data_capture_config"] = (
            capo_sagemaker.types.data_capture_config_summary.deserialize_aws_json_1_1(
                data["DataCaptureConfig"]
            )
        )
    if data.get("EndpointStatus") is not None:
        import capo_sagemaker.types.endpoint_status

        out["endpoint_status"] = (
            capo_sagemaker.types.endpoint_status.deserialize_aws_json_1_1(
                data["EndpointStatus"]
            )
        )
    if data.get("FailureReason") is not None:
        out["failure_reason"] = data["FailureReason"]
    if data.get("CreationTime") is not None:
        import capo_sagemaker.types.timestamp

        out["creation_time"] = capo_sagemaker.types.timestamp.deserialize_aws_json_1_1(
            data["CreationTime"]
        )
    if data.get("LastModifiedTime") is not None:
        import capo_sagemaker.types.timestamp

        out["last_modified_time"] = (
            capo_sagemaker.types.timestamp.deserialize_aws_json_1_1(
                data["LastModifiedTime"]
            )
        )
    if data.get("LastDeploymentConfig") is not None:
        import capo_sagemaker.types.deployment_config

        out["last_deployment_config"] = (
            capo_sagemaker.types.deployment_config.deserialize_aws_json_1_1(
                data["LastDeploymentConfig"]
            )
        )
    if data.get("AsyncInferenceConfig") is not None:
        import capo_sagemaker.types.async_inference_config

        out["async_inference_config"] = (
            capo_sagemaker.types.async_inference_config.deserialize_aws_json_1_1(
                data["AsyncInferenceConfig"]
            )
        )
    if data.get("PendingDeploymentSummary") is not None:
        import capo_sagemaker.types.pending_deployment_summary

        out["pending_deployment_summary"] = (
            capo_sagemaker.types.pending_deployment_summary.deserialize_aws_json_1_1(
                data["PendingDeploymentSummary"]
            )
        )
    if data.get("ExplainerConfig") is not None:
        import capo_sagemaker.types.explainer_config

        out["explainer_config"] = (
            capo_sagemaker.types.explainer_config.deserialize_aws_json_1_1(
                data["ExplainerConfig"]
            )
        )
    if data.get("ShadowProductionVariants") is not None:
        import capo_sagemaker.types.production_variant_summary_list

        out["shadow_production_variants"] = (
            capo_sagemaker.types.production_variant_summary_list.deserialize_aws_json_1_1(
                data["ShadowProductionVariants"]
            )
        )
    if data.get("MetricsConfig") is not None:
        import capo_sagemaker.types.metrics_config

        out["metrics_config"] = (
            capo_sagemaker.types.metrics_config.deserialize_aws_json_1_1(
                data["MetricsConfig"]
            )
        )
    return out
