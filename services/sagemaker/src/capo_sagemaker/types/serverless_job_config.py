"""Generated from Smithy shape ``com.amazonaws.sagemaker#ServerlessJobConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_sagemaker.errors import DeserializationError

if TYPE_CHECKING:
    import capo_sagemaker.types.accept_eula
    import capo_sagemaker.types.customization_technique
    import capo_sagemaker.types.evaluation_type
    import capo_sagemaker.types.evaluator_arn
    import capo_sagemaker.types.peft
    import capo_sagemaker.types.sequence_length
    import capo_sagemaker.types.serverless_job_base_model_arn
    import capo_sagemaker.types.serverless_job_type


class ServerlessJobConfig(TypedDict, closed=True):
    base_model_arn: (
        "capo_sagemaker.types.serverless_job_base_model_arn.ServerlessJobBaseModelArn"
    )
    """<p> The base model Amazon Resource Name (ARN) in <a href="https://docs.aws.amazon.com/sagemaker/latest/dg/jumpstart-foundation-models-use.html">SageMaker Public Hub</a>. SageMaker always selects the latest version of the provided model. </p>"""
    accept_eula: NotRequired["capo_sagemaker.types.accept_eula.AcceptEula"]
    """<p> Specifies agreement to the model end-user license agreement (EULA). The <code>AcceptEula</code> value must be explicitly defined as <code>True</code> in order to accept the EULA that this model requires. You are responsible for reviewing and complying with any applicable license terms and making sure they are acceptable for your use case before downloading or using a model. For more information, see <a href="https://docs.aws.amazon.com/sagemaker/latest/dg/jumpstart-foundation-models-choose.html#jumpstart-foundation-models-choose-eula">End-user license agreements</a> section for more details on accepting the EULA. </p>"""
    job_type: "capo_sagemaker.types.serverless_job_type.ServerlessJobType"
    """<p> The serverless training job type. </p>"""
    customization_technique: NotRequired[
        "capo_sagemaker.types.customization_technique.CustomizationTechnique"
    ]
    """<p> The model customization technique. </p>"""
    peft: NotRequired["capo_sagemaker.types.peft.Peft"]
    """<p> The parameter-efficient fine-tuning configuration. </p>"""
    evaluation_type: NotRequired["capo_sagemaker.types.evaluation_type.EvaluationType"]
    """<p> The evaluation job type. Required when serverless job type is <code>Evaluation</code>. </p>"""
    evaluator_arn: NotRequired["capo_sagemaker.types.evaluator_arn.EvaluatorArn"]
    """<p> The evaluator Amazon Resource Name (ARN) used as reward function or reward prompt. </p>"""
    sequence_length: NotRequired["capo_sagemaker.types.sequence_length.SequenceLength"]
    """<p> The maximum sequence length, in tokens, that the customization job supports. SageMaker uses this value to select a training configuration for the base model that you specify. The parameter supports the following values: </p> <ul> <li> <p> <code>1K</code> </p> </li> <li> <p> <code>2K</code> </p> </li> <li> <p> <code>4K</code> </p> </li> <li> <p> <code>8K</code> </p> </li> <li> <p> <code>16K</code> </p> </li> <li> <p> <code>32K</code> </p> </li> <li> <p> <code>64K</code> </p> </li> <li> <p> <code>128K</code> </p> </li> </ul> <p> If you don't specify a value, SageMaker selects a training configuration based on the other values that you specify. The selection is not restricted to a particular sequence length. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ServerlessJobConfig) -> dict:
    out: dict = {}
    out["BaseModelArn"] = value["base_model_arn"]
    if "accept_eula" in value:
        out["AcceptEula"] = value["accept_eula"]
    import capo_sagemaker.types.serverless_job_type

    out["JobType"] = capo_sagemaker.types.serverless_job_type.serialize_aws_json_1_1(
        value["job_type"]
    )
    if "customization_technique" in value:
        import capo_sagemaker.types.customization_technique

        out["CustomizationTechnique"] = (
            capo_sagemaker.types.customization_technique.serialize_aws_json_1_1(
                value["customization_technique"]
            )
        )
    if "peft" in value:
        import capo_sagemaker.types.peft

        out["Peft"] = capo_sagemaker.types.peft.serialize_aws_json_1_1(value["peft"])
    if "evaluation_type" in value:
        import capo_sagemaker.types.evaluation_type

        out["EvaluationType"] = (
            capo_sagemaker.types.evaluation_type.serialize_aws_json_1_1(
                value["evaluation_type"]
            )
        )
    if "evaluator_arn" in value:
        out["EvaluatorArn"] = value["evaluator_arn"]
    if "sequence_length" in value:
        out["SequenceLength"] = value["sequence_length"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ServerlessJobConfig:
    out: ServerlessJobConfig = {}  # type: ignore[typeddict-item]
    if data.get("BaseModelArn") is not None:
        out["base_model_arn"] = data["BaseModelArn"]
    else:
        raise DeserializationError("ServerlessJobConfig.base_model_arn required")
    if data.get("AcceptEula") is not None:
        out["accept_eula"] = data["AcceptEula"]
    if data.get("JobType") is not None:
        import capo_sagemaker.types.serverless_job_type

        out["job_type"] = (
            capo_sagemaker.types.serverless_job_type.deserialize_aws_json_1_1(
                data["JobType"]
            )
        )
    else:
        raise DeserializationError("ServerlessJobConfig.job_type required")
    if data.get("CustomizationTechnique") is not None:
        import capo_sagemaker.types.customization_technique

        out["customization_technique"] = (
            capo_sagemaker.types.customization_technique.deserialize_aws_json_1_1(
                data["CustomizationTechnique"]
            )
        )
    if data.get("Peft") is not None:
        import capo_sagemaker.types.peft

        out["peft"] = capo_sagemaker.types.peft.deserialize_aws_json_1_1(data["Peft"])
    if data.get("EvaluationType") is not None:
        import capo_sagemaker.types.evaluation_type

        out["evaluation_type"] = (
            capo_sagemaker.types.evaluation_type.deserialize_aws_json_1_1(
                data["EvaluationType"]
            )
        )
    if data.get("EvaluatorArn") is not None:
        out["evaluator_arn"] = data["EvaluatorArn"]
    if data.get("SequenceLength") is not None:
        out["sequence_length"] = data["SequenceLength"]
    return out
