"""Generated from Smithy shape ``com.amazonaws.cloudwatchomni#CreateAccessGrantInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudwatchomni.errors import DeserializationError

if TYPE_CHECKING:
    import capo_cloudwatchomni.types.access_grant_permission
    import capo_cloudwatchomni.types.access_grant_principal
    import capo_cloudwatchomni.types.client_token
    import capo_cloudwatchomni.types.domain_id
    import capo_cloudwatchomni.types.scoped_actions_list
    import capo_cloudwatchomni.types.space_id
    import capo_cloudwatchomni.types.tag_map


class CreateAccessGrantInput(TypedDict, closed=True):
    domain_id: "capo_cloudwatchomni.types.domain_id.DomainId"
    """The ID of the domain that contains the space."""
    space_id: "capo_cloudwatchomni.types.space_id.SpaceId"
    """The ID of the space to scope the grant to."""
    name: "str"
    """A name that identifies the access grant."""
    principal: "capo_cloudwatchomni.types.access_grant_principal.AccessGrantPrincipal"
    """The principal receiving the grant."""
    permission: (
        "capo_cloudwatchomni.types.access_grant_permission.AccessGrantPermission"
    )
    """The permission to grant. Exactly one permission is granted per request."""
    scoped_actions: NotRequired[
        "capo_cloudwatchomni.types.scoped_actions_list.ScopedActionsList"
    ]
    """Groups of actions to allow, each with the resource scopes and conditions that limit those actions."""
    tags: NotRequired["capo_cloudwatchomni.types.tag_map.TagMap"]
    """The tags to associate with the access grant."""
    client_token: NotRequired["capo_cloudwatchomni.types.client_token.ClientToken"]
    """Idempotency token for safe retries. Repeated requests with the same token return the original result instead of creating a duplicate."""


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: CreateAccessGrantInput) -> dict:
    out: dict = {}
    out["domainId"] = value["domain_id"]
    out["spaceId"] = value["space_id"]
    out["name"] = value["name"]
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
    if "scoped_actions" in value:
        import capo_cloudwatchomni.types.scoped_actions_list

        out["scopedActions"] = (
            capo_cloudwatchomni.types.scoped_actions_list.serialize_cbor(
                value["scoped_actions"]
            )
        )
    if "tags" in value:
        import capo_cloudwatchomni.types.tag_map

        out["tags"] = capo_cloudwatchomni.types.tag_map.serialize_cbor(value["tags"])
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    return out


def deserialize_cbor(data: dict) -> CreateAccessGrantInput:
    out: CreateAccessGrantInput = {}  # type: ignore[typeddict-item]
    if data.get("domainId") is not None:
        out["domain_id"] = data["domainId"]
    else:
        out["domain_id"] = ""
    if data.get("spaceId") is not None:
        out["space_id"] = data["spaceId"]
    else:
        out["space_id"] = ""
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("principal") is not None:
        import capo_cloudwatchomni.types.access_grant_principal

        out["principal"] = (
            capo_cloudwatchomni.types.access_grant_principal.deserialize_cbor(
                data["principal"]
            )
        )
    else:
        raise DeserializationError("CreateAccessGrantInput.principal required")
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
    if data.get("scopedActions") is not None:
        import capo_cloudwatchomni.types.scoped_actions_list

        out["scoped_actions"] = (
            capo_cloudwatchomni.types.scoped_actions_list.deserialize_cbor(
                data["scopedActions"]
            )
        )
    if data.get("tags") is not None:
        import capo_cloudwatchomni.types.tag_map

        out["tags"] = capo_cloudwatchomni.types.tag_map.deserialize_cbor(data["tags"])
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    return out
