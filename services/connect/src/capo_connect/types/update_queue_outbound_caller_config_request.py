"""Generated from Smithy shape ``com.amazonaws.connect#UpdateQueueOutboundCallerConfigRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_connect.errors import DeserializationError

if TYPE_CHECKING:
    import capo_connect.types.instance_id
    import capo_connect.types.outbound_caller_config
    import capo_connect.types.queue_id


class UpdateQueueOutboundCallerConfigRequest(TypedDict, closed=True):
    instance_id: "capo_connect.types.instance_id.InstanceId"
    """<p>The identifier of the Connect Customer instance. You can <a href="https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html">find the instance ID</a> in the Amazon Resource Name (ARN) of the instance.</p>"""
    queue_id: "capo_connect.types.queue_id.QueueId"
    """<p>The identifier for the queue.</p>"""
    outbound_caller_config: (
        "capo_connect.types.outbound_caller_config.OutboundCallerConfig"
    )
    """<p>The outbound caller ID name, number, and outbound whisper flow.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateQueueOutboundCallerConfigRequest) -> dict:
    out: dict = {}
    import capo_connect.types.outbound_caller_config

    out["OutboundCallerConfig"] = (
        capo_connect.types.outbound_caller_config.serialize_json(
            value["outbound_caller_config"]
        )
    )
    return out


def deserialize_json(data: dict) -> UpdateQueueOutboundCallerConfigRequest:
    out: UpdateQueueOutboundCallerConfigRequest = {}  # type: ignore[typeddict-item]
    if data.get("OutboundCallerConfig") is not None:
        import capo_connect.types.outbound_caller_config

        out["outbound_caller_config"] = (
            capo_connect.types.outbound_caller_config.deserialize_json(
                data["OutboundCallerConfig"]
            )
        )
    else:
        raise DeserializationError(
            "UpdateQueueOutboundCallerConfigRequest.outbound_caller_config required"
        )
    return out
