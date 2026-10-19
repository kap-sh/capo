"""Generated from Smithy shape ``com.amazonaws.appmesh#ListenerTlsFileCertificate``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_app_mesh.types.file_path


class ListenerTlsFileCertificate(TypedDict, closed=True):
    certificate_chain: "capo_app_mesh.types.file_path.FilePath"
    """<p>The certificate chain for the certificate.</p>"""
    private_key: "capo_app_mesh.types.file_path.FilePath"
    """<p>The private key for a certificate stored on the file system of the virtual node that the proxy is running on.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListenerTlsFileCertificate) -> dict:
    out: dict = {}
    out["certificateChain"] = value["certificate_chain"]
    out["privateKey"] = value["private_key"]
    return out


def deserialize_json(data: dict) -> ListenerTlsFileCertificate:
    out: ListenerTlsFileCertificate = {}  # type: ignore[typeddict-item]
    if data.get("certificateChain") is not None:
        out["certificate_chain"] = data["certificateChain"]
    else:
        out["certificate_chain"] = ""
    if data.get("privateKey") is not None:
        out["private_key"] = data["privateKey"]
    else:
        out["private_key"] = ""
    return out
