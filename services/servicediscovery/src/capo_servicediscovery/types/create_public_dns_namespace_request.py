"""Generated from Smithy shape ``com.amazonaws.servicediscovery#CreatePublicDnsNamespaceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_servicediscovery.types.namespace_name_public
    import capo_servicediscovery.types.public_dns_namespace_properties
    import capo_servicediscovery.types.resource_description
    import capo_servicediscovery.types.resource_id
    import capo_servicediscovery.types.tag_list


class CreatePublicDnsNamespaceRequest(TypedDict, closed=True):
    name: "capo_servicediscovery.types.namespace_name_public.NamespaceNamePublic"
    """<p>The name that you want to assign to this namespace.</p> <note> <p>Do not include sensitive information in the name. The name is publicly available using DNS queries.</p> </note>"""
    creator_request_id: NotRequired[
        "capo_servicediscovery.types.resource_id.ResourceId"
    ]
    """<p>A unique string that identifies the request and that allows failed <code>CreatePublicDnsNamespace</code> requests to be retried without the risk of running the operation twice. <code>CreatorRequestId</code> can be any unique string (for example, a date/timestamp).</p>"""
    description: NotRequired[
        "capo_servicediscovery.types.resource_description.ResourceDescription"
    ]
    """<p>A description for the namespace.</p>"""
    tags: NotRequired["capo_servicediscovery.types.tag_list.TagList"]
    """<p>The tags to add to the namespace. Each tag consists of a key and an optional value that you define. Tags keys can be up to 128 characters in length, and tag values can be up to 256 characters in length.</p>"""
    properties: NotRequired[
        "capo_servicediscovery.types.public_dns_namespace_properties.PublicDnsNamespaceProperties"
    ]
    """<p>Properties for the public DNS namespace.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreatePublicDnsNamespaceRequest) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    if "creator_request_id" in value:
        out["CreatorRequestId"] = value["creator_request_id"]
    if "description" in value:
        out["Description"] = value["description"]
    if "tags" in value:
        import capo_servicediscovery.types.tag_list

        out["Tags"] = capo_servicediscovery.types.tag_list.serialize_aws_json_1_1(
            value["tags"]
        )
    if "properties" in value:
        import capo_servicediscovery.types.public_dns_namespace_properties

        out["Properties"] = (
            capo_servicediscovery.types.public_dns_namespace_properties.serialize_aws_json_1_1(
                value["properties"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreatePublicDnsNamespaceRequest:
    out: CreatePublicDnsNamespaceRequest = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        out["name"] = ""
    if data.get("CreatorRequestId") is not None:
        out["creator_request_id"] = data["CreatorRequestId"]
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("Tags") is not None:
        import capo_servicediscovery.types.tag_list

        out["tags"] = capo_servicediscovery.types.tag_list.deserialize_aws_json_1_1(
            data["Tags"]
        )
    if data.get("Properties") is not None:
        import capo_servicediscovery.types.public_dns_namespace_properties

        out["properties"] = (
            capo_servicediscovery.types.public_dns_namespace_properties.deserialize_aws_json_1_1(
                data["Properties"]
            )
        )
    return out
