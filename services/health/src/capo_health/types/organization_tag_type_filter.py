"""Generated from Smithy shape ``com.amazonaws.health#OrganizationTagTypeFilter``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_health.types.organization_tag_type

OrganizationTagTypeFilter: TypeAlias = list[
    "capo_health.types.organization_tag_type.OrganizationTagType"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: OrganizationTagTypeFilter) -> list:
    import capo_health.types.organization_tag_type

    out: list = []
    for item in value:
        out.append(capo_health.types.organization_tag_type.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> OrganizationTagTypeFilter:
    import capo_health.types.organization_tag_type

    out: OrganizationTagTypeFilter = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_health.types.organization_tag_type.deserialize_aws_json_1_1(item)
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: OrganizationTagTypeFilter) -> list:
    import capo_health.types.organization_tag_type

    out: list = []
    for item in value:
        out.append(capo_health.types.organization_tag_type.serialize_cbor(item))
    return out


def deserialize_cbor(data: list) -> OrganizationTagTypeFilter:
    import capo_health.types.organization_tag_type

    out: OrganizationTagTypeFilter = []
    for item in data:
        if item is None:
            continue
        out.append(capo_health.types.organization_tag_type.deserialize_cbor(item))
    return out
