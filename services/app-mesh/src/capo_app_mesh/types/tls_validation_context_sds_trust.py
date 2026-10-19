"""Generated from Smithy shape ``com.amazonaws.appmesh#TlsValidationContextSdsTrust``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_app_mesh.types.sds_secret_name


class TlsValidationContextSdsTrust(TypedDict, closed=True):
    secret_name: "capo_app_mesh.types.sds_secret_name.SdsSecretName"
    """<p>A reference to an object that represents the name of the secret for a Transport Layer Security (TLS) Secret Discovery Service validation context trust.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TlsValidationContextSdsTrust) -> dict:
    out: dict = {}
    out["secretName"] = value["secret_name"]
    return out


def deserialize_json(data: dict) -> TlsValidationContextSdsTrust:
    out: TlsValidationContextSdsTrust = {}  # type: ignore[typeddict-item]
    if data.get("secretName") is not None:
        out["secret_name"] = data["secretName"]
    else:
        out["secret_name"] = ""
    return out
