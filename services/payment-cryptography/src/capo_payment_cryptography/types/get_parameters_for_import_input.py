"""Generated from Smithy shape ``com.amazonaws.paymentcryptography#GetParametersForImportInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_payment_cryptography.types.key_algorithm
    import capo_payment_cryptography.types.key_material_type


class GetParametersForImportInput(TypedDict, closed=True):
    key_material_type: (
        "capo_payment_cryptography.types.key_material_type.KeyMaterialType"
    )
    """<p>The method to use for key material import. Import token is only required for TR-34 WrappedKeyBlock (<code>TR34_KEY_BLOCK</code>) and RSA WrappedKeyCryptogram (<code>KEY_CRYPTOGRAM</code>).</p> <p>Import token is not required for TR-31, root public key cerificate or trusted public key certificate.</p>"""
    wrapping_key_algorithm: "capo_payment_cryptography.types.key_algorithm.KeyAlgorithm"
    """<p>The wrapping key algorithm to generate a wrapping key certificate. This certificate wraps the key under import.</p> <p>At this time, <code>RSA_2048</code> is the allowed algorithm for TR-34 WrappedKeyBlock import. Additionally, <code>RSA_2048</code>, <code>RSA_3072</code>, <code>RSA_4096</code> are the allowed algorithms for RSA WrappedKeyCryptogram import.</p>"""
    reuse_last_generated_token: NotRequired["bool"]
    """<p>Specifies whether to reuse the existing import token and wrapping key certificate. If set to <code>true</code> and a valid import token exists for the same key material type and wrapping key algorithm with at least 7 days of remaining validity, the existing token and wrapping key certificate are returned. Otherwise, a new import token and wrapping key certificate are generated. The default value is <code>false</code>, which generates a new import token and wrapping key certificate on every call.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetParametersForImportInput) -> dict:
    out: dict = {}
    out["KeyMaterialType"] = value["key_material_type"]
    out["WrappingKeyAlgorithm"] = value["wrapping_key_algorithm"]
    if "reuse_last_generated_token" in value:
        out["ReuseLastGeneratedToken"] = value["reuse_last_generated_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> GetParametersForImportInput:
    out: GetParametersForImportInput = {}  # type: ignore[typeddict-item]
    if data.get("KeyMaterialType") is not None:
        out["key_material_type"] = data["KeyMaterialType"]
    else:
        out["key_material_type"] = ""
    if data.get("WrappingKeyAlgorithm") is not None:
        out["wrapping_key_algorithm"] = data["WrappingKeyAlgorithm"]
    else:
        out["wrapping_key_algorithm"] = ""
    if data.get("ReuseLastGeneratedToken") is not None:
        out["reuse_last_generated_token"] = data["ReuseLastGeneratedToken"]
    return out
