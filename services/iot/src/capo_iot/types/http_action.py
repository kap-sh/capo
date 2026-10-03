"""Generated from Smithy shape ``com.amazonaws.iot#HttpAction``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_iot.errors import DeserializationError

if TYPE_CHECKING:
    import capo_iot.types.batch_config
    import capo_iot.types.enable_batching
    import capo_iot.types.header_list
    import capo_iot.types.http_authorization
    import capo_iot.types.url


class HttpAction(TypedDict, closed=True):
    url: "capo_iot.types.url.Url"
    """<p>The endpoint URL. If substitution templates are used in the URL, you must also specify a <code>confirmationUrl</code>. If this is a new destination, a new <code>TopicRuleDestination</code> is created if possible.</p>"""
    confirmation_url: NotRequired["capo_iot.types.url.Url"]
    """<p>The URL to which IoT sends a confirmation message. The value of the confirmation URL must be a prefix of the endpoint URL. If you do not specify a confirmation URL IoT uses the endpoint URL as the confirmation URL. If you use substitution templates in the confirmationUrl, you must create and enable topic rule destinations that match each possible value of the substitution template before traffic is allowed to your endpoint URL.</p>"""
    headers: NotRequired["capo_iot.types.header_list.HeaderList"]
    """<p>The HTTP headers to send with the message data.</p>"""
    auth: NotRequired["capo_iot.types.http_authorization.HttpAuthorization"]
    """<p>The authentication method to use when sending data to an HTTPS endpoint.</p>"""
    enable_batching: NotRequired["capo_iot.types.enable_batching.EnableBatching"]
    """<p>Whether to process the HTTP action messages into a single request. Value can be true or false.</p>"""
    batch_config: NotRequired["capo_iot.types.batch_config.BatchConfig"]
    """<p>The configuration settings for batching. For more information, see <a href="https://docs.aws.amazon.com/iot/latest/developerguide/http_batching.html"> Batching HTTP action messages</a>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: HttpAction) -> dict:
    out: dict = {}
    out["url"] = value["url"]
    if "confirmation_url" in value:
        out["confirmationUrl"] = value["confirmation_url"]
    if "headers" in value:
        import capo_iot.types.header_list

        out["headers"] = capo_iot.types.header_list.serialize_json(value["headers"])
    if "auth" in value:
        import capo_iot.types.http_authorization

        out["auth"] = capo_iot.types.http_authorization.serialize_json(value["auth"])
    if "enable_batching" in value:
        out["enableBatching"] = value["enable_batching"]
    if "batch_config" in value:
        import capo_iot.types.batch_config

        out["batchConfig"] = capo_iot.types.batch_config.serialize_json(
            value["batch_config"]
        )
    return out


def deserialize_json(data: dict) -> HttpAction:
    out: HttpAction = {}  # type: ignore[typeddict-item]
    if data.get("url") is not None:
        out["url"] = data["url"]
    else:
        raise DeserializationError("HttpAction.url required")
    if data.get("confirmationUrl") is not None:
        out["confirmation_url"] = data["confirmationUrl"]
    if data.get("headers") is not None:
        import capo_iot.types.header_list

        out["headers"] = capo_iot.types.header_list.deserialize_json(data["headers"])
    if data.get("auth") is not None:
        import capo_iot.types.http_authorization

        out["auth"] = capo_iot.types.http_authorization.deserialize_json(data["auth"])
    if data.get("enableBatching") is not None:
        out["enable_batching"] = data["enableBatching"]
    if data.get("batchConfig") is not None:
        import capo_iot.types.batch_config

        out["batch_config"] = capo_iot.types.batch_config.deserialize_json(
            data["batchConfig"]
        )
    return out
