"""Generated from Smithy shape ``com.amazonaws.chimesdkmediapipelines#CreateMediaPipelineKinesisVideoStreamPoolRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_chime_sdk_media_pipelines.errors import DeserializationError

if TYPE_CHECKING:
    import capo_chime_sdk_media_pipelines.types.client_request_token
    import capo_chime_sdk_media_pipelines.types.kinesis_video_stream_configuration
    import capo_chime_sdk_media_pipelines.types.kinesis_video_stream_pool_name
    import capo_chime_sdk_media_pipelines.types.tag_list


class CreateMediaPipelineKinesisVideoStreamPoolRequest(TypedDict, closed=True):
    stream_configuration: "capo_chime_sdk_media_pipelines.types.kinesis_video_stream_configuration.KinesisVideoStreamConfiguration"
    """<p>The configuration settings for the stream.</p>"""
    pool_name: "capo_chime_sdk_media_pipelines.types.kinesis_video_stream_pool_name.KinesisVideoStreamPoolName"
    """<p>The name of the pool.</p>"""
    client_request_token: NotRequired[
        "capo_chime_sdk_media_pipelines.types.client_request_token.ClientRequestToken"
    ]
    """<p>The token assigned to the client making the request.</p>"""
    tags: NotRequired["capo_chime_sdk_media_pipelines.types.tag_list.TagList"]
    """<p>The tags assigned to the stream pool.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateMediaPipelineKinesisVideoStreamPoolRequest) -> dict:
    out: dict = {}
    import capo_chime_sdk_media_pipelines.types.kinesis_video_stream_configuration

    out["StreamConfiguration"] = (
        capo_chime_sdk_media_pipelines.types.kinesis_video_stream_configuration.serialize_json(
            value["stream_configuration"]
        )
    )
    out["PoolName"] = value["pool_name"]
    if "client_request_token" in value:
        out["ClientRequestToken"] = value["client_request_token"]
    if "tags" in value:
        import capo_chime_sdk_media_pipelines.types.tag_list

        out["Tags"] = capo_chime_sdk_media_pipelines.types.tag_list.serialize_json(
            value["tags"]
        )
    return out


def deserialize_json(data: dict) -> CreateMediaPipelineKinesisVideoStreamPoolRequest:
    out: CreateMediaPipelineKinesisVideoStreamPoolRequest = {}  # type: ignore[typeddict-item]
    if data.get("StreamConfiguration") is not None:
        import capo_chime_sdk_media_pipelines.types.kinesis_video_stream_configuration

        out["stream_configuration"] = (
            capo_chime_sdk_media_pipelines.types.kinesis_video_stream_configuration.deserialize_json(
                data["StreamConfiguration"]
            )
        )
    else:
        raise DeserializationError(
            "CreateMediaPipelineKinesisVideoStreamPoolRequest.stream_configuration required"
        )
    if data.get("PoolName") is not None:
        out["pool_name"] = data["PoolName"]
    else:
        raise DeserializationError(
            "CreateMediaPipelineKinesisVideoStreamPoolRequest.pool_name required"
        )
    if data.get("ClientRequestToken") is not None:
        out["client_request_token"] = data["ClientRequestToken"]
    if data.get("Tags") is not None:
        import capo_chime_sdk_media_pipelines.types.tag_list

        out["tags"] = capo_chime_sdk_media_pipelines.types.tag_list.deserialize_json(
            data["Tags"]
        )
    return out


def redact_sensitive(
    value: CreateMediaPipelineKinesisVideoStreamPoolRequest,
) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "client_request_token" in value:
        out["client_request_token"] = "*** Sensitive Data Redacted ***"
    return out
