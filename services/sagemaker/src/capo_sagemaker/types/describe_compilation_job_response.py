"""Generated from Smithy shape ``com.amazonaws.sagemaker#DescribeCompilationJobResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.compilation_job_arn
    import capo_sagemaker.types.compilation_job_status
    import capo_sagemaker.types.creation_time
    import capo_sagemaker.types.derived_information
    import capo_sagemaker.types.entity_name
    import capo_sagemaker.types.failure_reason
    import capo_sagemaker.types.inference_image
    import capo_sagemaker.types.input_config
    import capo_sagemaker.types.last_modified_time
    import capo_sagemaker.types.model_artifacts
    import capo_sagemaker.types.model_digests
    import capo_sagemaker.types.model_package_arn
    import capo_sagemaker.types.neo_vpc_config
    import capo_sagemaker.types.output_config
    import capo_sagemaker.types.role_arn
    import capo_sagemaker.types.stopping_condition
    import capo_sagemaker.types.timestamp


class DescribeCompilationJobResponse(TypedDict, closed=True):
    compilation_job_name: NotRequired["capo_sagemaker.types.entity_name.EntityName"]
    """<p>The name of the model compilation job.</p>"""
    compilation_job_arn: NotRequired[
        "capo_sagemaker.types.compilation_job_arn.CompilationJobArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the model compilation job.</p>"""
    compilation_job_status: NotRequired[
        "capo_sagemaker.types.compilation_job_status.CompilationJobStatus"
    ]
    """<p>The status of the model compilation job.</p>"""
    compilation_start_time: NotRequired["capo_sagemaker.types.timestamp.Timestamp"]
    """<p>The time when the model compilation job started the <code>CompilationJob</code> instances. </p> <p>You are billed for the time between this timestamp and the timestamp in the <code>CompilationEndTime</code> field. In Amazon CloudWatch Logs, the start time might be later than this time. That's because it takes time to download the compilation job, which depends on the size of the compilation job container. </p>"""
    compilation_end_time: NotRequired["capo_sagemaker.types.timestamp.Timestamp"]
    """<p>The time when the model compilation job on a compilation job instance ended. For a successful or stopped job, this is when the job's model artifacts have finished uploading. For a failed job, this is when Amazon SageMaker AI detected that the job failed. </p>"""
    stopping_condition: NotRequired[
        "capo_sagemaker.types.stopping_condition.StoppingCondition"
    ]
    """<p>Specifies a limit to how long a model compilation job can run. When the job reaches the time limit, Amazon SageMaker AI ends the compilation job. Use this API to cap model training costs.</p>"""
    inference_image: NotRequired["capo_sagemaker.types.inference_image.InferenceImage"]
    """<p>The inference image to use when compiling a model. Specify an image only if the target device is a cloud instance.</p>"""
    model_package_version_arn: NotRequired[
        "capo_sagemaker.types.model_package_arn.ModelPackageArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the versioned model package that was provided to SageMaker Neo when you initiated a compilation job.</p>"""
    creation_time: NotRequired["capo_sagemaker.types.creation_time.CreationTime"]
    """<p>The time that the model compilation job was created.</p>"""
    last_modified_time: NotRequired[
        "capo_sagemaker.types.last_modified_time.LastModifiedTime"
    ]
    """<p>The time that the status of the model compilation job was last modified.</p>"""
    failure_reason: NotRequired["capo_sagemaker.types.failure_reason.FailureReason"]
    """<p>If a model compilation job failed, the reason it failed. </p>"""
    model_artifacts: NotRequired["capo_sagemaker.types.model_artifacts.ModelArtifacts"]
    """<p>Information about the location in Amazon S3 that has been configured for storing the model artifacts used in the compilation job.</p>"""
    model_digests: NotRequired["capo_sagemaker.types.model_digests.ModelDigests"]
    """<p>Provides a BLAKE2 hash value that identifies the compiled model artifacts in Amazon S3.</p>"""
    role_arn: NotRequired["capo_sagemaker.types.role_arn.RoleArn"]
    """<p>The Amazon Resource Name (ARN) of an IAM role that Amazon SageMaker AI assumes to perform the model compilation job.</p>"""
    input_config: NotRequired["capo_sagemaker.types.input_config.InputConfig"]
    """<p>Information about the location in Amazon S3 of the input model artifacts, the name and shape of the expected data inputs, and the framework in which the model was trained.</p>"""
    output_config: NotRequired["capo_sagemaker.types.output_config.OutputConfig"]
    """<p>Information about the output location for the compiled model and the target device that the model runs on.</p>"""
    vpc_config: NotRequired["capo_sagemaker.types.neo_vpc_config.NeoVpcConfig"]
    """<p>A <a href="https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_VpcConfig.html">VpcConfig</a> object that specifies the VPC that you want your compilation job to connect to. Control access to your models by configuring the VPC. For more information, see <a href="https://docs.aws.amazon.com/sagemaker/latest/dg/neo-vpc.html">Protect Compilation Jobs by Using an Amazon Virtual Private Cloud</a>.</p>"""
    derived_information: NotRequired[
        "capo_sagemaker.types.derived_information.DerivedInformation"
    ]
    """<p>Information that SageMaker Neo automatically derived about the model.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeCompilationJobResponse) -> dict:
    out: dict = {}
    if "compilation_job_name" in value:
        out["CompilationJobName"] = value["compilation_job_name"]
    if "compilation_job_arn" in value:
        out["CompilationJobArn"] = value["compilation_job_arn"]
    if "compilation_job_status" in value:
        import capo_sagemaker.types.compilation_job_status

        out["CompilationJobStatus"] = (
            capo_sagemaker.types.compilation_job_status.serialize_aws_json_1_1(
                value["compilation_job_status"]
            )
        )
    if "compilation_start_time" in value:
        import capo_sagemaker.types.timestamp

        out["CompilationStartTime"] = (
            capo_sagemaker.types.timestamp.serialize_aws_json_1_1(
                value["compilation_start_time"]
            )
        )
    if "compilation_end_time" in value:
        import capo_sagemaker.types.timestamp

        out["CompilationEndTime"] = (
            capo_sagemaker.types.timestamp.serialize_aws_json_1_1(
                value["compilation_end_time"]
            )
        )
    if "stopping_condition" in value:
        import capo_sagemaker.types.stopping_condition

        out["StoppingCondition"] = (
            capo_sagemaker.types.stopping_condition.serialize_aws_json_1_1(
                value["stopping_condition"]
            )
        )
    if "inference_image" in value:
        out["InferenceImage"] = value["inference_image"]
    if "model_package_version_arn" in value:
        out["ModelPackageVersionArn"] = value["model_package_version_arn"]
    if "creation_time" in value:
        import capo_sagemaker.types.creation_time

        out["CreationTime"] = capo_sagemaker.types.creation_time.serialize_aws_json_1_1(
            value["creation_time"]
        )
    if "last_modified_time" in value:
        import capo_sagemaker.types.last_modified_time

        out["LastModifiedTime"] = (
            capo_sagemaker.types.last_modified_time.serialize_aws_json_1_1(
                value["last_modified_time"]
            )
        )
    if "failure_reason" in value:
        out["FailureReason"] = value["failure_reason"]
    if "model_artifacts" in value:
        import capo_sagemaker.types.model_artifacts

        out["ModelArtifacts"] = (
            capo_sagemaker.types.model_artifacts.serialize_aws_json_1_1(
                value["model_artifacts"]
            )
        )
    if "model_digests" in value:
        import capo_sagemaker.types.model_digests

        out["ModelDigests"] = capo_sagemaker.types.model_digests.serialize_aws_json_1_1(
            value["model_digests"]
        )
    if "role_arn" in value:
        out["RoleArn"] = value["role_arn"]
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
    if "derived_information" in value:
        import capo_sagemaker.types.derived_information

        out["DerivedInformation"] = (
            capo_sagemaker.types.derived_information.serialize_aws_json_1_1(
                value["derived_information"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeCompilationJobResponse:
    out: DescribeCompilationJobResponse = {}  # type: ignore[typeddict-item]
    if data.get("CompilationJobName") is not None:
        out["compilation_job_name"] = data["CompilationJobName"]
    if data.get("CompilationJobArn") is not None:
        out["compilation_job_arn"] = data["CompilationJobArn"]
    if data.get("CompilationJobStatus") is not None:
        import capo_sagemaker.types.compilation_job_status

        out["compilation_job_status"] = (
            capo_sagemaker.types.compilation_job_status.deserialize_aws_json_1_1(
                data["CompilationJobStatus"]
            )
        )
    if data.get("CompilationStartTime") is not None:
        import capo_sagemaker.types.timestamp

        out["compilation_start_time"] = (
            capo_sagemaker.types.timestamp.deserialize_aws_json_1_1(
                data["CompilationStartTime"]
            )
        )
    if data.get("CompilationEndTime") is not None:
        import capo_sagemaker.types.timestamp

        out["compilation_end_time"] = (
            capo_sagemaker.types.timestamp.deserialize_aws_json_1_1(
                data["CompilationEndTime"]
            )
        )
    if data.get("StoppingCondition") is not None:
        import capo_sagemaker.types.stopping_condition

        out["stopping_condition"] = (
            capo_sagemaker.types.stopping_condition.deserialize_aws_json_1_1(
                data["StoppingCondition"]
            )
        )
    if data.get("InferenceImage") is not None:
        out["inference_image"] = data["InferenceImage"]
    if data.get("ModelPackageVersionArn") is not None:
        out["model_package_version_arn"] = data["ModelPackageVersionArn"]
    if data.get("CreationTime") is not None:
        import capo_sagemaker.types.creation_time

        out["creation_time"] = (
            capo_sagemaker.types.creation_time.deserialize_aws_json_1_1(
                data["CreationTime"]
            )
        )
    if data.get("LastModifiedTime") is not None:
        import capo_sagemaker.types.last_modified_time

        out["last_modified_time"] = (
            capo_sagemaker.types.last_modified_time.deserialize_aws_json_1_1(
                data["LastModifiedTime"]
            )
        )
    if data.get("FailureReason") is not None:
        out["failure_reason"] = data["FailureReason"]
    if data.get("ModelArtifacts") is not None:
        import capo_sagemaker.types.model_artifacts

        out["model_artifacts"] = (
            capo_sagemaker.types.model_artifacts.deserialize_aws_json_1_1(
                data["ModelArtifacts"]
            )
        )
    if data.get("ModelDigests") is not None:
        import capo_sagemaker.types.model_digests

        out["model_digests"] = (
            capo_sagemaker.types.model_digests.deserialize_aws_json_1_1(
                data["ModelDigests"]
            )
        )
    if data.get("RoleArn") is not None:
        out["role_arn"] = data["RoleArn"]
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
    if data.get("DerivedInformation") is not None:
        import capo_sagemaker.types.derived_information

        out["derived_information"] = (
            capo_sagemaker.types.derived_information.deserialize_aws_json_1_1(
                data["DerivedInformation"]
            )
        )
    return out
