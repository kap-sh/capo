"""Generated from Smithy shape ``com.amazonaws.launchwizard#AccountConstraint``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_launch_wizard.errors import DeserializationError, SerializationError
from capo_launch_wizard.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_launch_wizard.types.delegated_admin_constraint
    import capo_launch_wizard.types.management_account_constraint


class _AccountConstraint_managementAccount(TypedDict, closed=True):
    managementAccount: "capo_launch_wizard.types.management_account_constraint.ManagementAccountConstraint"


class _AccountConstraint_delegatedAdmin(TypedDict, closed=True):
    delegatedAdmin: (
        "capo_launch_wizard.types.delegated_admin_constraint.DelegatedAdminConstraint"
    )


AccountConstraint: TypeAlias = (
    _AccountConstraint_managementAccount
    | _AccountConstraint_delegatedAdmin
    | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: AccountConstraint) -> dict:
    if isinstance(value, UnknownUnionMember):
        raise SerializationError(
            f"AccountConstraint: cannot serialize unknown variant {value.name!r}"
        )
    elif "managementAccount" in value:
        import capo_launch_wizard.types.management_account_constraint

        return {
            "managementAccount": capo_launch_wizard.types.management_account_constraint.serialize_json(
                value["managementAccount"]
            )
        }
    elif "delegatedAdmin" in value:
        import capo_launch_wizard.types.delegated_admin_constraint

        return {
            "delegatedAdmin": capo_launch_wizard.types.delegated_admin_constraint.serialize_json(
                value["delegatedAdmin"]
            )
        }
    else:
        raise SerializationError("AccountConstraint: no variant present")


def deserialize_json(data: dict) -> AccountConstraint:
    if data.get("managementAccount") is not None:
        import capo_launch_wizard.types.management_account_constraint

        return {
            "managementAccount": capo_launch_wizard.types.management_account_constraint.deserialize_json(
                data["managementAccount"]
            )
        }
    elif data.get("delegatedAdmin") is not None:
        import capo_launch_wizard.types.delegated_admin_constraint

        return {
            "delegatedAdmin": capo_launch_wizard.types.delegated_admin_constraint.deserialize_json(
                data["delegatedAdmin"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return UnknownUnionMember(name)
        raise DeserializationError("AccountConstraint: no recognized variant key")
