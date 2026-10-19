"""Generated from Smithy shape ``com.amazonaws.cleanroomsml#GetTrainedModelResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_cleanroomsml.types.account_id
    import capo_cleanroomsml.types.configured_model_algorithm_association_arn
    import capo_cleanroomsml.types.environment
    import capo_cleanroomsml.types.hyper_parameters
    import capo_cleanroomsml.types.incremental_training_data_channels_output
    import capo_cleanroomsml.types.kms_key_arn
    import capo_cleanroomsml.types.logs_status
    import capo_cleanroomsml.types.metrics_status
    import capo_cleanroomsml.types.model_training_data_channels
    import capo_cleanroomsml.types.name_string
    import capo_cleanroomsml.types.resource_config
    import capo_cleanroomsml.types.resource_description
    import capo_cleanroomsml.types.status_details
    import capo_cleanroomsml.types.stopping_condition
    import capo_cleanroomsml.types.tag_map
    import capo_cleanroomsml.types.trained_model_arn
    import capo_cleanroomsml.types.trained_model_status
    import capo_cleanroomsml.types.training_input_mode
    import capo_cleanroomsml.types.uuid


class GetTrainedModelResponse(TypedDict, closed=True):
    membership_identifier: "capo_cleanroomsml.types.uuid.UUID"
    """<p>The membership ID of the member that created the trained model.</p>"""
    collaboration_identifier: "capo_cleanroomsml.types.uuid.UUID"
    """<p>The collaboration ID of the collaboration that contains the trained model.</p>"""
    trained_model_arn: "capo_cleanroomsml.types.trained_model_arn.TrainedModelArn"
    """<p>The Amazon Resource Name (ARN) of the trained model.</p>"""
    version_identifier: NotRequired["capo_cleanroomsml.types.uuid.UUID"]
    """<p>The version identifier of the trained model. This unique identifier distinguishes this version from other versions of the same trained model.</p>"""
    incremental_training_data_channels: NotRequired[
        "capo_cleanroomsml.types.incremental_training_data_channels_output.IncrementalTrainingDataChannelsOutput"
    ]
    """<p>Information about the incremental training data channels used to create this version of the trained model. This includes details about the base model that was used for incremental training and the channel configuration.</p>"""
    name: "capo_cleanroomsml.types.name_string.NameString"
    """<p>The name of the trained model.</p>"""
    description: NotRequired[
        "capo_cleanroomsml.types.resource_description.ResourceDescription"
    ]
    """<p>The description of the trained model.</p>"""
    status: "capo_cleanroomsml.types.trained_model_status.TrainedModelStatus"
    """<p>The status of the trained model.</p>"""
    status_details: NotRequired["capo_cleanroomsml.types.status_details.StatusDetails"]
    configured_model_algorithm_association_arn: "capo_cleanroomsml.types.configured_model_algorithm_association_arn.ConfiguredModelAlgorithmAssociationArn"
    """<p>The Amazon Resource Name (ARN) of the configured model algorithm association that was used to create the trained model.</p>"""
    resource_config: NotRequired[
        "capo_cleanroomsml.types.resource_config.ResourceConfig"
    ]
    """<p>The EC2 resource configuration that was used to create the trained model.</p>"""
    training_input_mode: NotRequired[
        "capo_cleanroomsml.types.training_input_mode.TrainingInputMode"
    ]
    """<p>The input mode that was used for accessing the training data when this trained model was created. This indicates how the training data was made available to the training algorithm.</p>"""
    stopping_condition: NotRequired[
        "capo_cleanroomsml.types.stopping_condition.StoppingCondition"
    ]
    """<p>The stopping condition that was used to terminate model training.</p>"""
    metrics_status: NotRequired["capo_cleanroomsml.types.metrics_status.MetricsStatus"]
    """<p>The status of the model metrics.</p>"""
    metrics_status_details: NotRequired["str"]
    """<p>Details about the metrics status for the trained model.</p>"""
    logs_status: NotRequired["capo_cleanroomsml.types.logs_status.LogsStatus"]
    """<p>The logs status for the trained model.</p>"""
    logs_status_details: NotRequired["str"]
    """<p>Details about the logs status for the trained model.</p>"""
    training_container_image_digest: NotRequired["str"]
    """<p>Information about the training image container.</p>"""
    ml_model_training_payer_account_id: NotRequired[
        "capo_cleanroomsml.types.account_id.AccountId"
    ]
    """<p>The account ID of the member that is responsible for paying for model training costs.</p>"""
    create_time: "datetime.datetime"
    """<p>The time at which the trained model was created.</p>"""
    update_time: "datetime.datetime"
    """<p>The most recent time at which the trained model was updated.</p>"""
    hyperparameters: NotRequired[
        "capo_cleanroomsml.types.hyper_parameters.HyperParameters"
    ]
    """<p>The hyperparameters that were used to create the trained model.</p>"""
    environment: NotRequired["capo_cleanroomsml.types.environment.Environment"]
    """<p>The EC2 environment that was used to create the trained model.</p>"""
    kms_key_arn: NotRequired["capo_cleanroomsml.types.kms_key_arn.KmsKeyArn"]
    """<p>The Amazon Resource Name (ARN) of the KMS key. This key is used to encrypt and decrypt customer-owned data in the trained ML model and associated data.</p>"""
    tags: NotRequired["capo_cleanroomsml.types.tag_map.TagMap"]
    """<p>The optional metadata that you applied to the resource to help you categorize and organize them. Each tag consists of a key and an optional value, both of which you define.</p> <p>The following basic restrictions apply to tags:</p> <ul> <li> <p>Maximum number of tags per resource - 50.</p> </li> <li> <p>For each resource, each tag key must be unique, and each tag key can have only one value.</p> </li> <li> <p>Maximum key length - 128 Unicode characters in UTF-8.</p> </li> <li> <p>Maximum value length - 256 Unicode characters in UTF-8.</p> </li> <li> <p>If your tagging schema is used across multiple services and resources, remember that other services may have restrictions on allowed characters. Generally allowed characters are: letters, numbers, and spaces representable in UTF-8, and the following characters: + - = . _ : / @.</p> </li> <li> <p>Tag keys and values are case sensitive.</p> </li> <li> <p>Do not use aws:, AWS:, or any upper or lowercase combination of such as a prefix for keys as it is reserved for AWS use. You cannot edit or delete tag keys with this prefix. Values can have this prefix. If a tag value has aws as its prefix but the key does not, then Clean Rooms ML considers it to be a user tag and will count against the limit of 50 tags. Tags with only the key prefix of aws do not count against your tags per resource limit.</p> </li> </ul>"""
    data_channels: (
        "capo_cleanroomsml.types.model_training_data_channels.ModelTrainingDataChannels"
    )
    """<p>The data channels that were used for the trained model.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetTrainedModelResponse) -> dict:
    out: dict = {}
    out["membershipIdentifier"] = value["membership_identifier"]
    out["collaborationIdentifier"] = value["collaboration_identifier"]
    out["trainedModelArn"] = value["trained_model_arn"]
    if "version_identifier" in value:
        out["versionIdentifier"] = value["version_identifier"]
    if "incremental_training_data_channels" in value:
        import capo_cleanroomsml.types.incremental_training_data_channels_output

        out["incrementalTrainingDataChannels"] = (
            capo_cleanroomsml.types.incremental_training_data_channels_output.serialize_json(
                value["incremental_training_data_channels"]
            )
        )
    out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    import capo_cleanroomsml.types.trained_model_status

    out["status"] = capo_cleanroomsml.types.trained_model_status.serialize_json(
        value["status"]
    )
    if "status_details" in value:
        import capo_cleanroomsml.types.status_details

        out["statusDetails"] = capo_cleanroomsml.types.status_details.serialize_json(
            value["status_details"]
        )
    out["configuredModelAlgorithmAssociationArn"] = value[
        "configured_model_algorithm_association_arn"
    ]
    if "resource_config" in value:
        import capo_cleanroomsml.types.resource_config

        out["resourceConfig"] = capo_cleanroomsml.types.resource_config.serialize_json(
            value["resource_config"]
        )
    if "training_input_mode" in value:
        import capo_cleanroomsml.types.training_input_mode

        out["trainingInputMode"] = (
            capo_cleanroomsml.types.training_input_mode.serialize_json(
                value["training_input_mode"]
            )
        )
    if "stopping_condition" in value:
        import capo_cleanroomsml.types.stopping_condition

        out["stoppingCondition"] = (
            capo_cleanroomsml.types.stopping_condition.serialize_json(
                value["stopping_condition"]
            )
        )
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
    if "training_container_image_digest" in value:
        out["trainingContainerImageDigest"] = value["training_container_image_digest"]
    if "ml_model_training_payer_account_id" in value:
        out["mlModelTrainingPayerAccountId"] = value[
            "ml_model_training_payer_account_id"
        ]
    import capo_cleanroomsml._protocol.serialize

    out["createTime"] = capo_cleanroomsml._protocol.serialize.fmt_date_time(
        value["create_time"]
    )
    import capo_cleanroomsml._protocol.serialize

    out["updateTime"] = capo_cleanroomsml._protocol.serialize.fmt_date_time(
        value["update_time"]
    )
    if "hyperparameters" in value:
        import capo_cleanroomsml.types.hyper_parameters

        out["hyperparameters"] = (
            capo_cleanroomsml.types.hyper_parameters.serialize_json(
                value["hyperparameters"]
            )
        )
    if "environment" in value:
        import capo_cleanroomsml.types.environment

        out["environment"] = capo_cleanroomsml.types.environment.serialize_json(
            value["environment"]
        )
    if "kms_key_arn" in value:
        out["kmsKeyArn"] = value["kms_key_arn"]
    if "tags" in value:
        import capo_cleanroomsml.types.tag_map

        out["tags"] = capo_cleanroomsml.types.tag_map.serialize_json(value["tags"])
    import capo_cleanroomsml.types.model_training_data_channels

    out["dataChannels"] = (
        capo_cleanroomsml.types.model_training_data_channels.serialize_json(
            value["data_channels"]
        )
    )
    return out


