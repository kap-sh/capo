"""Generated from Smithy shape ``com.amazonaws.vpclattice#StartDomainVerificationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_vpc_lattice.types.client_token
    import capo_vpc_lattice.types.domain_name
    import capo_vpc_lattice.types.tag_map


class StartDomainVerificationRequest(TypedDict, closed=True):
    client_token: NotRequired["capo_vpc_lattice.types.client_token.ClientToken"]
    """<p> A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If you retry a request that completed successfully using the same client token and parameters, the retry succeeds without performing any actions. If the parameters aren't identical, the retry fails. </p>"""
    domain_name: "capo_vpc_lattice.types.domain_name.DomainName"
    """<p> The domain name to verify ownership for. </p>"""
    tags: NotRequired["capo_vpc_lattice.types.tag_map.TagMap"]
    """<p> The tags for the domain verification. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartDomainVerificationRequest) -> dict:
    out: dict = {}
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    out["domainName"] = value["domain_name"]
    if "tags" in value:
        import capo_vpc_lattice.types.tag_map

        out["tags"] = capo_vpc_lattice.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> StartDomainVerificationRequest:
    out: StartDomainVerificationRequest = {}  # type: ignore[typeddict-item]
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    if data.get("domainName") is not None:
        out["domain_name"] = data["domainName"]
    else:
        out["domain_name"] = ""
    if data.get("tags") is not None:
        import capo_vpc_lattice.types.tag_map

        out["tags"] = capo_vpc_lattice.types.tag_map.deserialize_json(data["tags"])
    return out
