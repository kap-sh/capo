"""Generated from Smithy shape ``com.amazonaws.datazone#PolicyGrantPrincipal``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_datazone.errors import DeserializationError, SerializationError
from capo_datazone.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_datazone.types.domain_unit_policy_grant_principal
    import capo_datazone.types.group_policy_grant_principal
    import capo_datazone.types.project_policy_grant_principal
    import capo_datazone.types.user_policy_grant_principal


class _PolicyGrantPrincipal_user(TypedDict, closed=True):
    user: "capo_datazone.types.user_policy_grant_principal.UserPolicyGrantPrincipal"


class _PolicyGrantPrincipal_group(TypedDict, closed=True):
    group: "capo_datazone.types.group_policy_grant_principal.GroupPolicyGrantPrincipal"


class _PolicyGrantPrincipal_project(TypedDict, closed=True):
    project: (
        "capo_datazone.types.project_policy_grant_principal.ProjectPolicyGrantPrincipal"
    )


class _PolicyGrantPrincipal_domainUnit(TypedDict, closed=True):
    domainUnit: "capo_datazone.types.domain_unit_policy_grant_principal.DomainUnitPolicyGrantPrincipal"


PolicyGrantPrincipal: TypeAlias = (
    _PolicyGrantPrincipal_user
    | _PolicyGrantPrincipal_group
    | _PolicyGrantPrincipal_project
    | _PolicyGrantPrincipal_domainUnit
    | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: PolicyGrantPrincipal) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"PolicyGrantPrincipal: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "user" in value:
        import capo_datazone.types.user_policy_grant_principal

        return {
            "user": capo_datazone.types.user_policy_grant_principal.serialize_json(
                value["user"]
            )
        }
    elif "group" in value:
        import capo_datazone.types.group_policy_grant_principal

        return {
            "group": capo_datazone.types.group_policy_grant_principal.serialize_json(
                value["group"]
            )
        }
    elif "project" in value:
        import capo_datazone.types.project_policy_grant_principal

        return {
            "project": capo_datazone.types.project_policy_grant_principal.serialize_json(
                value["project"]
            )
        }
    elif "domainUnit" in value:
        import capo_datazone.types.domain_unit_policy_grant_principal

        return {
            "domainUnit": capo_datazone.types.domain_unit_policy_grant_principal.serialize_json(
                value["domainUnit"]
            )
        }
    else:
        raise SerializationError("PolicyGrantPrincipal: no variant present")


def deserialize_json(data: dict) -> PolicyGrantPrincipal:
    if data.get("user") is not None:
        import capo_datazone.types.user_policy_grant_principal

        return {
            "user": capo_datazone.types.user_policy_grant_principal.deserialize_json(
                data["user"]
            )
        }
    elif data.get("group") is not None:
        import capo_datazone.types.group_policy_grant_principal

        return {
            "group": capo_datazone.types.group_policy_grant_principal.deserialize_json(
                data["group"]
            )
        }
    elif data.get("project") is not None:
        import capo_datazone.types.project_policy_grant_principal

        return {
            "project": capo_datazone.types.project_policy_grant_principal.deserialize_json(
                data["project"]
            )
        }
    elif data.get("domainUnit") is not None:
        import capo_datazone.types.domain_unit_policy_grant_principal

        return {
            "domainUnit": capo_datazone.types.domain_unit_policy_grant_principal.deserialize_json(
                data["domainUnit"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("PolicyGrantPrincipal: no recognized variant key")