def deserialize_json(data: dict) -> GetTrainedModelResponse:
    out: GetTrainedModelResponse = {}  # type: ignore[typeddict-item]
    if data.get("membershipIdentifier") is not None:
        out["membership_identifier"] = data["membershipIdentifier"]
    else:
        out["membership_identifier"] = ""
    if data.get("collaborationIdentifier") is not None:
        out["collaboration_identifier"] = data["collaborationIdentifier"]
    else:
        out["collaboration_identifier"] = ""
    if data.get("trainedModelArn") is not None:
        out["trained_model_arn"] = data["trainedModelArn"]
    else:
        out["trained_model_arn"] = ""
    if data.get("versionIdentifier") is not None:
        out["version_identifier"] = data["versionIdentifier"]
    if data.get("incrementalTrainingDataChannels") is not None:
        import capo_cleanroomsml.types.incremental_training_data_channels_output

        out["incremental_training_data_channels"] = (
            capo_cleanroomsml.types.incremental_training_data_channels_output.deserialize_json(
                data["incrementalTrainingDataChannels"]
            )
        )
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("status") is not None:
        import capo_cleanroomsml.types.trained_model_status

        out["status"] = capo_cleanroomsml.types.trained_model_status.deserialize_json(
            data["status"]
        )
    else:
        import typing

        out["status"] = typing.cast(
            "capo_cleanroomsml.types.trained_model_status.TrainedModelStatus", ""
        )
    if data.get("statusDetails") is not None:
        import capo_cleanroomsml.types.status_details

        out["status_details"] = capo_cleanroomsml.types.status_details.deserialize_json(
            data["statusDetails"]
        )
    if data.get("configuredModelAlgorithmAssociationArn") is not None:
        out["configured_model_algorithm_association_arn"] = data[
            "configuredModelAlgorithmAssociationArn"
        ]
    else:
        out["configured_model_algorithm_association_arn"] = ""
    if data.get("resourceConfig") is not None:
        import capo_cleanroomsml.types.resource_config

        out["resource_config"] = (
            capo_cleanroomsml.types.resource_config.deserialize_json(
                data["resourceConfig"]
            )
        )
    if data.get("trainingInputMode") is not None:
        import capo_cleanroomsml.types.training_input_mode

        out["training_input_mode"] = (
            capo_cleanroomsml.types.training_input_mode.deserialize_json(
                data["trainingInputMode"]
            )
        )
    if data.get("stoppingCondition") is not None:
        import capo_cleanroomsml.types.stopping_condition

        out["stopping_condition"] = (
            capo_cleanroomsml.types.stopping_condition.deserialize_json(
                data["stoppingCondition"]
            )
        )
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
    if data.get("trainingContainerImageDigest") is not None:
        out["training_container_image_digest"] = data["trainingContainerImageDigest"]
    if data.get("mlModelTrainingPayerAccountId") is not None:
        out["ml_model_training_payer_account_id"] = data[
            "mlModelTrainingPayerAccountId"
        ]
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
    if data.get("hyperparameters") is not None:
        import capo_cleanroomsml.types.hyper_parameters

        out["hyperparameters"] = (
            capo_cleanroomsml.types.hyper_parameters.deserialize_json(
                data["hyperparameters"]
            )
        )
    if data.get("environment") is not None:
        import capo_cleanroomsml.types.environment

        out["environment"] = capo_cleanroomsml.types.environment.deserialize_json(
            data["environment"]
        )
    if data.get("kmsKeyArn") is not None:
        out["kms_key_arn"] = data["kmsKeyArn"]
    if data.get("tags") is not None:
        import capo_cleanroomsml.types.tag_map

        out["tags"] = capo_cleanroomsml.types.tag_map.deserialize_json(data["tags"])
    if data.get("dataChannels") is not None:
        import capo_cleanroomsml.types.model_training_data_channels

        out["data_channels"] = (
            capo_cleanroomsml.types.model_training_data_channels.deserialize_json(
                data["dataChannels"]
            )
        )
    else:
        out["data_channels"] = []
    return out
