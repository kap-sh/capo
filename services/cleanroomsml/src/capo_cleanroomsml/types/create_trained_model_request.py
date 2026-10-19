"""Generated from Smithy shape ``com.amazonaws.cleanroomsml#CreateTrainedModelRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cleanroomsml.errors import DeserializationError

if TYPE_CHECKING:
    import capo_cleanroomsml.types.account_id
    import capo_cleanroomsml.types.configured_model_algorithm_association_arn
    import capo_cleanroomsml.types.environment
    import capo_cleanroomsml.types.hyper_parameters
    import capo_cleanroomsml.types.incremental_training_data_channels
    import capo_cleanroomsml.types.kms_key_arn
    import capo_cleanroomsml.types.model_training_data_channels
    import capo_cleanroomsml.types.name_string
    import capo_cleanroomsml.types.resource_config
    import capo_cleanroomsml.types.resource_description
    import capo_cleanroomsml.types.stopping_condition
    import capo_cleanroomsml.types.tag_map
    import capo_cleanroomsml.types.training_input_mode
    import capo_cleanroomsml.types.uuid


class CreateTrainedModelRequest(TypedDict, closed=True):
    membership_identifier: "capo_cleanroomsml.types.uuid.UUID"
    """<p>The membership ID of the member that is creating the trained model.</p>"""
    name: "capo_cleanroomsml.types.name_string.NameString"
    """<p>The name of the trained model.</p>"""
    configured_model_algorithm_association_arn: "capo_cleanroomsml.types.configured_model_algorithm_association_arn.ConfiguredModelAlgorithmAssociationArn"
    """<p>The associated configured model algorithm used to train this model.</p>"""
    hyperparameters: NotRequired[
        "capo_cleanroomsml.types.hyper_parameters.HyperParameters"
    ]
    """<p>Algorithm-specific parameters that influence the quality of the model. You set hyperparameters before you start the learning process.</p>"""
    environment: NotRequired["capo_cleanroomsml.types.environment.Environment"]
    """<p>The environment variables to set in the Docker container.</p>"""
    resource_config: "capo_cleanroomsml.types.resource_config.ResourceConfig"
    """<p>Information about the EC2 resources that are used to train this model.</p>"""
    stopping_condition: NotRequired[
        "capo_cleanroomsml.types.stopping_condition.StoppingCondition"
    ]
    """<p>The criteria that is used to stop model training.</p>"""
    incremental_training_data_channels: NotRequired[
        "capo_cleanroomsml.types.incremental_training_data_channels.IncrementalTrainingDataChannels"
    ]
    """<p>Specifies the incremental training data channels for the trained model. </p> <p>Incremental training allows you to create a new trained model with updates without retraining from scratch. You can specify up to one incremental training data channel that references a previously trained model and its version.</p> <p>Limit: Maximum of 20 channels total (including both <code>incrementalTrainingDataChannels</code> and <code>dataChannels</code>).</p>"""
    data_channels: (
        "capo_cleanroomsml.types.model_training_data_channels.ModelTrainingDataChannels"
    )
    """<p>Defines the data channels that are used as input for the trained model request.</p> <p>Limit: Maximum of 20 channels total (including both <code>dataChannels</code> and <code>incrementalTrainingDataChannels</code>).</p>"""
    training_input_mode: NotRequired[
        "capo_cleanroomsml.types.training_input_mode.TrainingInputMode"
    ]
    """<p>The input mode for accessing the training data. This parameter determines how the training data is made available to the training algorithm. Valid values are:</p> <ul> <li> <p> <code>File</code> - The training data is downloaded to the training instance and made available as files.</p> </li> <li> <p> <code>FastFile</code> - The training data is streamed directly from Amazon S3 to the training algorithm, providing faster access for large datasets.</p> </li> <li> <p> <code>Pipe</code> - The training data is streamed to the training algorithm using named pipes, which can improve performance for certain algorithms.</p> </li> </ul>"""
    description: NotRequired[
        "capo_cleanroomsml.types.resource_description.ResourceDescription"
    ]
    """<p>The description of the trained model.</p>"""
    kms_key_arn: NotRequired["capo_cleanroomsml.types.kms_key_arn.KmsKeyArn"]
    """<p>The Amazon Resource Name (ARN) of the KMS key. This key is used to encrypt and decrypt customer-owned data in the trained ML model and the associated data.</p>"""
    tags: NotRequired["capo_cleanroomsml.types.tag_map.TagMap"]
    """<p>The optional metadata that you apply to the resource to help you categorize and organize them. Each tag consists of a key and an optional value, both of which you define.</p> <p>The following basic restrictions apply to tags:</p> <ul> <li> <p>Maximum number of tags per resource - 50.</p> </li> <li> <p>For each resource, each tag key must be unique, and each tag key can have only one value.</p> </li> <li> <p>Maximum key length - 128 Unicode characters in UTF-8.</p> </li> <li> <p>Maximum value length - 256 Unicode characters in UTF-8.</p> </li> <li> <p>If your tagging schema is used across multiple services and resources, remember that other services may have restrictions on allowed characters. Generally allowed characters are: letters, numbers, and spaces representable in UTF-8, and the following characters: + - = . _ : / @.</p> </li> <li> <p>Tag keys and values are case sensitive.</p> </li> <li> <p>Do not use aws:, AWS:, or any upper or lowercase combination of such as a prefix for keys as it is reserved for AWS use. You cannot edit or delete tag keys with this prefix. Values can have this prefix. If a tag value has aws as its prefix but the key does not, then Clean Rooms ML considers it to be a user tag and will count against the limit of 50 tags. Tags with only the key prefix of aws do not count against your tags per resource limit.</p> </li> </ul>"""
    ml_model_training_payer_account_id: NotRequired[
        "capo_cleanroomsml.types.account_id.AccountId"
    ]
    """<p>The account ID of the member that is responsible for paying for model training costs.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateTrainedModelRequest) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    out["configuredModelAlgorithmAssociationArn"] = value[
        "configured_model_algorithm_association_arn"
    ]
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
    import capo_cleanroomsml.types.resource_config

    out["resourceConfig"] = capo_cleanroomsml.types.resource_config.serialize_json(
        value["resource_config"]
    )
    if "stopping_condition" in value:
        import capo_cleanroomsml.types.stopping_condition

        out["stoppingCondition"] = (
            capo_cleanroomsml.types.stopping_condition.serialize_json(
                value["stopping_condition"]
            )
        )
    if "incremental_training_data_channels" in value:
        import capo_cleanroomsml.types.incremental_training_data_channels

        out["incrementalTrainingDataChannels"] = (
            capo_cleanroomsml.types.incremental_training_data_channels.serialize_json(
                value["incremental_training_data_channels"]
            )
        )
    import capo_cleanroomsml.types.model_training_data_channels

    out["dataChannels"] = (
        capo_cleanroomsml.types.model_training_data_channels.serialize_json(
            value["data_channels"]
        )
    )
    if "training_input_mode" in value:
        import capo_cleanroomsml.types.training_input_mode

        out["trainingInputMode"] = (
            capo_cleanroomsml.types.training_input_mode.serialize_json(
                value["training_input_mode"]
            )
        )
    if "description" in value:
        out["description"] = value["description"]
    if "kms_key_arn" in value:
        out["kmsKeyArn"] = value["kms_key_arn"]
    if "tags" in value:
        import capo_cleanroomsml.types.tag_map

        out["tags"] = capo_cleanroomsml.types.tag_map.serialize_json(value["tags"])
    if "ml_model_training_payer_account_id" in value:
        out["mlModelTrainingPayerAccountId"] = value[
            "ml_model_training_payer_account_id"
        ]
    return out


