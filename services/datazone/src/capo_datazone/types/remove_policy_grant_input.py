"""Generated from Smithy shape ``com.amazonaws.datazone#RemovePolicyGrantInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_datazone.types.client_token
    import capo_datazone.types.domain_id
    import capo_datazone.types.grant_identifier
    import capo_datazone.types.managed_policy_type
    import capo_datazone.types.policy_grant_principal
    import capo_datazone.types.target_entity_type


class RemovePolicyGrantInput(TypedDict, closed=True):
    domain_identifier: "capo_datazone.types.domain_id.DomainId"
    """<p>The ID of the domain where you want to remove a policy grant.</p>"""
    entity_type: "capo_datazone.types.target_entity_type.TargetEntityType"
    """<p>The type of the entity from which you want to remove a policy grant.</p>"""
    entity_identifier: "str"
    """<p>The ID of the entity from which you want to remove a policy grant.</p>"""
    policy_type: "capo_datazone.types.managed_policy_type.ManagedPolicyType"
    """<p>The type of the policy that you want to remove.</p>"""
    principal: "capo_datazone.types.policy_grant_principal.PolicyGrantPrincipal"
    """<p>The principal from which you want to remove a policy grant.</p>"""
    grant_identifier: NotRequired[
        "capo_datazone.types.grant_identifier.GrantIdentifier"
    ]
    """<p>The ID of the policy grant that is to be removed from a specified entity.</p>"""
    client_token: NotRequired["capo_datazone.types.client_token.ClientToken"]
    """<p>A unique, case-sensitive identifier that is provided to ensure the idempotency of the request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RemovePolicyGrantInput) -> dict:
    out: dict = {}
    import capo_datazone.types.managed_policy_type

    out["policyType"] = capo_datazone.types.managed_policy_type.serialize_json(
        value["policy_type"]
    )
    import capo_datazone.types.policy_grant_principal

    out["principal"] = capo_datazone.types.policy_grant_principal.serialize_json(
        value["principal"]
    )
    if "grant_identifier" in value:
        out["grantIdentifier"] = value["grant_identifier"]
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    return out


def deserialize_json(data: dict) -> RemovePolicyGrantInput:
    out: RemovePolicyGrantInput = {}  # type: ignore[typeddict-item]
    if data.get("policyType") is not None:
        import capo_datazone.types.managed_policy_type

        out["policy_type"] = capo_datazone.types.managed_policy_type.deserialize_json(
            data["policyType"]
        )
    else:
        import typing

        out["policy_type"] = typing.cast(
            "capo_datazone.types.managed_policy_type.ManagedPolicyType", ""
        )
    if data.get("principal") is not None:
        import capo_datazone.types.policy_grant_principal

        out["principal"] = capo_datazone.types.policy_grant_principal.deserialize_json(
            data["principal"]
        )
    else:
        import capo_datazone.types._unknown

        out["principal"] = capo_datazone.types._unknown.UnknownUnionMember("")
    if data.get("grantIdentifier") is not None:
        out["grant_identifier"] = data["grantIdentifier"]
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    return out
