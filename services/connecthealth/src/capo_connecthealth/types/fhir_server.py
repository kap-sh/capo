"""Generated from Smithy shape ``com.amazonaws.connecthealth#FHIRServer``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connecthealth.types.non_empty_string
    import capo_connecthealth.types.sensitive_non_empty_string


class FHIRServer(TypedDict, closed=True):
    fhir_endpoint: "capo_connecthealth.types.non_empty_string.NonEmptyString"
    """<p>FHIR server endpoint URL for accessing patient data.</p>"""
    oauth_token: NotRequired[
        "capo_connecthealth.types.sensitive_non_empty_string.SensitiveNonEmptyString"
    ]
    """<p>OAuth token for authenticating with the FHIR server.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FHIRServer) -> dict:
    out: dict = {}
    out["fhirEndpoint"] = value["fhir_endpoint"]
    if "oauth_token" in value:
        out["oauthToken"] = value["oauth_token"]
    return out


def deserialize_json(data: dict) -> FHIRServer:
    out: FHIRServer = {}  # type: ignore[typeddict-item]
    if data.get("fhirEndpoint") is not None:
        out["fhir_endpoint"] = data["fhirEndpoint"]
    else:
        out["fhir_endpoint"] = ""
    if data.get("oauthToken") is not None:
        out["oauth_token"] = data["oauthToken"]
    return out


def redact_sensitive(value: FHIRServer) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "oauth_token" in value:
        out["oauth_token"] = "*** Sensitive Data Redacted ***"
    return out
