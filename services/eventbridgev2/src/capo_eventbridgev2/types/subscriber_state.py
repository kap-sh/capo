"""Generated from Smithy shape ``com.amazonaws.eventbridgev2#SubscriberState``."""

from typing import Literal, TypeAlias, cast

"""Customer-controlled run state of a subscriber, set on create or update. Distinct from the bus lifecycle vocabulary, where ACTIVE means "provisioned and healthy". Delivery requires State RUNNING on a subscriber that is not revoked."""
SubscriberState: TypeAlias = Literal[
    "RUNNING",
    "STOPPED",
]


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: SubscriberState) -> str:
    return value


def deserialize_cbor(data: str) -> SubscriberState:
    return cast(SubscriberState, data)
