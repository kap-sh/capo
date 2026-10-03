"""Generated from Smithy shape ``com.amazonaws.bedrock#CreateEvaluationJobRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_bedrock.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock.types.application_type
    import capo_bedrock.types.evaluation_config
    import capo_bedrock.types.evaluation_inference_config
    import capo_bedrock.types.evaluation_job_description
    import capo_bedrock.types.evaluation_job_name
    import capo_bedrock.types.evaluation_output_data_config
    import capo_bedrock.types.idempotency_token
    import capo_bedrock.types.kms_key_id
    import capo_bedrock.types.role_arn
    import capo_bedrock.types.tag_list


class CreateEvaluationJobRequest(TypedDict, closed=True):
    job_name: "capo_bedrock.types.evaluation_job_name.EvaluationJobName"
    """<p>A name for the evaluation job. Names must unique with your Amazon Web Services account, and your account's Amazon Web Services region.</p>"""
    job_description: NotRequired[
        "capo_bedrock.types.evaluation_job_description.EvaluationJobDescription"
    ]
    """<p>A description of the evaluation job.</p>"""
    client_request_token: NotRequired[
        "capo_bedrock.types.idempotency_token.IdempotencyToken"
    ]
    """<p>A unique, case-sensitive identifier to ensure that the API request completes no more than one time. If this token matches a previous request, Amazon Bedrock ignores the request, but does not return an error. For more information, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html">Ensuring idempotency</a>.</p>"""
    role_arn: "capo_bedrock.types.role_arn.RoleArn"
    """<p>The Amazon Resource Name (ARN) of an IAM service role that Amazon Bedrock can assume to perform tasks on your behalf. To learn more about the required permissions, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/model-evaluation-security.html">Required permissions for model evaluations</a>.</p>"""
    customer_encryption_key_id: NotRequired["capo_bedrock.types.kms_key_id.KmsKeyId"]
    """<p>Specify your customer managed encryption key Amazon Resource Name (ARN) that will be used to encrypt your evaluation job.</p>"""
    job_tags: NotRequired["capo_bedrock.types.tag_list.TagList"]
    """<p>Tags to attach to the model evaluation job.</p>"""
    application_type: NotRequired["capo_bedrock.types.application_type.ApplicationType"]
    """<p>Specifies whether the evaluation job is for evaluating a model or evaluating a knowledge base (retrieval and response generation).</p>"""
    evaluation_config: "capo_bedrock.types.evaluation_config.EvaluationConfig"
    """<p>Contains the configuration details of either an automated or human-based evaluation job.</p>"""
    inference_config: (
        "capo_bedrock.types.evaluation_inference_config.EvaluationInferenceConfig"
    )
    """<p>Contains the configuration details of the inference model for the evaluation job.</p> <p>For model evaluation jobs, automated jobs support a single model or <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/cross-region-inference.html">inference profile</a>, and jobs that use human workers support two models or inference profiles.</p>"""
    output_data_config: (
        "capo_bedrock.types.evaluation_output_data_config.EvaluationOutputDataConfig"
    )
    """<p>Contains the configuration details of the Amazon S3 bucket for storing the results of the evaluation job.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateEvaluationJobRequest) -> dict:
    out: dict = {}
    out["jobName"] = value["job_name"]
    if "job_description" in value:
        out["jobDescription"] = value["job_description"]
    if "client_request_token" in value:
        out["clientRequestToken"] = value["client_request_token"]
    out["roleArn"] = value["role_arn"]
    if "customer_encryption_key_id" in value:
        out["customerEncryptionKeyId"] = value["customer_encryption_key_id"]
    if "job_tags" in value:
        import capo_bedrock.types.tag_list

        out["jobTags"] = capo_bedrock.types.tag_list.serialize_json(value["job_tags"])
    if "application_type" in value:
        import capo_bedrock.types.application_type

        out["applicationType"] = capo_bedrock.types.application_type.serialize_json(
            value["application_type"]
        )
    import capo_bedrock.types.evaluation_config

    out["evaluationConfig"] = capo_bedrock.types.evaluation_config.serialize_json(
        value["evaluation_config"]
    )
    import capo_bedrock.types.evaluation_inference_config

    out["inferenceConfig"] = (
        capo_bedrock.types.evaluation_inference_config.serialize_json(
            value["inference_config"]
        )
    )
    import capo_bedrock.types.evaluation_output_data_config

    out["outputDataConfig"] = (
        capo_bedrock.types.evaluation_output_data_config.serialize_json(
            value["output_data_config"]
        )
    )
    return out


def deserialize_json(data: dict) -> CreateEvaluationJobRequest:
    out: CreateEvaluationJobRequest = {}  # type: ignore[typeddict-item]
    if data.get("jobName") is not None:
        out["job_name"] = data["jobName"]
    else:
        raise DeserializationError("CreateEvaluationJobRequest.job_name required")
    if data.get("jobDescription") is not None:
        out["job_description"] = data["jobDescription"]
    if data.get("clientRequestToken") is not None:
        out["client_request_token"] = data["clientRequestToken"]
    if data.get("roleArn") is not None:
        out["role_arn"] = data["roleArn"]
    else:
        raise DeserializationError("CreateEvaluationJobRequest.role_arn required")
    if data.get("customerEncryptionKeyId") is not None:
        out["customer_encryption_key_id"] = data["customerEncryptionKeyId"]
    if data.get("jobTags") is not None:
        import capo_bedrock.types.tag_list

        out["job_tags"] = capo_bedrock.types.tag_list.deserialize_json(data["jobTags"])
    if data.get("applicationType") is not None:
        import capo_bedrock.types.application_type

        out["application_type"] = capo_bedrock.types.application_type.deserialize_json(
            data["applicationType"]
        )
    if data.get("evaluationConfig") is not None:
        import capo_bedrock.types.evaluation_config

        out["evaluation_config"] = (
            capo_bedrock.types.evaluation_config.deserialize_json(
                data["evaluationConfig"]
            )
        )
    else:
        raise DeserializationError(
            "CreateEvaluationJobRequest.evaluation_config required"
        )
    if data.get("inferenceConfig") is not None:
        import capo_bedrock.types.evaluation_inference_config

        out["inference_config"] = (
            capo_bedrock.types.evaluation_inference_config.deserialize_json(
                data["inferenceConfig"]
            )
        )
    else:
        raise DeserializationError(
            "CreateEvaluationJobRequest.inference_config required"
        )
    if data.get("outputDataConfig") is not None:
        import capo_bedrock.types.evaluation_output_data_config

        out["output_data_config"] = (
            capo_bedrock.types.evaluation_output_data_config.deserialize_json(
                data["outputDataConfig"]
            )
        )
    else:
        raise DeserializationError(
            "CreateEvaluationJobRequest.output_data_config required"
        )
    return out
