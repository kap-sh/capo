"""Generated from Smithy shape ``com.amazonaws.partnercentralmarketing#CampaignSortName``."""

from typing import Literal, TypeAlias, cast

"""The attribute `ListCampaigns` sorts by."""
CampaignSortName: TypeAlias = Literal[
    "NAME",
    "STATE",
    "START_ON",
    "CREATED_AT",
]


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: CampaignSortName) -> str:
    return value


def deserialize_cbor(data: str) -> CampaignSortName:
    return cast(CampaignSortName, data)
