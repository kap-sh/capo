"""Generated from Smithy shape ``com.amazonaws.connect#InstanceStorageConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connect.types.association_id
    import capo_connect.types.kinesis_firehose_config
    import capo_connect.types.kinesis_stream_config
    import capo_connect.types.kinesis_video_stream_config
    import capo_connect.types.s3_config
    import capo_connect.types.storage_type


class InstanceStorageConfig(TypedDict, closed=True):
    association_id: NotRequired["capo_connect.types.association_id.AssociationId"]
    """<p>The existing association identifier that uniquely identifies the resource type and storage config for the given instance ID.</p>"""
    storage_type: "capo_connect.types.storage_type.StorageType"
    """<p>A valid storage type.</p>"""
    s3_config: NotRequired["capo_connect.types.s3_config.S3Config"]
    """<p>The S3 bucket configuration.</p>"""
    kinesis_video_stream_config: NotRequired[
        "capo_connect.types.kinesis_video_stream_config.KinesisVideoStreamConfig"
    ]
    """<p>The configuration of the Kinesis video stream.</p>"""
    kinesis_stream_config: NotRequired[
        "capo_connect.types.kinesis_stream_config.KinesisStreamConfig"
    ]
    """<p>The configuration of the Kinesis data stream.</p>"""
    kinesis_firehose_config: NotRequired[
        "capo_connect.types.kinesis_firehose_config.KinesisFirehoseConfig"
    ]
    """<p>The configuration of the Kinesis Firehose delivery stream.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: InstanceStorageConfig) -> dict:
    out: dict = {}
    if "association_id" in value:
        out["AssociationId"] = value["association_id"]
    import capo_connect.types.storage_type

    out["StorageType"] = capo_connect.types.storage_type.serialize_json(
        value["storage_type"]
    )
    if "s3_config" in value:
        import capo_connect.types.s3_config

        out["S3Config"] = capo_connect.types.s3_config.serialize_json(
            value["s3_config"]
        )
    if "kinesis_video_stream_config" in value:
        import capo_connect.types.kinesis_video_stream_config

        out["KinesisVideoStreamConfig"] = (
            capo_connect.types.kinesis_video_stream_config.serialize_json(
                value["kinesis_video_stream_config"]
            )
        )
    if "kinesis_stream_config" in value:
        import capo_connect.types.kinesis_stream_config

        out["KinesisStreamConfig"] = (
            capo_connect.types.kinesis_stream_config.serialize_json(
                value["kinesis_stream_config"]
            )
        )
    if "kinesis_firehose_config" in value:
        import capo_connect.types.kinesis_firehose_config

        out["KinesisFirehoseConfig"] = (
            capo_connect.types.kinesis_firehose_config.serialize_json(
                value["kinesis_firehose_config"]
            )
        )
    return out


def deserialize_json(data: dict) -> InstanceStorageConfig:
    out: InstanceStorageConfig = {}  # type: ignore[typeddict-item]
    if data.get("AssociationId") is not None:
        out["association_id"] = data["AssociationId"]
    if data.get("StorageType") is not None:
        import capo_connect.types.storage_type

        out["storage_type"] = capo_connect.types.storage_type.deserialize_json(
            data["StorageType"]
        )
    else:
        import typing

        out["storage_type"] = typing.cast(
            "capo_connect.types.storage_type.StorageType", ""
        )
    if data.get("S3Config") is not None:
        import capo_connect.types.s3_config

        out["s3_config"] = capo_connect.types.s3_config.deserialize_json(
            data["S3Config"]
        )
    if data.get("KinesisVideoStreamConfig") is not None:
        import capo_connect.types.kinesis_video_stream_config

        out["kinesis_video_stream_config"] = (
            capo_connect.types.kinesis_video_stream_config.deserialize_json(
                data["KinesisVideoStreamConfig"]
            )
        )
    if data.get("KinesisStreamConfig") is not None:
        import capo_connect.types.kinesis_stream_config

        out["kinesis_stream_config"] = (
            capo_connect.types.kinesis_stream_config.deserialize_json(
                data["KinesisStreamConfig"]
            )
        )
    if data.get("KinesisFirehoseConfig") is not None:
        import capo_connect.types.kinesis_firehose_config

        out["kinesis_firehose_config"] = (
            capo_connect.types.kinesis_firehose_config.deserialize_json(
                data["KinesisFirehoseConfig"]
            )
        )
    return out
