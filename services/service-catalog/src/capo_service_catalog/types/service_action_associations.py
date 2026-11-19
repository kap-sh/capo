"""Generated from Smithy shape ``com.amazonaws.servicecatalog#ServiceActionAssociations``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_service_catalog.types.service_action_association

ServiceActionAssociations: TypeAlias = list[
    "capo_service_catalog.types.service_action_association.ServiceActionAssociation"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ServiceActionAssociations) -> list:
    import capo_service_catalog.types.service_action_association

    out: list = []
    for item in value:
        out.append(
            capo_service_catalog.types.service_action_association.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ServiceActionAssociations:
    import capo_service_catalog.types.service_action_association

    out: ServiceActionAssociations = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_service_catalog.types.service_action_association.deserialize_aws_json_1_1(
                item
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ServiceActionAssociations) -> list:
    import capo_service_catalog.types.service_action_association

    out: list = []
    for item in value:
        out.append(
            capo_service_catalog.types.service_action_association.serialize_cbor(item)
        )
    return out


def deserialize_cbor(data: list) -> ServiceActionAssociations:
    import capo_service_catalog.types.service_action_association

    out: ServiceActionAssociations = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_service_catalog.types.service_action_association.deserialize_cbor(item)
        )
    return out
