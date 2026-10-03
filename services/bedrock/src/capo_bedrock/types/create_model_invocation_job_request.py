"""Generated from Smithy shape ``com.amazonaws.bedrock#CreateModelInvocationJobRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_bedrock.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock.types.model_id
    import capo_bedrock.types.model_invocation_idempotency_token
    import capo_bedrock.types.model_invocation_job_input_data_config
    import capo_bedrock.types.model_invocation_job_name
    import capo_bedrock.types.model_invocation_job_output_data_config
    import capo_bedrock.types.model_invocation_job_timeout_duration_in_hours
    import capo_bedrock.types.model_invocation_type
    import capo_bedrock.types.role_arn
    import capo_bedrock.types.tag_list
    import capo_bedrock.types.vpc_config


class CreateModelInvocationJobRequest(TypedDict, closed=True):
    job_name: "capo_bedrock.types.model_invocation_job_name.ModelInvocationJobName"
    """<p>A name to give the batch inference job.</p>"""
    role_arn: "capo_bedrock.types.role_arn.RoleArn"
    """<p>The Amazon Resource Name (ARN) of the service role with permissions to carry out and manage batch inference. You can use the console to create a default service role or follow the steps at <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/batch-iam-sr.html">Create a service role for batch inference</a>.</p>"""
    client_request_token: NotRequired[
        "capo_bedrock.types.model_invocation_idempotency_token.ModelInvocationIdempotencyToken"
    ]
    """<p>A unique, case-sensitive identifier to ensure that the API request completes no more than one time. If this token matches a previous request, Amazon Bedrock ignores the request, but does not return an error. For more information, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html">Ensuring idempotency</a>.</p>"""
    model_id: "capo_bedrock.types.model_id.ModelId"
    """<p>The unique identifier of the foundation model to use for the batch inference job.</p>"""
    input_data_config: "capo_bedrock.types.model_invocation_job_input_data_config.ModelInvocationJobInputDataConfig"
    """<p>Details about the location of the input to the batch inference job.</p>"""
    output_data_config: "capo_bedrock.types.model_invocation_job_output_data_config.ModelInvocationJobOutputDataConfig"
    """<p>Details about the location of the output of the batch inference job.</p>"""
    vpc_config: NotRequired["capo_bedrock.types.vpc_config.VpcConfig"]
    """<p>The configuration of the Virtual Private Cloud (VPC) for the data in the batch inference job. For more information, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/batch-vpc">Protect batch inference jobs using a VPC</a>.</p>"""
    timeout_duration_in_hours: NotRequired[
        "capo_bedrock.types.model_invocation_job_timeout_duration_in_hours.ModelInvocationJobTimeoutDurationInHours"
    ]
    """<p>The number of hours after which to force the batch inference job to time out.</p>"""
    tags: NotRequired["capo_bedrock.types.tag_list.TagList"]
    """<p>Any tags to associate with the batch inference job. For more information, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/tagging.html">Tagging Amazon Bedrock resources</a>.</p>"""
    model_invocation_type: (
        "capo_bedrock.types.model_invocation_type.ModelInvocationType"
    )
    """<p>The invocation endpoint for ModelInvocationJob</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateModelInvocationJobRequest) -> dict:
    out: dict = {}
    out["jobName"] = value["job_name"]
    out["roleArn"] = value["role_arn"]
    if "client_request_token" in value:
        out["clientRequestToken"] = value["client_request_token"]
    out["modelId"] = value["model_id"]
    import capo_bedrock.types.model_invocation_job_input_data_config

    out["inputDataConfig"] = (
        capo_bedrock.types.model_invocation_job_input_data_config.serialize_json(
            value["input_data_config"]
        )
    )
    import capo_bedrock.types.model_invocation_job_output_data_config

    out["outputDataConfig"] = (
        capo_bedrock.types.model_invocation_job_output_data_config.serialize_json(
            value["output_data_config"]
        )
    )
    if "vpc_config" in value:
        import capo_bedrock.types.vpc_config

        out["vpcConfig"] = capo_bedrock.types.vpc_config.serialize_json(
            value["vpc_config"]
        )
    if "timeout_duration_in_hours" in value:
        out["timeoutDurationInHours"] = value["timeout_duration_in_hours"]
    if "tags" in value:
        import capo_bedrock.types.tag_list

        out["tags"] = capo_bedrock.types.tag_list.serialize_json(value["tags"])
    import capo_bedrock.types.model_invocation_type

    out["modelInvocationType"] = (
        capo_bedrock.types.model_invocation_type.serialize_json(
            value.get("model_invocation_type", "InvokeModel")
        )
    )
    return out


def deserialize_json(data: dict) -> CreateModelInvocationJobRequest:
    out: CreateModelInvocationJobRequest = {}  # type: ignore[typeddict-item]
    if data.get("jobName") is not None:
        out["job_name"] = data["jobName"]
    else:
        raise DeserializationError("CreateModelInvocationJobRequest.job_name required")
    if data.get("roleArn") is not None:
        out["role_arn"] = data["roleArn"]
    else:
        raise DeserializationError("CreateModelInvocationJobRequest.role_arn required")
    if data.get("clientRequestToken") is not None:
        out["client_request_token"] = data["clientRequestToken"]
    if data.get("modelId") is not None:
        out["model_id"] = data["modelId"]
    else:
        raise DeserializationError("CreateModelInvocationJobRequest.model_id required")
    if data.get("inputDataConfig") is not None:
        import capo_bedrock.types.model_invocation_job_input_data_config

        out["input_data_config"] = (
            capo_bedrock.types.model_invocation_job_input_data_config.deserialize_json(
                data["inputDataConfig"]
            )
        )
    else:
        raise DeserializationError(
            "CreateModelInvocationJobRequest.input_data_config required"
        )
    if data.get("outputDataConfig") is not None:
        import capo_bedrock.types.model_invocation_job_output_data_config

        out["output_data_config"] = (
            capo_bedrock.types.model_invocation_job_output_data_config.deserialize_json(
                data["outputDataConfig"]
            )
        )
    else:
        raise DeserializationError(
            "CreateModelInvocationJobRequest.output_data_config required"
        )
    if data.get("vpcConfig") is not None:
        import capo_bedrock.types.vpc_config

        out["vpc_config"] = capo_bedrock.types.vpc_config.deserialize_json(
            data["vpcConfig"]
        )
    if data.get("timeoutDurationInHours") is not None:
        out["timeout_duration_in_hours"] = data["timeoutDurationInHours"]
    if data.get("tags") is not None:
        import capo_bedrock.types.tag_list

        out["tags"] = capo_bedrock.types.tag_list.deserialize_json(data["tags"])
    if data.get("modelInvocationType") is not None:
        import capo_bedrock.types.model_invocation_type

        out["model_invocation_type"] = (
            capo_bedrock.types.model_invocation_type.deserialize_json(
                data["modelInvocationType"]
            )
        )
    else:
        out["model_invocation_type"] = "InvokeModel"
    return out
