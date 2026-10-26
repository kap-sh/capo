"""Generated from Smithy shape ``com.amazonaws.paymentcryptographydata#TranslateKeyMaterialInput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_payment_cryptography_data.types.incoming_key_material
    import capo_payment_cryptography_data.types.key_check_value_algorithm
    import capo_payment_cryptography_data.types.outgoing_key_material


class TranslateKeyMaterialInput(TypedDict, closed=True):
    incoming_key_material: (
        "capo_payment_cryptography_data.types.incoming_key_material.IncomingKeyMaterial"
    )
    """<p>Parameter information of the TR31WrappedKeyBlock containing the transaction key.</p>"""
    outgoing_key_material: (
        "capo_payment_cryptography_data.types.outgoing_key_material.OutgoingKeyMaterial"
    )
    """<p>Parameter information of the wrapping key used to wrap the transaction key in the outgoing TR31WrappedKeyBlock.</p>"""
    key_check_value_algorithm: NotRequired[
        "capo_payment_cryptography_data.types.key_check_value_algorithm.KeyCheckValueAlgorithm"
    ]
    """<p>The key check value (KCV) algorithm used for calculating the KCV of the derived key.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TranslateKeyMaterialInput) -> dict:
    out: dict = {}
    import capo_payment_cryptography_data.types.incoming_key_material

    out["IncomingKeyMaterial"] = (
        capo_payment_cryptography_data.types.incoming_key_material.serialize_json(
            value["incoming_key_material"]
        )
    )
    import capo_payment_cryptography_data.types.outgoing_key_material

    out["OutgoingKeyMaterial"] = (
        capo_payment_cryptography_data.types.outgoing_key_material.serialize_json(
            value["outgoing_key_material"]
        )
    )
    if "key_check_value_algorithm" in value:
        out["KeyCheckValueAlgorithm"] = value["key_check_value_algorithm"]
    return out


def deserialize_json(data: dict) -> TranslateKeyMaterialInput:
    out: TranslateKeyMaterialInput = {}  # type: ignore[typeddict-item]
    if data.get("IncomingKeyMaterial") is not None:
        import capo_payment_cryptography_data.types.incoming_key_material

        out["incoming_key_material"] = (
            capo_payment_cryptography_data.types.incoming_key_material.deserialize_json(
                data["IncomingKeyMaterial"]
            )
        )
    else:
        out["incoming_key_material"] = {"$unknown": {"name": ""}}
    if data.get("OutgoingKeyMaterial") is not None:
        import capo_payment_cryptography_data.types.outgoing_key_material

        out["outgoing_key_material"] = (
            capo_payment_cryptography_data.types.outgoing_key_material.deserialize_json(
                data["OutgoingKeyMaterial"]
            )
        )
    else:
        out["outgoing_key_material"] = {"$unknown": {"name": ""}}
    if data.get("KeyCheckValueAlgorithm") is not None:
        out["key_check_value_algorithm"] = data["KeyCheckValueAlgorithm"]
    return out


def redact_sensitive(value: TranslateKeyMaterialInput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "incoming_key_material" in value:
        import capo_payment_cryptography_data.types.incoming_key_material

        out["incoming_key_material"] = (
            capo_payment_cryptography_data.types.incoming_key_material.redact_sensitive(
                value["incoming_key_material"]
            )
        )
    return out
