"""Generated from Smithy shape ``com.amazonaws.mailmanager#CreateRelayRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_mailmanager.errors import DeserializationError

if TYPE_CHECKING:
    import capo_mailmanager.types.idempotency_token
    import capo_mailmanager.types.relay_authentication
    import capo_mailmanager.types.relay_name
    import capo_mailmanager.types.relay_server_name
    import capo_mailmanager.types.relay_server_port
    import capo_mailmanager.types.tag_list


class CreateRelayRequest(TypedDict, closed=True):
    client_token: NotRequired[
        "capo_mailmanager.types.idempotency_token.IdempotencyToken"
    ]
    """<p>A unique token that Amazon SES uses to recognize subsequent retries of the same request.</p>"""
    relay_name: "capo_mailmanager.types.relay_name.RelayName"
    """<p>The unique name of the relay resource.</p>"""
    server_name: "capo_mailmanager.types.relay_server_name.RelayServerName"
    """<p>The destination relay server address.</p>"""
    server_port: "capo_mailmanager.types.relay_server_port.RelayServerPort"
    """<p>The destination relay server port.</p>"""
    authentication: "capo_mailmanager.types.relay_authentication.RelayAuthentication"
    """<p>Authentication for the relay destination server—specify the secretARN where the SMTP credentials are stored.</p>"""
    tags: NotRequired["capo_mailmanager.types.tag_list.TagList"]
    """<p>The tags used to organize, track, or control access for the resource. For example, { "tags": {"key1":"value1", "key2":"value2"} }.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CreateRelayRequest) -> dict:
    out: dict = {}
    if "client_token" in value:
        out["ClientToken"] = value["client_token"]
    out["RelayName"] = value["relay_name"]
    out["ServerName"] = value["server_name"]
    out["ServerPort"] = value["server_port"]
    import capo_mailmanager.types.relay_authentication

    out["Authentication"] = (
        capo_mailmanager.types.relay_authentication.serialize_aws_json_1_0(
            value["authentication"]
        )
    )
    if "tags" in value:
        import capo_mailmanager.types.tag_list

        out["Tags"] = capo_mailmanager.types.tag_list.serialize_aws_json_1_0(
            value["tags"]
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> CreateRelayRequest:
    out: CreateRelayRequest = {}  # type: ignore[typeddict-item]
    if data.get("ClientToken") is not None:
        out["client_token"] = data["ClientToken"]
    if data.get("RelayName") is not None:
        out["relay_name"] = data["RelayName"]
    else:
        raise DeserializationError("CreateRelayRequest.relay_name required")
    if data.get("ServerName") is not None:
        out["server_name"] = data["ServerName"]
    else:
        raise DeserializationError("CreateRelayRequest.server_name required")
    if data.get("ServerPort") is not None:
        out["server_port"] = data["ServerPort"]
    else:
        raise DeserializationError("CreateRelayRequest.server_port required")
    if data.get("Authentication") is not None:
        import capo_mailmanager.types.relay_authentication

        out["authentication"] = (
            capo_mailmanager.types.relay_authentication.deserialize_aws_json_1_0(
                data["Authentication"]
            )
        )
    else:
        raise DeserializationError("CreateRelayRequest.authentication required")
    if data.get("Tags") is not None:
        import capo_mailmanager.types.tag_list

        out["tags"] = capo_mailmanager.types.tag_list.deserialize_aws_json_1_0(
            data["Tags"]
        )
    return out
