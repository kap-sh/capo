"""Generated from Smithy shape ``com.amazonaws.health#OrganizationTagList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_health.types.organization_tag

OrganizationTagList: TypeAlias = list[
    "capo_health.types.organization_tag.OrganizationTag"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: OrganizationTagList) -> list:
    import capo_health.types.organization_tag

    out: list = []
    for item in value:
        out.append(capo_health.types.organization_tag.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> OrganizationTagList:
    import capo_health.types.organization_tag

    out: OrganizationTagList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_health.types.organization_tag.deserialize_aws_json_1_1(item))
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: OrganizationTagList) -> list:
    import capo_health.types.organization_tag

    out: list = []
    for item in value:
        out.append(capo_health.types.organization_tag.serialize_cbor(item))
    return out


def deserialize_cbor(data: list) -> OrganizationTagList:
    import capo_health.types.organization_tag

    out: OrganizationTagList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_health.types.organization_tag.deserialize_cbor(item))
    return out
