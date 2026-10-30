"""Generated from Smithy shape ``com.amazonaws.lightsail#InstanceHealthStatus``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lightsail.types.instance_health_status_detail_list
    import capo_lightsail.types.instance_health_status_value


class InstanceHealthStatus(TypedDict, closed=True):
    status: NotRequired[
        "capo_lightsail.types.instance_health_status_value.InstanceHealthStatusValue"
    ]
    """<p>The status.</p> <p>The following values are possible:</p> <ul> <li> <p> <code>ok</code> - All checks are passing. The instance is reachable.</p> </li> <li> <p> <code>impaired</code> - One or more checks have failed.</p> </li> <li> <p> <code>initializing</code> - The instance was recently started, and the checks are in progress.</p> </li> <li> <p> <code>insufficient-data</code> - There isn't enough data yet to determine the result.</p> </li> <li> <p> <code>not-applicable</code> - The check doesn't apply because the instance isn't running.</p> </li> </ul>"""
    details: NotRequired[
        "capo_lightsail.types.instance_health_status_detail_list.InstanceHealthStatusDetailList"
    ]
    """<p>The system instance health or instance health.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InstanceHealthStatus) -> dict:
    out: dict = {}
    if "status" in value:
        import capo_lightsail.types.instance_health_status_value

        out["status"] = (
            capo_lightsail.types.instance_health_status_value.serialize_aws_json_1_1(
                value["status"]
            )
        )
    if "details" in value:
        import capo_lightsail.types.instance_health_status_detail_list

        out["details"] = (
            capo_lightsail.types.instance_health_status_detail_list.serialize_aws_json_1_1(
                value["details"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> InstanceHealthStatus:
    out: InstanceHealthStatus = {}  # type: ignore[typeddict-item]
    if data.get("status") is not None:
        import capo_lightsail.types.instance_health_status_value

        out["status"] = (
            capo_lightsail.types.instance_health_status_value.deserialize_aws_json_1_1(
                data["status"]
            )
        )
    if data.get("details") is not None:
        import capo_lightsail.types.instance_health_status_detail_list

        out["details"] = (
            capo_lightsail.types.instance_health_status_detail_list.deserialize_aws_json_1_1(
                data["details"]
            )
        )
    return out
