"""Generated from Smithy shape ``com.amazonaws.cloudwatchomni#CreateDomainAccessGrantForOrganizationInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudwatchomni.errors import DeserializationError

if TYPE_CHECKING:
    import capo_cloudwatchomni.types.client_token
    import capo_cloudwatchomni.types.domain_id
    import capo_cloudwatchomni.types.organization_access_grant_principal
    import capo_cloudwatchomni.types.organization_grant_permission
    import capo_cloudwatchomni.types.tag_map


class CreateDomainAccessGrantForOrganizationInput(TypedDict, closed=True):
    domain_id: "capo_cloudwatchomni.types.domain_id.DomainId"
    """The ID of the organization domain to create the grant on."""
    name: "str"
    """A name that identifies the access grant."""
    principal: "capo_cloudwatchomni.types.organization_access_grant_principal.OrganizationAccessGrantPrincipal"
    """The principal receiving the grant."""
    permission: "capo_cloudwatchomni.types.organization_grant_permission.OrganizationGrantPermission"
    """The permission to grant."""
    tags: NotRequired["capo_cloudwatchomni.types.tag_map.TagMap"]
    """The tags to associate with the access grant."""
    client_token: NotRequired["capo_cloudwatchomni.types.client_token.ClientToken"]
    """Idempotency token for safe retries. Repeated requests with the same token return the original result instead of creating a duplicate."""


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: CreateDomainAccessGrantForOrganizationInput) -> dict:
    out: dict = {}
    out["domainId"] = value["domain_id"]
    out["name"] = value["name"]
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
    if "tags" in value:
        import capo_cloudwatchomni.types.tag_map

        out["tags"] = capo_cloudwatchomni.types.tag_map.serialize_cbor(value["tags"])
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    return out


def deserialize_cbor(data: dict) -> CreateDomainAccessGrantForOrganizationInput:
    out: CreateDomainAccessGrantForOrganizationInput = {}  # type: ignore[typeddict-item]
    if data.get("domainId") is not None:
        out["domain_id"] = data["domainId"]
    else:
        out["domain_id"] = ""
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("principal") is not None:
        import capo_cloudwatchomni.types.organization_access_grant_principal

        out["principal"] = (
            capo_cloudwatchomni.types.organization_access_grant_principal.deserialize_cbor(
                data["principal"]
            )
        )
    else:
        raise DeserializationError(
            "CreateDomainAccessGrantForOrganizationInput.principal required"
        )
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
    if data.get("tags") is not None:
        import capo_cloudwatchomni.types.tag_map

        out["tags"] = capo_cloudwatchomni.types.tag_map.deserialize_cbor(data["tags"])
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    return out
