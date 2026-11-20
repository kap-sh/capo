"""Generated from Smithy shape ``com.amazonaws.partnercentralmarketing#EngagementGroupIdList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_partnercentral_marketing.types.engagement_group_id

EngagementGroupIdList: TypeAlias = list[
    "capo_partnercentral_marketing.types.engagement_group_id.EngagementGroupId"
]


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: EngagementGroupIdList) -> list:
    return list(value)


def deserialize_cbor(data: list) -> EngagementGroupIdList:
    return [item for item in data if item is not None]
