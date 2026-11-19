"""Generated from Smithy shape ``com.amazonaws.workspaces#DeletableCertificateBasedAuthPropertiesList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_workspaces.types.deletable_certificate_based_auth_property

DeletableCertificateBasedAuthPropertiesList: TypeAlias = list[
    "capo_workspaces.types.deletable_certificate_based_auth_property.DeletableCertificateBasedAuthProperty"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeletableCertificateBasedAuthPropertiesList) -> list:
    import capo_workspaces.types.deletable_certificate_based_auth_property

    out: list = []
    for item in value:
        out.append(
            capo_workspaces.types.deletable_certificate_based_auth_property.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> DeletableCertificateBasedAuthPropertiesList:
    import capo_workspaces.types.deletable_certificate_based_auth_property

    out: DeletableCertificateBasedAuthPropertiesList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_workspaces.types.deletable_certificate_based_auth_property.deserialize_aws_json_1_1(
                item
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DeletableCertificateBasedAuthPropertiesList) -> list:
    import capo_workspaces.types.deletable_certificate_based_auth_property

    out: list = []
    for item in value:
        out.append(
            capo_workspaces.types.deletable_certificate_based_auth_property.serialize_cbor(
                item
            )
        )
    return out


def deserialize_cbor(data: list) -> DeletableCertificateBasedAuthPropertiesList:
    import capo_workspaces.types.deletable_certificate_based_auth_property

    out: DeletableCertificateBasedAuthPropertiesList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_workspaces.types.deletable_certificate_based_auth_property.deserialize_cbor(
                item
            )
        )
    return out
