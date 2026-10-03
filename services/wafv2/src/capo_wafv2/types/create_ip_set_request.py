"""Generated from Smithy shape ``com.amazonaws.wafv2#CreateIPSetRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_wafv2.errors import DeserializationError

if TYPE_CHECKING:
    import capo_wafv2.types.entity_description
    import capo_wafv2.types.entity_name
    import capo_wafv2.types.ip_address_version
    import capo_wafv2.types.ip_addresses
    import capo_wafv2.types.scope
    import capo_wafv2.types.tag_list


class CreateIPSetRequest(TypedDict, closed=True):
    name: "capo_wafv2.types.entity_name.EntityName"
    """<p>The name of the IP set. You cannot change the name of an <code>IPSet</code> after you create it.</p>"""
    scope: "capo_wafv2.types.scope.Scope"
    """<p>Specifies whether this is for a global resource type, such as a Amazon CloudFront distribution. For an Amplify application, use <code>CLOUDFRONT</code>.</p> <p>To work with CloudFront, you must also specify the Region US East (N. Virginia) as follows: </p> <ul> <li> <p>CLI - Specify the Region when you use the CloudFront scope: <code>--scope=CLOUDFRONT --region=us-east-1</code>. </p> </li> <li> <p>API and SDKs - For all calls, use the Region endpoint us-east-1. </p> </li> </ul>"""
    description: NotRequired["capo_wafv2.types.entity_description.EntityDescription"]
    """<p>A description of the IP set that helps with identification. </p>"""
    ip_address_version: "capo_wafv2.types.ip_address_version.IPAddressVersion"
    """<p>The version of the IP addresses, either <code>IPV4</code> or <code>IPV6</code>. </p>"""
    addresses: "capo_wafv2.types.ip_addresses.IPAddresses"
    """<p>Contains an array of strings that specifies zero or more IP addresses or blocks of IP addresses that you want WAF to inspect for in incoming requests. All addresses must be specified using Classless Inter-Domain Routing (CIDR) notation. WAF supports all IPv4 and IPv6 CIDR ranges except for <code>/0</code>. </p> <p>Example address strings: </p> <ul> <li> <p>For requests that originated from the IP address 192.0.2.44, specify <code>192.0.2.44/32</code>.</p> </li> <li> <p>For requests that originated from IP addresses from 192.0.2.0 to 192.0.2.255, specify <code>192.0.2.0/24</code>.</p> </li> <li> <p>For requests that originated from the IP address 1111:0000:0000:0000:0000:0000:0000:0111, specify <code>1111:0000:0000:0000:0000:0000:0000:0111/128</code>.</p> </li> <li> <p>For requests that originated from IP addresses 1111:0000:0000:0000:0000:0000:0000:0000 to 1111:0000:0000:0000:ffff:ffff:ffff:ffff, specify <code>1111:0000:0000:0000:0000:0000:0000:0000/64</code>.</p> </li> </ul> <p>For more information about CIDR notation, see the Wikipedia entry <a href="https://en.wikipedia.org/wiki/Classless_Inter-Domain_Routing">Classless Inter-Domain Routing</a>.</p> <p>Example JSON <code>Addresses</code> specifications: </p> <ul> <li> <p>Empty array: <code>"Addresses": []</code> </p> </li> <li> <p>Array with one address: <code>"Addresses": ["192.0.2.44/32"]</code> </p> </li> <li> <p>Array with three addresses: <code>"Addresses": ["192.0.2.44/32", "192.0.2.0/24", "192.0.0.0/16"]</code> </p> </li> <li> <p>INVALID specification: <code>"Addresses": [""]</code> INVALID </p> </li> </ul>"""
    tags: NotRequired["capo_wafv2.types.tag_list.TagList"]
    """<p>An array of key:value pairs to associate with the resource.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateIPSetRequest) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    import capo_wafv2.types.scope

    out["Scope"] = capo_wafv2.types.scope.serialize_aws_json_1_1(value["scope"])
    if "description" in value:
        out["Description"] = value["description"]
    import capo_wafv2.types.ip_address_version

    out["IPAddressVersion"] = (
        capo_wafv2.types.ip_address_version.serialize_aws_json_1_1(
            value["ip_address_version"]
        )
    )
    import capo_wafv2.types.ip_addresses

    out["Addresses"] = capo_wafv2.types.ip_addresses.serialize_aws_json_1_1(
        value["addresses"]
    )
    if "tags" in value:
        import capo_wafv2.types.tag_list

        out["Tags"] = capo_wafv2.types.tag_list.serialize_aws_json_1_1(value["tags"])
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateIPSetRequest:
    out: CreateIPSetRequest = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("CreateIPSetRequest.name required")
    if data.get("Scope") is not None:
        import capo_wafv2.types.scope

        out["scope"] = capo_wafv2.types.scope.deserialize_aws_json_1_1(data["Scope"])
    else:
        raise DeserializationError("CreateIPSetRequest.scope required")
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("IPAddressVersion") is not None:
        import capo_wafv2.types.ip_address_version

        out["ip_address_version"] = (
            capo_wafv2.types.ip_address_version.deserialize_aws_json_1_1(
                data["IPAddressVersion"]
            )
        )
    else:
        raise DeserializationError("CreateIPSetRequest.ip_address_version required")
    if data.get("Addresses") is not None:
        import capo_wafv2.types.ip_addresses

        out["addresses"] = capo_wafv2.types.ip_addresses.deserialize_aws_json_1_1(
            data["Addresses"]
        )
    else:
        raise DeserializationError("CreateIPSetRequest.addresses required")
    if data.get("Tags") is not None:
        import capo_wafv2.types.tag_list

        out["tags"] = capo_wafv2.types.tag_list.deserialize_aws_json_1_1(data["Tags"])
    return out
