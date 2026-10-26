"""Generated from Smithy shape ``com.amazonaws.datazone#AddPolicyGrantInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_datazone.types.client_token
    import capo_datazone.types.domain_id
    import capo_datazone.types.managed_policy_type
    import capo_datazone.types.policy_grant_detail
    import capo_datazone.types.policy_grant_principal
    import capo_datazone.types.target_entity_type


class AddPolicyGrantInput(TypedDict, closed=True):
    domain_identifier: "capo_datazone.types.domain_id.DomainId"
    """<p>The ID of the domain where you want to add a policy grant.</p>"""
    entity_type: "capo_datazone.types.target_entity_type.TargetEntityType"
    """<p>The type of entity (resource) to which the grant is added.</p>"""
    entity_identifier: "str"
    """<p>The ID of the entity (resource) to which you want to add a policy grant.</p>"""
    policy_type: "capo_datazone.types.managed_policy_type.ManagedPolicyType"
    """<p>The type of policy that you want to grant.</p>"""
    principal: "capo_datazone.types.policy_grant_principal.PolicyGrantPrincipal"
    """<p>The principal to whom the permissions are granted.</p>"""
    detail: "capo_datazone.types.policy_grant_detail.PolicyGrantDetail"
    """<p>The details of the policy grant.</p>"""
    client_token: NotRequired["capo_datazone.types.client_token.ClientToken"]
    """<p>A unique, case-sensitive identifier that is provided to ensure the idempotency of the request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AddPolicyGrantInput) -> dict:
    out: dict = {}
    import capo_datazone.types.managed_policy_type

    out["policyType"] = capo_datazone.types.managed_policy_type.serialize_json(
        value["policy_type"]
    )
    import capo_datazone.types.policy_grant_principal

    out["principal"] = capo_datazone.types.policy_grant_principal.serialize_json(
        value["principal"]
    )
    import capo_datazone.types.policy_grant_detail

    out["detail"] = capo_datazone.types.policy_grant_detail.serialize_json(
        value["detail"]
    )
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    return out


def deserialize_json(data: dict) -> AddPolicyGrantInput:
    out: AddPolicyGrantInput = {}  # type: ignore[typeddict-item]
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
        out["principal"] = {"$unknown": {"name": ""}}
    if data.get("detail") is not None:
        import capo_datazone.types.policy_grant_detail

        out["detail"] = capo_datazone.types.policy_grant_detail.deserialize_json(
            data["detail"]
        )
    else:
        out["detail"] = {"$unknown": {"name": ""}}
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    return out
