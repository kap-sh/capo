"""Generated from Smithy shape ``com.amazonaws.cloudwatchomni#OrganizationAccessGrantPrincipal``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cloudwatchomni.types.access_grant_principal_attribute_list
    import capo_cloudwatchomni.types.organization_grant_principal_type
    import capo_cloudwatchomni.types.organization_principal_id


class OrganizationAccessGrantPrincipal(TypedDict, closed=True):
    principal_type: "capo_cloudwatchomni.types.organization_grant_principal_type.OrganizationGrantPrincipalType"
    """The type of principal receiving the grant."""
    principal_id: NotRequired[
        "capo_cloudwatchomni.types.organization_principal_id.OrganizationPrincipalId"
    ]
    """The ID of the principal receiving the grant."""
    principal_attributes: NotRequired[
        "capo_cloudwatchomni.types.access_grant_principal_attribute_list.AccessGrantPrincipalAttributeList"
    ]
    """Attribute conditions for attribute-based access. When provided, the grant targets any principal matching all specified conditions. Supported only for IDC_USER principals."""


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: OrganizationAccessGrantPrincipal) -> dict:
    out: dict = {}
    import capo_cloudwatchomni.types.organization_grant_principal_type

    out["principalType"] = (
        capo_cloudwatchomni.types.organization_grant_principal_type.serialize_cbor(
            value["principal_type"]
        )
    )
    if "principal_id" in value:
        out["principalId"] = value["principal_id"]
    if "principal_attributes" in value:
        import capo_cloudwatchomni.types.access_grant_principal_attribute_list

        out["principalAttributes"] = (
            capo_cloudwatchomni.types.access_grant_principal_attribute_list.serialize_cbor(
                value["principal_attributes"]
            )
        )
    return out


def deserialize_cbor(data: dict) -> OrganizationAccessGrantPrincipal:
    out: OrganizationAccessGrantPrincipal = {}  # type: ignore[typeddict-item]
    if data.get("principalType") is not None:
        import capo_cloudwatchomni.types.organization_grant_principal_type

        out["principal_type"] = (
            capo_cloudwatchomni.types.organization_grant_principal_type.deserialize_cbor(
                data["principalType"]
            )
        )
    else:
        import typing

        out["principal_type"] = typing.cast(
            "capo_cloudwatchomni.types.organization_grant_principal_type.OrganizationGrantPrincipalType",
            "",
        )
    if data.get("principalId") is not None:
        out["principal_id"] = data["principalId"]
    if data.get("principalAttributes") is not None:
        import capo_cloudwatchomni.types.access_grant_principal_attribute_list

        out["principal_attributes"] = (
            capo_cloudwatchomni.types.access_grant_principal_attribute_list.deserialize_cbor(
                data["principalAttributes"]
            )
        )
    return out
