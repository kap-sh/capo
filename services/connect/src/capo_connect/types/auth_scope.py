"""Generated from Smithy shape ``com.amazonaws.connect#AuthScope``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connect.types.auth_code_entity_type
    import capo_connect.types.customer_profiles_domain_name
    import capo_connect.types.entity_id
    import capo_connect.types.security_profile_ids


class AuthScope(TypedDict, closed=True):
    security_profile_ids: NotRequired[
        "capo_connect.types.security_profile_ids.SecurityProfileIds"
    ]
    """<p>The list of security profile identifiers to scope the session to. Maximum of 10 security profiles.</p>"""
    entity_type: "capo_connect.types.auth_code_entity_type.AuthCodeEntityType"
    """<p>The type of entity to scope the session to.</p>"""
    entity_id: NotRequired["capo_connect.types.entity_id.EntityId"]
    """<p>The identifier of the entity to scope the session to.</p>"""
    domain_name: NotRequired[
        "capo_connect.types.customer_profiles_domain_name.CustomerProfilesDomainName"
    ]
    """<p>The name of the Customer Profiles domain to scope the session to.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AuthScope) -> dict:
    out: dict = {}
    if "security_profile_ids" in value:
        import capo_connect.types.security_profile_ids

        out["SecurityProfileIds"] = (
            capo_connect.types.security_profile_ids.serialize_json(
                value["security_profile_ids"]
            )
        )
    import capo_connect.types.auth_code_entity_type

    out["EntityType"] = capo_connect.types.auth_code_entity_type.serialize_json(
        value["entity_type"]
    )
    if "entity_id" in value:
        out["EntityId"] = value["entity_id"]
    if "domain_name" in value:
        out["DomainName"] = value["domain_name"]
    return out


def deserialize_json(data: dict) -> AuthScope:
    out: AuthScope = {}  # type: ignore[typeddict-item]
    if data.get("SecurityProfileIds") is not None:
        import capo_connect.types.security_profile_ids

        out["security_profile_ids"] = (
            capo_connect.types.security_profile_ids.deserialize_json(
                data["SecurityProfileIds"]
            )
        )
    if data.get("EntityType") is not None:
        import capo_connect.types.auth_code_entity_type

        out["entity_type"] = capo_connect.types.auth_code_entity_type.deserialize_json(
            data["EntityType"]
        )
    else:
        import typing

        out["entity_type"] = typing.cast(
            "capo_connect.types.auth_code_entity_type.AuthCodeEntityType", ""
        )
    if data.get("EntityId") is not None:
        out["entity_id"] = data["EntityId"]
    if data.get("DomainName") is not None:
        out["domain_name"] = data["DomainName"]
    return out
