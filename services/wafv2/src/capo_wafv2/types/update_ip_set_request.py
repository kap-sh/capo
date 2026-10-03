"""Generated from Smithy shape ``com.amazonaws.wafv2#UpdateIPSetRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_wafv2.errors import DeserializationError

if TYPE_CHECKING:
    import capo_wafv2.types.entity_description
    import capo_wafv2.types.entity_id
    import capo_wafv2.types.entity_name
    import capo_wafv2.types.ip_addresses
    import capo_wafv2.types.lock_token
    import capo_wafv2.types.scope


class UpdateIPSetRequest(TypedDict, closed=True):
    name: "capo_wafv2.types.entity_name.EntityName"
    """<p>The name of the IP set. You cannot change the name of an <code>IPSet</code> after you create it.</p>"""
    scope: "capo_wafv2.types.scope.Scope"
    """<p>Specifies whether this is for a global resource type, such as a Amazon CloudFront distribution. For an Amplify application, use <code>CLOUDFRONT</code>.</p> <p>To work with CloudFront, you must also specify the Region US East (N. Virginia) as follows: </p> <ul> <li> <p>CLI - Specify the Region when you use the CloudFront scope: <code>--scope=CLOUDFRONT --region=us-east-1</code>. </p> </li> <li> <p>API and SDKs - For all calls, use the Region endpoint us-east-1. </p> </li> </ul>"""
    id: "capo_wafv2.types.entity_id.EntityId"
    """<p>A unique identifier for the set. This ID is returned in the responses to create and list commands. You provide it to operations like update and delete.</p>"""
    description: NotRequired["capo_wafv2.types.entity_description.EntityDescription"]
    """<p>A description of the IP set that helps with identification. </p>"""
    addresses: "capo_wafv2.types.ip_addresses.IPAddresses"
    """<p>Contains an array of strings that specifies zero or more IP addresses or blocks of IP addresses that you want WAF to inspect for in incoming requests. All addresses must be specified using Classless Inter-Domain Routing (CIDR) notation. WAF supports all IPv4 and IPv6 CIDR ranges except for <code>/0</code>. </p> <p>Example address strings: </p> <ul> <li> <p>For requests that originated from the IP address 192.0.2.44, specify <code>192.0.2.44/32</code>.</p> </li> <li> <p>For requests that originated from IP addresses from 192.0.2.0 to 192.0.2.255, specify <code>192.0.2.0/24</code>.</p> </li> <li> <p>For requests that originated from the IP address 1111:0000:0000:0000:0000:0000:0000:0111, specify <code>1111:0000:0000:0000:0000:0000:0000:0111/128</code>.</p> </li> <li> <p>For requests that originated from IP addresses 1111:0000:0000:0000:0000:0000:0000:0000 to 1111:0000:0000:0000:ffff:ffff:ffff:ffff, specify <code>1111:0000:0000:0000:0000:0000:0000:0000/64</code>.</p> </li> </ul> <p>For more information about CIDR notation, see the Wikipedia entry <a href="https://en.wikipedia.org/wiki/Classless_Inter-Domain_Routing">Classless Inter-Domain Routing</a>.</p> <p>Example JSON <code>Addresses</code> specifications: </p> <ul> <li> <p>Empty array: <code>"Addresses": []</code> </p> </li> <li> <p>Array with one address: <code>"Addresses": ["192.0.2.44/32"]</code> </p> </li> <li> <p>Array with three addresses: <code>"Addresses": ["192.0.2.44/32", "192.0.2.0/24", "192.0.0.0/16"]</code> </p> </li> <li> <p>INVALID specification: <code>"Addresses": [""]</code> INVALID </p> </li> </ul>"""
    lock_token: "capo_wafv2.types.lock_token.LockToken"
    """<p>A token used for optimistic locking. WAF returns a token to your <code>get</code> and <code>list</code> requests, to mark the state of the entity at the time of the request. To make changes to the entity associated with the token, you provide the token to operations like <code>update</code> and <code>delete</code>. WAF uses the token to ensure that no changes have been made to the entity since you last retrieved it. If a change has been made, the update fails with a <code>WAFOptimisticLockException</code>. If this happens, perform another <code>get</code>, and use the new token returned by that operation. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateIPSetRequest) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    import capo_wafv2.types.scope

    out["Scope"] = capo_wafv2.types.scope.serialize_aws_json_1_1(value["scope"])
    out["Id"] = value["id"]
    if "description" in value:
        out["Description"] = value["description"]
    import capo_wafv2.types.ip_addresses

    out["Addresses"] = capo_wafv2.types.ip_addresses.serialize_aws_json_1_1(
        value["addresses"]
    )
    out["LockToken"] = value["lock_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateIPSetRequest:
    out: UpdateIPSetRequest = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("UpdateIPSetRequest.name required")
    if data.get("Scope") is not None:
        import capo_wafv2.types.scope

        out["scope"] = capo_wafv2.types.scope.deserialize_aws_json_1_1(data["Scope"])
    else:
        raise DeserializationError("UpdateIPSetRequest.scope required")
    if data.get("Id") is not None:
        out["id"] = data["Id"]
    else:
        raise DeserializationError("UpdateIPSetRequest.id required")
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("Addresses") is not None:
        import capo_wafv2.types.ip_addresses

        out["addresses"] = capo_wafv2.types.ip_addresses.deserialize_aws_json_1_1(
            data["Addresses"]
        )
    else:
        raise DeserializationError("UpdateIPSetRequest.addresses required")
    if data.get("LockToken") is not None:
        out["lock_token"] = data["LockToken"]
    else:
        raise DeserializationError("UpdateIPSetRequest.lock_token required")
    return out
