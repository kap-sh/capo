"""Generated from Smithy shape ``com.amazonaws.marketplacemetering#RegisterUsageRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_marketplace_metering.types.nonce
    import capo_marketplace_metering.types.product_code
    import capo_marketplace_metering.types.version_integer


class RegisterUsageRequest(TypedDict, closed=True):
    product_code: "capo_marketplace_metering.types.product_code.ProductCode"
    """<p>Product code is used to uniquely identify a product in Amazon Web Services Marketplace. The product code should be the same as the one used during the publishing of a new product.</p>"""
    public_key_version: "capo_marketplace_metering.types.version_integer.VersionInteger"
    """<p>Public Key Version provided by Amazon Web Services Marketplace</p>"""
    nonce: NotRequired["capo_marketplace_metering.types.nonce.Nonce"]
    """<p>(Optional) To scope down the registration to a specific running software instance and guard against replay attacks.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RegisterUsageRequest) -> dict:
    out: dict = {}
    out["ProductCode"] = value["product_code"]
    out["PublicKeyVersion"] = value["public_key_version"]
    if "nonce" in value:
        out["Nonce"] = value["nonce"]
    return out


def deserialize_aws_json_1_1(data: dict) -> RegisterUsageRequest:
    out: RegisterUsageRequest = {}  # type: ignore[typeddict-item]
    if data.get("ProductCode") is not None:
        out["product_code"] = data["ProductCode"]
    else:
        out["product_code"] = ""
    if data.get("PublicKeyVersion") is not None:
        out["public_key_version"] = data["PublicKeyVersion"]
    else:
        out["public_key_version"] = 0
    if data.get("Nonce") is not None:
        out["nonce"] = data["Nonce"]
    return out
