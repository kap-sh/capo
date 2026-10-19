"""Generated from Smithy shape ``com.amazonaws.cloudwatchomni#CreateOneTimeDeepLinkCodeInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cloudwatchomni.types.domain_id


class CreateOneTimeDeepLinkCodeInput(TypedDict, closed=True):
    domain_id: "capo_cloudwatchomni.types.domain_id.DomainId"
    """The ID of the domain to generate the code for."""
    ttl_seconds: NotRequired["int"]
    """How long the code remains valid, in seconds. Defaults to 300."""
    redirect_url: NotRequired["str"]
    """The URL to redirect to after the deep-link code is used. Must be an HTTPS URL in the domain with a path of /auth/callback, and cannot include a query string or fragment. If omitted, no redirect is applied."""


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: CreateOneTimeDeepLinkCodeInput) -> dict:
    out: dict = {}
    out["domainId"] = value["domain_id"]
    if "ttl_seconds" in value:
        out["ttlSeconds"] = value["ttl_seconds"]
    if "redirect_url" in value:
        out["redirectUrl"] = value["redirect_url"]
    return out


def deserialize_cbor(data: dict) -> CreateOneTimeDeepLinkCodeInput:
    out: CreateOneTimeDeepLinkCodeInput = {}  # type: ignore[typeddict-item]
    if data.get("domainId") is not None:
        out["domain_id"] = data["domainId"]
    else:
        out["domain_id"] = ""
    if data.get("ttlSeconds") is not None:
        out["ttl_seconds"] = data["ttlSeconds"]
    if data.get("redirectUrl") is not None:
        out["redirect_url"] = data["redirectUrl"]
    return out
