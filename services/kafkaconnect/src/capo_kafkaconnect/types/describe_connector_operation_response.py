"""Generated from Smithy shape ``com.amazonaws.kafkaconnect#DescribeConnectorOperationResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_kafkaconnect.types.__list_of_connector_operation_step
    import capo_kafkaconnect.types.__string
    import capo_kafkaconnect.types.__timestamp_iso8601
    import capo_kafkaconnect.types.connector_configuration
    import capo_kafkaconnect.types.connector_operation_state
    import capo_kafkaconnect.types.connector_operation_type
    import capo_kafkaconnect.types.state_description
    import capo_kafkaconnect.types.worker_setting


class DescribeConnectorOperationResponse(TypedDict, closed=True):
    connector_arn: NotRequired["capo_kafkaconnect.types.__string.__string"]
    """<p>The Amazon Resource Name (ARN) of the connector.</p>"""
    connector_operation_arn: NotRequired["capo_kafkaconnect.types.__string.__string"]
    """<p>The Amazon Resource Name (ARN) of the connector operation.</p>"""
    connector_operation_state: NotRequired[
        "capo_kafkaconnect.types.connector_operation_state.ConnectorOperationState"
    ]
    """<p>The state of the connector operation.</p>"""
    connector_operation_type: NotRequired[
        "capo_kafkaconnect.types.connector_operation_type.ConnectorOperationType"
    ]
    """<p>The type of connector operation performed.</p>"""
    operation_steps: NotRequired[
        "capo_kafkaconnect.types.__list_of_connector_operation_step.__listOfConnectorOperationStep"
    ]
    """<p>The array of operation steps taken.</p>"""
    origin_worker_setting: NotRequired[
        "capo_kafkaconnect.types.worker_setting.WorkerSetting"
    ]
    """<p>The origin worker setting.</p>"""
    origin_connector_configuration: NotRequired[
        "capo_kafkaconnect.types.connector_configuration.ConnectorConfiguration"
    ]
    """<p>The origin connector configuration.</p>"""
    target_worker_setting: NotRequired[
        "capo_kafkaconnect.types.worker_setting.WorkerSetting"
    ]
    """<p>The target worker setting.</p>"""
    target_connector_configuration: NotRequired[
        "capo_kafkaconnect.types.connector_configuration.ConnectorConfiguration"
    ]
    """<p>The target connector configuration.</p>"""
    error_info: NotRequired[
        "capo_kafkaconnect.types.state_description.StateDescription"
    ]
    creation_time: NotRequired[
        "capo_kafkaconnect.types.__timestamp_iso8601.__timestampIso8601"
    ]
    """<p>The time when the operation was created.</p>"""
    end_time: NotRequired[
        "capo_kafkaconnect.types.__timestamp_iso8601.__timestampIso8601"
    ]
    """<p>The time when the operation ended.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeConnectorOperationResponse) -> dict:
    out: dict = {}
    if "connector_arn" in value:
        out["connectorArn"] = value["connector_arn"]
    if "connector_operation_arn" in value:
        out["connectorOperationArn"] = value["connector_operation_arn"]
    if "connector_operation_state" in value:
        out["connectorOperationState"] = value["connector_operation_state"]
    if "connector_operation_type" in value:
        out["connectorOperationType"] = value["connector_operation_type"]
    if "operation_steps" in value:
        import capo_kafkaconnect.types.__list_of_connector_operation_step

        out["operationSteps"] = (
            capo_kafkaconnect.types.__list_of_connector_operation_step.serialize_json(
                value["operation_steps"]
            )
        )
    if "origin_worker_setting" in value:
        import capo_kafkaconnect.types.worker_setting

        out["originWorkerSetting"] = (
            capo_kafkaconnect.types.worker_setting.serialize_json(
                value["origin_worker_setting"]
            )
        )
    if "origin_connector_configuration" in value:
        import capo_kafkaconnect.types.connector_configuration

        out["originConnectorConfiguration"] = (
            capo_kafkaconnect.types.connector_configuration.serialize_json(
                value["origin_connector_configuration"]
            )
        )
    if "target_worker_setting" in value:
        import capo_kafkaconnect.types.worker_setting

        out["targetWorkerSetting"] = (
            capo_kafkaconnect.types.worker_setting.serialize_json(
                value["target_worker_setting"]
            )
        )
    if "target_connector_configuration" in value:
        import capo_kafkaconnect.types.connector_configuration

        out["targetConnectorConfiguration"] = (
            capo_kafkaconnect.types.connector_configuration.serialize_json(
                value["target_connector_configuration"]
            )
        )
    if "error_info" in value:
        import capo_kafkaconnect.types.state_description

        out["errorInfo"] = capo_kafkaconnect.types.state_description.serialize_json(
            value["error_info"]
        )
    if "creation_time" in value:
        import capo_kafkaconnect.types.__timestamp_iso8601

        out["creationTime"] = (
            capo_kafkaconnect.types.__timestamp_iso8601.serialize_json(
                value["creation_time"]
            )
        )
    if "end_time" in value:
        import capo_kafkaconnect.types.__timestamp_iso8601

        out["endTime"] = capo_kafkaconnect.types.__timestamp_iso8601.serialize_json(
            value["end_time"]
        )
    return out


