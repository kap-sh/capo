"""Generated from Smithy shape ``com.amazonaws.partnercentralmarketing#CampaignAssetActivationStatus``."""

from typing import Literal, TypeAlias, cast

"""How ONE asset's activation is going, inside a task. Pairs with CampaignAssetActivationTaskStatus: that one is the aggregate, this one is a single asset's contribution to it. Partner Central names its task status per flow rather than sharing one, and this follows that. Deliberately NOT `AttemptStatus`, even though the three values coincide today. `AttemptStatus` is the **asset's own attempt** axis (`LastActivationStatus`); this is a **per-asset outcome inside a task resource**. Identical values do not make two things the same axis, and sharing one enum across unrelated axes means a value added for either appears in the SDK of both. A dedicated enum is additive and safe — do not "simplify" this back."""
CampaignAssetActivationStatus: TypeAlias = Literal[
    "IN_PROGRESS",
    "SUCCEEDED",
    "FAILED",
]


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: CampaignAssetActivationStatus) -> str:
    return value


def deserialize_cbor(data: str) -> CampaignAssetActivationStatus:
    return cast(CampaignAssetActivationStatus, data)
