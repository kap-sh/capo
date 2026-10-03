"""Generated from Smithy shape ``com.amazonaws.rtbfabric#CreateLinkRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_rtbfabric.errors import DeserializationError

if TYPE_CHECKING:
    import capo_rtbfabric.types.gateway_id
    import capo_rtbfabric.types.link_attributes
    import capo_rtbfabric.types.link_log_settings
    import capo_rtbfabric.types.link_timeout_in_millis
    import capo_rtbfabric.types.tags_map


class CreateLinkRequest(TypedDict, closed=True):
    gateway_id: "capo_rtbfabric.types.gateway_id.GatewayId"
    """<p>The unique identifier of the gateway.</p>"""
    peer_gateway_id: "capo_rtbfabric.types.gateway_id.GatewayId"
    """<p>The unique identifier of the peer gateway.</p>"""
    attributes: NotRequired["capo_rtbfabric.types.link_attributes.LinkAttributes"]
    """<p>Attributes of the link.</p>"""
    http_responder_allowed: NotRequired["bool"]
    """<p>Boolean to specify if an HTTP responder is allowed.</p>"""
    tags: NotRequired["capo_rtbfabric.types.tags_map.TagsMap"]
    """<p>A map of the key-value pairs of the tag or tags to assign to the resource.</p>"""
    log_settings: "capo_rtbfabric.types.link_log_settings.LinkLogSettings"
    """<p>Application log settings for the link. This value is required. Under <code>applicationLogs.sampling</code>, the <code>errorLog</code> and <code>filterLog</code> fields set the percentage of eligible events to log. Valid values range from <code>0</code> through <code>100</code>. To turn off application logs, set both fields to <code>0</code>, as in <code>{"applicationLogs":{"sampling":{"errorLog":0,"filterLog":0}}}</code>.</p>"""
    timeout_in_millis: NotRequired[
        "capo_rtbfabric.types.link_timeout_in_millis.LinkTimeoutInMillis"
    ]
    """<p>The timeout value in milliseconds.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateLinkRequest) -> dict:
    out: dict = {}
    out["peerGatewayId"] = value["peer_gateway_id"]
    if "attributes" in value:
        import capo_rtbfabric.types.link_attributes

        out["attributes"] = capo_rtbfabric.types.link_attributes.serialize_json(
            value["attributes"]
        )
    if "http_responder_allowed" in value:
        out["httpResponderAllowed"] = value["http_responder_allowed"]
    if "tags" in value:
        import capo_rtbfabric.types.tags_map

        out["tags"] = capo_rtbfabric.types.tags_map.serialize_json(value["tags"])
    import capo_rtbfabric.types.link_log_settings

    out["logSettings"] = capo_rtbfabric.types.link_log_settings.serialize_json(
        value["log_settings"]
    )
    if "timeout_in_millis" in value:
        out["timeoutInMillis"] = value["timeout_in_millis"]
    return out


def deserialize_json(data: dict) -> CreateLinkRequest:
    out: CreateLinkRequest = {}  # type: ignore[typeddict-item]
    if data.get("peerGatewayId") is not None:
        out["peer_gateway_id"] = data["peerGatewayId"]
    else:
        raise DeserializationError("CreateLinkRequest.peer_gateway_id required")
    if data.get("attributes") is not None:
        import capo_rtbfabric.types.link_attributes

        out["attributes"] = capo_rtbfabric.types.link_attributes.deserialize_json(
            data["attributes"]
        )
    if data.get("httpResponderAllowed") is not None:
        out["http_responder_allowed"] = data["httpResponderAllowed"]
    if data.get("tags") is not None:
        import capo_rtbfabric.types.tags_map

        out["tags"] = capo_rtbfabric.types.tags_map.deserialize_json(data["tags"])
    if data.get("logSettings") is not None:
        import capo_rtbfabric.types.link_log_settings

        out["log_settings"] = capo_rtbfabric.types.link_log_settings.deserialize_json(
            data["logSettings"]
        )
    else:
        raise DeserializationError("CreateLinkRequest.log_settings required")
    if data.get("timeoutInMillis") is not None:
        out["timeout_in_millis"] = data["timeoutInMillis"]
    return out
