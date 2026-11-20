"""Generated from Smithy shape ``com.amazonaws.partnercentralmarketing#CampaignSetting``."""

from typing import Literal, TypeAlias, cast

"""A campaign setting, named by its `Campaign` member: one an asset field shows, or one an asset needs before it can activate (`ActivationIssue$CampaignSetting`)."""
CampaignSetting: TypeAlias = Literal[
    "SENDER_EMAIL",
    "END_ON",
    "EMAIL_TARGET",
    "PRIVACY_POLICY_URL",
    "PARTNER_ADDRESS",
    "PARTNER_BADGE",
]


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: CampaignSetting) -> str:
    return value


def deserialize_cbor(data: str) -> CampaignSetting:
    return cast(CampaignSetting, data)
