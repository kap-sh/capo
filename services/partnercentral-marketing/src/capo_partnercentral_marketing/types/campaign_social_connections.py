"""Generated from Smithy shape ``com.amazonaws.partnercentralmarketing#CampaignSocialConnections``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_partnercentral_marketing.types.campaign_social_connection_ids
    import capo_partnercentral_marketing.types.platform

CampaignSocialConnections: TypeAlias = dict[
    "capo_partnercentral_marketing.types.platform.Platform",
    "capo_partnercentral_marketing.types.campaign_social_connection_ids.CampaignSocialConnectionIds",
]


# --- rpcv2Cbor ser/de ---
def serialize_cbor(input_to_serialize: CampaignSocialConnections) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import capo_partnercentral_marketing.types.campaign_social_connection_ids
        import capo_partnercentral_marketing.types.platform

        out[capo_partnercentral_marketing.types.platform.serialize_cbor(key)] = (
            capo_partnercentral_marketing.types.campaign_social_connection_ids.serialize_cbor(
                value
            )
        )
    return out


def deserialize_cbor(data: dict) -> CampaignSocialConnections:
    out: CampaignSocialConnections = {}
    for key, value in data.items():
        import capo_partnercentral_marketing.types.platform

        if value is None:
            continue
        import capo_partnercentral_marketing.types.campaign_social_connection_ids

        out[capo_partnercentral_marketing.types.platform.deserialize_cbor(key)] = (
            capo_partnercentral_marketing.types.campaign_social_connection_ids.deserialize_cbor(
                value
            )
        )
    return out
