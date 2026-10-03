"""Generated from Smithy shape ``com.amazonaws.connect#UpdateMetricMetadataRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connect.types.instance_id
    import capo_connect.types.metric_description
    import capo_connect.types.metric_id
    import capo_connect.types.metric_name


class UpdateMetricMetadataRequest(TypedDict, closed=True):
    instance_id: "capo_connect.types.instance_id.InstanceId"
    """<p>The identifier of the Connect Customer instance. You can <a href="https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html">find the instance ID</a> in the Amazon Resource Name (ARN) of the instance.</p>"""
    metric_id: "capo_connect.types.metric_id.MetricId"
    """<p>The identifier of the metric to update. Adding the <code>$SAVED</code> qualifier will update the saved version of the metric. Adding <code>$LATEST</code> or omitting a qualifier will update the published version.</p>"""
    name: NotRequired["capo_connect.types.metric_name.MetricName"]
    """<p>The updated name of the metric.</p>"""
    description: NotRequired["capo_connect.types.metric_description.MetricDescription"]
    """<p>The updated description of the metric.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateMetricMetadataRequest) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "description" in value:
        out["Description"] = value["description"]
    return out


def deserialize_json(data: dict) -> UpdateMetricMetadataRequest:
    out: UpdateMetricMetadataRequest = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    return out
