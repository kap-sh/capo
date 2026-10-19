"""Generated from Smithy shape ``com.amazonaws.cloudwatchomni#OrganizationAccessGrantSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudwatchomni.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import capo_cloudwatchomni.types.access_grant_type
    import capo_cloudwatchomni.types.arn
    import capo_cloudwatchomni.types.domain_id
    import capo_cloudwatchomni.types.grant_id
    import capo_cloudwatchomni.types.organization_access_grant_principal
    import capo_cloudwatchomni.types.organization_grant_permission


class OrganizationAccessGrantSummary(TypedDict, closed=True):
    grant_id: "capo_cloudwatchomni.types.grant_id.GrantId"
    """The unique ID of the access grant."""
    grant_arn: "capo_cloudwatchomni.types.arn.Arn"
    """The Amazon Resource Name (ARN) of the access grant."""
    name: NotRequired["str"]
    """A name that identifies the access grant."""
    domain_id: "capo_cloudwatchomni.types.domain_id.DomainId"
    """The ID of the organization domain the grant belongs to."""
    principal: "capo_cloudwatchomni.types.organization_access_grant_principal.OrganizationAccessGrantPrincipal"
    """The principal receiving the grant."""
    permission: "capo_cloudwatchomni.types.organization_grant_permission.OrganizationGrantPermission"
    """The permission granted."""
    grant_type: "capo_cloudwatchomni.types.access_grant_type.AccessGrantType"
    """Who manages the grant."""
    created_at: "datetime.datetime"
    """The timestamp when the access grant was created."""
    updated_at: "datetime.datetime"
    """The timestamp when the access grant was last updated."""


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: OrganizationAccessGrantSummary) -> dict:
    out: dict = {}
    out["grantId"] = value["grant_id"]
    out["grantArn"] = value["grant_arn"]
    if "name" in value:
        out["name"] = value["name"]
    out["domainId"] = value["domain_id"]
    import capo_cloudwatchomni.types.organization_access_grant_principal

    out["principal"] = (
        capo_cloudwatchomni.types.organization_access_grant_principal.serialize_cbor(
            value["principal"]
        )
    )
    import capo_cloudwatchomni.types.organization_grant_permission

    out["permission"] = (
        capo_cloudwatchomni.types.organization_grant_permission.serialize_cbor(
            value["permission"]
        )
    )
    import capo_cloudwatchomni.types.access_grant_type

    out["grantType"] = capo_cloudwatchomni.types.access_grant_type.serialize_cbor(
        value["grant_type"]
    )
    import capo_cloudwatchomni.types._prelude.timestamp

    out["createdAt"] = capo_cloudwatchomni.types._prelude.timestamp.serialize_cbor(
        value["created_at"]
    )
    import capo_cloudwatchomni.types._prelude.timestamp

    out["updatedAt"] = capo_cloudwatchomni.types._prelude.timestamp.serialize_cbor(
        value["updated_at"]
    )
    return out


def deserialize_cbor(data: dict) -> OrganizationAccessGrantSummary:
    out: OrganizationAccessGrantSummary = {}  # type: ignore[typeddict-item]
    if data.get("grantId") is not None:
        out["grant_id"] = data["grantId"]
    else:
        out["grant_id"] = ""
    if data.get("grantArn") is not None:
        out["grant_arn"] = data["grantArn"]
    else:
        out["grant_arn"] = ""
    if data.get("name") is not None:
        out["name"] = data["name"]
    if data.get("domainId") is not None:
        out["domain_id"] = data["domainId"]
    else:
        out["domain_id"] = ""
    if data.get("principal") is not None:
        import capo_cloudwatchomni.types.organization_access_grant_principal

        out["principal"] = (
            capo_cloudwatchomni.types.organization_access_grant_principal.deserialize_cbor(
                data["principal"]
            )
        )
    else:
        raise DeserializationError("OrganizationAccessGrantSummary.principal required")
    if data.get("permission") is not None:
        import capo_cloudwatchomni.types.organization_grant_permission

        out["permission"] = (
            capo_cloudwatchomni.types.organization_grant_permission.deserialize_cbor(
                data["permission"]
            )
        )
    else:
        import typing

        out["permission"] = typing.cast(
            "capo_cloudwatchomni.types.organization_grant_permission.OrganizationGrantPermission",
            "",
        )
    if data.get("grantType") is not None:
        import capo_cloudwatchomni.types.access_grant_type

        out["grant_type"] = (
            capo_cloudwatchomni.types.access_grant_type.deserialize_cbor(
                data["grantType"]
            )
        )
    else:
        import typing

        out["grant_type"] = typing.cast(
            "capo_cloudwatchomni.types.access_grant_type.AccessGrantType", ""
        )
    if data.get("createdAt") is not None:
        import capo_cloudwatchomni.types._prelude.timestamp

        out["created_at"] = (
            capo_cloudwatchomni.types._prelude.timestamp.deserialize_cbor(
                data["createdAt"]
            )
        )
    else:
        import datetime

        out["created_at"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    if data.get("updatedAt") is not None:
        import capo_cloudwatchomni.types._prelude.timestamp

        out["updated_at"] = (
            capo_cloudwatchomni.types._prelude.timestamp.deserialize_cbor(
                data["updatedAt"]
            )
        )
    else:
        import datetime

        out["updated_at"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    return out
