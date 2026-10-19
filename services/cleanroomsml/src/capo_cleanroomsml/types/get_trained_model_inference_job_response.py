"""Generated from Smithy shape ``com.amazonaws.cleanroomsml#GetTrainedModelInferenceJobResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cleanroomsml.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import capo_cleanroomsml.types.account_id
    import capo_cleanroomsml.types.configured_model_algorithm_association_arn
    import capo_cleanroomsml.types.inference_container_execution_parameters
    import capo_cleanroomsml.types.inference_environment_map
    import capo_cleanroomsml.types.inference_output_configuration
    import capo_cleanroomsml.types.inference_resource_config
    import capo_cleanroomsml.types.kms_key_arn
    import capo_cleanroomsml.types.logs_status
    import capo_cleanroomsml.types.metrics_status
    import capo_cleanroomsml.types.model_inference_data_source
    import capo_cleanroomsml.types.name_string
    import capo_cleanroomsml.types.resource_description
    import capo_cleanroomsml.types.status_details
    import capo_cleanroomsml.types.tag_map
    import capo_cleanroomsml.types.trained_model_arn
    import capo_cleanroomsml.types.trained_model_inference_job_arn
    import capo_cleanroomsml.types.trained_model_inference_job_status
    import capo_cleanroomsml.types.uuid


class GetTrainedModelInferenceJobResponse(TypedDict, closed=True):
    create_time: "datetime.datetime"
    """<p>The time at which the trained model inference job was created.</p>"""
    update_time: "datetime.datetime"
    """<p>The most recent time at which the trained model inference job was updated.</p>"""
    trained_model_inference_job_arn: "capo_cleanroomsml.types.trained_model_inference_job_arn.TrainedModelInferenceJobArn"
    """<p>The Amazon Resource Name (ARN) of the trained model inference job.</p>"""
    configured_model_algorithm_association_arn: NotRequired[
        "capo_cleanroomsml.types.configured_model_algorithm_association_arn.ConfiguredModelAlgorithmAssociationArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the configured model algorithm association that was used for the trained model inference job.</p>"""
    name: "capo_cleanroomsml.types.name_string.NameString"
    """<p>The name of the trained model inference job.</p>"""
    status: "capo_cleanroomsml.types.trained_model_inference_job_status.TrainedModelInferenceJobStatus"
    """<p>The status of the trained model inference job.</p>"""
    trained_model_arn: "capo_cleanroomsml.types.trained_model_arn.TrainedModelArn"
    """<p>The Amazon Resource Name (ARN) for the trained model that was used for the trained model inference job.</p>"""
    trained_model_version_identifier: NotRequired["capo_cleanroomsml.types.uuid.UUID"]
    """<p>The version identifier of the trained model used for this inference job. This identifies the specific version of the trained model that was used to generate the inference results.</p>"""
    resource_config: (
        "capo_cleanroomsml.types.inference_resource_config.InferenceResourceConfig"
    )
    """<p>The resource configuration information for the trained model inference job.</p>"""
    output_configuration: "capo_cleanroomsml.types.inference_output_configuration.InferenceOutputConfiguration"
    """<p>The output configuration information for the trained model inference job.</p>"""
    membership_identifier: "capo_cleanroomsml.types.uuid.UUID"
    """<p>The membership ID of the membership that contains the trained model inference job.</p>"""
    data_source: (
        "capo_cleanroomsml.types.model_inference_data_source.ModelInferenceDataSource"
    )
    """<p>The data source that was used for the trained model inference job.</p>"""
    container_execution_parameters: NotRequired[
        "capo_cleanroomsml.types.inference_container_execution_parameters.InferenceContainerExecutionParameters"
    ]
    """<p>The execution parameters for the model inference job container.</p>"""
    status_details: NotRequired["capo_cleanroomsml.types.status_details.StatusDetails"]
    description: NotRequired[
        "capo_cleanroomsml.types.resource_description.ResourceDescription"
    ]
    """<p>The description of the trained model inference job.</p>"""
    inference_container_image_digest: NotRequired["str"]
    """<p>Information about the training container image.</p>"""
    environment: NotRequired[
        "capo_cleanroomsml.types.inference_environment_map.InferenceEnvironmentMap"
    ]
    """<p>The environment variables to set in the Docker container.</p>"""
    kms_key_arn: NotRequired["capo_cleanroomsml.types.kms_key_arn.KmsKeyArn"]
    """<p>The Amazon Resource Name (ARN) of the KMS key. This key is used to encrypt and decrypt customer-owned data in the ML inference job and associated data.</p>"""
    metrics_status: NotRequired["capo_cleanroomsml.types.metrics_status.MetricsStatus"]
    """<p>The metrics status for the trained model inference job.</p>"""
    metrics_status_details: NotRequired["str"]
    """<p>Details about the metrics status for the trained model inference job.</p>"""
    logs_status: NotRequired["capo_cleanroomsml.types.logs_status.LogsStatus"]
    """<p>The logs status for the trained model inference job.</p>"""
    logs_status_details: NotRequired["str"]
    """<p>Details about the logs status for the trained model inference job.</p>"""
    tags: NotRequired["capo_cleanroomsml.types.tag_map.TagMap"]
    """<p>The optional metadata that you applied to the resource to help you categorize and organize them. Each tag consists of a key and an optional value, both of which you define.</p> <p>The following basic restrictions apply to tags:</p> <ul> <li> <p>Maximum number of tags per resource - 50.</p> </li> <li> <p>For each resource, each tag key must be unique, and each tag key can have only one value.</p> </li> <li> <p>Maximum key length - 128 Unicode characters in UTF-8.</p> </li> <li> <p>Maximum value length - 256 Unicode characters in UTF-8.</p> </li> <li> <p>If your tagging schema is used across multiple services and resources, remember that other services may have restrictions on allowed characters. Generally allowed characters are: letters, numbers, and spaces representable in UTF-8, and the following characters: + - = . _ : / @.</p> </li> <li> <p>Tag keys and values are case sensitive.</p> </li> <li> <p>Do not use aws:, AWS:, or any upper or lowercase combination of such as a prefix for keys as it is reserved for AWS use. You cannot edit or delete tag keys with this prefix. Values can have this prefix. If a tag value has aws as its prefix but the key does not, then Clean Rooms ML considers it to be a user tag and will count against the limit of 50 tags. Tags with only the key prefix of aws do not count against your tags per resource limit.</p> </li> </ul>"""
    ml_model_inference_payer_account_id: NotRequired[
        "capo_cleanroomsml.types.account_id.AccountId"
    ]
    """<p>The account ID of the member that is responsible for paying for model inference costs.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetTrainedModelInferenceJobResponse) -> dict:
    out: dict = {}
    import capo_cleanroomsml._protocol.serialize

    out["createTime"] = capo_cleanroomsml._protocol.serialize.fmt_date_time(
        value["create_time"]
    )
    import capo_cleanroomsml._protocol.serialize

    out["updateTime"] = capo_cleanroomsml._protocol.serialize.fmt_date_time(
        value["update_time"]
    )
    out["trainedModelInferenceJobArn"] = value["trained_model_inference_job_arn"]
    if "configured_model_algorithm_association_arn" in value:
        out["configuredModelAlgorithmAssociationArn"] = value[
            "configured_model_algorithm_association_arn"
        ]
    out["name"] = value["name"]
    import capo_cleanroomsml.types.trained_model_inference_job_status

    out["status"] = (
        capo_cleanroomsml.types.trained_model_inference_job_status.serialize_json(
            value["status"]
        )
    )
    out["trainedModelArn"] = value["trained_model_arn"]
    if "trained_model_version_identifier" in value:
        out["trainedModelVersionIdentifier"] = value["trained_model_version_identifier"]
    import capo_cleanroomsml.types.inference_resource_config

    out["resourceConfig"] = (
        capo_cleanroomsml.types.inference_resource_config.serialize_json(
            value["resource_config"]
        )
    )
    import capo_cleanroomsml.types.inference_output_configuration

    out["outputConfiguration"] = (
        capo_cleanroomsml.types.inference_output_configuration.serialize_json(
            value["output_configuration"]
        )
    )
    out["membershipIdentifier"] = value["membership_identifier"]
    import capo_cleanroomsml.types.model_inference_data_source

    out["dataSource"] = (
        capo_cleanroomsml.types.model_inference_data_source.serialize_json(
            value["data_source"]
        )
    )
    if "container_execution_parameters" in value:
        import capo_cleanroomsml.types.inference_container_execution_parameters

        out["containerExecutionParameters"] = (
            capo_cleanroomsml.types.inference_container_execution_parameters.serialize_json(
                value["container_execution_parameters"]
            )
        )
    if "status_details" in value:
        import capo_cleanroomsml.types.status_details

        out["statusDetails"] = capo_cleanroomsml.types.status_details.serialize_json(
            value["status_details"]
        )
    if "description" in value:
        out["description"] = value["description"]
    if "inference_container_image_digest" in value:
        out["inferenceContainerImageDigest"] = value["inference_container_image_digest"]
    if "environment" in value:
        import capo_cleanroomsml.types.inference_environment_map

        out["environment"] = (
            capo_cleanroomsml.types.inference_environment_map.serialize_json(
                value["environment"]
            )
        )
    if "kms_key_arn" in value:
        out["kmsKeyArn"] = value["kms_key_arn"]
    if "metrics_status" in value:
        import capo_cleanroomsml.types.metrics_status

        out["metricsStatus"] = capo_cleanroomsml.types.metrics_status.serialize_json(
            value["metrics_status"]
        )
    if "metrics_status_details" in value:
        out["metricsStatusDetails"] = value["metrics_status_details"]
    if "logs_status" in value:
        import capo_cleanroomsml.types.logs_status

        out["logsStatus"] = capo_cleanroomsml.types.logs_status.serialize_json(
            value["logs_status"]
        )
    if "logs_status_details" in value:
        out["logsStatusDetails"] = value["logs_status_details"]
    if "tags" in value:
        import capo_cleanroomsml.types.tag_map

        out["tags"] = capo_cleanroomsml.types.tag_map.serialize_json(value["tags"])
    if "ml_model_inference_payer_account_id" in value:
        out["mlModelInferencePayerAccountId"] = value[
            "ml_model_inference_payer_account_id"
        ]
    return out


def deserialize_json(data: dict) -> GetTrainedModelInferenceJobResponse:
    out: GetTrainedModelInferenceJobResponse = {}  # type: ignore[typeddict-item]
    if data.get("createTime") is not None:
        import datetime

        out["create_time"] = datetime.datetime.fromisoformat(
            data["createTime"].replace("Z", "+00:00")
        )
    else:
        import datetime

        out["create_time"] = datetime.datetime.fromtimestamp(
            0, tz=datetime.timezone.utc
        )
    if data.get("updateTime") is not None:
        import datetime

        out["update_time"] = datetime.datetime.fromisoformat(
            data["updateTime"].replace("Z", "+00:00")
        )
    else:
        import datetime

        out["update_time"] = datetime.datetime.fromtimestamp(
            0, tz=datetime.timezone.utc
        )
    if data.get("trainedModelInferenceJobArn") is not None:
        out["trained_model_inference_job_arn"] = data["trainedModelInferenceJobArn"]
    else:
        out["trained_model_inference_job_arn"] = ""
    if data.get("configuredModelAlgorithmAssociationArn") is not None:
        out["configured_model_algorithm_association_arn"] = data[
            "configuredModelAlgorithmAssociationArn"
        ]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("status") is not None:
        import capo_cleanroomsml.types.trained_model_inference_job_status

        out["status"] = (
            capo_cleanroomsml.types.trained_model_inference_job_status.deserialize_json(
                data["status"]
            )
        )
    else:
        import typing

        out["status"] = typing.cast(
            "capo_cleanroomsml.types.trained_model_inference_job_status.TrainedModelInferenceJobStatus",
            "",
        )
    if data.get("trainedModelArn") is not None:
        out["trained_model_arn"] = data["trainedModelArn"]
    else:
        out["trained_model_arn"] = ""
    if data.get("trainedModelVersionIdentifier") is not None:
        out["trained_model_version_identifier"] = data["trainedModelVersionIdentifier"]
    if data.get("resourceConfig") is not None:
        import capo_cleanroomsml.types.inference_resource_config

        out["resource_config"] = (
            capo_cleanroomsml.types.inference_resource_config.deserialize_json(
                data["resourceConfig"]
            )
        )
    else:
        raise DeserializationError(
            "GetTrainedModelInferenceJobResponse.resource_config required"
        )
    if data.get("outputConfiguration") is not None:
        import capo_cleanroomsml.types.inference_output_configuration

        out["output_configuration"] = (
            capo_cleanroomsml.types.inference_output_configuration.deserialize_json(
                data["outputConfiguration"]
            )
        )
    else:
        raise DeserializationError(
            "GetTrainedModelInferenceJobResponse.output_configuration required"
        )
    if data.get("membershipIdentifier") is not None:
        out["membership_identifier"] = data["membershipIdentifier"]
    else:
        out["membership_identifier"] = ""
    if data.get("dataSource") is not None:
        import capo_cleanroomsml.types.model_inference_data_source

        out["data_source"] = (
            capo_cleanroomsml.types.model_inference_data_source.deserialize_json(
                data["dataSource"]
            )
        )
    else:
        raise DeserializationError(
            "GetTrainedModelInferenceJobResponse.data_source required"
        )
    if data.get("containerExecutionParameters") is not None:
        import capo_cleanroomsml.types.inference_container_execution_parameters

        out["container_execution_parameters"] = (
            capo_cleanroomsml.types.inference_container_execution_parameters.deserialize_json(
                data["containerExecutionParameters"]
            )
        )
    if data.get("statusDetails") is not None:
        import capo_cleanroomsml.types.status_details

        out["status_details"] = capo_cleanroomsml.types.status_details.deserialize_json(
            data["statusDetails"]
        )
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("inferenceContainerImageDigest") is not None:
        out["inference_container_image_digest"] = data["inferenceContainerImageDigest"]
    if data.get("environment") is not None:
        import capo_cleanroomsml.types.inference_environment_map

        out["environment"] = (
            capo_cleanroomsml.types.inference_environment_map.deserialize_json(
                data["environment"]
            )
        )
    if data.get("kmsKeyArn") is not None:
        out["kms_key_arn"] = data["kmsKeyArn"]
    if data.get("metricsStatus") is not None:
        import capo_cleanroomsml.types.metrics_status

        out["metrics_status"] = capo_cleanroomsml.types.metrics_status.deserialize_json(
            data["metricsStatus"]
        )
    if data.get("metricsStatusDetails") is not None:
        out["metrics_status_details"] = data["metricsStatusDetails"]
    if data.get("logsStatus") is not None:
        import capo_cleanroomsml.types.logs_status

        out["logs_status"] = capo_cleanroomsml.types.logs_status.deserialize_json(
            data["logsStatus"]
        )
    if data.get("logsStatusDetails") is not None:
        out["logs_status_details"] = data["logsStatusDetails"]
    if data.get("tags") is not None:
        import capo_cleanroomsml.types.tag_map

        out["tags"] = capo_cleanroomsml.types.tag_map.deserialize_json(data["tags"])
    if data.get("mlModelInferencePayerAccountId") is not None:
        out["ml_model_inference_payer_account_id"] = data[
            "mlModelInferencePayerAccountId"
        ]
    return out
