"""Generated from Smithy shape ``com.amazonaws.health#OrganizationEventList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_health.types.organization_event

OrganizationEventList: TypeAlias = list[
    "capo_health.types.organization_event.OrganizationEvent"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: OrganizationEventList) -> list:
    import capo_health.types.organization_event

    out: list = []
    for item in value:
        out.append(capo_health.types.organization_event.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> OrganizationEventList:
    import capo_health.types.organization_event

    out: OrganizationEventList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_health.types.organization_event.deserialize_aws_json_1_1(item))
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: OrganizationEventList) -> list:
    import capo_health.types.organization_event

    out: list = []
    for item in value:
        out.append(capo_health.types.organization_event.serialize_cbor(item))
    return out


def deserialize_cbor(data: list) -> OrganizationEventList:
    import capo_health.types.organization_event

    out: OrganizationEventList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_health.types.organization_event.deserialize_cbor(item))
    return out
