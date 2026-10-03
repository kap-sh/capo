"""Generated from Smithy shape ``com.amazonaws.codedeploy#ZonalConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codedeploy.types.minimum_healthy_hosts_per_zone
    import capo_codedeploy.types.wait_time_in_seconds


class ZonalConfig(TypedDict, closed=True):
    first_zone_monitor_duration_in_seconds: NotRequired[
        "capo_codedeploy.types.wait_time_in_seconds.WaitTimeInSeconds"
    ]
    """<p>The period of time, in seconds, that CodeDeploy must wait after completing a deployment to the <i>first</i> Availability Zone. CodeDeploy will wait this amount of time before starting a deployment to the second Availability Zone. You might set this option if you want to allow extra bake time for the first Availability Zone. If you don't specify a value for <code>firstZoneMonitorDurationInSeconds</code>, then CodeDeploy uses the <code>monitorDurationInSeconds</code> value for the first Availability Zone.</p> <p>For more information about the zonal configuration feature, see <a href="https://docs.aws.amazon.com/codedeploy/latest/userguide/deployment-configurations-create.html#zonal-config">zonal configuration</a> in the <i>CodeDeploy User Guide</i>.</p>"""
    monitor_duration_in_seconds: NotRequired[
        "capo_codedeploy.types.wait_time_in_seconds.WaitTimeInSeconds"
    ]
    """<p>The period of time, in seconds, that CodeDeploy must wait after completing a deployment to an Availability Zone. CodeDeploy will wait this amount of time before starting a deployment to the next Availability Zone. Consider adding a monitor duration to give the deployment some time to prove itself (or 'bake') in one Availability Zone before it is released in the next zone. If you don't specify a <code>monitorDurationInSeconds</code>, CodeDeploy starts deploying to the next Availability Zone immediately.</p> <p>For more information about the zonal configuration feature, see <a href="https://docs.aws.amazon.com/codedeploy/latest/userguide/deployment-configurations-create.html#zonal-config">zonal configuration</a> in the <i>CodeDeploy User Guide</i>.</p>"""
    minimum_healthy_hosts_per_zone: NotRequired[
        "capo_codedeploy.types.minimum_healthy_hosts_per_zone.MinimumHealthyHostsPerZone"
    ]
    """<p>The number or percentage of instances that must remain available per Availability Zone during a deployment. This option works in conjunction with the <code>MinimumHealthyHosts</code> option. For more information, see <a href="https://docs.aws.amazon.com/codedeploy/latest/userguide/instances-health.html#minimum-healthy-hosts-az">About the minimum number of healthy hosts per Availability Zone</a> in the <i>CodeDeploy User Guide</i>.</p> <p>If you don't specify the <code>minimumHealthyHostsPerZone</code> option, then CodeDeploy uses a default value of <code>0</code> percent.</p> <p>For more information about the zonal configuration feature, see <a href="https://docs.aws.amazon.com/codedeploy/latest/userguide/deployment-configurations-create.html#zonal-config">zonal configuration</a> in the <i>CodeDeploy User Guide</i>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ZonalConfig) -> dict:
    out: dict = {}
    if "first_zone_monitor_duration_in_seconds" in value:
        out["firstZoneMonitorDurationInSeconds"] = value[
            "first_zone_monitor_duration_in_seconds"
        ]
    if "monitor_duration_in_seconds" in value:
        out["monitorDurationInSeconds"] = value["monitor_duration_in_seconds"]
    if "minimum_healthy_hosts_per_zone" in value:
        import capo_codedeploy.types.minimum_healthy_hosts_per_zone

        out["minimumHealthyHostsPerZone"] = (
            capo_codedeploy.types.minimum_healthy_hosts_per_zone.serialize_aws_json_1_1(
                value["minimum_healthy_hosts_per_zone"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ZonalConfig:
    out: ZonalConfig = {}  # type: ignore[typeddict-item]
    if data.get("firstZoneMonitorDurationInSeconds") is not None:
        out["first_zone_monitor_duration_in_seconds"] = data[
            "firstZoneMonitorDurationInSeconds"
        ]
    if data.get("monitorDurationInSeconds") is not None:
        out["monitor_duration_in_seconds"] = data["monitorDurationInSeconds"]
    if data.get("minimumHealthyHostsPerZone") is not None:
        import capo_codedeploy.types.minimum_healthy_hosts_per_zone

        out["minimum_healthy_hosts_per_zone"] = (
            capo_codedeploy.types.minimum_healthy_hosts_per_zone.deserialize_aws_json_1_1(
                data["minimumHealthyHostsPerZone"]
            )
        )
    return out
