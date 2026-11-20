"""Generated from Smithy shape ``com.amazonaws.partnercentralmarketing#CampaignState``."""

from typing import Literal, TypeAlias, cast

"""A campaign's state, derived on every read from its `EndOn` and its assets: 1. `COMPLETED` once the UTC date is after `EndOn` (so a campaign ending today completes at the next UTC midnight). A campaign with no `EndOn` never completes, and cannot activate until it has one; 2. otherwise `ACTIVE` when any of its assets is `ACTIVE`; 3. otherwise `DRAFT`, including a campaign with no assets. A summary of the assets, not a lifecycle: nothing transitions it, it is never stored, and it gates no operation by itself: the refusal on a completed campaign (`CAMPAIGN_COMPLETED`) reads the same `EndOn`. Otherwise whether an asset can be edited, activated or deleted depends on that asset. So a scheduled email counts as `ACTIVE` once armed, before it sends; a campaign stays `DRAFT` during its first activation; deactivating its only active email or social post returns it to `DRAFT`; and a `COMPLETED` campaign can still have live landing pages."""
CampaignState: TypeAlias = Literal[
    "DRAFT",
    "ACTIVE",
    "COMPLETED",
]


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: CampaignState) -> str:
    return value


def deserialize_cbor(data: str) -> CampaignState:
    return cast(CampaignState, data)
