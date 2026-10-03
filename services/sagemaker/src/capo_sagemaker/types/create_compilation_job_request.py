"""Generated from Smithy shape ``com.amazonaws.sagemaker#CreateCompilationJobRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.entity_name
    import capo_sagemaker.types.input_config
    import capo_sagemaker.types.model_package_arn
    import capo_sagemaker.types.neo_vpc_config
    import capo_sagemaker.types.output_config
    import capo_sagemaker.types.role_arn
    import capo_sagemaker.types.stopping_condition
    import capo_sagemaker.types.tag_list


class CreateCompilationJobRequest(TypedDict, closed=True):
    compilation_job_name: NotRequired["capo_sagemaker.types.entity_name.EntityName"]
    """<p>A name for the model compilation job. The name must be unique within the Amazon Web Services Region and within your Amazon Web Services account. </p>"""
    role_arn: NotRequired["capo_sagemaker.types.role_arn.RoleArn"]
    """<p>The Amazon Resource Name (ARN) of an IAM role that enables Amazon SageMaker AI to perform tasks on your behalf. </p> <p>During model compilation, Amazon SageMaker AI needs your permission to:</p> <ul> <li> <p>Read input data from an S3 bucket</p> </li> <li> <p>Write model artifacts to an S3 bucket</p> </li> <li> <p>Write logs to Amazon CloudWatch Logs</p> </li> <li> <p>Publish metrics to Amazon CloudWatch</p> </li> </ul> <p>You grant permissions for all of these tasks to an IAM role. To pass this role to Amazon SageMaker AI, the caller of this API must have the <code>iam:PassRole</code> permission. For more information, see <a href="https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-roles.html">Amazon SageMaker AI Roles.</a> </p>"""
    model_package_version_arn: NotRequired[
        "capo_sagemaker.types.model_package_arn.ModelPackageArn"
    ]
    """<p>The Amazon Resource Name (ARN) of a versioned model package. Provide either a <code>ModelPackageVersionArn</code> or an <code>InputConfig</code> object in the request syntax. The presence of both objects in the <code>CreateCompilationJob</code> request will return an exception.</p>"""
    input_config: NotRequired["capo_sagemaker.types.input_config.InputConfig"]
    """<p>Provides information about the location of input model artifacts, the name and shape of the expected data inputs, and the framework in which the model was trained.</p>"""
    output_config: NotRequired["capo_sagemaker.types.output_config.OutputConfig"]
    """<p>Provides information about the output location for the compiled model and the target device the model runs on.</p>"""
    vpc_config: NotRequired["capo_sagemaker.types.neo_vpc_config.NeoVpcConfig"]
    """<p>A <a href="https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_VpcConfig.html">VpcConfig</a> object that specifies the VPC that you want your compilation job to connect to. Control access to your models by configuring the VPC. For more information, see <a href="https://docs.aws.amazon.com/sagemaker/latest/dg/neo-vpc.html">Protect Compilation Jobs by Using an Amazon Virtual Private Cloud</a>.</p>"""
    stopping_condition: NotRequired[
        "capo_sagemaker.types.stopping_condition.StoppingCondition"
    ]
    """<p>Specifies a limit to how long a model compilation job can run. When the job reaches the time limit, Amazon SageMaker AI ends the compilation job. Use this API to cap model training costs.</p>"""
    tags: NotRequired["capo_sagemaker.types.tag_list.TagList"]
    """<p>An array of key-value pairs. You can use tags to categorize your Amazon Web Services resources in different ways, for example, by purpose, owner, or environment. For more information, see <a href="https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html">Tagging Amazon Web Services Resources</a>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateCompilationJobRequest) -> dict:
    out: dict = {}
    if "compilation_job_name" in value:
        out["CompilationJobName"] = value["compilation_job_name"]
    if "role_arn" in value:
        out["RoleArn"] = value["role_arn"]
    if "model_package_version_arn" in value:
        out["ModelPackageVersionArn"] = value["model_package_version_arn"]
    if "input_config" in value:
        import capo_sagemaker.types.input_config

        out["InputConfig"] = capo_sagemaker.types.input_config.serialize_aws_json_1_1(
            value["input_config"]
        )
    if "output_config" in value:
        import capo_sagemaker.types.output_config

        out["OutputConfig"] = capo_sagemaker.types.output_config.serialize_aws_json_1_1(
            value["output_config"]
        )
    if "vpc_config" in value:
        import capo_sagemaker.types.neo_vpc_config

        out["VpcConfig"] = capo_sagemaker.types.neo_vpc_config.serialize_aws_json_1_1(
            value["vpc_config"]
        )
    if "stopping_condition" in value:
        import capo_sagemaker.types.stopping_condition

        out["StoppingCondition"] = (
            capo_sagemaker.types.stopping_condition.serialize_aws_json_1_1(
                value["stopping_condition"]
            )
        )
    if "tags" in value:
        import capo_sagemaker.types.tag_list

        out["Tags"] = capo_sagemaker.types.tag_list.serialize_aws_json_1_1(
            value["tags"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateCompilationJobRequest:
    out: CreateCompilationJobRequest = {}  # type: ignore[typeddict-item]
    if data.get("CompilationJobName") is not None:
        out["compilation_job_name"] = data["CompilationJobName"]
    if data.get("RoleArn") is not None:
        out["role_arn"] = data["RoleArn"]
    if data.get("ModelPackageVersionArn") is not None:
        out["model_package_version_arn"] = data["ModelPackageVersionArn"]
    if data.get("InputConfig") is not None:
        import capo_sagemaker.types.input_config

        out["input_config"] = (
            capo_sagemaker.types.input_config.deserialize_aws_json_1_1(
                data["InputConfig"]
            )
        )
    if data.get("OutputConfig") is not None:
        import capo_sagemaker.types.output_config

        out["output_config"] = (
            capo_sagemaker.types.output_config.deserialize_aws_json_1_1(
                data["OutputConfig"]
            )
        )
    if data.get("VpcConfig") is not None:
        import capo_sagemaker.types.neo_vpc_config

        out["vpc_config"] = (
            capo_sagemaker.types.neo_vpc_config.deserialize_aws_json_1_1(
                data["VpcConfig"]
            )
        )
    if data.get("StoppingCondition") is not None:
        import capo_sagemaker.types.stopping_condition

        out["stopping_condition"] = (
            capo_sagemaker.types.stopping_condition.deserialize_aws_json_1_1(
                data["StoppingCondition"]
            )
        )
    if data.get("Tags") is not None:
        import capo_sagemaker.types.tag_list

        out["tags"] = capo_sagemaker.types.tag_list.deserialize_aws_json_1_1(
            data["Tags"]
        )
    return out
