"""Generated from Smithy shape ``com.amazonaws.cleanroomsml#ModelTrainingDataChannel``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_cleanroomsml.types.ml_input_channel_arn
    import capo_cleanroomsml.types.model_training_data_channel_name
    import capo_cleanroomsml.types.s3_data_distribution_type


class ModelTrainingDataChannel(TypedDict, closed=True):
    ml_input_channel_arn: (
        "capo_cleanroomsml.types.ml_input_channel_arn.MLInputChannelArn"
    )
    """<p>The Amazon Resource Name (ARN) of the ML input channel for this model training data channel.</p>"""
    channel_name: "capo_cleanroomsml.types.model_training_data_channel_name.ModelTrainingDataChannelName"
    """<p>The name of the training data channel.</p>"""
    s3_data_distribution_type: (
        "capo_cleanroomsml.types.s3_data_distribution_type.S3DataDistributionType"
    )
    """<p>Specifies how the training data stored in Amazon S3 should be distributed to training instances. This parameter controls the data distribution strategy for the training job:</p> <ul> <li> <p> <code>FullyReplicated</code> - The entire dataset is replicated on each training instance. This is suitable for smaller datasets and algorithms that require access to the complete dataset.</p> </li> <li> <p> <code>ShardedByS3Key</code> - The dataset is distributed across training instances based on Amazon S3 key names. This is suitable for larger datasets and distributed training scenarios where each instance processes a subset of the data.</p> </li> </ul>"""


# --- restJson1 ser/de ---
def serialize_json(value: ModelTrainingDataChannel) -> dict:
    out: dict = {}
    out["mlInputChannelArn"] = value["ml_input_channel_arn"]
    out["channelName"] = value["channel_name"]
    import capo_cleanroomsml.types.s3_data_distribution_type

    out["s3DataDistributionType"] = (
        capo_cleanroomsml.types.s3_data_distribution_type.serialize_json(
            value.get("s3_data_distribution_type", "FullyReplicated")
        )
    )
    return out


def deserialize_json(data: dict) -> ModelTrainingDataChannel:
    out: ModelTrainingDataChannel = {}  # type: ignore[typeddict-item]
    if data.get("mlInputChannelArn") is not None:
        out["ml_input_channel_arn"] = data["mlInputChannelArn"]
    else:
        out["ml_input_channel_arn"] = ""
    if data.get("channelName") is not None:
        out["channel_name"] = data["channelName"]
    else:
        out["channel_name"] = ""
    if data.get("s3DataDistributionType") is not None:
        import capo_cleanroomsml.types.s3_data_distribution_type

        out["s3_data_distribution_type"] = (
            capo_cleanroomsml.types.s3_data_distribution_type.deserialize_json(
                data["s3DataDistributionType"]
            )
        )
    else:
        out["s3_data_distribution_type"] = "FullyReplicated"
    return out
