"""Generated from Smithy shape ``com.amazonaws.connect#GetContactMetricsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_connect.errors import DeserializationError

if TYPE_CHECKING:
    import capo_connect.types.contact_metrics
    import capo_connect.types.instance_id_or_arn


class GetContactMetricsRequest(TypedDict, closed=True):
    instance_id: "capo_connect.types.instance_id_or_arn.InstanceIdOrArn"
    """<p>The identifier of the Connect Customer instance. You can <a href="https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html">find the instance ID</a> in the Amazon Resource Name (ARN) of the instance.</p>"""
    contact_id: "capo_connect.types.instance_id_or_arn.InstanceIdOrArn"
    """<p>The identifier of the contact in this instance of Connect Customer. </p>"""
    metrics: "capo_connect.types.contact_metrics.ContactMetrics"
    """<p>A list of contact level metrics to retrieve.Supported metrics include POSITION_IN_QUEUE (the contact's current position in the queue) and ESTIMATED_WAIT_TIME (the predicted time in seconds until the contact is connected to an agent)</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetContactMetricsRequest) -> dict:
    out: dict = {}
    out["InstanceId"] = value["instance_id"]
    out["ContactId"] = value["contact_id"]
    import capo_connect.types.contact_metrics

    out["Metrics"] = capo_connect.types.contact_metrics.serialize_json(value["metrics"])
    return out


def deserialize_json(data: dict) -> GetContactMetricsRequest:
    out: GetContactMetricsRequest = {}  # type: ignore[typeddict-item]
    if data.get("InstanceId") is not None:
        out["instance_id"] = data["InstanceId"]
    else:
        raise DeserializationError("GetContactMetricsRequest.instance_id required")
    if data.get("ContactId") is not None:
        out["contact_id"] = data["ContactId"]
    else:
        raise DeserializationError("GetContactMetricsRequest.contact_id required")
    if data.get("Metrics") is not None:
        import capo_connect.types.contact_metrics

        out["metrics"] = capo_connect.types.contact_metrics.deserialize_json(
            data["Metrics"]
        )
    else:
        raise DeserializationError("GetContactMetricsRequest.metrics required")
    return out
