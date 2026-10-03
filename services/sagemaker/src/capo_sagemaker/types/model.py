"""Generated from Smithy shape ``com.amazonaws.sagemaker#Model``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.boolean
    import capo_sagemaker.types.container_definition
    import capo_sagemaker.types.container_definition_list
    import capo_sagemaker.types.deployment_recommendation
    import capo_sagemaker.types.inference_execution_config
    import capo_sagemaker.types.model_arn
    import capo_sagemaker.types.model_name
    import capo_sagemaker.types.role_arn
    import capo_sagemaker.types.tag_list
    import capo_sagemaker.types.timestamp
    import capo_sagemaker.types.vpc_config


class Model(TypedDict, closed=True):
    model_name: NotRequired["capo_sagemaker.types.model_name.ModelName"]
    """<p>The name of the model.</p>"""
    primary_container: NotRequired[
        "capo_sagemaker.types.container_definition.ContainerDefinition"
    ]
    containers: NotRequired[
        "capo_sagemaker.types.container_definition_list.ContainerDefinitionList"
    ]
    """<p>The containers in the inference pipeline.</p>"""
    inference_execution_config: NotRequired[
        "capo_sagemaker.types.inference_execution_config.InferenceExecutionConfig"
    ]
    execution_role_arn: NotRequired["capo_sagemaker.types.role_arn.RoleArn"]
    """<p>The Amazon Resource Name (ARN) of the IAM role that you specified for the model.</p>"""
    vpc_config: NotRequired["capo_sagemaker.types.vpc_config.VpcConfig"]
    creation_time: NotRequired["capo_sagemaker.types.timestamp.Timestamp"]
    """<p>A timestamp that indicates when the model was created.</p>"""
    model_arn: NotRequired["capo_sagemaker.types.model_arn.ModelArn"]
    """<p>The Amazon Resource Name (ARN) of the model.</p>"""
    enable_network_isolation: NotRequired["capo_sagemaker.types.boolean.Boolean"]
    """<p>Isolates the model container. No inbound or outbound network calls can be made to or from the model container.</p>"""
    tags: NotRequired["capo_sagemaker.types.tag_list.TagList"]
    """<p>A list of key-value pairs associated with the model. For more information, see <a href="https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html">Tagging Amazon Web Services resources</a> in the <i>Amazon Web Services General Reference Guide</i>.</p>"""
    deployment_recommendation: NotRequired[
        "capo_sagemaker.types.deployment_recommendation.DeploymentRecommendation"
    ]
    """<p>A set of recommended deployment configurations for the model.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Model) -> dict:
    out: dict = {}
    if "model_name" in value:
        out["ModelName"] = value["model_name"]
    if "primary_container" in value:
        import capo_sagemaker.types.container_definition

        out["PrimaryContainer"] = (
            capo_sagemaker.types.container_definition.serialize_aws_json_1_1(
                value["primary_container"]
            )
        )
    if "containers" in value:
        import capo_sagemaker.types.container_definition_list

        out["Containers"] = (
            capo_sagemaker.types.container_definition_list.serialize_aws_json_1_1(
                value["containers"]
            )
        )
    if "inference_execution_config" in value:
        import capo_sagemaker.types.inference_execution_config

        out["InferenceExecutionConfig"] = (
            capo_sagemaker.types.inference_execution_config.serialize_aws_json_1_1(
                value["inference_execution_config"]
            )
        )
    if "execution_role_arn" in value:
        out["ExecutionRoleArn"] = value["execution_role_arn"]
    if "vpc_config" in value:
        import capo_sagemaker.types.vpc_config

        out["VpcConfig"] = capo_sagemaker.types.vpc_config.serialize_aws_json_1_1(
            value["vpc_config"]
        )
    if "creation_time" in value:
        import capo_sagemaker.types.timestamp

        out["CreationTime"] = capo_sagemaker.types.timestamp.serialize_aws_json_1_1(
            value["creation_time"]
        )
    if "model_arn" in value:
        out["ModelArn"] = value["model_arn"]
    if "enable_network_isolation" in value:
        out["EnableNetworkIsolation"] = value["enable_network_isolation"]
    if "tags" in value:
        import capo_sagemaker.types.tag_list

        out["Tags"] = capo_sagemaker.types.tag_list.serialize_aws_json_1_1(
            value["tags"]
        )
    if "deployment_recommendation" in value:
        import capo_sagemaker.types.deployment_recommendation

        out["DeploymentRecommendation"] = (
            capo_sagemaker.types.deployment_recommendation.serialize_aws_json_1_1(
                value["deployment_recommendation"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> Model:
    out: Model = {}  # type: ignore[typeddict-item]
    if data.get("ModelName") is not None:
        out["model_name"] = data["ModelName"]
    if data.get("PrimaryContainer") is not None:
        import capo_sagemaker.types.container_definition

        out["primary_container"] = (
            capo_sagemaker.types.container_definition.deserialize_aws_json_1_1(
                data["PrimaryContainer"]
            )
        )
    if data.get("Containers") is not None:
        import capo_sagemaker.types.container_definition_list

        out["containers"] = (
            capo_sagemaker.types.container_definition_list.deserialize_aws_json_1_1(
                data["Containers"]
            )
        )
    if data.get("InferenceExecutionConfig") is not None:
        import capo_sagemaker.types.inference_execution_config

        out["inference_execution_config"] = (
            capo_sagemaker.types.inference_execution_config.deserialize_aws_json_1_1(
                data["InferenceExecutionConfig"]
            )
        )
    if data.get("ExecutionRoleArn") is not None:
        out["execution_role_arn"] = data["ExecutionRoleArn"]
    if data.get("VpcConfig") is not None:
        import capo_sagemaker.types.vpc_config

        out["vpc_config"] = capo_sagemaker.types.vpc_config.deserialize_aws_json_1_1(
            data["VpcConfig"]
        )
    if data.get("CreationTime") is not None:
        import capo_sagemaker.types.timestamp

        out["creation_time"] = capo_sagemaker.types.timestamp.deserialize_aws_json_1_1(
            data["CreationTime"]
        )
    if data.get("ModelArn") is not None:
        out["model_arn"] = data["ModelArn"]
    if data.get("EnableNetworkIsolation") is not None:
        out["enable_network_isolation"] = data["EnableNetworkIsolation"]
    if data.get("Tags") is not None:
        import capo_sagemaker.types.tag_list

        out["tags"] = capo_sagemaker.types.tag_list.deserialize_aws_json_1_1(
            data["Tags"]
        )
    if data.get("DeploymentRecommendation") is not None:
        import capo_sagemaker.types.deployment_recommendation

        out["deployment_recommendation"] = (
            capo_sagemaker.types.deployment_recommendation.deserialize_aws_json_1_1(
                data["DeploymentRecommendation"]
            )
        )
    return out
