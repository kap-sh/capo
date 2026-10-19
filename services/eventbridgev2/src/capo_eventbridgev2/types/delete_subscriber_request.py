"""Generated from Smithy shape ``com.amazonaws.eventbridgev2#DeleteSubscriberRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_eventbridgev2.types.subscriber_arn


class DeleteSubscriberRequest(TypedDict, closed=True):
    subscriber_arn: "capo_eventbridgev2.types.subscriber_arn.SubscriberArn"


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DeleteSubscriberRequest) -> dict:
    out: dict = {}
    out["SubscriberArn"] = value["subscriber_arn"]
    return out


def deserialize_cbor(data: dict) -> DeleteSubscriberRequest:
    out: DeleteSubscriberRequest = {}  # type: ignore[typeddict-item]
    if data.get("SubscriberArn") is not None:
        out["subscriber_arn"] = data["SubscriberArn"]
    else:
        out["subscriber_arn"] = ""
    return out
