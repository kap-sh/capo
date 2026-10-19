"""Generated from Smithy shape ``com.amazonaws.lightsail#ImportKeyPairRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_lightsail.types.base64
    import capo_lightsail.types.resource_name


class ImportKeyPairRequest(TypedDict, closed=True):
    key_pair_name: "capo_lightsail.types.resource_name.ResourceName"
    """<p>The name of the key pair for which you want to import the public key.</p>"""
    public_key_base64: "capo_lightsail.types.base64.Base64"
    """<p>A base64-encoded public key of the <code>ssh-rsa</code> type.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ImportKeyPairRequest) -> dict:
    out: dict = {}
    out["keyPairName"] = value["key_pair_name"]
    out["publicKeyBase64"] = value["public_key_base64"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ImportKeyPairRequest:
    out: ImportKeyPairRequest = {}  # type: ignore[typeddict-item]
    if data.get("keyPairName") is not None:
        out["key_pair_name"] = data["keyPairName"]
    else:
        out["key_pair_name"] = ""
    if data.get("publicKeyBase64") is not None:
        out["public_key_base64"] = data["publicKeyBase64"]
    else:
        out["public_key_base64"] = ""
    return out
