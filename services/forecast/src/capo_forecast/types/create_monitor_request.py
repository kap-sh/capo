"""Generated from Smithy shape ``com.amazonaws.forecast#CreateMonitorRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_forecast.errors import DeserializationError

if TYPE_CHECKING:
    import capo_forecast.types.arn
    import capo_forecast.types.name
    import capo_forecast.types.tags


class CreateMonitorRequest(TypedDict, closed=True):
    monitor_name: "capo_forecast.types.name.Name"
    """<p>The name of the monitor resource.</p>"""
    resource_arn: "capo_forecast.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) of the predictor to monitor.</p>"""
    tags: NotRequired["capo_forecast.types.tags.Tags"]
    """<p>A list of <a href="https://docs.aws.amazon.com/forecast/latest/dg/tagging-forecast-resources.html">tags</a> to apply to the monitor resource.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateMonitorRequest) -> dict:
    out: dict = {}
    out["MonitorName"] = value["monitor_name"]
    out["ResourceArn"] = value["resource_arn"]
    if "tags" in value:
        import capo_forecast.types.tags

        out["Tags"] = capo_forecast.types.tags.serialize_aws_json_1_1(value["tags"])
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateMonitorRequest:
    out: CreateMonitorRequest = {}  # type: ignore[typeddict-item]
    if data.get("MonitorName") is not None:
        out["monitor_name"] = data["MonitorName"]
    else:
        raise DeserializationError("CreateMonitorRequest.monitor_name required")
    if data.get("ResourceArn") is not None:
        out["resource_arn"] = data["ResourceArn"]
    else:
        raise DeserializationError("CreateMonitorRequest.resource_arn required")
    if data.get("Tags") is not None:
        import capo_forecast.types.tags

        out["tags"] = capo_forecast.types.tags.deserialize_aws_json_1_1(data["Tags"])
    return out
