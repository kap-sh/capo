"""Generated from Smithy shape ``com.amazonaws.sagemaker#DescribeEndpointConfigOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.async_inference_config
    import capo_sagemaker.types.boolean
    import capo_sagemaker.types.data_capture_config
    import capo_sagemaker.types.endpoint_config_arn
    import capo_sagemaker.types.endpoint_config_name
    import capo_sagemaker.types.explainer_config
    import capo_sagemaker.types.kms_key_id
    import capo_sagemaker.types.metrics_config
    import capo_sagemaker.types.production_variant_list
    import capo_sagemaker.types.role_arn
    import capo_sagemaker.types.timestamp
    import capo_sagemaker.types.vpc_config


class DescribeEndpointConfigOutput(TypedDict, closed=True):
    endpoint_config_name: NotRequired[
        "capo_sagemaker.types.endpoint_config_name.EndpointConfigName"
    ]
    """<p>Name of the SageMaker endpoint configuration.</p>"""
    endpoint_config_arn: NotRequired[
        "capo_sagemaker.types.endpoint_config_arn.EndpointConfigArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the endpoint configuration.</p>"""
    production_variants: NotRequired[
        "capo_sagemaker.types.production_variant_list.ProductionVariantList"
    ]
    """<p>An array of <code>ProductionVariant</code> objects, one for each model that you want to host at this endpoint.</p>"""
    data_capture_config: NotRequired[
        "capo_sagemaker.types.data_capture_config.DataCaptureConfig"
    ]
    kms_key_id: NotRequired["capo_sagemaker.types.kms_key_id.KmsKeyId"]
    """<p>Amazon Web Services KMS key ID Amazon SageMaker uses to encrypt data when storing it on the ML storage volume attached to the instance.</p>"""
    creation_time: NotRequired["capo_sagemaker.types.timestamp.Timestamp"]
    """<p>A timestamp that shows when the endpoint configuration was created.</p>"""
    async_inference_config: NotRequired[
        "capo_sagemaker.types.async_inference_config.AsyncInferenceConfig"
    ]
    """<p>Returns the description of an endpoint configuration created using the <a href="https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateEndpointConfig.html"> <code>CreateEndpointConfig</code> </a> API.</p>"""
    explainer_config: NotRequired[
        "capo_sagemaker.types.explainer_config.ExplainerConfig"
    ]
    """<p>The configuration parameters for an explainer.</p>"""
    shadow_production_variants: NotRequired[
        "capo_sagemaker.types.production_variant_list.ProductionVariantList"
    ]
    """<p>An array of <code>ProductionVariant</code> objects, one for each model that you want to host at this endpoint in shadow mode with production traffic replicated from the model specified on <code>ProductionVariants</code>.</p>"""
    execution_role_arn: NotRequired["capo_sagemaker.types.role_arn.RoleArn"]
    """<p>The Amazon Resource Name (ARN) of the IAM role that you assigned to the endpoint configuration.</p>"""
    vpc_config: NotRequired["capo_sagemaker.types.vpc_config.VpcConfig"]
    enable_network_isolation: NotRequired["capo_sagemaker.types.boolean.Boolean"]
    """<p>Indicates whether all model containers deployed to the endpoint are isolated. If they are, no inbound or outbound network calls can be made to or from the model containers.</p>"""
    metrics_config: NotRequired["capo_sagemaker.types.metrics_config.MetricsConfig"]
    """<p>The configuration parameters for utilization metrics.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeEndpointConfigOutput) -> dict:
    out: dict = {}
    if "endpoint_config_name" in value:
        out["EndpointConfigName"] = value["endpoint_config_name"]
    if "endpoint_config_arn" in value:
        out["EndpointConfigArn"] = value["endpoint_config_arn"]
    if "production_variants" in value:
        import capo_sagemaker.types.production_variant_list

        out["ProductionVariants"] = (
            capo_sagemaker.types.production_variant_list.serialize_aws_json_1_1(
                value["production_variants"]
            )
        )
    if "data_capture_config" in value:
        import capo_sagemaker.types.data_capture_config

        out["DataCaptureConfig"] = (
            capo_sagemaker.types.data_capture_config.serialize_aws_json_1_1(
                value["data_capture_config"]
            )
        )
    if "kms_key_id" in value:
        out["KmsKeyId"] = value["kms_key_id"]
    if "creation_time" in value:
        import capo_sagemaker.types.timestamp

        out["CreationTime"] = capo_sagemaker.types.timestamp.serialize_aws_json_1_1(
            value["creation_time"]
        )
    if "async_inference_config" in value:
        import capo_sagemaker.types.async_inference_config

        out["AsyncInferenceConfig"] = (
            capo_sagemaker.types.async_inference_config.serialize_aws_json_1_1(
                value["async_inference_config"]
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
        import capo_sagemaker.types.production_variant_list

        out["ShadowProductionVariants"] = (
            capo_sagemaker.types.production_variant_list.serialize_aws_json_1_1(
                value["shadow_production_variants"]
            )
        )
    if "execution_role_arn" in value:
        out["ExecutionRoleArn"] = value["execution_role_arn"]
    if "vpc_config" in value:
        import capo_sagemaker.types.vpc_config

        out["VpcConfig"] = capo_sagemaker.types.vpc_config.serialize_aws_json_1_1(
            value["vpc_config"]
        )
    if "enable_network_isolation" in value:
        out["EnableNetworkIsolation"] = value["enable_network_isolation"]
    if "metrics_config" in value:
        import capo_sagemaker.types.metrics_config

        out["MetricsConfig"] = (
            capo_sagemaker.types.metrics_config.serialize_aws_json_1_1(
                value["metrics_config"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeEndpointConfigOutput:
    out: DescribeEndpointConfigOutput = {}  # type: ignore[typeddict-item]
    if data.get("EndpointConfigName") is not None:
        out["endpoint_config_name"] = data["EndpointConfigName"]
    if data.get("EndpointConfigArn") is not None:
        out["endpoint_config_arn"] = data["EndpointConfigArn"]
    if data.get("ProductionVariants") is not None:
        import capo_sagemaker.types.production_variant_list

        out["production_variants"] = (
            capo_sagemaker.types.production_variant_list.deserialize_aws_json_1_1(
                data["ProductionVariants"]
            )
        )
    if data.get("DataCaptureConfig") is not None:
        import capo_sagemaker.types.data_capture_config

        out["data_capture_config"] = (
            capo_sagemaker.types.data_capture_config.deserialize_aws_json_1_1(
                data["DataCaptureConfig"]
            )
        )
    if data.get("KmsKeyId") is not None:
        out["kms_key_id"] = data["KmsKeyId"]
    if data.get("CreationTime") is not None:
        import capo_sagemaker.types.timestamp

        out["creation_time"] = capo_sagemaker.types.timestamp.deserialize_aws_json_1_1(
            data["CreationTime"]
        )
    if data.get("AsyncInferenceConfig") is not None:
        import capo_sagemaker.types.async_inference_config

        out["async_inference_config"] = (
            capo_sagemaker.types.async_inference_config.deserialize_aws_json_1_1(
                data["AsyncInferenceConfig"]
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
        import capo_sagemaker.types.production_variant_list

        out["shadow_production_variants"] = (
            capo_sagemaker.types.production_variant_list.deserialize_aws_json_1_1(
                data["ShadowProductionVariants"]
            )
        )
    if data.get("ExecutionRoleArn") is not None:
        out["execution_role_arn"] = data["ExecutionRoleArn"]
    if data.get("VpcConfig") is not None:
        import capo_sagemaker.types.vpc_config

        out["vpc_config"] = capo_sagemaker.types.vpc_config.deserialize_aws_json_1_1(
            data["VpcConfig"]
        )
    if data.get("EnableNetworkIsolation") is not None:
        out["enable_network_isolation"] = data["EnableNetworkIsolation"]
    if data.get("MetricsConfig") is not None:
        import capo_sagemaker.types.metrics_config

        out["metrics_config"] = (
            capo_sagemaker.types.metrics_config.deserialize_aws_json_1_1(
                data["MetricsConfig"]
            )
        )
    return out
