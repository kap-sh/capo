"""Generated from Smithy shape ``com.amazonaws.chimesdkmediapipelines#ConcatenationSink``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

from capo_chime_sdk_media_pipelines.errors import DeserializationError

if TYPE_CHECKING:
    import capo_chime_sdk_media_pipelines.types.concatenation_sink_type
    import capo_chime_sdk_media_pipelines.types.s3_bucket_sink_configuration


class ConcatenationSink(TypedDict, closed=True):
    type: "capo_chime_sdk_media_pipelines.types.concatenation_sink_type.ConcatenationSinkType"
    """<p>The type of data sink in the configuration object.</p>"""
    s3_bucket_sink_configuration: "capo_chime_sdk_media_pipelines.types.s3_bucket_sink_configuration.S3BucketSinkConfiguration"
    """<p>The configuration settings for an Amazon S3 bucket sink.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ConcatenationSink) -> dict:
    out: dict = {}
    import capo_chime_sdk_media_pipelines.types.concatenation_sink_type

    out["Type"] = (
        capo_chime_sdk_media_pipelines.types.concatenation_sink_type.serialize_json(
            value["type"]
        )
    )
    import capo_chime_sdk_media_pipelines.types.s3_bucket_sink_configuration

    out["S3BucketSinkConfiguration"] = (
        capo_chime_sdk_media_pipelines.types.s3_bucket_sink_configuration.serialize_json(
            value["s3_bucket_sink_configuration"]
        )
    )
    return out


def deserialize_json(data: dict) -> ConcatenationSink:
    out: ConcatenationSink = {}  # type: ignore[typeddict-item]
    if data.get("Type") is not None:
        import capo_chime_sdk_media_pipelines.types.concatenation_sink_type

        out["type"] = (
            capo_chime_sdk_media_pipelines.types.concatenation_sink_type.deserialize_json(
                data["Type"]
            )
        )
    else:
        import typing

        out["type"] = typing.cast(
            "capo_chime_sdk_media_pipelines.types.concatenation_sink_type.ConcatenationSinkType",
            "",
        )
    if data.get("S3BucketSinkConfiguration") is not None:
        import capo_chime_sdk_media_pipelines.types.s3_bucket_sink_configuration

        out["s3_bucket_sink_configuration"] = (
            capo_chime_sdk_media_pipelines.types.s3_bucket_sink_configuration.deserialize_json(
                data["S3BucketSinkConfiguration"]
            )
        )
    else:
        raise DeserializationError(
            "ConcatenationSink.s3_bucket_sink_configuration required"
        )
    return out


def redact_sensitive(value: ConcatenationSink) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "s3_bucket_sink_configuration" in value:
        import capo_chime_sdk_media_pipelines.types.s3_bucket_sink_configuration

        out["s3_bucket_sink_configuration"] = (
            capo_chime_sdk_media_pipelines.types.s3_bucket_sink_configuration.redact_sensitive(
                value["s3_bucket_sink_configuration"]
            )
        )
    return out
