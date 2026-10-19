"""Generated from Smithy shape ``com.amazonaws.supplychain#DataIntegrationEventDatasetTargetDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_supplychain.errors import DeserializationError

if TYPE_CHECKING:
    import capo_supplychain.types.data_integration_dataset_arn
    import capo_supplychain.types.data_integration_event_dataset_load_execution_details
    import capo_supplychain.types.data_integration_event_dataset_operation_type


class DataIntegrationEventDatasetTargetDetails(TypedDict, closed=True):
    dataset_identifier: (
        "capo_supplychain.types.data_integration_dataset_arn.DataIntegrationDatasetArn"
    )
    """<p>The datalake dataset ARN identifier.</p>"""
    operation_type: "capo_supplychain.types.data_integration_event_dataset_operation_type.DataIntegrationEventDatasetOperationType"
    """<p>The target dataset load operation type. The available options are:</p> <ul> <li> <p> <b>APPEND</b> - Add new records to the dataset. Noted that this operation type will just try to append records as-is without any primary key or partition constraints.</p> </li> <li> <p> <b>UPSERT</b> - Modify existing records in the dataset with primary key configured, events for datasets without primary keys are not allowed. If event data contains primary keys that match records in the dataset within same partition, then those existing records (in that partition) will be updated. If primary keys do not match, new records will be added. Note that if dataset contain records with duplicate primary key values in the same partition, those duplicate records will be deduped into one updated record.</p> </li> <li> <p> <b>DELETE</b> - Remove existing records in the dataset with primary key configured, events for datasets without primary keys are not allowed. If event data contains primary keys that match records in the dataset within same partition, then those existing records (in that partition) will be deleted. If primary keys do not match, no actions will be done. Note that if dataset contain records with duplicate primary key values in the same partition, all those duplicates will be removed.</p> </li> </ul>"""
    dataset_load_execution: "capo_supplychain.types.data_integration_event_dataset_load_execution_details.DataIntegrationEventDatasetLoadExecutionDetails"
    """<p>The target dataset load execution.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DataIntegrationEventDatasetTargetDetails) -> dict:
    out: dict = {}
    out["datasetIdentifier"] = value["dataset_identifier"]
    import capo_supplychain.types.data_integration_event_dataset_operation_type

    out["operationType"] = (
        capo_supplychain.types.data_integration_event_dataset_operation_type.serialize_json(
            value["operation_type"]
        )
    )
    import capo_supplychain.types.data_integration_event_dataset_load_execution_details

    out["datasetLoadExecution"] = (
        capo_supplychain.types.data_integration_event_dataset_load_execution_details.serialize_json(
            value["dataset_load_execution"]
        )
    )
    return out


def deserialize_json(data: dict) -> DataIntegrationEventDatasetTargetDetails:
    out: DataIntegrationEventDatasetTargetDetails = {}  # type: ignore[typeddict-item]
    if data.get("datasetIdentifier") is not None:
        out["dataset_identifier"] = data["datasetIdentifier"]
    else:
        out["dataset_identifier"] = ""
    if data.get("operationType") is not None:
        import capo_supplychain.types.data_integration_event_dataset_operation_type

        out["operation_type"] = (
            capo_supplychain.types.data_integration_event_dataset_operation_type.deserialize_json(
                data["operationType"]
            )
        )
    else:
        import typing

        out["operation_type"] = typing.cast(
            "capo_supplychain.types.data_integration_event_dataset_operation_type.DataIntegrationEventDatasetOperationType",
            "",
        )
    if data.get("datasetLoadExecution") is not None:
        import capo_supplychain.types.data_integration_event_dataset_load_execution_details

        out["dataset_load_execution"] = (
            capo_supplychain.types.data_integration_event_dataset_load_execution_details.deserialize_json(
                data["datasetLoadExecution"]
            )
        )
    else:
        raise DeserializationError(
            "DataIntegrationEventDatasetTargetDetails.dataset_load_execution required"
        )
    return out
