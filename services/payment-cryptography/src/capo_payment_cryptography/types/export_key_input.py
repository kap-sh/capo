"""Generated from Smithy shape ``com.amazonaws.paymentcryptography#ExportKeyInput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_payment_cryptography.errors import DeserializationError

if TYPE_CHECKING:
    import capo_payment_cryptography.types.export_attributes
    import capo_payment_cryptography.types.export_key_material
    import capo_payment_cryptography.types.key_arn_or_key_alias_type


class ExportKeyInput(TypedDict, closed=True):
    key_material: (
        "capo_payment_cryptography.types.export_key_material.ExportKeyMaterial"
    )
    """<p>The key block format type, for example, TR-34 or TR-31, to use during key material export.</p>"""
    export_key_identifier: (
        "capo_payment_cryptography.types.key_arn_or_key_alias_type.KeyArnOrKeyAliasType"
    )
    """<p>The <code>KeyARN</code> of the key under export from Amazon Web Services Payment Cryptography.</p>"""
    export_attributes: NotRequired[
        "capo_payment_cryptography.types.export_attributes.ExportAttributes"
    ]
    """<p>The attributes for IPEK generation during export.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ExportKeyInput) -> dict:
    out: dict = {}
    import capo_payment_cryptography.types.export_key_material

    out["KeyMaterial"] = (
        capo_payment_cryptography.types.export_key_material.serialize_aws_json_1_0(
            value["key_material"]
        )
    )
    out["ExportKeyIdentifier"] = value["export_key_identifier"]
    if "export_attributes" in value:
        import capo_payment_cryptography.types.export_attributes

        out["ExportAttributes"] = (
            capo_payment_cryptography.types.export_attributes.serialize_aws_json_1_0(
                value["export_attributes"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> ExportKeyInput:
    out: ExportKeyInput = {}  # type: ignore[typeddict-item]
    if data.get("KeyMaterial") is not None:
        import capo_payment_cryptography.types.export_key_material

        out["key_material"] = (
            capo_payment_cryptography.types.export_key_material.deserialize_aws_json_1_0(
                data["KeyMaterial"]
            )
        )
    else:
        raise DeserializationError("ExportKeyInput.key_material required")
    if data.get("ExportKeyIdentifier") is not None:
        out["export_key_identifier"] = data["ExportKeyIdentifier"]
    else:
        raise DeserializationError("ExportKeyInput.export_key_identifier required")
    if data.get("ExportAttributes") is not None:
        import capo_payment_cryptography.types.export_attributes

        out["export_attributes"] = (
            capo_payment_cryptography.types.export_attributes.deserialize_aws_json_1_0(
                data["ExportAttributes"]
            )
        )
    return out


def redact_sensitive(value: ExportKeyInput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "key_material" in value:
        import capo_payment_cryptography.types.export_key_material

        out["key_material"] = (
            capo_payment_cryptography.types.export_key_material.redact_sensitive(
                value["key_material"]
            )
        )
    return out
