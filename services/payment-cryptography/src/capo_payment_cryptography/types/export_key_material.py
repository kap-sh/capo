"""Generated from Smithy shape ``com.amazonaws.paymentcryptography#ExportKeyMaterial``."""

from typing import TYPE_CHECKING, Any, TypeAlias

from typing_extensions import TypedDict

from capo_payment_cryptography.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import capo_payment_cryptography.types.export_as2805_key_cryptogram
    import capo_payment_cryptography.types.export_diffie_hellman_tr31_key_block
    import capo_payment_cryptography.types.export_key_cryptogram
    import capo_payment_cryptography.types.export_tr31_key_block
    import capo_payment_cryptography.types.export_tr34_key_block


class _ExportKeyMaterial_Tr31KeyBlock(TypedDict, closed=True):
    Tr31KeyBlock: (
        "capo_payment_cryptography.types.export_tr31_key_block.ExportTr31KeyBlock"
    )


class _ExportKeyMaterial_Tr34KeyBlock(TypedDict, closed=True):
    Tr34KeyBlock: (
        "capo_payment_cryptography.types.export_tr34_key_block.ExportTr34KeyBlock"
    )


class _ExportKeyMaterial_KeyCryptogram(TypedDict, closed=True):
    KeyCryptogram: (
        "capo_payment_cryptography.types.export_key_cryptogram.ExportKeyCryptogram"
    )


class _ExportKeyMaterial_DiffieHellmanTr31KeyBlock(TypedDict, closed=True):
    DiffieHellmanTr31KeyBlock: "capo_payment_cryptography.types.export_diffie_hellman_tr31_key_block.ExportDiffieHellmanTr31KeyBlock"


class _ExportKeyMaterial_As2805KeyCryptogram(TypedDict, closed=True):
    As2805KeyCryptogram: "capo_payment_cryptography.types.export_as2805_key_cryptogram.ExportAs2805KeyCryptogram"


ExportKeyMaterial: TypeAlias = (
    _ExportKeyMaterial_Tr31KeyBlock
    | _ExportKeyMaterial_Tr34KeyBlock
    | _ExportKeyMaterial_KeyCryptogram
    | _ExportKeyMaterial_DiffieHellmanTr31KeyBlock
    | _ExportKeyMaterial_As2805KeyCryptogram
)


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ExportKeyMaterial) -> dict:
    if "Tr31KeyBlock" in value:
        import capo_payment_cryptography.types.export_tr31_key_block

        return {
            "Tr31KeyBlock": capo_payment_cryptography.types.export_tr31_key_block.serialize_aws_json_1_0(
                value["Tr31KeyBlock"]
            )
        }
    elif "Tr34KeyBlock" in value:
        import capo_payment_cryptography.types.export_tr34_key_block

        return {
            "Tr34KeyBlock": capo_payment_cryptography.types.export_tr34_key_block.serialize_aws_json_1_0(
                value["Tr34KeyBlock"]
            )
        }
    elif "KeyCryptogram" in value:
        import capo_payment_cryptography.types.export_key_cryptogram

        return {
            "KeyCryptogram": capo_payment_cryptography.types.export_key_cryptogram.serialize_aws_json_1_0(
                value["KeyCryptogram"]
            )
        }
    elif "DiffieHellmanTr31KeyBlock" in value:
        import capo_payment_cryptography.types.export_diffie_hellman_tr31_key_block

        return {
            "DiffieHellmanTr31KeyBlock": capo_payment_cryptography.types.export_diffie_hellman_tr31_key_block.serialize_aws_json_1_0(
                value["DiffieHellmanTr31KeyBlock"]
            )
        }
    elif "As2805KeyCryptogram" in value:
        import capo_payment_cryptography.types.export_as2805_key_cryptogram

        return {
            "As2805KeyCryptogram": capo_payment_cryptography.types.export_as2805_key_cryptogram.serialize_aws_json_1_0(
                value["As2805KeyCryptogram"]
            )
        }
    else:
        raise SerializationError("ExportKeyMaterial: no variant present")


def deserialize_aws_json_1_0(data: dict) -> ExportKeyMaterial:
    if data.get("Tr31KeyBlock") is not None:
        import capo_payment_cryptography.types.export_tr31_key_block

        return {
            "Tr31KeyBlock": capo_payment_cryptography.types.export_tr31_key_block.deserialize_aws_json_1_0(
                data["Tr31KeyBlock"]
            )
        }
    elif data.get("Tr34KeyBlock") is not None:
        import capo_payment_cryptography.types.export_tr34_key_block

        return {
            "Tr34KeyBlock": capo_payment_cryptography.types.export_tr34_key_block.deserialize_aws_json_1_0(
                data["Tr34KeyBlock"]
            )
        }
    elif data.get("KeyCryptogram") is not None:
        import capo_payment_cryptography.types.export_key_cryptogram

        return {
            "KeyCryptogram": capo_payment_cryptography.types.export_key_cryptogram.deserialize_aws_json_1_0(
                data["KeyCryptogram"]
            )
        }
    elif data.get("DiffieHellmanTr31KeyBlock") is not None:
        import capo_payment_cryptography.types.export_diffie_hellman_tr31_key_block

        return {
            "DiffieHellmanTr31KeyBlock": capo_payment_cryptography.types.export_diffie_hellman_tr31_key_block.deserialize_aws_json_1_0(
                data["DiffieHellmanTr31KeyBlock"]
            )
        }
    elif data.get("As2805KeyCryptogram") is not None:
        import capo_payment_cryptography.types.export_as2805_key_cryptogram

        return {
            "As2805KeyCryptogram": capo_payment_cryptography.types.export_as2805_key_cryptogram.deserialize_aws_json_1_0(
                data["As2805KeyCryptogram"]
            )
        }
    else:
        raise DeserializationError("ExportKeyMaterial: no recognized variant key")


def redact_sensitive(value: ExportKeyMaterial) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "Tr31KeyBlock" in value:
        import capo_payment_cryptography.types.export_tr31_key_block

        out["Tr31KeyBlock"] = (
            capo_payment_cryptography.types.export_tr31_key_block.redact_sensitive(
                value["Tr31KeyBlock"]
            )
        )
    if "Tr34KeyBlock" in value:
        import capo_payment_cryptography.types.export_tr34_key_block

        out["Tr34KeyBlock"] = (
            capo_payment_cryptography.types.export_tr34_key_block.redact_sensitive(
                value["Tr34KeyBlock"]
            )
        )
    if "DiffieHellmanTr31KeyBlock" in value:
        import capo_payment_cryptography.types.export_diffie_hellman_tr31_key_block

        out["DiffieHellmanTr31KeyBlock"] = (
            capo_payment_cryptography.types.export_diffie_hellman_tr31_key_block.redact_sensitive(
                value["DiffieHellmanTr31KeyBlock"]
            )
        )
    return out
