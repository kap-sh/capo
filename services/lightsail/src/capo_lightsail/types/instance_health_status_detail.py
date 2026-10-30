"""Generated from Smithy shape ``com.amazonaws.lightsail#InstanceHealthStatusDetail``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lightsail.types.instance_health_status_detail_name
    import capo_lightsail.types.instance_health_status_detail_value
    import capo_lightsail.types.iso_date


class InstanceHealthStatusDetail(TypedDict, closed=True):
    name: NotRequired[
        "capo_lightsail.types.instance_health_status_detail_name.InstanceHealthStatusDetailName"
    ]
    """<p>The type of instance status. The only possible value is <code>reachability</code>.</p>"""
    status: NotRequired[
        "capo_lightsail.types.instance_health_status_detail_value.InstanceHealthStatusDetailValue"
    ]
    """<p>The status.</p> <p>The following values are possible:</p> <ul> <li> <p> <code>passed</code> - The check passed.</p> </li> <li> <p> <code>failed</code> - The check failed.</p> </li> <li> <p> <code>initializing</code> - The check is in progress.</p> </li> <li> <p> <code>insufficient-data</code> - There isn't enough data yet to determine the result.</p> </li> </ul>"""
    impaired_since: NotRequired["capo_lightsail.types.iso_date.IsoDate"]
    """<p>The time when a status check failed. For an instance that was launched and impaired, this is the time when the instance was launched.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InstanceHealthStatusDetail) -> dict:
    out: dict = {}
    if "name" in value:
        import capo_lightsail.types.instance_health_status_detail_name

        out["name"] = (
            capo_lightsail.types.instance_health_status_detail_name.serialize_aws_json_1_1(
                value["name"]
            )
        )
    if "status" in value:
        import capo_lightsail.types.instance_health_status_detail_value

        out["status"] = (
            capo_lightsail.types.instance_health_status_detail_value.serialize_aws_json_1_1(
                value["status"]
            )
        )
    if "impaired_since" in value:
        import capo_lightsail.types.iso_date

        out["impairedSince"] = capo_lightsail.types.iso_date.serialize_aws_json_1_1(
            value["impaired_since"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> InstanceHealthStatusDetail:
    out: InstanceHealthStatusDetail = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        import capo_lightsail.types.instance_health_status_detail_name

        out["name"] = (
            capo_lightsail.types.instance_health_status_detail_name.deserialize_aws_json_1_1(
                data["name"]
            )
        )
    if data.get("status") is not None:
        import capo_lightsail.types.instance_health_status_detail_value

        out["status"] = (
            capo_lightsail.types.instance_health_status_detail_value.deserialize_aws_json_1_1(
                data["status"]
            )
        )
    if data.get("impairedSince") is not None:
        import capo_lightsail.types.iso_date

        out["impaired_since"] = capo_lightsail.types.iso_date.deserialize_aws_json_1_1(
            data["impairedSince"]
        )
    return out
