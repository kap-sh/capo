"""Generated from Smithy shape ``com.amazonaws.lightsail#CheckSubdomainAvailabilityRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lightsail.types.boolean
    import capo_lightsail.types.string


class CheckSubdomainAvailabilityRequest(TypedDict, closed=True):
    subdomain_name: "capo_lightsail.types.string.string"
    """<p>The subdomain to check (for example, <code>mysite</code> or <code>blog.mysite</code>).</p> <p>A subdomain can contain one or two labels separated by a period (<code>.</code>). Each label must start and end with a lowercase letter or a number, and can contain only lowercase letters, numbers, and hyphens (<code>-</code>). The name can be up to 39 characters long, including periods. Labels that start with <code>xn--</code> aren't supported, and some names are reserved.</p> <p>Specify only the subdomain. A web address, such as <code>mysite.amazonlightsail.com</code>, isn't accepted.</p>"""
    reserve: NotRequired["capo_lightsail.types.boolean.boolean"]
    """<p>Specifies whether to reserve the subdomain for your account if it's available. A reservation holds the subdomain for 15 minutes so that other accounts can't create it. Checking the subdomain again doesn't extend the reservation.</p> <p>For a nested subdomain, such as <code>blog.mysite</code>, the top-level subdomain (<code>mysite</code>) is reserved.</p> <p>You can have up to 5 active reservations at a time.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CheckSubdomainAvailabilityRequest) -> dict:
    out: dict = {}
    out["subdomainName"] = value["subdomain_name"]
    if "reserve" in value:
        out["reserve"] = value["reserve"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CheckSubdomainAvailabilityRequest:
    out: CheckSubdomainAvailabilityRequest = {}  # type: ignore[typeddict-item]
    if data.get("subdomainName") is not None:
        out["subdomain_name"] = data["subdomainName"]
    else:
        out["subdomain_name"] = ""
    if data.get("reserve") is not None:
        out["reserve"] = data["reserve"]
    return out
