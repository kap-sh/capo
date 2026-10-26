"""Generated from Smithy shape ``com.amazonaws.ssmincidents#UpdateReplicationSetAction``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_ssm_incidents.errors import DeserializationError, SerializationError
from capo_ssm_incidents.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_ssm_incidents.types.add_region_action
    import capo_ssm_incidents.types.delete_region_action


class _UpdateReplicationSetAction_addRegionAction(TypedDict, closed=True):
    addRegionAction: "capo_ssm_incidents.types.add_region_action.AddRegionAction"


class _UpdateReplicationSetAction_deleteRegionAction(TypedDict, closed=True):
    deleteRegionAction: (
        "capo_ssm_incidents.types.delete_region_action.DeleteRegionAction"
    )


UpdateReplicationSetAction: TypeAlias = (
    _UpdateReplicationSetAction_addRegionAction
    | _UpdateReplicationSetAction_deleteRegionAction
    | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: UpdateReplicationSetAction) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"UpdateReplicationSetAction: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "addRegionAction" in value:
        import capo_ssm_incidents.types.add_region_action

        return {
            "addRegionAction": capo_ssm_incidents.types.add_region_action.serialize_json(
                value["addRegionAction"]
            )
        }
    elif "deleteRegionAction" in value:
        import capo_ssm_incidents.types.delete_region_action

        return {
            "deleteRegionAction": capo_ssm_incidents.types.delete_region_action.serialize_json(
                value["deleteRegionAction"]
            )
        }
    else:
        raise SerializationError("UpdateReplicationSetAction: no variant present")


def deserialize_json(data: dict) -> UpdateReplicationSetAction:
    if data.get("addRegionAction") is not None:
        import capo_ssm_incidents.types.add_region_action

        return {
            "addRegionAction": capo_ssm_incidents.types.add_region_action.deserialize_json(
                data["addRegionAction"]
            )
        }
    elif data.get("deleteRegionAction") is not None:
        import capo_ssm_incidents.types.delete_region_action

        return {
            "deleteRegionAction": capo_ssm_incidents.types.delete_region_action.deserialize_json(
                data["deleteRegionAction"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError(
            "UpdateReplicationSetAction: no recognized variant key"
        )
