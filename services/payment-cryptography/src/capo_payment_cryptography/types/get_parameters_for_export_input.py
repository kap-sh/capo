"""Generated from Smithy shape ``com.amazonaws.paymentcryptography#GetParametersForExportInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_payment_cryptography.types.key_algorithm
    import capo_payment_cryptography.types.key_material_type


class GetParametersForExportInput(TypedDict, closed=True):
    key_material_type: (
        "capo_payment_cryptography.types.key_material_type.KeyMaterialType"
    )
    """<p>The key block format type (for example, TR-34 or TR-31) to use during key material export. Export token is only required for a TR-34 key export, <code>TR34_KEY_BLOCK</code>. Export token is not required for TR-31 key export.</p>"""
    signing_key_algorithm: "capo_payment_cryptography.types.key_algorithm.KeyAlgorithm"
    """<p>The signing key algorithm to generate a signing key certificate. This certificate signs the wrapped key under export within the TR-34 key block. <code>RSA_2048</code> is the only signing key algorithm allowed.</p>"""
    reuse_last_generated_token: NotRequired["bool"]
    """<p>Specifies whether to reuse the existing export token and signing key certificate. If set to <code>true</code> and a valid export token exists for the same key material type and signing key algorithm with at least 7 days of remaining validity, the existing token and signing key certificate are returned. Otherwise, a new export token and signing key certificate are generated. The default value is <code>false</code>, which generates a new export token and signing key certificate on every call.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetParametersForExportInput) -> dict:
    out: dict = {}
    out["KeyMaterialType"] = value["key_material_type"]
    out["SigningKeyAlgorithm"] = value["signing_key_algorithm"]
    if "reuse_last_generated_token" in value:
        out["ReuseLastGeneratedToken"] = value["reuse_last_generated_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> GetParametersForExportInput:
    out: GetParametersForExportInput = {}  # type: ignore[typeddict-item]
    if data.get("KeyMaterialType") is not None:
        out["key_material_type"] = data["KeyMaterialType"]
    else:
        out["key_material_type"] = ""
    if data.get("SigningKeyAlgorithm") is not None:
        out["signing_key_algorithm"] = data["SigningKeyAlgorithm"]
    else:
        out["signing_key_algorithm"] = ""
    if data.get("ReuseLastGeneratedToken") is not None:
        out["reuse_last_generated_token"] = data["ReuseLastGeneratedToken"]
    return out
