"""Generated from Smithy shape ``com.amazonaws.finspace#CreateKxScalingGroupRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_finspace.types.availability_zone_id
    import capo_finspace.types.client_token
    import capo_finspace.types.kx_environment_id
    import capo_finspace.types.kx_host_type
    import capo_finspace.types.kx_scaling_group_name
    import capo_finspace.types.tag_map


class CreateKxScalingGroupRequest(TypedDict, closed=True):
    client_token: "capo_finspace.types.client_token.ClientToken"
    """<p>A token that ensures idempotency. This token expires in 10 minutes.</p>"""
    environment_id: "capo_finspace.types.kx_environment_id.KxEnvironmentId"
    """<p>A unique identifier for the kdb environment, where you want to create the scaling group. </p>"""
    scaling_group_name: "capo_finspace.types.kx_scaling_group_name.KxScalingGroupName"
    """<p>A unique identifier for the kdb scaling group. </p>"""
    host_type: "capo_finspace.types.kx_host_type.KxHostType"
    """<p> The memory and CPU capabilities of the scaling group host on which FinSpace Managed kdb clusters will be placed.</p> <p>You can add one of the following values:</p> <ul> <li> <p> <code>kx.sg.large</code> – The host type with a configuration of 16 GiB memory and 2 vCPUs.</p> </li> <li> <p> <code>kx.sg.xlarge</code> – The host type with a configuration of 32 GiB memory and 4 vCPUs.</p> </li> <li> <p> <code>kx.sg.2xlarge</code> – The host type with a configuration of 64 GiB memory and 8 vCPUs.</p> </li> <li> <p> <code>kx.sg.4xlarge</code> – The host type with a configuration of 108 GiB memory and 16 vCPUs.</p> </li> <li> <p> <code>kx.sg.8xlarge</code> – The host type with a configuration of 216 GiB memory and 32 vCPUs.</p> </li> <li> <p> <code>kx.sg.16xlarge</code> – The host type with a configuration of 432 GiB memory and 64 vCPUs.</p> </li> <li> <p> <code>kx.sg.32xlarge</code> – The host type with a configuration of 864 GiB memory and 128 vCPUs.</p> </li> <li> <p> <code>kx.sg1.16xlarge</code> – The host type with a configuration of 1949 GiB memory and 64 vCPUs.</p> </li> <li> <p> <code>kx.sg1.24xlarge</code> – The host type with a configuration of 2948 GiB memory and 96 vCPUs.</p> </li> </ul>"""
    availability_zone_id: "capo_finspace.types.availability_zone_id.AvailabilityZoneId"
    """<p>The identifier of the availability zones.</p>"""
    tags: NotRequired["capo_finspace.types.tag_map.TagMap"]
    """<p> A list of key-value pairs to label the scaling group. You can add up to 50 tags to a scaling group. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateKxScalingGroupRequest) -> dict:
    out: dict = {}
    out["clientToken"] = value["client_token"]
    out["scalingGroupName"] = value["scaling_group_name"]
    out["hostType"] = value["host_type"]
    out["availabilityZoneId"] = value["availability_zone_id"]
    if "tags" in value:
        import capo_finspace.types.tag_map

        out["tags"] = capo_finspace.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> CreateKxScalingGroupRequest:
    out: CreateKxScalingGroupRequest = {}  # type: ignore[typeddict-item]
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    else:
        out["client_token"] = ""
    if data.get("scalingGroupName") is not None:
        out["scaling_group_name"] = data["scalingGroupName"]
    else:
        out["scaling_group_name"] = ""
    if data.get("hostType") is not None:
        out["host_type"] = data["hostType"]
    else:
        out["host_type"] = ""
    if data.get("availabilityZoneId") is not None:
        out["availability_zone_id"] = data["availabilityZoneId"]
    else:
        out["availability_zone_id"] = ""
    if data.get("tags") is not None:
        import capo_finspace.types.tag_map

        out["tags"] = capo_finspace.types.tag_map.deserialize_json(data["tags"])
    return out
