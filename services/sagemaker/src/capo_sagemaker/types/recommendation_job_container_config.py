"""Generated from Smithy shape ``com.amazonaws.sagemaker#RecommendationJobContainerConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.recommendation_job_data_input_config
    import capo_sagemaker.types.recommendation_job_framework_version
    import capo_sagemaker.types.recommendation_job_payload_config
    import capo_sagemaker.types.recommendation_job_supported_endpoint_type
    import capo_sagemaker.types.recommendation_job_supported_instance_types
    import capo_sagemaker.types.recommendation_job_supported_response_mime_types
    import capo_sagemaker.types.string


class RecommendationJobContainerConfig(TypedDict, closed=True):
    domain: NotRequired["capo_sagemaker.types.string.String"]
    """<p>The machine learning domain of the model and its components.</p> <p>Valid Values: <code>COMPUTER_VISION | NATURAL_LANGUAGE_PROCESSING | MACHINE_LEARNING</code> </p>"""
    task: NotRequired["capo_sagemaker.types.string.String"]
    """<p>The machine learning task that the model accomplishes.</p> <p>Valid Values: <code>IMAGE_CLASSIFICATION | OBJECT_DETECTION | TEXT_GENERATION | IMAGE_SEGMENTATION | FILL_MASK | CLASSIFICATION | REGRESSION | OTHER</code> </p>"""
    framework: NotRequired["capo_sagemaker.types.string.String"]
    """<p>The machine learning framework of the container image.</p> <p>Valid Values: <code>TENSORFLOW | PYTORCH | XGBOOST | SAGEMAKER-SCIKIT-LEARN</code> </p>"""
    framework_version: NotRequired[
        "capo_sagemaker.types.recommendation_job_framework_version.RecommendationJobFrameworkVersion"
    ]
    """<p>The framework version of the container image.</p>"""
    payload_config: NotRequired[
        "capo_sagemaker.types.recommendation_job_payload_config.RecommendationJobPayloadConfig"
    ]
    """<p>Specifies the <code>SamplePayloadUrl</code> and all other sample payload-related fields.</p>"""
    nearest_model_name: NotRequired["capo_sagemaker.types.string.String"]
    """<p>The name of a pre-trained machine learning model benchmarked by Amazon SageMaker Inference Recommender that matches your model.</p> <p>Valid Values: <code>efficientnetb7 | unet | xgboost | faster-rcnn-resnet101 | nasnetlarge | vgg16 | inception-v3 | mask-rcnn | sagemaker-scikit-learn | densenet201-gluon | resnet18v2-gluon | xception | densenet201 | yolov4 | resnet152 | bert-base-cased | xceptionV1-keras | resnet50 | retinanet</code> </p>"""
    supported_instance_types: NotRequired[
        "capo_sagemaker.types.recommendation_job_supported_instance_types.RecommendationJobSupportedInstanceTypes"
    ]
    """<p>A list of the instance types that are used to generate inferences in real-time.</p>"""
    supported_endpoint_type: NotRequired[
        "capo_sagemaker.types.recommendation_job_supported_endpoint_type.RecommendationJobSupportedEndpointType"
    ]
    """<p>The endpoint type to receive recommendations for. By default this is null, and the results of the inference recommendation job return a combined list of both real-time and serverless benchmarks. By specifying a value for this field, you can receive a longer list of benchmarks for the desired endpoint type.</p>"""
    data_input_config: NotRequired[
        "capo_sagemaker.types.recommendation_job_data_input_config.RecommendationJobDataInputConfig"
    ]
    """<p>Specifies the name and shape of the expected data inputs for your trained model with a JSON dictionary form. This field is used for optimizing your model using SageMaker Neo. For more information, see <a href="https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_InputConfig.html#sagemaker-Type-InputConfig-DataInputConfig">DataInputConfig</a>.</p>"""
    supported_response_mime_types: NotRequired[
        "capo_sagemaker.types.recommendation_job_supported_response_mime_types.RecommendationJobSupportedResponseMIMETypes"
    ]
    """<p>The supported MIME types for the output data.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RecommendationJobContainerConfig) -> dict:
    out: dict = {}
    if "domain" in value:
        out["Domain"] = value["domain"]
    if "task" in value:
        out["Task"] = value["task"]
    if "framework" in value:
        out["Framework"] = value["framework"]
    if "framework_version" in value:
        out["FrameworkVersion"] = value["framework_version"]
    if "payload_config" in value:
        import capo_sagemaker.types.recommendation_job_payload_config

        out["PayloadConfig"] = (
            capo_sagemaker.types.recommendation_job_payload_config.serialize_aws_json_1_1(
                value["payload_config"]
            )
        )
    if "nearest_model_name" in value:
        out["NearestModelName"] = value["nearest_model_name"]
    if "supported_instance_types" in value:
        import capo_sagemaker.types.recommendation_job_supported_instance_types

        out["SupportedInstanceTypes"] = (
            capo_sagemaker.types.recommendation_job_supported_instance_types.serialize_aws_json_1_1(
                value["supported_instance_types"]
            )
        )
    if "supported_endpoint_type" in value:
        import capo_sagemaker.types.recommendation_job_supported_endpoint_type

        out["SupportedEndpointType"] = (
            capo_sagemaker.types.recommendation_job_supported_endpoint_type.serialize_aws_json_1_1(
                value["supported_endpoint_type"]
            )
        )
    if "data_input_config" in value:
        out["DataInputConfig"] = value["data_input_config"]
    if "supported_response_mime_types" in value:
        import capo_sagemaker.types.recommendation_job_supported_response_mime_types

        out["SupportedResponseMIMETypes"] = (
            capo_sagemaker.types.recommendation_job_supported_response_mime_types.serialize_aws_json_1_1(
                value["supported_response_mime_types"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> RecommendationJobContainerConfig:
    out: RecommendationJobContainerConfig = {}  # type: ignore[typeddict-item]
    if data.get("Domain") is not None:
        out["domain"] = data["Domain"]
    if data.get("Task") is not None:
        out["task"] = data["Task"]
    if data.get("Framework") is not None:
        out["framework"] = data["Framework"]
    if data.get("FrameworkVersion") is not None:
        out["framework_version"] = data["FrameworkVersion"]
    if data.get("PayloadConfig") is not None:
        import capo_sagemaker.types.recommendation_job_payload_config

        out["payload_config"] = (
            capo_sagemaker.types.recommendation_job_payload_config.deserialize_aws_json_1_1(
                data["PayloadConfig"]
            )
        )
    if data.get("NearestModelName") is not None:
        out["nearest_model_name"] = data["NearestModelName"]
    if data.get("SupportedInstanceTypes") is not None:
        import capo_sagemaker.types.recommendation_job_supported_instance_types

        out["supported_instance_types"] = (
            capo_sagemaker.types.recommendation_job_supported_instance_types.deserialize_aws_json_1_1(
                data["SupportedInstanceTypes"]
            )
        )
    if data.get("SupportedEndpointType") is not None:
        import capo_sagemaker.types.recommendation_job_supported_endpoint_type

        out["supported_endpoint_type"] = (
            capo_sagemaker.types.recommendation_job_supported_endpoint_type.deserialize_aws_json_1_1(
                data["SupportedEndpointType"]
            )
        )
    if data.get("DataInputConfig") is not None:
        out["data_input_config"] = data["DataInputConfig"]
    if data.get("SupportedResponseMIMETypes") is not None:
        import capo_sagemaker.types.recommendation_job_supported_response_mime_types

        out["supported_response_mime_types"] = (
            capo_sagemaker.types.recommendation_job_supported_response_mime_types.deserialize_aws_json_1_1(
                data["SupportedResponseMIMETypes"]
            )
        )
    return out
