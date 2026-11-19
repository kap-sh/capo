"""Generated from Smithy shape ``com.amazonaws.lightsail#Subdomain``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lightsail.types.integer
    import capo_lightsail.types.iso_date
    import capo_lightsail.types.non_empty_string
    import capo_lightsail.types.resource_location
    import capo_lightsail.types.string
    import capo_lightsail.types.subdomain_attachable_resource
    import capo_lightsail.types.subdomain_list
    import capo_lightsail.types.subdomain_state
    import capo_lightsail.types.tag_list


class Subdomain(TypedDict, closed=True):
    subdomain_name: NotRequired["capo_lightsail.types.string.string"]
    """<p>The subdomain (for example, <code>mysite</code> or <code>blog.mysite</code>). To get the web address, use the <code>fqdn</code> parameter.</p>"""
    arn: NotRequired["capo_lightsail.types.non_empty_string.NonEmptyString"]
    """<p>The Amazon Resource Name (ARN) of the subdomain.</p> <p>If you create a subdomain with a depth of 2, such as <code>blog.mysite</code>, without first creating the subdomain with a depth of 1 (<code>mysite</code>), Lightsail holds <code>mysite</code> for your account in the <code>IMPLICIT</code> state. It doesn't have an ARN until you create a subdomain with that name.</p>"""
    fqdn: NotRequired["capo_lightsail.types.string.string"]
    """<p>The web address of the subdomain, which is the subdomain followed by <code>amazonlightsail.com</code> (for example, <code>blog.mysite.amazonlightsail.com</code>).</p>"""
    depth: NotRequired["capo_lightsail.types.integer.integer"]
    """<p>The number of labels in the subdomain. A top-level subdomain, such as <code>mysite</code>, has a depth of <code>1</code>. A nested subdomain, such as <code>blog.mysite</code>, has a depth of <code>2</code>.</p>"""
    state: NotRequired["capo_lightsail.types.subdomain_state.SubdomainState"]
    """<p>The state of the subdomain.</p> <p>The following states are possible:</p> <ul> <li> <p> <code>CREATING</code> – The subdomain is being created.</p> </li> <li> <p> <code>CREATE_FAILED</code> – The subdomain couldn't be created. Delete the subdomain, and then create it again if the name is still available.</p> </li> <li> <p> <code>UNATTACHED</code> – The subdomain is ready, and isn't associated with a resource.</p> </li> <li> <p> <code>ATTACHING</code> – The subdomain is being associated with a resource.</p> </li> <li> <p> <code>ATTACHED</code> – The subdomain is associated with a resource, and routes traffic to it.</p> </li> <li> <p> <code>DETACHING</code> – The subdomain is being disassociated from a resource.</p> </li> <li> <p> <code>TRANSFERRING</code> – The subdomain is being moved from one resource to another resource.</p> </li> <li> <p> <code>IMPLICIT</code> – The subdomain is the parent of one or more nested subdomains that you created, but you didn't create the parent subdomain itself. You can't associate or delete a subdomain in this state. To use it, create it with the <code>CreateSubdomain</code> action.</p> </li> </ul>"""
    attached_resource: NotRequired[
        "capo_lightsail.types.subdomain_attachable_resource.SubdomainAttachableResource"
    ]
    """<p>An object that describes the resource that the subdomain is associated with.</p> <p>When the subdomain is in the <code>TRANSFERRING</code> state, this is the resource that the subdomain is being moved from.</p>"""
    attaching_resource: NotRequired[
        "capo_lightsail.types.subdomain_attachable_resource.SubdomainAttachableResource"
    ]
    """<p>An object that describes the resource that the subdomain is being associated with.</p> <p>This parameter is returned only when the subdomain is in the <code>ATTACHING</code> or <code>TRANSFERRING</code> state.</p>"""
    location: NotRequired["capo_lightsail.types.resource_location.ResourceLocation"]
    """<p>An object that describes the location of the subdomain, such as the AWS Region.</p>"""
    created_at: NotRequired["capo_lightsail.types.iso_date.IsoDate"]
    """<p>The timestamp when the subdomain was created.</p>"""
    parent_fqdn: NotRequired["capo_lightsail.types.string.string"]
    """<p>The web address of the parent subdomain (for example, <code>mysite.amazonlightsail.com</code> for <code>blog.mysite</code>).</p> <p>This parameter isn't returned for a subdomain with a depth of 1.</p>"""
    children: NotRequired["capo_lightsail.types.subdomain_list.SubdomainList"]
    """<p>An array of objects that describe the nested subdomains of the subdomain.</p> <p>This parameter is returned only by the <code>GetSubdomains</code> action when you don't specify a subdomain.</p>"""
    tags: NotRequired["capo_lightsail.types.tag_list.TagList"]
    """<p>The tag keys and optional values for the subdomain. For more information about tags in Lightsail, see the <a href="https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-tags">Lightsail Developer Guide</a>.</p> <p>This parameter is returned only by the <code>GetSubdomains</code> action when you specify a subdomain.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Subdomain) -> dict:
    out: dict = {}
    if "subdomain_name" in value:
        out["subdomainName"] = value["subdomain_name"]
    if "arn" in value:
        out["arn"] = value["arn"]
    if "fqdn" in value:
        out["fqdn"] = value["fqdn"]
    if "depth" in value:
        out["depth"] = value["depth"]
    if "state" in value:
        import capo_lightsail.types.subdomain_state

        out["state"] = capo_lightsail.types.subdomain_state.serialize_aws_json_1_1(
            value["state"]
        )
    if "attached_resource" in value:
        import capo_lightsail.types.subdomain_attachable_resource

        out["attachedResource"] = (
            capo_lightsail.types.subdomain_attachable_resource.serialize_aws_json_1_1(
                value["attached_resource"]
            )
        )
    if "attaching_resource" in value:
        import capo_lightsail.types.subdomain_attachable_resource

        out["attachingResource"] = (
            capo_lightsail.types.subdomain_attachable_resource.serialize_aws_json_1_1(
                value["attaching_resource"]
            )
        )
    if "location" in value:
        import capo_lightsail.types.resource_location

        out["location"] = capo_lightsail.types.resource_location.serialize_aws_json_1_1(
            value["location"]
        )
    if "created_at" in value:
        import capo_lightsail.types.iso_date

        out["createdAt"] = capo_lightsail.types.iso_date.serialize_aws_json_1_1(
            value["created_at"]
        )
    if "parent_fqdn" in value:
        out["parentFqdn"] = value["parent_fqdn"]
    if "children" in value:
        import capo_lightsail.types.subdomain_list

        out["children"] = capo_lightsail.types.subdomain_list.serialize_aws_json_1_1(
            value["children"]
        )
    if "tags" in value:
        import capo_lightsail.types.tag_list

        out["tags"] = capo_lightsail.types.tag_list.serialize_aws_json_1_1(
            value["tags"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> Subdomain:
    out: Subdomain = {}  # type: ignore[typeddict-item]
    if data.get("subdomainName") is not None:
        out["subdomain_name"] = data["subdomainName"]
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    if data.get("fqdn") is not None:
        out["fqdn"] = data["fqdn"]
    if data.get("depth") is not None:
        out["depth"] = data["depth"]
    if data.get("state") is not None:
        import capo_lightsail.types.subdomain_state

        out["state"] = capo_lightsail.types.subdomain_state.deserialize_aws_json_1_1(
            data["state"]
        )
    if data.get("attachedResource") is not None:
        import capo_lightsail.types.subdomain_attachable_resource

        out["attached_resource"] = (
            capo_lightsail.types.subdomain_attachable_resource.deserialize_aws_json_1_1(
                data["attachedResource"]
            )
        )
    if data.get("attachingResource") is not None:
        import capo_lightsail.types.subdomain_attachable_resource

        out["attaching_resource"] = (
            capo_lightsail.types.subdomain_attachable_resource.deserialize_aws_json_1_1(
                data["attachingResource"]
            )
        )
    if data.get("location") is not None:
        import capo_lightsail.types.resource_location

        out["location"] = (
            capo_lightsail.types.resource_location.deserialize_aws_json_1_1(
                data["location"]
            )
        )
    if data.get("createdAt") is not None:
        import capo_lightsail.types.iso_date

        out["created_at"] = capo_lightsail.types.iso_date.deserialize_aws_json_1_1(
            data["createdAt"]
        )
    if data.get("parentFqdn") is not None:
        out["parent_fqdn"] = data["parentFqdn"]
    if data.get("children") is not None:
        import capo_lightsail.types.subdomain_list

        out["children"] = capo_lightsail.types.subdomain_list.deserialize_aws_json_1_1(
            data["children"]
        )
    if data.get("tags") is not None:
        import capo_lightsail.types.tag_list

        out["tags"] = capo_lightsail.types.tag_list.deserialize_aws_json_1_1(
            data["tags"]
        )
    return out
