"""Generated from Smithy shape ``com.amazonaws.rum#PutRumMetricsDestinationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_rum.errors import DeserializationError

if TYPE_CHECKING:
    import capo_rum.types.app_monitor_name
    import capo_rum.types.destination_arn
    import capo_rum.types.iam_role_arn
    import capo_rum.types.metric_destination


class PutRumMetricsDestinationRequest(TypedDict, closed=True):
    app_monitor_name: "capo_rum.types.app_monitor_name.AppMonitorName"
    """<p>The name of the CloudWatch RUM app monitor that will send the metrics.</p>"""
    destination: "capo_rum.types.metric_destination.MetricDestination"
    """<p>Defines the destination to send the metrics to. Valid values are <code>CloudWatch</code> and <code>Evidently</code>. If you specify <code>Evidently</code>, you must also specify the ARN of the CloudWatchEvidently experiment that is to be the destination and an IAM role that has permission to write to the experiment.</p>"""
    destination_arn: NotRequired["capo_rum.types.destination_arn.DestinationArn"]
    """<p>Use this parameter only if <code>Destination</code> is <code>Evidently</code>. This parameter specifies the ARN of the Evidently experiment that will receive the extended metrics.</p>"""
    iam_role_arn: NotRequired["capo_rum.types.iam_role_arn.IamRoleArn"]
    """<p>This parameter is required if <code>Destination</code> is <code>Evidently</code>. If <code>Destination</code> is <code>CloudWatch</code>, don't use this parameter.</p> <p>This parameter specifies the ARN of an IAM role that RUM will assume to write to the Evidently experiment that you are sending metrics to. This role must have permission to write to that experiment.</p> <p>If you specify this parameter, you must be signed on to a role that has <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html">PassRole</a> permissions attached to it, to allow the role to be passed. The <a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/auth-and-access-control-cw.html#managed-policies-cloudwatch-RUM"> CloudWatchAmazonCloudWatchRUMFullAccess</a> policy doesn't include <code>PassRole</code> permissions.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PutRumMetricsDestinationRequest) -> dict:
    out: dict = {}
    out["Destination"] = value["destination"]
    if "destination_arn" in value:
        out["DestinationArn"] = value["destination_arn"]
    if "iam_role_arn" in value:
        out["IamRoleArn"] = value["iam_role_arn"]
    return out


def deserialize_json(data: dict) -> PutRumMetricsDestinationRequest:
    out: PutRumMetricsDestinationRequest = {}  # type: ignore[typeddict-item]
    if data.get("Destination") is not None:
        out["destination"] = data["Destination"]
    else:
        raise DeserializationError(
            "PutRumMetricsDestinationRequest.destination required"
        )
    if data.get("DestinationArn") is not None:
        out["destination_arn"] = data["DestinationArn"]
    if data.get("IamRoleArn") is not None:
        out["iam_role_arn"] = data["IamRoleArn"]
    return out
