"""Generated from Smithy shape ``com.amazonaws.appstream#EntitlementAttributeList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_appstream.types.entitlement_attribute

EntitlementAttributeList: TypeAlias = list[
    "capo_appstream.types.entitlement_attribute.EntitlementAttribute"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EntitlementAttributeList) -> list:
    import capo_appstream.types.entitlement_attribute

    out: list = []
    for item in value:
        out.append(
            capo_appstream.types.entitlement_attribute.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> EntitlementAttributeList:
    import capo_appstream.types.entitlement_attribute

    out: EntitlementAttributeList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_appstream.types.entitlement_attribute.deserialize_aws_json_1_1(item)
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: EntitlementAttributeList) -> list:
    import capo_appstream.types.entitlement_attribute

    out: list = []
    for item in value:
        out.append(capo_appstream.types.entitlement_attribute.serialize_cbor(item))
    return out


def deserialize_cbor(data: list) -> EntitlementAttributeList:
    import capo_appstream.types.entitlement_attribute

    out: EntitlementAttributeList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_appstream.types.entitlement_attribute.deserialize_cbor(item))
    return out
