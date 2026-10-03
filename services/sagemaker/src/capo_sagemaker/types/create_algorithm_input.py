"""Generated from Smithy shape ``com.amazonaws.sagemaker#CreateAlgorithmInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.algorithm_validation_specification
    import capo_sagemaker.types.certify_for_marketplace
    import capo_sagemaker.types.entity_description
    import capo_sagemaker.types.entity_name
    import capo_sagemaker.types.inference_specification
    import capo_sagemaker.types.tag_list
    import capo_sagemaker.types.training_specification


class CreateAlgorithmInput(TypedDict, closed=True):
    algorithm_name: NotRequired["capo_sagemaker.types.entity_name.EntityName"]
    """<p>The name of the algorithm.</p>"""
    algorithm_description: NotRequired[
        "capo_sagemaker.types.entity_description.EntityDescription"
    ]
    """<p>A description of the algorithm.</p>"""
    training_specification: NotRequired[
        "capo_sagemaker.types.training_specification.TrainingSpecification"
    ]
    """<p>Specifies details about training jobs run by this algorithm, including the following:</p> <ul> <li> <p>The Amazon ECR path of the container and the version digest of the algorithm.</p> </li> <li> <p>The hyperparameters that the algorithm supports.</p> </li> <li> <p>The instance types that the algorithm supports for training.</p> </li> <li> <p>Whether the algorithm supports distributed training.</p> </li> <li> <p>The metrics that the algorithm emits to Amazon CloudWatch.</p> </li> <li> <p>Which metrics that the algorithm emits can be used as the objective metric for hyperparameter tuning jobs.</p> </li> <li> <p>The input channels that the algorithm supports for training data. For example, an algorithm might support <code>train</code>, <code>validation</code>, and <code>test</code> channels.</p> </li> </ul>"""
    inference_specification: NotRequired[
        "capo_sagemaker.types.inference_specification.InferenceSpecification"
    ]
    """<p>Specifies details about inference jobs that the algorithm runs, including the following:</p> <ul> <li> <p>The Amazon ECR paths of containers that contain the inference code and model artifacts.</p> </li> <li> <p>The instance types that the algorithm supports for transform jobs and real-time endpoints used for inference.</p> </li> <li> <p>The input and output content formats that the algorithm supports for inference.</p> </li> </ul>"""
    validation_specification: NotRequired[
        "capo_sagemaker.types.algorithm_validation_specification.AlgorithmValidationSpecification"
    ]
    """<p>Specifies configurations for one or more training jobs and that SageMaker runs to test the algorithm's training code and, optionally, one or more batch transform jobs that SageMaker runs to test the algorithm's inference code.</p>"""
    certify_for_marketplace: NotRequired[
        "capo_sagemaker.types.certify_for_marketplace.CertifyForMarketplace"
    ]
    """<p>Whether to certify the algorithm so that it can be listed in Amazon Web Services Marketplace.</p>"""
    tags: NotRequired["capo_sagemaker.types.tag_list.TagList"]
    """<p>An array of key-value pairs. You can use tags to categorize your Amazon Web Services resources in different ways, for example, by purpose, owner, or environment. For more information, see <a href="https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html">Tagging Amazon Web Services Resources</a>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateAlgorithmInput) -> dict:
    out: dict = {}
    if "algorithm_name" in value:
        out["AlgorithmName"] = value["algorithm_name"]
    if "algorithm_description" in value:
        out["AlgorithmDescription"] = value["algorithm_description"]
    if "training_specification" in value:
        import capo_sagemaker.types.training_specification

        out["TrainingSpecification"] = (
            capo_sagemaker.types.training_specification.serialize_aws_json_1_1(
                value["training_specification"]
            )
        )
    if "inference_specification" in value:
        import capo_sagemaker.types.inference_specification

        out["InferenceSpecification"] = (
            capo_sagemaker.types.inference_specification.serialize_aws_json_1_1(
                value["inference_specification"]
            )
        )
    if "validation_specification" in value:
        import capo_sagemaker.types.algorithm_validation_specification

        out["ValidationSpecification"] = (
            capo_sagemaker.types.algorithm_validation_specification.serialize_aws_json_1_1(
                value["validation_specification"]
            )
        )
    if "certify_for_marketplace" in value:
        out["CertifyForMarketplace"] = value["certify_for_marketplace"]
    if "tags" in value:
        import capo_sagemaker.types.tag_list

        out["Tags"] = capo_sagemaker.types.tag_list.serialize_aws_json_1_1(
            value["tags"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateAlgorithmInput:
    out: CreateAlgorithmInput = {}  # type: ignore[typeddict-item]
    if data.get("AlgorithmName") is not None:
        out["algorithm_name"] = data["AlgorithmName"]
    if data.get("AlgorithmDescription") is not None:
        out["algorithm_description"] = data["AlgorithmDescription"]
    if data.get("TrainingSpecification") is not None:
        import capo_sagemaker.types.training_specification

        out["training_specification"] = (
            capo_sagemaker.types.training_specification.deserialize_aws_json_1_1(
                data["TrainingSpecification"]
            )
        )
    if data.get("InferenceSpecification") is not None:
        import capo_sagemaker.types.inference_specification

        out["inference_specification"] = (
            capo_sagemaker.types.inference_specification.deserialize_aws_json_1_1(
                data["InferenceSpecification"]
            )
        )
    if data.get("ValidationSpecification") is not None:
        import capo_sagemaker.types.algorithm_validation_specification

        out["validation_specification"] = (
            capo_sagemaker.types.algorithm_validation_specification.deserialize_aws_json_1_1(
                data["ValidationSpecification"]
            )
        )
    if data.get("CertifyForMarketplace") is not None:
        out["certify_for_marketplace"] = data["CertifyForMarketplace"]
    if data.get("Tags") is not None:
        import capo_sagemaker.types.tag_list

        out["tags"] = capo_sagemaker.types.tag_list.deserialize_aws_json_1_1(
            data["Tags"]
        )
    return out
