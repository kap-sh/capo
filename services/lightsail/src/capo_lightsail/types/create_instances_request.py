"""Generated from Smithy shape ``com.amazonaws.lightsail#CreateInstancesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_lightsail.errors import DeserializationError

if TYPE_CHECKING:
    import capo_lightsail.types.add_on_request_list
    import capo_lightsail.types.ip_address_type
    import capo_lightsail.types.non_empty_string
    import capo_lightsail.types.resource_name
    import capo_lightsail.types.string
    import capo_lightsail.types.string_list
    import capo_lightsail.types.tag_list


class CreateInstancesRequest(TypedDict, closed=True):
    instance_names: "capo_lightsail.types.string_list.StringList"
    """<p>The names to use for your new Lightsail instances. Separate multiple values using quotation marks and commas, for example: <code>["MyFirstInstance","MySecondInstance"]</code> </p>"""
    availability_zone: "capo_lightsail.types.string.string"
    """<p>The Availability Zone in which to create your instance. Use the following format: <code>us-east-2a</code> (case sensitive). You can get a list of Availability Zones by using the <a href="http://docs.aws.amazon.com/lightsail/2016-11-28/api-reference/API_GetRegions.html">get regions</a> operation. Be sure to add the <code>include Availability Zones</code> parameter to your request.</p>"""
    custom_image_name: NotRequired["capo_lightsail.types.resource_name.ResourceName"]
    """<p>(Discontinued) The name for your custom image.</p> <note> <p>In releases prior to June 12, 2017, this parameter was ignored by the API. It is now discontinued.</p> </note>"""
    blueprint_id: "capo_lightsail.types.non_empty_string.NonEmptyString"
    """<p>The ID for a virtual private server image (<code>app_wordpress_x_x</code> or <code>app_lamp_x_x</code>). Use the <code>get blueprints</code> operation to return a list of available images (or <i>blueprints</i>).</p> <note> <p>Use active blueprints when creating new instances. Inactive blueprints are listed to support customers with existing instances and are not necessarily available to create new instances. Blueprints are marked inactive when they become outdated due to operating system updates or new application releases.</p> </note>"""
    bundle_id: "capo_lightsail.types.non_empty_string.NonEmptyString"
    """<p>The bundle of specification information for your virtual private server (or <i>instance</i>), including the pricing plan (<code>medium_x_x</code>).</p>"""
    user_data: NotRequired["capo_lightsail.types.string.string"]
    """<p>A launch script you can create that configures a server with additional user data. For example, you might want to run <code>apt-get -y update</code>.</p> <note> <p>Depending on the machine image you choose, the command to get software on your instance varies. Amazon Linux and CentOS use <code>yum</code>, Debian and Ubuntu use <code>apt-get</code>, and FreeBSD uses <code>pkg</code>. For a complete list, see the <a href="https://docs.aws.amazon.com/lightsail/latest/userguide/compare-options-choose-lightsail-instance-image">Amazon Lightsail Developer Guide</a>.</p> </note>"""
    key_pair_name: NotRequired["capo_lightsail.types.resource_name.ResourceName"]
    """<p>The name of your key pair.</p>"""
    tags: NotRequired["capo_lightsail.types.tag_list.TagList"]
    """<p>The tag keys and optional values to add to the resource during create.</p> <p>Use the <code>TagResource</code> action to tag a resource after it's created.</p>"""
    add_ons: NotRequired["capo_lightsail.types.add_on_request_list.AddOnRequestList"]
    """<p>An array of objects representing the add-ons to enable for the new instance.</p>"""
    ip_address_type: NotRequired["capo_lightsail.types.ip_address_type.IpAddressType"]
    """<p>The IP address type for the instance.</p> <p>The possible values are <code>ipv4</code> for IPv4 only, <code>ipv6</code> for IPv6 only, and <code>dualstack</code> for IPv4 and IPv6.</p> <p>The default value is <code>dualstack</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateInstancesRequest) -> dict:
    out: dict = {}
    import capo_lightsail.types.string_list

    out["instanceNames"] = capo_lightsail.types.string_list.serialize_aws_json_1_1(
        value["instance_names"]
    )
    out["availabilityZone"] = value["availability_zone"]
    if "custom_image_name" in value:
        out["customImageName"] = value["custom_image_name"]
    out["blueprintId"] = value["blueprint_id"]
    out["bundleId"] = value["bundle_id"]
    if "user_data" in value:
        out["userData"] = value["user_data"]
    if "key_pair_name" in value:
        out["keyPairName"] = value["key_pair_name"]
    if "tags" in value:
        import capo_lightsail.types.tag_list

        out["tags"] = capo_lightsail.types.tag_list.serialize_aws_json_1_1(
            value["tags"]
        )
    if "add_ons" in value:
        import capo_lightsail.types.add_on_request_list

        out["addOns"] = capo_lightsail.types.add_on_request_list.serialize_aws_json_1_1(
            value["add_ons"]
        )
    if "ip_address_type" in value:
        import capo_lightsail.types.ip_address_type

        out["ipAddressType"] = (
            capo_lightsail.types.ip_address_type.serialize_aws_json_1_1(
                value["ip_address_type"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateInstancesRequest:
    out: CreateInstancesRequest = {}  # type: ignore[typeddict-item]
    if data.get("instanceNames") is not None:
        import capo_lightsail.types.string_list

        out["instance_names"] = (
            capo_lightsail.types.string_list.deserialize_aws_json_1_1(
                data["instanceNames"]
            )
        )
    else:
        raise DeserializationError("CreateInstancesRequest.instance_names required")
    if data.get("availabilityZone") is not None:
        out["availability_zone"] = data["availabilityZone"]
    else:
        raise DeserializationError("CreateInstancesRequest.availability_zone required")
    if data.get("customImageName") is not None:
        out["custom_image_name"] = data["customImageName"]
    if data.get("blueprintId") is not None:
        out["blueprint_id"] = data["blueprintId"]
    else:
        raise DeserializationError("CreateInstancesRequest.blueprint_id required")
    if data.get("bundleId") is not None:
        out["bundle_id"] = data["bundleId"]
    else:
        raise DeserializationError("CreateInstancesRequest.bundle_id required")
    if data.get("userData") is not None:
        out["user_data"] = data["userData"]
    if data.get("keyPairName") is not None:
        out["key_pair_name"] = data["keyPairName"]
    if data.get("tags") is not None:
        import capo_lightsail.types.tag_list

        out["tags"] = capo_lightsail.types.tag_list.deserialize_aws_json_1_1(
            data["tags"]
        )
    if data.get("addOns") is not None:
        import capo_lightsail.types.add_on_request_list

        out["add_ons"] = (
            capo_lightsail.types.add_on_request_list.deserialize_aws_json_1_1(
                data["addOns"]
            )
        )
    if data.get("ipAddressType") is not None:
        import capo_lightsail.types.ip_address_type

        out["ip_address_type"] = (
            capo_lightsail.types.ip_address_type.deserialize_aws_json_1_1(
                data["ipAddressType"]
            )
        )
    return out
