"""Generated from Smithy shape ``com.amazonaws.partnercentralmarketing#CampaignAssetState``."""

from typing import Literal, TypeAlias, cast

"""The lifecycle position of a campaign asset. Answers exactly one question — is the asset live — and reports current truth only. The evaluations *about* the asset are separate members: `LastActivationStatus` for how the last hand-over to the delivery platform ended, and `DeliveryStatus` for the send. No member's value depends on another's, so there is nothing to rank. `State` rather than `Status`, and narrowing this enum is what *earns* the name rather than putting it at risk. The AWS Common Terms test for `State` is whether a resource exposes "two or more resource attributes, one of which may refer to status" — and `CampaignAsset` now exposes exactly that shape: `State` beside `LastActivationStatus` and `DeliveryStatus`. So this is no longer a lone enum dressed up as a condition; it is the lifecycle position sitting next to the named status attributes, flat rather than nested. Read on its own the member looks like a single attribute and the standard would ask for `Status`; read on the resource it is the aggregate the standard reserves `State` for. Same-domain precedent: Amazon Connect Campaigns uses `State` for a campaign's lifecycle and `Status` for a job. Recorded for API office hours. Distinguish a stopped asset from one never started by whether StartedAt is set; StartedAt is never cleared, not even by a stop. This enum carried five values, `IN_PROGRESS` and `FAILED` alongside the two below plus `COMPLETED`, and all three were removed rather than deprecated. `IN_PROGRESS` and `FAILED` went because **a single projected value could not answer "is it live?"** — a live asset with a scan in flight and a *stopped* asset with a scan in flight both projected `IN_PROGRESS`, and `FAILED` collapsed the same way, because the projection ranked its inputs by a frozen precedence and precedence discards facts. The fact it discarded was liveness. The three internal axes the projection read now map onto this member plus `LastActivationStatus` plus one internal-only distinction, with no information lost. See campaign-asset-design.md §2 and §6. `COMPLETED` went because it was doing delivery's job: it meant "delivered", which is a delivery outcome and not a lifecycle position. For an email it was exactly `DeliveryStatus = DELIVERED`, already modelled and already on the asset; for a social post it was **unachievable**, because this service cannot observe social delivery at all — so half of its stated meaning, "the email was sent, or the post published", was never reachable. The other three startable types have no delivery event whatever. It had no writer and no reader. Anyone reintroducing a terminal position needs a fact observable for **every** startable type, which `DeliveryStatus` explicitly is not — it covers only EMAIL and SOCIAL_POST."""
CampaignAssetState: TypeAlias = Literal[
    "INACTIVE",
    "ACTIVE",
]


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: CampaignAssetState) -> str:
    return value


def deserialize_cbor(data: str) -> CampaignAssetState:
    return cast(CampaignAssetState, data)
