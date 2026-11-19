"""Generated from Smithy shape ``com.amazonaws.lightsail#CreateSubdomainRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lightsail.types.string
    import capo_lightsail.types.tag_list


class CreateSubdomainRequest(TypedDict, closed=True):
    subdomain_name: "capo_lightsail.types.string.string"
    """<p>The subdomain to create (for example, <code>mysite</code> or <code>blog.mysite</code>).</p> <p>A subdomain can contain one or two labels separated by a period (<code>.</code>). Each label must start and end with a lowercase letter or a number, and can contain only lowercase letters, numbers, and hyphens (<code>-</code>). The name can be up to 39 characters long, including periods. Labels that start with <code>xn--</code> aren't supported, and some names are reserved.</p> <p>Specify only the subdomain. A web address, such as <code>mysite.amazonlightsail.com</code>, isn't accepted.</p> <p>To create a nested subdomain, you must own the top-level subdomain or be able to create it.</p>"""
    tags: NotRequired["capo_lightsail.types.tag_list.TagList"]
    """<p>The tag keys and optional values to add to the subdomain during create.</p> <p>Use the <code>TagResource</code> action to tag a resource after it's created.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateSubdomainRequest) -> dict:
    out: dict = {}
    out["subdomainName"] = value["subdomain_name"]
    if "tags" in value:
        import capo_lightsail.types.tag_list

        out["tags"] = capo_lightsail.types.tag_list.serialize_aws_json_1_1(
            value["tags"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateSubdomainRequest:
    out: CreateSubdomainRequest = {}  # type: ignore[typeddict-item]
    if data.get("subdomainName") is not None:
        out["subdomain_name"] = data["subdomainName"]
    else:
        out["subdomain_name"] = ""
    if data.get("tags") is not None:
        import capo_lightsail.types.tag_list

        out["tags"] = capo_lightsail.types.tag_list.deserialize_aws_json_1_1(
            data["tags"]
        )
    return out
