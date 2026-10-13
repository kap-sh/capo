"""Generated from Smithy shape ``com.amazonaws.paymentcryptography#WrappedKey``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_payment_cryptography.errors import DeserializationError

if TYPE_CHECKING:
    import capo_payment_cryptography.types.key_arn
    import capo_payment_cryptography.types.key_check_value
    import capo_payment_cryptography.types.key_check_value_algorithm
    import capo_payment_cryptography.types.key_material
    import capo_payment_cryptography.types.wrapped_key_material_format


class WrappedKey(TypedDict, closed=True):
    wrapping_key_arn: "capo_payment_cryptography.types.key_arn.KeyArn"
    """<p>The <code>KeyARN</code> of the wrapped key.</p>"""
    wrapped_key_material_format: "capo_payment_cryptography.types.wrapped_key_material_format.WrappedKeyMaterialFormat"
    """<p>The key block format of a wrapped key.</p>"""
    key_material: "capo_payment_cryptography.types.key_material.KeyMaterial"
    """<p>Parameter information for generating a wrapped key using TR-31 or TR-34 skey exchange method.</p>"""
    key_check_value: NotRequired[
        "capo_payment_cryptography.types.key_check_value.KeyCheckValue"
    ]
    """<p>The key check value (KCV) is used to check if all parties holding a given key have the same key or to detect that a key has changed.</p>"""
    key_check_value_algorithm: NotRequired[
        "capo_payment_cryptography.types.key_check_value_algorithm.KeyCheckValueAlgorithm"
    ]
    """<p>The algorithm that Amazon Web Services Payment Cryptography uses to calculate the key check value (KCV). It is used to validate the key integrity.</p> <p>For TDES keys, the KCV is computed by encrypting 8 bytes, each with value of zero, with the key to be checked and retaining the 3 highest order bytes of the encrypted result. For AES keys, the KCV is computed using a CMAC algorithm where the input data is 16 bytes of zero and retaining the 3 highest order bytes of the encrypted result. For HMAC keys, the KCV is computed using the hash selected at key creation on a zero-length message, taking the leftmost 3 bytes.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: WrappedKey) -> dict:
    out: dict = {}
    out["WrappingKeyArn"] = value["wrapping_key_arn"]
    out["WrappedKeyMaterialFormat"] = value["wrapped_key_material_format"]
    out["KeyMaterial"] = value["key_material"]
    if "key_check_value" in value:
        out["KeyCheckValue"] = value["key_check_value"]
    if "key_check_value_algorithm" in value:
        out["KeyCheckValueAlgorithm"] = value["key_check_value_algorithm"]
    return out


def deserialize_aws_json_1_0(data: dict) -> WrappedKey:
    out: WrappedKey = {}  # type: ignore[typeddict-item]
    if data.get("WrappingKeyArn") is not None:
        out["wrapping_key_arn"] = data["WrappingKeyArn"]
    else:
        raise DeserializationError("WrappedKey.wrapping_key_arn required")
    if data.get("WrappedKeyMaterialFormat") is not None:
        out["wrapped_key_material_format"] = data["WrappedKeyMaterialFormat"]
    else:
        raise DeserializationError("WrappedKey.wrapped_key_material_format required")
    if data.get("KeyMaterial") is not None:
        out["key_material"] = data["KeyMaterial"]
    else:
        raise DeserializationError("WrappedKey.key_material required")
    if data.get("KeyCheckValue") is not None:
        out["key_check_value"] = data["KeyCheckValue"]
    if data.get("KeyCheckValueAlgorithm") is not None:
        out["key_check_value_algorithm"] = data["KeyCheckValueAlgorithm"]
    return out


def redact_sensitive(value: WrappedKey) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "key_material" in value:
        out["key_material"] = "*** Sensitive Data Redacted ***"
    return out
