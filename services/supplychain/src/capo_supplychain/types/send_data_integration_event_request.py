"""Generated from Smithy shape ``com.amazonaws.supplychain#SendDataIntegrationEventRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_supplychain.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import capo_supplychain.types.client_token
    import capo_supplychain.types.data_integration_event_data
    import capo_supplychain.types.data_integration_event_dataset_target_configuration
    import capo_supplychain.types.data_integration_event_group_id
    import capo_supplychain.types.data_integration_event_type
    import capo_supplychain.types.uuid


class SendDataIntegrationEventRequest(TypedDict, closed=True):
    instance_id: "capo_supplychain.types.uuid.UUID"
    """<p>The AWS Supply Chain instance identifier.</p>"""
    event_type: (
        "capo_supplychain.types.data_integration_event_type.DataIntegrationEventType"
    )
    """<p>The data event type.</p> <ul> <li> <p> <b>scn.data.dataset</b> - Send data directly to any specified dataset.</p> </li> <li> <p> <b>scn.data.supplyplan</b> - Send data to <a href="https://docs.aws.amazon.com/aws-supply-chain/latest/userguide/supply-plan-entity.html">supply_plan</a> dataset.</p> </li> <li> <p> <b>scn.data.shipmentstoporder</b> - Send data to <a href="https://docs.aws.amazon.com/aws-supply-chain/latest/userguide/replenishment-shipment-stop-order-entity.html">shipment_stop_order</a> dataset.</p> </li> <li> <p> <b>scn.data.shipmentstop</b> - Send data to <a href="https://docs.aws.amazon.com/aws-supply-chain/latest/userguide/replenishment-shipment-stop-entity.html">shipment_stop</a> dataset.</p> </li> <li> <p> <b>scn.data.shipment</b> - Send data to <a href="https://docs.aws.amazon.com/aws-supply-chain/latest/userguide/replenishment-shipment-entity.html">shipment</a> dataset.</p> </li> <li> <p> <b>scn.data.reservation</b> - Send data to <a href="https://docs.aws.amazon.com/aws-supply-chain/latest/userguide/planning-reservation-entity.html">reservation</a> dataset.</p> </li> <li> <p> <b>scn.data.processproduct</b> - Send data to <a href="https://docs.aws.amazon.com/aws-supply-chain/latest/userguide/operation-process-product-entity.html">process_product</a> dataset.</p> </li> <li> <p> <b>scn.data.processoperation</b> - Send data to <a href="https://docs.aws.amazon.com/aws-supply-chain/latest/userguide/operation-process-operation-entity.html">process_operation</a> dataset.</p> </li> <li> <p> <b>scn.data.processheader</b> - Send data to <a href="https://docs.aws.amazon.com/aws-supply-chain/latest/userguide/operation-process-header-entity.html">process_header</a> dataset.</p> </li> <li> <p> <b>scn.data.forecast</b> - Send data to <a href="https://docs.aws.amazon.com/aws-supply-chain/latest/userguide/forecast-forecast-entity.html">forecast</a> dataset.</p> </li> <li> <p> <b>scn.data.inventorylevel</b> - Send data to <a href="https://docs.aws.amazon.com/aws-supply-chain/latest/userguide/inventory_mgmnt-inv-level-entity.html">inv_level</a> dataset.</p> </li> <li> <p> <b>scn.data.inboundorder</b> - Send data to <a href="https://docs.aws.amazon.com/aws-supply-chain/latest/userguide/replenishment-inbound-order-entity.html">inbound_order</a> dataset.</p> </li> <li> <p> <b>scn.data.inboundorderline</b> - Send data to <a href="https://docs.aws.amazon.com/aws-supply-chain/latest/userguide/replenishment-inbound-order-line-entity.html">inbound_order_line</a> dataset.</p> </li> <li> <p> <b>scn.data.inboundorderlineschedule</b> - Send data to <a href="https://docs.aws.amazon.com/aws-supply-chain/latest/userguide/replenishment-inbound-order-line-schedule-entity.html">inbound_order_line_schedule</a> dataset.</p> </li> <li> <p> <b>scn.data.outboundorderline</b> - Send data to <a href="https://docs.aws.amazon.com/aws-supply-chain/latest/userguide/outbound-fulfillment-order-line-entity.html">outbound_order_line</a> dataset.</p> </li> <li> <p> <b>scn.data.outboundshipment</b> - Send data to <a href="https://docs.aws.amazon.com/aws-supply-chain/latest/userguide/outbound-fulfillment-shipment-entity.html">outbound_shipment</a> dataset.</p> </li> </ul>"""
    data: "capo_supplychain.types.data_integration_event_data.DataIntegrationEventData"
    """<p>The data payload of the event, should follow the data schema of the target dataset, or see <a href="https://docs.aws.amazon.com/aws-supply-chain/latest/userguide/data-model-asc.html">Data entities supported in AWS Supply Chain</a>. To send single data record, use JsonObject format; to send multiple data records, use JsonArray format.</p> <p>Note that for AWS Supply Chain dataset under <b>asc</b> namespace, it has a connection_id internal field that is not allowed to be provided by client directly, they will be auto populated.</p>"""
    event_group_id: "capo_supplychain.types.data_integration_event_group_id.DataIntegrationEventGroupId"
    """<p>Event identifier (for example, orderId for InboundOrder) used for data sharding or partitioning. Noted under one eventGroupId of same eventType and instanceId, events are processed sequentially in the order they are received by the server.</p>"""
    event_timestamp: NotRequired["datetime.datetime"]
    """<p>The timestamp (in epoch seconds) associated with the event. If not provided, it will be assigned with current timestamp.</p>"""
    client_token: NotRequired["capo_supplychain.types.client_token.ClientToken"]
    """<p>The idempotent client token. The token is active for 8 hours, and within its lifetime, it ensures the request completes only once upon retry with same client token. If omitted, the AWS SDK generates a unique value so that AWS SDK can safely retry the request upon network errors.</p>"""
    dataset_target: NotRequired[
        "capo_supplychain.types.data_integration_event_dataset_target_configuration.DataIntegrationEventDatasetTargetConfiguration"
    ]
    """<p>The target dataset configuration for <b>scn.data.dataset</b> event type.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SendDataIntegrationEventRequest) -> dict:
    out: dict = {}
    import capo_supplychain.types.data_integration_event_type

    out["eventType"] = (
        capo_supplychain.types.data_integration_event_type.serialize_json(
            value["event_type"]
        )
    )
    out["data"] = value["data"]
    out["eventGroupId"] = value["event_group_id"]
    if "event_timestamp" in value:
        out["eventTimestamp"] = value["event_timestamp"].timestamp()
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    if "dataset_target" in value:
        import capo_supplychain.types.data_integration_event_dataset_target_configuration

        out["datasetTarget"] = (
            capo_supplychain.types.data_integration_event_dataset_target_configuration.serialize_json(
                value["dataset_target"]
            )
        )
    return out


