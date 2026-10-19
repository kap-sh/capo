"""Generated from Smithy shape ``com.amazonaws.mediaconnect#VpcRouterNetworkInterfaceConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_mediaconnect.types.security_group_id_list


class VpcRouterNetworkInterfaceConfiguration(TypedDict, closed=True):
    security_group_ids: (
        "capo_mediaconnect.types.security_group_id_list.SecurityGroupIdList"
    )
    """<p>The IDs of the security groups to associate with the router network interface within the VPC.</p>"""
    subnet_id: "str"
    """<p>The ID of the subnet within the VPC to associate the router network interface with.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: VpcRouterNetworkInterfaceConfiguration) -> dict:
    out: dict = {}
    import capo_mediaconnect.types.security_group_id_list

    out["securityGroupIds"] = (
        capo_mediaconnect.types.security_group_id_list.serialize_json(
            value["security_group_ids"]
        )
    )
    out["subnetId"] = value["subnet_id"]
    return out


def deserialize_json(data: dict) -> VpcRouterNetworkInterfaceConfiguration:
    out: VpcRouterNetworkInterfaceConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("securityGroupIds") is not None:
        import capo_mediaconnect.types.security_group_id_list

        out["security_group_ids"] = (
            capo_mediaconnect.types.security_group_id_list.deserialize_json(
                data["securityGroupIds"]
            )
        )
    else:
        out["security_group_ids"] = []
    if data.get("subnetId") is not None:
        out["subnet_id"] = data["subnetId"]
    else:
        out["subnet_id"] = ""
    return out
