"""Generated from Smithy shape ``com.amazonaws.licensemanager#Issuer``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_license_manager.types.string


class Issuer(TypedDict, closed=True):
    name: "capo_license_manager.types.string.String"
    """<p>Issuer name.</p>"""
    sign_key: NotRequired["capo_license_manager.types.string.String"]
    """<p>Asymmetric KMS key from Key Management Service. The KMS key must have a key usage of sign and verify, and support the RSASSA-PSS SHA-256 signing algorithm.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Issuer) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    if "sign_key" in value:
        out["SignKey"] = value["sign_key"]
    return out


def deserialize_aws_json_1_1(data: dict) -> Issuer:
    out: Issuer = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        out["name"] = ""
    if data.get("SignKey") is not None:
        out["sign_key"] = data["SignKey"]
    return out
