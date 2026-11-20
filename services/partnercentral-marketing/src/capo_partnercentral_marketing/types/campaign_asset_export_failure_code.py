"""Generated from Smithy shape ``com.amazonaws.partnercentralmarketing#CampaignAssetExportFailureCode``."""

from typing import Literal, TypeAlias, cast

"""Machine-readable cause of an export task failure. Dedicated to the export flow; see CampaignAssetExportFailureReason."""
CampaignAssetExportFailureCode: TypeAlias = Literal[
    "EXPORT_TIMEOUT",
    "EXPORT_TOO_LARGE",
    "PACKAGING_ERROR",
    "SOURCE_OBJECT_MISSING",
    "INTERNAL_ERROR",
]


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: CampaignAssetExportFailureCode) -> str:
    return value


def deserialize_cbor(data: str) -> CampaignAssetExportFailureCode:
    return cast(CampaignAssetExportFailureCode, data)