def deserialize_json(data: dict) -> CreateTrainedModelRequest:
    out: CreateTrainedModelRequest = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        raise DeserializationError("CreateTrainedModelRequest.name required")
    if data.get("configuredModelAlgorithmAssociationArn") is not None:
        out["configured_model_algorithm_association_arn"] = data[
            "configuredModelAlgorithmAssociationArn"
        ]
    else:
        raise DeserializationError(
            "CreateTrainedModelRequest.configured_model_algorithm_association_arn required"
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
    if data.get("resourceConfig") is not None:
        import capo_cleanroomsml.types.resource_config

        out["resource_config"] = (
            capo_cleanroomsml.types.resource_config.deserialize_json(
                data["resourceConfig"]
            )
        )
    else:
        raise DeserializationError("CreateTrainedModelRequest.resource_config required")
    if data.get("stoppingCondition") is not None:
        import capo_cleanroomsml.types.stopping_condition

        out["stopping_condition"] = (
            capo_cleanroomsml.types.stopping_condition.deserialize_json(
                data["stoppingCondition"]
            )
        )
    if data.get("incrementalTrainingDataChannels") is not None:
        import capo_cleanroomsml.types.incremental_training_data_channels

        out["incremental_training_data_channels"] = (
            capo_cleanroomsml.types.incremental_training_data_channels.deserialize_json(
                data["incrementalTrainingDataChannels"]
            )
        )
    if data.get("dataChannels") is not None:
        import capo_cleanroomsml.types.model_training_data_channels

        out["data_channels"] = (
            capo_cleanroomsml.types.model_training_data_channels.deserialize_json(
                data["dataChannels"]
            )
        )
    else:
        raise DeserializationError("CreateTrainedModelRequest.data_channels required")
    if data.get("trainingInputMode") is not None:
        import capo_cleanroomsml.types.training_input_mode

        out["training_input_mode"] = (
            capo_cleanroomsml.types.training_input_mode.deserialize_json(
                data["trainingInputMode"]
            )
        )
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("kmsKeyArn") is not None:
        out["kms_key_arn"] = data["kmsKeyArn"]
    if data.get("tags") is not None:
        import capo_cleanroomsml.types.tag_map

        out["tags"] = capo_cleanroomsml.types.tag_map.deserialize_json(data["tags"])
    if data.get("mlModelTrainingPayerAccountId") is not None:
        out["ml_model_training_payer_account_id"] = data[
            "mlModelTrainingPayerAccountId"
        ]
    return out
