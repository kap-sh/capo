"""Generated from Smithy shape ``com.amazonaws.appstream#SoftwareAssociationsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_appstream.types.software_associations

SoftwareAssociationsList: TypeAlias = list[
    "capo_appstream.types.software_associations.SoftwareAssociations"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SoftwareAssociationsList) -> list:
    import capo_appstream.types.software_associations

    out: list = []
    for item in value:
        out.append(
            capo_appstream.types.software_associations.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> SoftwareAssociationsList:
    import capo_appstream.types.software_associations

    out: SoftwareAssociationsList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_appstream.types.software_associations.deserialize_aws_json_1_1(item)
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: SoftwareAssociationsList) -> list:
    import capo_appstream.types.software_associations

    out: list = []
    for item in value:
        out.append(capo_appstream.types.software_associations.serialize_cbor(item))
    return out


def deserialize_cbor(data: list) -> SoftwareAssociationsList:
    import capo_appstream.types.software_associations

    out: SoftwareAssociationsList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_appstream.types.software_associations.deserialize_cbor(item))
    return out
