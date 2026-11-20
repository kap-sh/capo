"""Generated from Smithy shape ``com.amazonaws.partnercentralmarketing#PartnerProfileField``."""

from typing import Literal, TypeAlias, cast

"""A value of the partner's AWS Partner Central profile that an asset field shows, or that an asset needs before it can activate (`ActivationIssue$PartnerProfileField`). Each names a member of `PartnerProfileBranding`."""
PartnerProfileField: TypeAlias = Literal[
    "DISPLAY_NAME",
    "WEBSITE_URL",
    "LOGO",
    "WEBSITE_DOMAIN",
    "COPYRIGHT_LINE",
    "PARTNER_DETAILS",
    "COPYRIGHT_AND_DETAILS",
    "COPYRIGHT_YEAR_LINE",
]


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: PartnerProfileField) -> str:
    return value


def deserialize_cbor(data: str) -> PartnerProfileField:
    return cast(PartnerProfileField, data)
