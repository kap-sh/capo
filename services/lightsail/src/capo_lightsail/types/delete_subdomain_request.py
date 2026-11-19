"""Generated from Smithy shape ``com.amazonaws.lightsail#DeleteSubdomainRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_lightsail.types.string


class DeleteSubdomainRequest(TypedDict, closed=True):
    subdomain_name: "capo_lightsail.types.string.string"
    """<p>The subdomain to delete (for example, <code>mysite</code> or <code>blog.mysite</code>), not its web address.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteSubdomainRequest) -> dict:
    out: dict = {}
    out["subdomainName"] = value["subdomain_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteSubdomainRequest:
    out: DeleteSubdomainRequest = {}  # type: ignore[typeddict-item]
    if data.get("subdomainName") is not None:
        out["subdomain_name"] = data["subdomainName"]
    else:
        out["subdomain_name"] = ""
    return out
