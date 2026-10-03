"""Generated from Smithy shape ``com.amazonaws.migrationhubrefactorspaces#UrlEndpointInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_migration_hub_refactor_spaces.errors import DeserializationError

if TYPE_CHECKING:
    import capo_migration_hub_refactor_spaces.types.uri


class UrlEndpointInput(TypedDict, closed=True):
    url: "capo_migration_hub_refactor_spaces.types.uri.Uri"
    """<p>The URL to route traffic to. The URL must be an <a href="https://datatracker.ietf.org/doc/html/rfc3986">rfc3986-formatted URL</a>. If the host is a domain name, the name must be resolvable over the public internet. If the scheme is <code>https</code>, the top level domain of the host must be listed in the <a href="https://www.iana.org/domains/root/db">IANA root zone database</a>. </p>"""
    health_url: NotRequired["capo_migration_hub_refactor_spaces.types.uri.Uri"]
    """<p>The health check URL of the URL endpoint type. If the URL is a public endpoint, the <code>HealthUrl</code> must also be a public endpoint. If the URL is a private endpoint inside a virtual private cloud (VPC), the health URL must also be a private endpoint, and the host must be the same as the URL. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UrlEndpointInput) -> dict:
    out: dict = {}
    out["Url"] = value["url"]
    if "health_url" in value:
        out["HealthUrl"] = value["health_url"]
    return out


def deserialize_json(data: dict) -> UrlEndpointInput:
    out: UrlEndpointInput = {}  # type: ignore[typeddict-item]
    if data.get("Url") is not None:
        out["url"] = data["Url"]
    else:
        raise DeserializationError("UrlEndpointInput.url required")
    if data.get("HealthUrl") is not None:
        out["health_url"] = data["HealthUrl"]
    return out
