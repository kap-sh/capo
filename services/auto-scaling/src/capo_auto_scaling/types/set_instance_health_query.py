"""Generated from Smithy shape ``com.amazonaws.autoscaling#SetInstanceHealthQuery``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_auto_scaling._protocol.xml import Element

if TYPE_CHECKING:
    import capo_auto_scaling.types.should_respect_grace_period
    import capo_auto_scaling.types.xml_string_max_len19
    import capo_auto_scaling.types.xml_string_max_len32


class SetInstanceHealthQuery(TypedDict, closed=True):
    instance_id: NotRequired[
        "capo_auto_scaling.types.xml_string_max_len19.XmlStringMaxLen19"
    ]
    """<p>The ID of the instance.</p>"""
    health_status: NotRequired[
        "capo_auto_scaling.types.xml_string_max_len32.XmlStringMaxLen32"
    ]
    """<p>The health status of the instance. Set to <code>Healthy</code> to have the instance remain in service. Set to <code>Unhealthy</code> to have the instance be out of service. Amazon EC2 Auto Scaling terminates and replaces the unhealthy instance.</p>"""
    should_respect_grace_period: NotRequired[
        "capo_auto_scaling.types.should_respect_grace_period.ShouldRespectGracePeriod"
    ]
    """<p>If the Auto Scaling group of the specified instance has a <code>HealthCheckGracePeriod</code> specified for the group, by default, this call respects the grace period. Set this to <code>False</code>, to have the call not respect the grace period associated with the group.</p> <p>For more information about the health check grace period, see <a href="https://docs.aws.amazon.com/autoscaling/ec2/userguide/health-check-grace-period.html">Set the health check grace period for an Auto Scaling group</a> in the <i>Amazon EC2 Auto Scaling User Guide</i>.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: SetInstanceHealthQuery, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "instance_id" in value:
        pairs.append((f"{key_prefix}InstanceId", str(value["instance_id"])))
    if "health_status" in value:
        pairs.append((f"{key_prefix}HealthStatus", str(value["health_status"])))
    if "should_respect_grace_period" in value:
        pairs.append(
            (
                f"{key_prefix}ShouldRespectGracePeriod",
                "true" if value["should_respect_grace_period"] else "false",
            )
        )


def deserialize_query(el: Element) -> SetInstanceHealthQuery:
    out: SetInstanceHealthQuery = {}  # type: ignore[typeddict-item]
    child_instance_id = el.find("InstanceId")
    if child_instance_id is not None:
        out["instance_id"] = str(child_instance_id.text or "")
    child_health_status = el.find("HealthStatus")
    if child_health_status is not None:
        out["health_status"] = str(child_health_status.text or "")
    child_should_respect_grace_period = el.find("ShouldRespectGracePeriod")
    if child_should_respect_grace_period is not None:
        out["should_respect_grace_period"] = (
            child_should_respect_grace_period.text or ""
        ).lower() == "true"
    return out
