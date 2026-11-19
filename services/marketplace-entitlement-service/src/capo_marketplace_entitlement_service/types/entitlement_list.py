"""Generated from Smithy shape ``com.amazonaws.marketplaceentitlementservice#EntitlementList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_marketplace_entitlement_service.types.entitlement

EntitlementList: TypeAlias = list[
    "capo_marketplace_entitlement_service.types.entitlement.Entitlement"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EntitlementList) -> list:
    import capo_marketplace_entitlement_service.types.entitlement

    out: list = []
    for item in value:
        out.append(
            capo_marketplace_entitlement_service.types.entitlement.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> EntitlementList:
    import capo_marketplace_entitlement_service.types.entitlement

    out: EntitlementList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_marketplace_entitlement_service.types.entitlement.deserialize_aws_json_1_1(
                item
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: EntitlementList) -> list:
    import capo_marketplace_entitlement_service.types.entitlement

    out: list = []
    for item in value:
        out.append(
            capo_marketplace_entitlement_service.types.entitlement.serialize_cbor(item)
        )
    return out


def deserialize_cbor(data: list) -> EntitlementList:
    import capo_marketplace_entitlement_service.types.entitlement

    out: EntitlementList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_marketplace_entitlement_service.types.entitlement.deserialize_cbor(
                item
            )
        )
    return out
