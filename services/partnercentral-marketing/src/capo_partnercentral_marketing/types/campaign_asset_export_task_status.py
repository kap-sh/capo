"""Generated from Smithy shape ``com.amazonaws.partnercentralmarketing#CampaignAssetExportTaskStatus``."""

from typing import Literal, TypeAlias, cast

"""The state of a campaign asset export task."""
CampaignAssetExportTaskStatus: TypeAlias = Literal[
    "IN_PROGRESS",
    "COMPLETED",
    "FAILED",
]


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: CampaignAssetExportTaskStatus) -> str:
    return value


def deserialize_cbor(data: str) -> CampaignAssetExportTaskStatus:
    return cast(CampaignAssetExportTaskStatus, data)