def deserialize_json(data: dict) -> SendDataIntegrationEventRequest:
    out: SendDataIntegrationEventRequest = {}  # type: ignore[typeddict-item]
    if data.get("eventType") is not None:
        import capo_supplychain.types.data_integration_event_type

        out["event_type"] = (
            capo_supplychain.types.data_integration_event_type.deserialize_json(
                data["eventType"]
            )
        )
    else:
        raise DeserializationError(
            "SendDataIntegrationEventRequest.event_type required"
        )
    if data.get("data") is not None:
        out["data"] = data["data"]
    else:
        raise DeserializationError("SendDataIntegrationEventRequest.data required")
    if data.get("eventGroupId") is not None:
        out["event_group_id"] = data["eventGroupId"]
    else:
        raise DeserializationError(
            "SendDataIntegrationEventRequest.event_group_id required"
        )
    if data.get("eventTimestamp") is not None:
        import datetime

        out["event_timestamp"] = datetime.datetime.fromtimestamp(
            float(data["eventTimestamp"]), tz=datetime.timezone.utc
        )
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    if data.get("datasetTarget") is not None:
        import capo_supplychain.types.data_integration_event_dataset_target_configuration

        out["dataset_target"] = (
            capo_supplychain.types.data_integration_event_dataset_target_configuration.deserialize_json(
                data["datasetTarget"]
            )
        )
    return out
