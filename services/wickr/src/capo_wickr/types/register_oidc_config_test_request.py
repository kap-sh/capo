"""Generated from Smithy shape ``com.amazonaws.wickr#RegisterOidcConfigTestRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_wickr.types.generic_string
    import capo_wickr.types.network_id


class RegisterOidcConfigTestRequest(TypedDict, closed=True):
    network_id: "capo_wickr.types.network_id.NetworkId"
    """<p>The ID of the Wickr network for which the OIDC configuration will be tested.</p>"""
    extra_auth_params: NotRequired["capo_wickr.types.generic_string.GenericString"]
    """<p>Additional authentication parameters to include in the test (optional).</p>"""
    issuer: "capo_wickr.types.generic_string.GenericString"
    """<p>The issuer URL of the OIDC provider to test.</p>"""
    scopes: "capo_wickr.types.generic_string.GenericString"
    """<p>The OAuth scopes to test with the OIDC provider.</p>"""
    certificate: NotRequired["capo_wickr.types.generic_string.GenericString"]
    """<p>The CA certificate for secure communication with the OIDC provider (optional).</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RegisterOidcConfigTestRequest) -> dict:
    out: dict = {}
    if "extra_auth_params" in value:
        out["extraAuthParams"] = value["extra_auth_params"]
    out["issuer"] = value["issuer"]
    out["scopes"] = value["scopes"]
    if "certificate" in value:
        out["certificate"] = value["certificate"]
    return out


def deserialize_json(data: dict) -> RegisterOidcConfigTestRequest:
    out: RegisterOidcConfigTestRequest = {}  # type: ignore[typeddict-item]
    if data.get("extraAuthParams") is not None:
        out["extra_auth_params"] = data["extraAuthParams"]
    if data.get("issuer") is not None:
        out["issuer"] = data["issuer"]
    else:
        out["issuer"] = ""
    if data.get("scopes") is not None:
        out["scopes"] = data["scopes"]
    else:
        out["scopes"] = ""
    if data.get("certificate") is not None:
        out["certificate"] = data["certificate"]
    return out
