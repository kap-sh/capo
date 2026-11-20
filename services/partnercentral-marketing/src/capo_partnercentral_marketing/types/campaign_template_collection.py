"""Generated from Smithy shape ``com.amazonaws.partnercentralmarketing#CampaignTemplateCollection``."""

from typing import Literal, TypeAlias, cast

"""Which browsing context a campaign template belongs to. A classification of the template, not a resource: it decides where a client lists the template and grants nothing. Every partner may read and use a template in any collection. Clients must tolerate values added later."""
CampaignTemplateCollection: TypeAlias = Literal[
    "GENERAL",
    "BUILD_WITH_AI",
]


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: CampaignTemplateCollection) -> str:
    return value


def deserialize_cbor(data: str) -> CampaignTemplateCollection:
    return cast(CampaignTemplateCollection, data)
