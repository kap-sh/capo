"""Generated from Smithy shape ``com.amazonaws.elementalinference#ScheduleActionOperation``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_elementalinference.errors import DeserializationError, SerializationError
from capo_elementalinference.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_elementalinference.types.remove_clipping_data_source_configuration
    import capo_elementalinference.types.update_clipping_data_source_configuration
    import capo_elementalinference.types.update_output_status


class ScheduleActionOperationUpdateOutputStatusMember(TypedDict, closed=True):
    updateOutputStatus: (
        "capo_elementalinference.types.update_output_status.UpdateOutputStatus"
    )


class ScheduleActionOperationUpdateClippingDataSourceConfigurationMember(
    TypedDict, closed=True
):
    updateClippingDataSourceConfiguration: "capo_elementalinference.types.update_clipping_data_source_configuration.UpdateClippingDataSourceConfiguration"


class ScheduleActionOperationRemoveClippingDataSourceConfigurationMember(
    TypedDict, closed=True
):
    removeClippingDataSourceConfiguration: "capo_elementalinference.types.remove_clipping_data_source_configuration.RemoveClippingDataSourceConfiguration"


ScheduleActionOperation: TypeAlias = (
    ScheduleActionOperationUpdateOutputStatusMember
    | ScheduleActionOperationUpdateClippingDataSourceConfigurationMember
    | ScheduleActionOperationRemoveClippingDataSourceConfigurationMember
    | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: ScheduleActionOperation) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"ScheduleActionOperation: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "updateOutputStatus" in value:
        import capo_elementalinference.types.update_output_status

        return {
            "updateOutputStatus": capo_elementalinference.types.update_output_status.serialize_json(
                value["updateOutputStatus"]
            )
        }
    elif "updateClippingDataSourceConfiguration" in value:
        import capo_elementalinference.types.update_clipping_data_source_configuration

        return {
            "updateClippingDataSourceConfiguration": capo_elementalinference.types.update_clipping_data_source_configuration.serialize_json(
                value["updateClippingDataSourceConfiguration"]
            )
        }
    elif "removeClippingDataSourceConfiguration" in value:
        import capo_elementalinference.types.remove_clipping_data_source_configuration

        return {
            "removeClippingDataSourceConfiguration": capo_elementalinference.types.remove_clipping_data_source_configuration.serialize_json(
                value["removeClippingDataSourceConfiguration"]
            )
        }
    else:
        raise SerializationError("ScheduleActionOperation: no variant present")


def deserialize_json(data: dict) -> ScheduleActionOperation:
    if data.get("updateOutputStatus") is not None:
        import capo_elementalinference.types.update_output_status

        return {
            "updateOutputStatus": capo_elementalinference.types.update_output_status.deserialize_json(
                data["updateOutputStatus"]
            )
        }
    elif data.get("updateClippingDataSourceConfiguration") is not None:
        import capo_elementalinference.types.update_clipping_data_source_configuration

        return {
            "updateClippingDataSourceConfiguration": capo_elementalinference.types.update_clipping_data_source_configuration.deserialize_json(
                data["updateClippingDataSourceConfiguration"]
            )
        }
    elif data.get("removeClippingDataSourceConfiguration") is not None:
        import capo_elementalinference.types.remove_clipping_data_source_configuration

        return {
            "removeClippingDataSourceConfiguration": capo_elementalinference.types.remove_clipping_data_source_configuration.deserialize_json(
                data["removeClippingDataSourceConfiguration"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("ScheduleActionOperation: no recognized variant key")
