"""Generated from Smithy shape ``com.amazonaws.wickr#RegisterOpentdfConfigResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

from capo_wickr.errors import DeserializationError

if TYPE_CHECKING:
    import capo_wickr.types.generic_string
    import capo_wickr.types.sensitive_string


class RegisterOpentdfConfigResponse(TypedDict, closed=True):
    client_id: "capo_wickr.types.generic_string.GenericString"
    """<p>The OIDC client ID used for authenticating with the OpenTDF provider.</p>"""
    domain: "capo_wickr.types.generic_string.GenericString"
    """<p>The domain of the OpenTDF server.</p>"""
    client_secret: "capo_wickr.types.sensitive_string.SensitiveString"
    """<p>The OIDC client secret used for authenticating with the OpenTDF provider.</p>"""
    provider: "capo_wickr.types.generic_string.GenericString"
    """<p>The provider of the OpenTDF platform.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RegisterOpentdfConfigResponse) -> dict:
    out: dict = {}
    out["clientId"] = value["client_id"]
    out["domain"] = value["domain"]
    out["clientSecret"] = value["client_secret"]
    out["provider"] = value["provider"]
    return out


def deserialize_json(data: dict) -> RegisterOpentdfConfigResponse:
    out: RegisterOpentdfConfigResponse = {}  # type: ignore[typeddict-item]
    if data.get("clientId") is not None:
        out["client_id"] = data["clientId"]
    else:
        raise DeserializationError("RegisterOpentdfConfigResponse.client_id required")
    if data.get("domain") is not None:
        out["domain"] = data["domain"]
    else:
        raise DeserializationError("RegisterOpentdfConfigResponse.domain required")
    if data.get("clientSecret") is not None:
        out["client_secret"] = data["clientSecret"]
    else:
        raise DeserializationError(
            "RegisterOpentdfConfigResponse.client_secret required"
        )
    if data.get("provider") is not None:
        out["provider"] = data["provider"]
    else:
        raise DeserializationError("RegisterOpentdfConfigResponse.provider required")
    return out


def redact_sensitive(value: RegisterOpentdfConfigResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "client_secret" in value:
        out["client_secret"] = "*** Sensitive Data Redacted ***"
    return out