def deserialize_json(data: dict) -> DescribeConnectorOperationResponse:
    out: DescribeConnectorOperationResponse = {}  # type: ignore[typeddict-item]
    if data.get("connectorArn") is not None:
        out["connector_arn"] = data["connectorArn"]
    if data.get("connectorOperationArn") is not None:
        out["connector_operation_arn"] = data["connectorOperationArn"]
    if data.get("connectorOperationState") is not None:
        out["connector_operation_state"] = data["connectorOperationState"]
    if data.get("connectorOperationType") is not None:
        out["connector_operation_type"] = data["connectorOperationType"]
    if data.get("operationSteps") is not None:
        import capo_kafkaconnect.types.__list_of_connector_operation_step

        out["operation_steps"] = (
            capo_kafkaconnect.types.__list_of_connector_operation_step.deserialize_json(
                data["operationSteps"]
            )
        )
    if data.get("originWorkerSetting") is not None:
        import capo_kafkaconnect.types.worker_setting

        out["origin_worker_setting"] = (
            capo_kafkaconnect.types.worker_setting.deserialize_json(
                data["originWorkerSetting"]
            )
        )
    if data.get("originConnectorConfiguration") is not None:
        import capo_kafkaconnect.types.connector_configuration

        out["origin_connector_configuration"] = (
            capo_kafkaconnect.types.connector_configuration.deserialize_json(
                data["originConnectorConfiguration"]
            )
        )
    if data.get("targetWorkerSetting") is not None:
        import capo_kafkaconnect.types.worker_setting

        out["target_worker_setting"] = (
            capo_kafkaconnect.types.worker_setting.deserialize_json(
                data["targetWorkerSetting"]
            )
        )
    if data.get("targetConnectorConfiguration") is not None:
        import capo_kafkaconnect.types.connector_configuration

        out["target_connector_configuration"] = (
            capo_kafkaconnect.types.connector_configuration.deserialize_json(
                data["targetConnectorConfiguration"]
            )
        )
    if data.get("errorInfo") is not None:
        import capo_kafkaconnect.types.state_description

        out["error_info"] = capo_kafkaconnect.types.state_description.deserialize_json(
            data["errorInfo"]
        )
    if data.get("creationTime") is not None:
        import capo_kafkaconnect.types.__timestamp_iso8601

        out["creation_time"] = (
            capo_kafkaconnect.types.__timestamp_iso8601.deserialize_json(
                data["creationTime"]
            )
        )
    if data.get("endTime") is not None:
        import capo_kafkaconnect.types.__timestamp_iso8601

        out["end_time"] = capo_kafkaconnect.types.__timestamp_iso8601.deserialize_json(
            data["endTime"]
        )
    return out


def redact_sensitive(value: DescribeConnectorOperationResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "origin_connector_configuration" in value:
        out["origin_connector_configuration"] = "*** Sensitive Data Redacted ***"
    if "target_connector_configuration" in value:
        out["target_connector_configuration"] = "*** Sensitive Data Redacted ***"
    return out
