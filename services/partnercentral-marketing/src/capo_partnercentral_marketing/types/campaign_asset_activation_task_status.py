"""Generated from Smithy shape ``com.amazonaws.partnercentralmarketing#CampaignAssetActivationTaskStatus``."""

from typing import Literal, TypeAlias, cast

"""An activation task's status, aggregated over every asset it accepted. Pairs with CampaignAssetActivationStatus: this is the aggregate, that is one asset's contribution to it."""
CampaignAssetActivationTaskStatus: TypeAlias = Literal[
    "IN_PROGRESS",
    "SUCCEEDED",
    "PARTIAL_FAILURE",
    "FAILED",
]


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: CampaignAssetActivationTaskStatus) -> str:
    return value


def deserialize_cbor(data: str) -> CampaignAssetActivationTaskStatus:
    return cast(CampaignAssetActivationTaskStatus, data)
