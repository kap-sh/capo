"""Generated from Smithy shape ``com.amazonaws.connect#StartContactStreamingRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_connect.errors import DeserializationError

if TYPE_CHECKING:
    import capo_connect.types.chat_streaming_configuration
    import capo_connect.types.client_token
    import capo_connect.types.contact_id
    import capo_connect.types.instance_id


class StartContactStreamingRequest(TypedDict, closed=True):
    instance_id: "capo_connect.types.instance_id.InstanceId"
    """<p>The identifier of the Connect Customer instance. You can <a href="https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html">find the instance ID</a> in the Amazon Resource Name (ARN) of the instance.</p>"""
    contact_id: "capo_connect.types.contact_id.ContactId"
    """<p>The identifier of the contact. This is the identifier of the contact associated with the first interaction with the contact center.</p>"""
    chat_streaming_configuration: (
        "capo_connect.types.chat_streaming_configuration.ChatStreamingConfiguration"
    )
    """<p>The streaming configuration, such as the Amazon SNS streaming endpoint.</p>"""
    client_token: "capo_connect.types.client_token.ClientToken"
    """<p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If not provided, the Amazon Web Services SDK populates this field. For more information about idempotency, see <a href="https://aws.amazon.com/builders-library/making-retries-safe-with-idempotent-APIs/">Making retries safe with idempotent APIs</a>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartContactStreamingRequest) -> dict:
    out: dict = {}
    out["InstanceId"] = value["instance_id"]
    out["ContactId"] = value["contact_id"]
    import capo_connect.types.chat_streaming_configuration

    out["ChatStreamingConfiguration"] = (
        capo_connect.types.chat_streaming_configuration.serialize_json(
            value["chat_streaming_configuration"]
        )
    )
    out["ClientToken"] = value["client_token"]
    return out


def deserialize_json(data: dict) -> StartContactStreamingRequest:
    out: StartContactStreamingRequest = {}  # type: ignore[typeddict-item]
    if data.get("InstanceId") is not None:
        out["instance_id"] = data["InstanceId"]
    else:
        raise DeserializationError("StartContactStreamingRequest.instance_id required")
    if data.get("ContactId") is not None:
        out["contact_id"] = data["ContactId"]
    else:
        raise DeserializationError("StartContactStreamingRequest.contact_id required")
    if data.get("ChatStreamingConfiguration") is not None:
        import capo_connect.types.chat_streaming_configuration

        out["chat_streaming_configuration"] = (
            capo_connect.types.chat_streaming_configuration.deserialize_json(
                data["ChatStreamingConfiguration"]
            )
        )
    else:
        raise DeserializationError(
            "StartContactStreamingRequest.chat_streaming_configuration required"
        )
    if data.get("ClientToken") is not None:
        out["client_token"] = data["ClientToken"]
    else:
        raise DeserializationError("StartContactStreamingRequest.client_token required")
    return out
