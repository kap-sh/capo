"""Generated from Smithy shape ``com.amazonaws.paymentcryptographydata#WrappedWorkingKey``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_payment_cryptography_data.types.key_check_value
    import capo_payment_cryptography_data.types.key_material
    import capo_payment_cryptography_data.types.wrapped_key_material_format


class WrappedWorkingKey(TypedDict, closed=True):
    wrapped_key_material: (
        "capo_payment_cryptography_data.types.key_material.KeyMaterial"
    )
    """<p>The wrapped key block of the outgoing transaction key.</p>"""
    key_check_value: (
        "capo_payment_cryptography_data.types.key_check_value.KeyCheckValue"
    )
    """<p>The key check value (KCV) of the key contained within the outgoing TR31WrappedKeyBlock.</p> <p> The KCV is used to check if all parties holding a given key have the same key or to detect that a key has changed. For more information on KCV, see <a href="https://docs.aws.amazon.com/payment-cryptography/latest/userguide/terminology.html#terms.kcv">KCV</a> in the <i>Amazon Web Services Payment Cryptography User Guide</i>.</p>"""
    wrapped_key_material_format: "capo_payment_cryptography_data.types.wrapped_key_material_format.WrappedKeyMaterialFormat"
    """<p>The key block format of the wrapped key.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: WrappedWorkingKey) -> dict:
    out: dict = {}
    out["WrappedKeyMaterial"] = value["wrapped_key_material"]
    out["KeyCheckValue"] = value["key_check_value"]
    out["WrappedKeyMaterialFormat"] = value["wrapped_key_material_format"]
    return out


def deserialize_json(data: dict) -> WrappedWorkingKey:
    out: WrappedWorkingKey = {}  # type: ignore[typeddict-item]
    if data.get("WrappedKeyMaterial") is not None:
        out["wrapped_key_material"] = data["WrappedKeyMaterial"]
    else:
        out["wrapped_key_material"] = ""
    if data.get("KeyCheckValue") is not None:
        out["key_check_value"] = data["KeyCheckValue"]
    else:
        out["key_check_value"] = ""
    if data.get("WrappedKeyMaterialFormat") is not None:
        out["wrapped_key_material_format"] = data["WrappedKeyMaterialFormat"]
    else:
        out["wrapped_key_material_format"] = ""
    return out


def redact_sensitive(value: WrappedWorkingKey) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "wrapped_key_material" in value:
        out["wrapped_key_material"] = "*** Sensitive Data Redacted ***"
    return out
