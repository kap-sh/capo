"""Generated from Smithy shape ``com.amazonaws.cloudwatchomni#AccessGrant``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudwatchomni.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import capo_cloudwatchomni.types.access_grant_permission
    import capo_cloudwatchomni.types.access_grant_principal
    import capo_cloudwatchomni.types.access_grant_type
    import capo_cloudwatchomni.types.account_id
    import capo_cloudwatchomni.types.arn
    import capo_cloudwatchomni.types.domain_id
    import capo_cloudwatchomni.types.grant_id
    import capo_cloudwatchomni.types.scoped_actions_list
    import capo_cloudwatchomni.types.space_id


class AccessGrant(TypedDict, closed=True):
    grant_id: "capo_cloudwatchomni.types.grant_id.GrantId"
    """The unique ID of the access grant."""
    grant_arn: "capo_cloudwatchomni.types.arn.Arn"
    """The Amazon Resource Name (ARN) of the access grant."""
    name: NotRequired["str"]
    """A name that identifies the access grant."""
    account_id: "capo_cloudwatchomni.types.account_id.AccountId"
    """The AWS account ID that owns the grant."""
    domain_id: "capo_cloudwatchomni.types.domain_id.DomainId"
    """The ID of the domain the grant belongs to."""
    principal: "capo_cloudwatchomni.types.access_grant_principal.AccessGrantPrincipal"
    """The principal receiving the grant."""
    permission: (
        "capo_cloudwatchomni.types.access_grant_permission.AccessGrantPermission"
    )
    """The permission granted."""
    grant_type: "capo_cloudwatchomni.types.access_grant_type.AccessGrantType"
    """Who manages the grant."""
    created_by: "str"
    """The principal that created the grant."""
    created_at: "datetime.datetime"
    """The timestamp when the grant was created."""
    updated_at: "datetime.datetime"
    """The timestamp when the grant was last updated."""
    space_id: "capo_cloudwatchomni.types.space_id.SpaceId"
    """The space this grant applies to. Domain-scoped grants are returned by ListDomainAccessGrantsForOrganization instead."""
    scoped_actions: NotRequired[
        "capo_cloudwatchomni.types.scoped_actions_list.ScopedActionsList"
    ]
    """Groups of actions allowed by the grant, each with the resource scopes and conditions that limit those actions."""


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: AccessGrant) -> dict:
    out: dict = {}
    out["grantId"] = value["grant_id"]
    out["grantArn"] = value["grant_arn"]
    if "name" in value:
        out["name"] = value["name"]
    out["accountId"] = value["account_id"]
    out["domainId"] = value["domain_id"]
    import capo_cloudwatchomni.types.access_grant_principal

    out["principal"] = capo_cloudwatchomni.types.access_grant_principal.serialize_cbor(
        value["principal"]
    )
    import capo_cloudwatchomni.types.access_grant_permission

    out["permission"] = (
        capo_cloudwatchomni.types.access_grant_permission.serialize_cbor(
            value["permission"]
        )
    )
    import capo_cloudwatchomni.types.access_grant_type

    out["grantType"] = capo_cloudwatchomni.types.access_grant_type.serialize_cbor(
        value["grant_type"]
    )
    out["createdBy"] = value["created_by"]
    import capo_cloudwatchomni.types._prelude.timestamp

    out["createdAt"] = capo_cloudwatchomni.types._prelude.timestamp.serialize_cbor(
        value["created_at"]
    )
    import capo_cloudwatchomni.types._prelude.timestamp

    out["updatedAt"] = capo_cloudwatchomni.types._prelude.timestamp.serialize_cbor(
        value["updated_at"]
    )
    out["spaceId"] = value["space_id"]
    if "scoped_actions" in value:
        import capo_cloudwatchomni.types.scoped_actions_list

        out["scopedActions"] = (
            capo_cloudwatchomni.types.scoped_actions_list.serialize_cbor(
                value["scoped_actions"]
            )
        )
    return out


def deserialize_cbor(data: dict) -> AccessGrant:
    out: AccessGrant = {}  # type: ignore[typeddict-item]
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
    if data.get("accountId") is not None:
        out["account_id"] = data["accountId"]
    else:
        out["account_id"] = ""
    if data.get("domainId") is not None:
        out["domain_id"] = data["domainId"]
    else:
        out["domain_id"] = ""
    if data.get("principal") is not None:
        import capo_cloudwatchomni.types.access_grant_principal

        out["principal"] = (
            capo_cloudwatchomni.types.access_grant_principal.deserialize_cbor(
                data["principal"]
            )
        )
    else:
        raise DeserializationError("AccessGrant.principal required")
    if data.get("permission") is not None:
        import capo_cloudwatchomni.types.access_grant_permission

        out["permission"] = (
            capo_cloudwatchomni.types.access_grant_permission.deserialize_cbor(
                data["permission"]
            )
        )
    else:
        import typing

        out["permission"] = typing.cast(
            "capo_cloudwatchomni.types.access_grant_permission.AccessGrantPermission",
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
    if data.get("createdBy") is not None:
        out["created_by"] = data["createdBy"]
    else:
        out["created_by"] = ""
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
    if data.get("spaceId") is not None:
        out["space_id"] = data["spaceId"]
    else:
        out["space_id"] = ""
    if data.get("scopedActions") is not None:
        import capo_cloudwatchomni.types.scoped_actions_list

        out["scoped_actions"] = (
            capo_cloudwatchomni.types.scoped_actions_list.deserialize_cbor(
                data["scopedActions"]
            )
        )
    return out
