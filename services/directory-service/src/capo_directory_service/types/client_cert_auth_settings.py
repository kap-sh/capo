"""Generated from Smithy shape ``com.amazonaws.directoryservice#ClientCertAuthSettings``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_directory_service.types.ocsp_url


class ClientCertAuthSettings(TypedDict, closed=True):
    ocsp_url: NotRequired["capo_directory_service.types.ocsp_url.OCSPUrl"]
    """<p>Specifies the URL of the default OCSP server used to check for revocation status. A secondary value to any OCSP address found in the AIA extension of the user certificate.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ClientCertAuthSettings) -> dict:
    out: dict = {}
    if "ocsp_url" in value:
        out["OCSPUrl"] = value["ocsp_url"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ClientCertAuthSettings:
    out: ClientCertAuthSettings = {}  # type: ignore[typeddict-item]
    if data.get("OCSPUrl") is not None:
        out["ocsp_url"] = data["OCSPUrl"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ClientCertAuthSettings) -> dict:
    out: dict = {}
    if "ocsp_url" in value:
        out["OCSPUrl"] = value["ocsp_url"]
    return out


def deserialize_cbor(data: dict) -> ClientCertAuthSettings:
    out: ClientCertAuthSettings = {}  # type: ignore[typeddict-item]
    if data.get("OCSPUrl") is not None:
        out["ocsp_url"] = data["OCSPUrl"]
    return out
