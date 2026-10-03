"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsEc2LaunchTemplateDataMonitoringDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.boolean


class AwsEc2LaunchTemplateDataMonitoringDetails(TypedDict, closed=True):
    enabled: NotRequired["capo_securityhub.types.boolean.Boolean"]
    """<p> Enables detailed monitoring when <code>true</code> is specified. Otherwise, basic monitoring is enabled. For more information about detailed monitoring, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-cloudwatch-new.html">Enable or turn off detailed monitoring for your instances</a> in the <i>Amazon EC2 User Guide</i>. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsEc2LaunchTemplateDataMonitoringDetails) -> dict:
    out: dict = {}
    if "enabled" in value:
        out["Enabled"] = value["enabled"]
    return out


def deserialize_json(data: dict) -> AwsEc2LaunchTemplateDataMonitoringDetails:
    out: AwsEc2LaunchTemplateDataMonitoringDetails = {}  # type: ignore[typeddict-item]
    if data.get("Enabled") is not None:
        out["enabled"] = data["Enabled"]
    return out
