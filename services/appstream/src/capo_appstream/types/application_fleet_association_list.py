"""Generated from Smithy shape ``com.amazonaws.appstream#ApplicationFleetAssociationList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_appstream.types.application_fleet_association

ApplicationFleetAssociationList: TypeAlias = list[
    "capo_appstream.types.application_fleet_association.ApplicationFleetAssociation"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ApplicationFleetAssociationList) -> list:
    import capo_appstream.types.application_fleet_association

    out: list = []
    for item in value:
        out.append(
            capo_appstream.types.application_fleet_association.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ApplicationFleetAssociationList:
    import capo_appstream.types.application_fleet_association

    out: ApplicationFleetAssociationList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_appstream.types.application_fleet_association.deserialize_aws_json_1_1(
                item
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ApplicationFleetAssociationList) -> list:
    import capo_appstream.types.application_fleet_association

    out: list = []
    for item in value:
        out.append(
            capo_appstream.types.application_fleet_association.serialize_cbor(item)
        )
    return out


def deserialize_cbor(data: list) -> ApplicationFleetAssociationList:
    import capo_appstream.types.application_fleet_association

    out: ApplicationFleetAssociationList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_appstream.types.application_fleet_association.deserialize_cbor(item)
        )
    return out
