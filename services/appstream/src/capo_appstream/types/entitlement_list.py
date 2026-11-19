"""Generated from Smithy shape ``com.amazonaws.appstream#EntitlementList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_appstream.types.entitlement

EntitlementList: TypeAlias = list["capo_appstream.types.entitlement.Entitlement"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EntitlementList) -> list:
    import capo_appstream.types.entitlement

    out: list = []
    for item in value:
        out.append(capo_appstream.types.entitlement.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> EntitlementList:
    import capo_appstream.types.entitlement

    out: EntitlementList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_appstream.types.entitlement.deserialize_aws_json_1_1(item))
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: EntitlementList) -> list:
    import capo_appstream.types.entitlement

    out: list = []
    for item in value:
        out.append(capo_appstream.types.entitlement.serialize_cbor(item))
    return out


def deserialize_cbor(data: list) -> EntitlementList:
    import capo_appstream.types.entitlement

    out: EntitlementList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_appstream.types.entitlement.deserialize_cbor(item))
    return out
