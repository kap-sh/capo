"""Generated from Smithy shape ``com.amazonaws.lightsail#SetIpAddressTypeRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lightsail.types.boolean
    import capo_lightsail.types.ip_address_type
    import capo_lightsail.types.resource_name
    import capo_lightsail.types.resource_type


class SetIpAddressTypeRequest(TypedDict, closed=True):
    resource_type: "capo_lightsail.types.resource_type.ResourceType"
    """<p>The resource type.</p> <p>The resource values are <code>Distribution</code>, <code>Instance</code>, and <code>LoadBalancer</code>.</p> <note> <p>Distribution-related APIs are available only in the N. Virginia (<code>us-east-1</code>) Amazon Web Services Region. Set your Amazon Web Services Region configuration to <code>us-east-1</code> to create, view, or edit distributions.</p> </note>"""
    resource_name: "capo_lightsail.types.resource_name.ResourceName"
    """<p>The name of the resource for which to set the IP address type.</p>"""
    ip_address_type: "capo_lightsail.types.ip_address_type.IpAddressType"
    """<p>The IP address type to set for the specified resource.</p> <p>The possible values are <code>ipv4</code> for IPv4 only, <code>ipv6</code> for IPv6 only, and <code>dualstack</code> for IPv4 and IPv6.</p>"""
    accept_bundle_update: NotRequired["capo_lightsail.types.boolean.boolean"]
    """<p>Required parameter to accept the instance bundle update when changing to, and from, IPv6-only.</p> <note> <p>An instance bundle will change when switching from <code>dual-stack</code> or <code>ipv4</code>, to <code>ipv6</code>. It also changes when switching from <code>ipv6</code>, to <code>dual-stack</code> or <code>ipv4</code>.</p> <p>You must include this parameter in the command to update the bundle. For example, if you switch from <code>dual-stack</code> to <code>ipv6</code>, the bundle will be updated, and billing for the IPv6-only instance bundle begins immediately.</p> </note>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SetIpAddressTypeRequest) -> dict:
    out: dict = {}
    import capo_lightsail.types.resource_type

    out["resourceType"] = capo_lightsail.types.resource_type.serialize_aws_json_1_1(
        value["resource_type"]
    )
    out["resourceName"] = value["resource_name"]
    import capo_lightsail.types.ip_address_type

    out["ipAddressType"] = capo_lightsail.types.ip_address_type.serialize_aws_json_1_1(
        value["ip_address_type"]
    )
    if "accept_bundle_update" in value:
        out["acceptBundleUpdate"] = value["accept_bundle_update"]
    return out


def deserialize_aws_json_1_1(data: dict) -> SetIpAddressTypeRequest:
    out: SetIpAddressTypeRequest = {}  # type: ignore[typeddict-item]
    if data.get("resourceType") is not None:
        import capo_lightsail.types.resource_type

        out["resource_type"] = (
            capo_lightsail.types.resource_type.deserialize_aws_json_1_1(
                data["resourceType"]
            )
        )
    else:
        import typing

        out["resource_type"] = typing.cast(
            "capo_lightsail.types.resource_type.ResourceType", ""
        )
    if data.get("resourceName") is not None:
        out["resource_name"] = data["resourceName"]
    else:
        out["resource_name"] = ""
    if data.get("ipAddressType") is not None:
        import capo_lightsail.types.ip_address_type

        out["ip_address_type"] = (
            capo_lightsail.types.ip_address_type.deserialize_aws_json_1_1(
                data["ipAddressType"]
            )
        )
    else:
        import typing

        out["ip_address_type"] = typing.cast(
            "capo_lightsail.types.ip_address_type.IpAddressType", ""
        )
    if data.get("acceptBundleUpdate") is not None:
        out["accept_bundle_update"] = data["acceptBundleUpdate"]
    return out
