"""Generated from Smithy shape ``com.amazonaws.kinesisvideo#MediaSourceConfig``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_kinesis_video.types.media_uri_secret_arn
    import capo_kinesis_video.types.media_uri_type


class MediaSourceConfig(TypedDict, closed=True):
    media_uri_secret_arn: (
        "capo_kinesis_video.types.media_uri_secret_arn.MediaUriSecretArn"
    )
    """<p>The Amazon Web Services Secrets Manager ARN for the username and password of the camera, or a local media file location.</p>"""
    media_uri_type: "capo_kinesis_video.types.media_uri_type.MediaUriType"
    """<p>The Uniform Resource Identifier (URI) type. The <code>FILE_URI</code> value can be used to stream local media files.</p> <note> <p>Preview only supports the <code>RTSP_URI</code> media source URI format .</p> </note>"""


# --- restJson1 ser/de ---
def serialize_json(value: MediaSourceConfig) -> dict:
    out: dict = {}
    out["MediaUriSecretArn"] = value["media_uri_secret_arn"]
    import capo_kinesis_video.types.media_uri_type

    out["MediaUriType"] = capo_kinesis_video.types.media_uri_type.serialize_json(
        value["media_uri_type"]
    )
    return out


def deserialize_json(data: dict) -> MediaSourceConfig:
    out: MediaSourceConfig = {}  # type: ignore[typeddict-item]
    if data.get("MediaUriSecretArn") is not None:
        out["media_uri_secret_arn"] = data["MediaUriSecretArn"]
    else:
        out["media_uri_secret_arn"] = ""
    if data.get("MediaUriType") is not None:
        import capo_kinesis_video.types.media_uri_type

        out["media_uri_type"] = (
            capo_kinesis_video.types.media_uri_type.deserialize_json(
                data["MediaUriType"]
            )
        )
    else:
        import typing

        out["media_uri_type"] = typing.cast(
            "capo_kinesis_video.types.media_uri_type.MediaUriType", ""
        )
    return out


def redact_sensitive(value: MediaSourceConfig) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "media_uri_secret_arn" in value:
        out["media_uri_secret_arn"] = "*** Sensitive Data Redacted ***"
    return out
