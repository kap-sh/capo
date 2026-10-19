"""Generated from Smithy shape ``com.amazonaws.signer#SigningMaterial``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_signer.types.certificate_arn


class SigningMaterial(TypedDict, closed=True):
    certificate_arn: "capo_signer.types.certificate_arn.CertificateArn"
    """<p>The Amazon Resource Name (ARN) of the certificates that is used to sign your code.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SigningMaterial) -> dict:
    out: dict = {}
    out["certificateArn"] = value["certificate_arn"]
    return out


def deserialize_json(data: dict) -> SigningMaterial:
    out: SigningMaterial = {}  # type: ignore[typeddict-item]
    if data.get("certificateArn") is not None:
        out["certificate_arn"] = data["certificateArn"]
    else:
        out["certificate_arn"] = ""
    return out
