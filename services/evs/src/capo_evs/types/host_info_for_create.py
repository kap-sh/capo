"""Generated from Smithy shape ``com.amazonaws.evs#HostInfoForCreate``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_evs.types.dedicated_host_id
    import capo_evs.types.host_name
    import capo_evs.types.instance_type
    import capo_evs.types.key_name
    import capo_evs.types.placement_group_id


class HostInfoForCreate(TypedDict, closed=True):
    host_name: "capo_evs.types.host_name.HostName"
    """<p>The DNS hostname of the host. DNS hostnames for hosts must be unique across Amazon EVS environments and within VCF.</p>"""
    key_name: "capo_evs.types.key_name.KeyName"
    """<p>The name of the SSH key that is used to access the host.</p>"""
    instance_type: "capo_evs.types.instance_type.InstanceType"
    """<p>The EC2 instance type that represents the host.</p>"""
    placement_group_id: NotRequired[
        "capo_evs.types.placement_group_id.PlacementGroupId"
    ]
    """<p>The unique ID of the placement group where the host is placed.</p>"""
    dedicated_host_id: NotRequired["capo_evs.types.dedicated_host_id.DedicatedHostId"]
    """<p>The unique ID of the Amazon EC2 Dedicated Host.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: HostInfoForCreate) -> dict:
    out: dict = {}
    out["hostName"] = value["host_name"]
    out["keyName"] = value["key_name"]
    import capo_evs.types.instance_type

    out["instanceType"] = capo_evs.types.instance_type.serialize_aws_json_1_0(
        value["instance_type"]
    )
    if "placement_group_id" in value:
        out["placementGroupId"] = value["placement_group_id"]
    if "dedicated_host_id" in value:
        out["dedicatedHostId"] = value["dedicated_host_id"]
    return out


def deserialize_aws_json_1_0(data: dict) -> HostInfoForCreate:
    out: HostInfoForCreate = {}  # type: ignore[typeddict-item]
    if data.get("hostName") is not None:
        out["host_name"] = data["hostName"]
    else:
        out["host_name"] = ""
    if data.get("keyName") is not None:
        out["key_name"] = data["keyName"]
    else:
        out["key_name"] = ""
    if data.get("instanceType") is not None:
        import capo_evs.types.instance_type

        out["instance_type"] = capo_evs.types.instance_type.deserialize_aws_json_1_0(
            data["instanceType"]
        )
    else:
        import typing

        out["instance_type"] = typing.cast(
            "capo_evs.types.instance_type.InstanceType", ""
        )
    if data.get("placementGroupId") is not None:
        out["placement_group_id"] = data["placementGroupId"]
    if data.get("dedicatedHostId") is not None:
        out["dedicated_host_id"] = data["dedicatedHostId"]
    return out
