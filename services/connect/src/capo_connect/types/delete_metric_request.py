"""Generated from Smithy shape ``com.amazonaws.connect#DeleteMetricRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_connect.types.instance_id
    import capo_connect.types.metric_id


class DeleteMetricRequest(TypedDict, closed=True):
    instance_id: "capo_connect.types.instance_id.InstanceId"
    """<p>The identifier of the Connect Customer instance. You can <a href="https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html">find the instance ID</a> in the Amazon Resource Name (ARN) of the instance.</p>"""
    metric_id: "capo_connect.types.metric_id.MetricId"
    """<p>The identifier of the metric to delete.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteMetricRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteMetricRequest:
    out: DeleteMetricRequest = {}  # type: ignore[typeddict-item]
    return out
