"""Generated from Smithy shape ``com.amazonaws.networkflowmonitor#MonitorLocalResource``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_networkflowmonitor.types.monitor_local_resource_type


class MonitorLocalResource(TypedDict, closed=True):
    type: "capo_networkflowmonitor.types.monitor_local_resource_type.MonitorLocalResourceType"
    """<p>The type of the local resource. Valid values are <code>AWS::EC2::VPC</code> <code>AWS::AvailabilityZone</code>, <code>AWS::EC2::Subnet</code>, <code>AWS::EKS::Cluster</code>, or <code>AWS::Region</code>.</p>"""
    identifier: "str"
    """<p>The identifier of the local resource. The values you can specify are the following:</p> <ul> <li> <p>For a VPC, subnet or EKS cluster, this identifier is the VPC Amazon Resource Name (ARN), subnet ARN or cluster ARN.</p> </li> <li> <p>For an Availability Zone, this identifier is the AZ name, for example, us-west-2b.</p> </li> <li> <p>For a Region, this identifier is the Region name, for example, us-west-2.</p> </li> </ul>"""


# --- restJson1 ser/de ---
def serialize_json(value: MonitorLocalResource) -> dict:
    out: dict = {}
    import capo_networkflowmonitor.types.monitor_local_resource_type

    out["type"] = (
        capo_networkflowmonitor.types.monitor_local_resource_type.serialize_json(
            value["type"]
        )
    )
    out["identifier"] = value["identifier"]
    return out


def deserialize_json(data: dict) -> MonitorLocalResource:
    out: MonitorLocalResource = {}  # type: ignore[typeddict-item]
    if data.get("type") is not None:
        import capo_networkflowmonitor.types.monitor_local_resource_type

        out["type"] = (
            capo_networkflowmonitor.types.monitor_local_resource_type.deserialize_json(
                data["type"]
            )
        )
    else:
        import typing

        out["type"] = typing.cast(
            "capo_networkflowmonitor.types.monitor_local_resource_type.MonitorLocalResourceType",
            "",
        )
    if data.get("identifier") is not None:
        out["identifier"] = data["identifier"]
    else:
        out["identifier"] = ""
    return out
