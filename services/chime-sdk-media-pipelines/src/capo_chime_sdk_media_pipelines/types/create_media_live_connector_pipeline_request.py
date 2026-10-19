"""Generated from Smithy shape ``com.amazonaws.chimesdkmediapipelines#CreateMediaLiveConnectorPipelineRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_chime_sdk_media_pipelines.types.client_request_token
    import capo_chime_sdk_media_pipelines.types.live_connector_sink_list
    import capo_chime_sdk_media_pipelines.types.live_connector_source_list
    import capo_chime_sdk_media_pipelines.types.tag_list


class CreateMediaLiveConnectorPipelineRequest(TypedDict, closed=True):
    sources: "capo_chime_sdk_media_pipelines.types.live_connector_source_list.LiveConnectorSourceList"
    """<p>The media live connector pipeline's data sources.</p>"""
    sinks: "capo_chime_sdk_media_pipelines.types.live_connector_sink_list.LiveConnectorSinkList"
    """<p>The media live connector pipeline's data sinks.</p>"""
    client_request_token: NotRequired[
        "capo_chime_sdk_media_pipelines.types.client_request_token.ClientRequestToken"
    ]
    """<p>The token assigned to the client making the request.</p>"""
    tags: NotRequired["capo_chime_sdk_media_pipelines.types.tag_list.TagList"]
    """<p>The tags associated with the media live connector pipeline.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateMediaLiveConnectorPipelineRequest) -> dict:
    out: dict = {}
    import capo_chime_sdk_media_pipelines.types.live_connector_source_list

    out["Sources"] = (
        capo_chime_sdk_media_pipelines.types.live_connector_source_list.serialize_json(
            value["sources"]
        )
    )
    import capo_chime_sdk_media_pipelines.types.live_connector_sink_list

    out["Sinks"] = (
        capo_chime_sdk_media_pipelines.types.live_connector_sink_list.serialize_json(
            value["sinks"]
        )
    )
    if "client_request_token" in value:
        out["ClientRequestToken"] = value["client_request_token"]
    if "tags" in value:
        import capo_chime_sdk_media_pipelines.types.tag_list

        out["Tags"] = capo_chime_sdk_media_pipelines.types.tag_list.serialize_json(
            value["tags"]
        )
    return out


def deserialize_json(data: dict) -> CreateMediaLiveConnectorPipelineRequest:
    out: CreateMediaLiveConnectorPipelineRequest = {}  # type: ignore[typeddict-item]
    if data.get("Sources") is not None:
        import capo_chime_sdk_media_pipelines.types.live_connector_source_list

        out["sources"] = (
            capo_chime_sdk_media_pipelines.types.live_connector_source_list.deserialize_json(
                data["Sources"]
            )
        )
    else:
        out["sources"] = []
    if data.get("Sinks") is not None:
        import capo_chime_sdk_media_pipelines.types.live_connector_sink_list

        out["sinks"] = (
            capo_chime_sdk_media_pipelines.types.live_connector_sink_list.deserialize_json(
                data["Sinks"]
            )
        )
    else:
        out["sinks"] = []
    if data.get("ClientRequestToken") is not None:
        out["client_request_token"] = data["ClientRequestToken"]
    if data.get("Tags") is not None:
        import capo_chime_sdk_media_pipelines.types.tag_list

        out["tags"] = capo_chime_sdk_media_pipelines.types.tag_list.deserialize_json(
            data["Tags"]
        )
    return out


def redact_sensitive(value: CreateMediaLiveConnectorPipelineRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "sources" in value:
        import capo_chime_sdk_media_pipelines.types.live_connector_source_list

        out["sources"] = (
            capo_chime_sdk_media_pipelines.types.live_connector_source_list.redact_sensitive(
                value["sources"]
            )
        )
    if "sinks" in value:
        import capo_chime_sdk_media_pipelines.types.live_connector_sink_list

        out["sinks"] = (
            capo_chime_sdk_media_pipelines.types.live_connector_sink_list.redact_sensitive(
                value["sinks"]
            )
        )
    if "client_request_token" in value:
        out["client_request_token"] = "*** Sensitive Data Redacted ***"
    return out
