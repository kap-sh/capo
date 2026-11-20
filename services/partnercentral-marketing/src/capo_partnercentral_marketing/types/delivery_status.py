"""Generated from Smithy shape ``com.amazonaws.partnercentralmarketing#DeliveryStatus``."""

from typing import Literal, TypeAlias, cast

"""What the delivery platform did with an artifact it accepted. <p>Distinct from `LastActivationStatus`, which reports the hand-over *to* the platform. Once DG has the mailing armed, the hand-over `SUCCEEDED`; whether the platform then delivered is this member's business, and the two genuinely diverge — `LastActivationStatus = SUCCEEDED` with `DeliveryStatus = FAILED` is an ordinary combination, not a contradiction. <p>**EMAIL and SOCIAL_POST only.** Landing pages and documents have no delivery event at all. <p>`PENDING` until the platform shows the outcome. An email is `DELIVERED` once the platform reports it sent, and `FAILED` when the platform reports the send failed. A social post is `DELIVERED` once the platform has published it. A social post is never reported `FAILED` by an observation alone, because the platform retries a failed post. A send that has not resolved a day after its scheduled time stays `PENDING` while it is investigated, and is reported `FAILED` only if it will not go out. A `FAILED` asset can be deactivated and activated again to retry. See campaign-asset-design.md section 6.4."""
DeliveryStatus: TypeAlias = Literal[
    "PENDING",
    "DELIVERED",
    "FAILED",
]


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DeliveryStatus) -> str:
    return value


def deserialize_cbor(data: str) -> DeliveryStatus:
    return cast(DeliveryStatus, data)
