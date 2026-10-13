"""Generated from Smithy shape ``com.amazonaws.wickr#RegisterOpentdfConfigRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_wickr.errors import DeserializationError

if TYPE_CHECKING:
    import capo_wickr.types.generic_string
    import capo_wickr.types.network_id
    import capo_wickr.types.sensitive_string


class RegisterOpentdfConfigRequest(TypedDict, closed=True):
    network_id: "capo_wickr.types.network_id.NetworkId"
    """<p>The ID of the Wickr network for which OpenTDF integration will be configured.</p>"""
    client_id: "capo_wickr.types.generic_string.GenericString"
    """<p>The OIDC client ID used for authenticating with the OpenTDF provider.</p>"""
    client_secret: "capo_wickr.types.sensitive_string.SensitiveString"
    """<p>The OIDC client secret used for authenticating with the OpenTDF provider</p>"""
    domain: "capo_wickr.types.generic_string.GenericString"
    """<p>The domain of the OpenTDF server.</p>"""
    provider: "capo_wickr.types.generic_string.GenericString"
    """<p>The provider of the OpenTDF platform.</p> <note> <p>Currently only Virtru is supported as the OpenTDF provider.</p> </note>"""
    dry_run: NotRequired["bool"]
    """<p>Perform dry-run test connection of OpenTDF configuration (optional).</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RegisterOpentdfConfigRequest) -> dict:
    out: dict = {}
    out["clientId"] = value["client_id"]
    out["clientSecret"] = value["client_secret"]
    out["domain"] = value["domain"]
    out["provider"] = value["provider"]
    return out


def deserialize_json(data: dict) -> RegisterOpentdfConfigRequest:
    out: RegisterOpentdfConfigRequest = {}  # type: ignore[typeddict-item]
    if data.get("clientId") is not None:
        out["client_id"] = data["clientId"]
    else:
        raise DeserializationError("RegisterOpentdfConfigRequest.client_id required")
    if data.get("clientSecret") is not None:
        out["client_secret"] = data["clientSecret"]
    else:
        raise DeserializationError(
            "RegisterOpentdfConfigRequest.client_secret required"
        )
    if data.get("domain") is not None:
        out["domain"] = data["domain"]
    else:
        raise DeserializationError("RegisterOpentdfConfigRequest.domain required")
    if data.get("provider") is not None:
        out["provider"] = data["provider"]
    else:
        raise DeserializationError("RegisterOpentdfConfigRequest.provider required")
    return out


def redact_sensitive(value: RegisterOpentdfConfigRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "client_secret" in value:
        out["client_secret"] = "*** Sensitive Data Redacted ***"
    return out
