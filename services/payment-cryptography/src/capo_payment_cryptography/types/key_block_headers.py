"""Generated from Smithy shape ``com.amazonaws.paymentcryptography#KeyBlockHeaders``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_payment_cryptography.types.key_exportability
    import capo_payment_cryptography.types.key_modes_of_use
    import capo_payment_cryptography.types.key_version
    import capo_payment_cryptography.types.optional_blocks


class KeyBlockHeaders(TypedDict, closed=True):
    key_modes_of_use: NotRequired[
        "capo_payment_cryptography.types.key_modes_of_use.KeyModesOfUse"
    ]
    key_exportability: NotRequired[
        "capo_payment_cryptography.types.key_exportability.KeyExportability"
    ]
    """<p>Specifies subsequent exportability of the key within the key block after it is received by the receiving party. It can be used to further restrict exportability of the key after export from Amazon Web Services Payment Cryptography.</p> <p>When set to <code>EXPORTABLE</code>, the key can be subsequently exported by the receiver under a KEK using TR-31 or TR-34 key block export only. When set to <code>NON_EXPORTABLE</code>, the key cannot be subsequently exported by the receiver. When set to <code>SENSITIVE</code>, the key can be exported by the receiver under a KEK using TR-31, TR-34, RSA wrap and unwrap cryptogram or using a symmetric cryptogram key export method. For further information refer to <a href="https://webstore.ansi.org/standards/ascx9/ansix91432022">ANSI X9.143-2022</a>.</p>"""
    key_version: NotRequired["capo_payment_cryptography.types.key_version.KeyVersion"]
    """<p>Parameter used to indicate the version of the key carried in the key block or indicate the value carried in the key block is a component of a key.</p>"""
    optional_blocks: NotRequired[
        "capo_payment_cryptography.types.optional_blocks.OptionalBlocks"
    ]
    """<p>Parameter used to indicate the type of optional data in key block headers. Refer to <a href="https://webstore.ansi.org/standards/ascx9/ansix91432022">ANSI X9.143-2022</a> for information on allowed data type for optional blocks.</p> <p>Optional block character limit is 112 characters. For each optional block, 2 characters are reserved for optional block ID and 2 characters reserved for optional block length. More than one optional blocks can be included as long as the combined length does not increase 112 characters.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: KeyBlockHeaders) -> dict:
    out: dict = {}
    if "key_modes_of_use" in value:
        import capo_payment_cryptography.types.key_modes_of_use

        out["KeyModesOfUse"] = (
            capo_payment_cryptography.types.key_modes_of_use.serialize_aws_json_1_0(
                value["key_modes_of_use"]
            )
        )
    if "key_exportability" in value:
        out["KeyExportability"] = value["key_exportability"]
    if "key_version" in value:
        out["KeyVersion"] = value["key_version"]
    if "optional_blocks" in value:
        import capo_payment_cryptography.types.optional_blocks

        out["OptionalBlocks"] = (
            capo_payment_cryptography.types.optional_blocks.serialize_aws_json_1_0(
                value["optional_blocks"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> KeyBlockHeaders:
    out: KeyBlockHeaders = {}  # type: ignore[typeddict-item]
    if data.get("KeyModesOfUse") is not None:
        import capo_payment_cryptography.types.key_modes_of_use

        out["key_modes_of_use"] = (
            capo_payment_cryptography.types.key_modes_of_use.deserialize_aws_json_1_0(
                data["KeyModesOfUse"]
            )
        )
    if data.get("KeyExportability") is not None:
        out["key_exportability"] = data["KeyExportability"]
    if data.get("KeyVersion") is not None:
        out["key_version"] = data["KeyVersion"]
    if data.get("OptionalBlocks") is not None:
        import capo_payment_cryptography.types.optional_blocks

        out["optional_blocks"] = (
            capo_payment_cryptography.types.optional_blocks.deserialize_aws_json_1_0(
                data["OptionalBlocks"]
            )
        )
    return out
