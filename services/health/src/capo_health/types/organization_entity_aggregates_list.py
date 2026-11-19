"""Generated from Smithy shape ``com.amazonaws.health#OrganizationEntityAggregatesList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_health.types.organization_entity_aggregate

OrganizationEntityAggregatesList: TypeAlias = list[
    "capo_health.types.organization_entity_aggregate.OrganizationEntityAggregate"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: OrganizationEntityAggregatesList) -> list:
    import capo_health.types.organization_entity_aggregate

    out: list = []
    for item in value:
        out.append(
            capo_health.types.organization_entity_aggregate.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> OrganizationEntityAggregatesList:
    import capo_health.types.organization_entity_aggregate

    out: OrganizationEntityAggregatesList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_health.types.organization_entity_aggregate.deserialize_aws_json_1_1(
                item
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: OrganizationEntityAggregatesList) -> list:
    import capo_health.types.organization_entity_aggregate

    out: list = []
    for item in value:
        out.append(capo_health.types.organization_entity_aggregate.serialize_cbor(item))
    return out


def deserialize_cbor(data: list) -> OrganizationEntityAggregatesList:
    import capo_health.types.organization_entity_aggregate

    out: OrganizationEntityAggregatesList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_health.types.organization_entity_aggregate.deserialize_cbor(item)
        )
    return out
