"""Generated from Smithy shape ``com.amazonaws.sagemaker#CreateEndpointConfigInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.async_inference_config
    import capo_sagemaker.types.boolean
    import capo_sagemaker.types.data_capture_config
    import capo_sagemaker.types.endpoint_config_name
    import capo_sagemaker.types.explainer_config
    import capo_sagemaker.types.kms_key_id
    import capo_sagemaker.types.metrics_config
    import capo_sagemaker.types.production_variant_list
    import capo_sagemaker.types.role_arn
    import capo_sagemaker.types.tag_list
    import capo_sagemaker.types.vpc_config


class CreateEndpointConfigInput(TypedDict, closed=True):
    endpoint_config_name: NotRequired[
        "capo_sagemaker.types.endpoint_config_name.EndpointConfigName"
    ]
    """<p>The name of the endpoint configuration. You specify this name in a <a href="https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateEndpoint.html">CreateEndpoint</a> request. </p>"""
    production_variants: NotRequired[
        "capo_sagemaker.types.production_variant_list.ProductionVariantList"
    ]
    """<p>An array of <code>ProductionVariant</code> objects, one for each model that you want to host at this endpoint.</p>"""
    data_capture_config: NotRequired[
        "capo_sagemaker.types.data_capture_config.DataCaptureConfig"
    ]
    tags: NotRequired["capo_sagemaker.types.tag_list.TagList"]
    """<p>An array of key-value pairs. You can use tags to categorize your Amazon Web Services resources in different ways, for example, by purpose, owner, or environment. For more information, see <a href="https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html">Tagging Amazon Web Services Resources</a>.</p>"""
    kms_key_id: NotRequired["capo_sagemaker.types.kms_key_id.KmsKeyId"]
    """<p>The Amazon Resource Name (ARN) of a Amazon Web Services Key Management Service key that SageMaker uses to encrypt data on the storage volume attached to the ML compute instance that hosts the endpoint.</p> <p>The KmsKeyId can be any of the following formats: </p> <ul> <li> <p>Key ID: <code>1234abcd-12ab-34cd-56ef-1234567890ab</code> </p> </li> <li> <p>Key ARN: <code>arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab</code> </p> </li> <li> <p>Alias name: <code>alias/ExampleAlias</code> </p> </li> <li> <p>Alias name ARN: <code>arn:aws:kms:us-west-2:111122223333:alias/ExampleAlias</code> </p> </li> </ul> <p>The KMS key policy must grant permission to the IAM role that you specify in your <code>CreateEndpoint</code>, <code>UpdateEndpoint</code> requests. For more information, refer to the Amazon Web Services Key Management Service section<a href="https://docs.aws.amazon.com/kms/latest/developerguide/key-policies.html"> Using Key Policies in Amazon Web Services KMS </a> </p> <note> <p>Certain Nitro-based instances include local storage, dependent on the instance type. Local storage volumes are encrypted using a hardware module on the instance. If any of the models that you specify in the <code>ProductionVariants</code> parameter use nitro-based instances with local storage, the <code>KmsKeyId</code> parameter does not encrypt instance local storage.</p> <p>For a list of instance types that support local instance storage, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/InstanceStorage.html#instance-store-volumes">Instance Store Volumes</a>.</p> <p>For more information about local instance storage encryption, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ssd-instance-store.html">SSD Instance Store Volumes</a>.</p> </note>"""
    async_inference_config: NotRequired[
        "capo_sagemaker.types.async_inference_config.AsyncInferenceConfig"
    ]
    """<p>Specifies configuration for how an endpoint performs asynchronous inference. This is a required field in order for your Endpoint to be invoked using <a href="https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_runtime_InvokeEndpointAsync.html">InvokeEndpointAsync</a>.</p>"""
    explainer_config: NotRequired[
        "capo_sagemaker.types.explainer_config.ExplainerConfig"
    ]
    """<p>A member of <code>CreateEndpointConfig</code> that enables explainers.</p>"""
    shadow_production_variants: NotRequired[
        "capo_sagemaker.types.production_variant_list.ProductionVariantList"
    ]
    """<p>An array of <code>ProductionVariant</code> objects, one for each model that you want to host at this endpoint in shadow mode with production traffic replicated from the model specified on <code>ProductionVariants</code>. If you use this field, you can only specify one variant for <code>ProductionVariants</code> and one variant for <code>ShadowProductionVariants</code>.</p>"""
    execution_role_arn: NotRequired["capo_sagemaker.types.role_arn.RoleArn"]
    """<p>The Amazon Resource Name (ARN) of an IAM role that Amazon SageMaker AI can assume to perform actions on your behalf. For more information, see <a href="https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-roles.html">SageMaker AI Roles</a>. </p> <note> <p>To be able to pass this role to Amazon SageMaker AI, the caller of this action must have the <code>iam:PassRole</code> permission.</p> </note>"""
    vpc_config: NotRequired["capo_sagemaker.types.vpc_config.VpcConfig"]
    enable_network_isolation: NotRequired["capo_sagemaker.types.boolean.Boolean"]
    """<p>Sets whether all model containers deployed to the endpoint are isolated. If they are, no inbound or outbound network calls can be made to or from the model containers.</p>"""
    metrics_config: NotRequired["capo_sagemaker.types.metrics_config.MetricsConfig"]
    """<p>The configuration parameters for utilization metrics.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateEndpointConfigInput) -> dict:
    out: dict = {}
    if "endpoint_config_name" in value:
        out["EndpointConfigName"] = value["endpoint_config_name"]
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
    if "tags" in value:
        import capo_sagemaker.types.tag_list

        out["Tags"] = capo_sagemaker.types.tag_list.serialize_aws_json_1_1(
            value["tags"]
        )
    if "kms_key_id" in value:
        out["KmsKeyId"] = value["kms_key_id"]
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


def deserialize_aws_json_1_1(data: dict) -> CreateEndpointConfigInput:
    out: CreateEndpointConfigInput = {}  # type: ignore[typeddict-item]
    if data.get("EndpointConfigName") is not None:
        out["endpoint_config_name"] = data["EndpointConfigName"]
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
    if data.get("Tags") is not None:
        import capo_sagemaker.types.tag_list

        out["tags"] = capo_sagemaker.types.tag_list.deserialize_aws_json_1_1(
            data["Tags"]
        )
    if data.get("KmsKeyId") is not None:
        out["kms_key_id"] = data["KmsKeyId"]
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
