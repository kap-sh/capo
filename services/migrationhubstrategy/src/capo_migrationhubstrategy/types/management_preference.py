"""Generated from Smithy shape ``com.amazonaws.migrationhubstrategy#ManagementPreference``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_migrationhubstrategy.errors import DeserializationError, SerializationError
from capo_migrationhubstrategy.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_migrationhubstrategy.types.aws_managed_resources
    import capo_migrationhubstrategy.types.no_management_preference
    import capo_migrationhubstrategy.types.self_manage_resources


class _ManagementPreference_awsManagedResources(TypedDict, closed=True):
    awsManagedResources: (
        "capo_migrationhubstrategy.types.aws_managed_resources.AwsManagedResources"
    )


class _ManagementPreference_selfManageResources(TypedDict, closed=True):
    selfManageResources: (
        "capo_migrationhubstrategy.types.self_manage_resources.SelfManageResources"
    )


class _ManagementPreference_noPreference(TypedDict, closed=True):
    noPreference: "capo_migrationhubstrategy.types.no_management_preference.NoManagementPreference"


ManagementPreference: TypeAlias = (
    _ManagementPreference_awsManagedResources
    | _ManagementPreference_selfManageResources
    | _ManagementPreference_noPreference
    | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: ManagementPreference) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"ManagementPreference: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "awsManagedResources" in value:
        import capo_migrationhubstrategy.types.aws_managed_resources

        return {
            "awsManagedResources": capo_migrationhubstrategy.types.aws_managed_resources.serialize_json(
                value["awsManagedResources"]
            )
        }
    elif "selfManageResources" in value:
        import capo_migrationhubstrategy.types.self_manage_resources

        return {
            "selfManageResources": capo_migrationhubstrategy.types.self_manage_resources.serialize_json(
                value["selfManageResources"]
            )
        }
    elif "noPreference" in value:
        import capo_migrationhubstrategy.types.no_management_preference

        return {
            "noPreference": capo_migrationhubstrategy.types.no_management_preference.serialize_json(
                value["noPreference"]
            )
        }
    else:
        raise SerializationError("ManagementPreference: no variant present")


def deserialize_json(data: dict) -> ManagementPreference:
    if data.get("awsManagedResources") is not None:
        import capo_migrationhubstrategy.types.aws_managed_resources

        return {
            "awsManagedResources": capo_migrationhubstrategy.types.aws_managed_resources.deserialize_json(
                data["awsManagedResources"]
            )
        }
    elif data.get("selfManageResources") is not None:
        import capo_migrationhubstrategy.types.self_manage_resources

        return {
            "selfManageResources": capo_migrationhubstrategy.types.self_manage_resources.deserialize_json(
                data["selfManageResources"]
            )
        }
    elif data.get("noPreference") is not None:
        import capo_migrationhubstrategy.types.no_management_preference

        return {
            "noPreference": capo_migrationhubstrategy.types.no_management_preference.deserialize_json(
                data["noPreference"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("ManagementPreference: no recognized variant key")
