"""Generated from Smithy shape ``com.amazonaws.kms#GetParametersForImportResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_kms.types.ciphertext_type
    import capo_kms.types.date_type
    import capo_kms.types.key_id_type
    import capo_kms.types.plaintext_type


class GetParametersForImportResponse(TypedDict, closed=True):
    key_id: NotRequired["capo_kms.types.key_id_type.KeyIdType"]
    """<p>The Amazon Resource Name (<a href="https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#key-id-key-ARN">key ARN</a>) of the KMS key to use in a subsequent <a>ImportKeyMaterial</a> request. This is the same KMS key specified in the <code>GetParametersForImport</code> request.</p>"""
    import_token: NotRequired["capo_kms.types.ciphertext_type.CiphertextType"]
    """<p>The import token to send in a subsequent <a>ImportKeyMaterial</a> request.</p>"""
    public_key: NotRequired["capo_kms.types.plaintext_type.PlaintextType"]
    """<p>The public key to use to encrypt the key material before importing it with <a>ImportKeyMaterial</a>.</p>"""
    parameters_valid_to: NotRequired["capo_kms.types.date_type.DateType"]
    """<p>The time at which the import token and public key are no longer valid. After this time, you cannot use them to make an <a>ImportKeyMaterial</a> request and you must send another <code>GetParametersForImport</code> request to get new ones.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetParametersForImportResponse) -> dict:
    out: dict = {}
    if "key_id" in value:
        out["KeyId"] = value["key_id"]
    if "import_token" in value:
        import capo_kms.types.ciphertext_type

        out["ImportToken"] = capo_kms.types.ciphertext_type.serialize_aws_json_1_1(
            value["import_token"]
        )
    if "public_key" in value:
        import capo_kms.types.plaintext_type

        out["PublicKey"] = capo_kms.types.plaintext_type.serialize_aws_json_1_1(
            value["public_key"]
        )
    if "parameters_valid_to" in value:
        import capo_kms.types.date_type

        out["ParametersValidTo"] = capo_kms.types.date_type.serialize_aws_json_1_1(
            value["parameters_valid_to"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetParametersForImportResponse:
    out: GetParametersForImportResponse = {}  # type: ignore[typeddict-item]
    if data.get("KeyId") is not None:
        out["key_id"] = data["KeyId"]
    if data.get("ImportToken") is not None:
        import capo_kms.types.ciphertext_type

        out["import_token"] = capo_kms.types.ciphertext_type.deserialize_aws_json_1_1(
            data["ImportToken"]
        )
    if data.get("PublicKey") is not None:
        import capo_kms.types.plaintext_type

        out["public_key"] = capo_kms.types.plaintext_type.deserialize_aws_json_1_1(
            data["PublicKey"]
        )
    if data.get("ParametersValidTo") is not None:
        import capo_kms.types.date_type

        out["parameters_valid_to"] = capo_kms.types.date_type.deserialize_aws_json_1_1(
            data["ParametersValidTo"]
        )
    return out
