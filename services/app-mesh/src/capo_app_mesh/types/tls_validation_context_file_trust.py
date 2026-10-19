"""Generated from Smithy shape ``com.amazonaws.appmesh#TlsValidationContextFileTrust``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_app_mesh.types.file_path


class TlsValidationContextFileTrust(TypedDict, closed=True):
    certificate_chain: "capo_app_mesh.types.file_path.FilePath"
    """<p>The certificate trust chain for a certificate stored on the file system of the virtual node that the proxy is running on.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TlsValidationContextFileTrust) -> dict:
    out: dict = {}
    out["certificateChain"] = value["certificate_chain"]
    return out


def deserialize_json(data: dict) -> TlsValidationContextFileTrust:
    out: TlsValidationContextFileTrust = {}  # type: ignore[typeddict-item]
    if data.get("certificateChain") is not None:
        out["certificate_chain"] = data["certificateChain"]
    else:
        out["certificate_chain"] = ""
    return out
