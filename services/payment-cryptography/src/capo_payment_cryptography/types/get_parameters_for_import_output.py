"""Generated from Smithy shape ``com.amazonaws.paymentcryptography#GetParametersForImportOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_payment_cryptography.types.certificate_type
    import capo_payment_cryptography.types.import_token_id
    import capo_payment_cryptography.types.key_algorithm
    import capo_payment_cryptography.types.timestamp


class GetParametersForImportOutput(TypedDict, closed=True):
    wrapping_key_certificate: (
        "capo_payment_cryptography.types.certificate_type.CertificateType"
    )
    """<p>The wrapping key certificate in PEM format (base64 encoded) of the wrapping key for use within the TR-34 key block. The certificate expires in 30 days.</p>"""
    wrapping_key_certificate_chain: (
        "capo_payment_cryptography.types.certificate_type.CertificateType"
    )
    """<p>The Amazon Web Services Payment Cryptography root certificate authority (CA) that signed the wrapping key certificate in PEM format (base64 encoded).</p>"""
    wrapping_key_algorithm: "capo_payment_cryptography.types.key_algorithm.KeyAlgorithm"
    """<p>The algorithm of the wrapping key for use within TR-34 WrappedKeyBlock or RSA WrappedKeyCryptogram.</p>"""
    import_token: "capo_payment_cryptography.types.import_token_id.ImportTokenId"
    """<p>The import token to initiate key import into Amazon Web Services Payment Cryptography. The import token expires after 30 days. You can use the same import token to import multiple keys to the same service account.</p>"""
    parameters_valid_until_timestamp: (
        "capo_payment_cryptography.types.timestamp.Timestamp"
    )
    """<p>The validity period of the import token.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetParametersForImportOutput) -> dict:
    out: dict = {}
    out["WrappingKeyCertificate"] = value["wrapping_key_certificate"]
    out["WrappingKeyCertificateChain"] = value["wrapping_key_certificate_chain"]
    out["WrappingKeyAlgorithm"] = value["wrapping_key_algorithm"]
    out["ImportToken"] = value["import_token"]
    import capo_payment_cryptography.types.timestamp

    out["ParametersValidUntilTimestamp"] = (
        capo_payment_cryptography.types.timestamp.serialize_aws_json_1_0(
            value["parameters_valid_until_timestamp"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> GetParametersForImportOutput:
    out: GetParametersForImportOutput = {}  # type: ignore[typeddict-item]
    if data.get("WrappingKeyCertificate") is not None:
        out["wrapping_key_certificate"] = data["WrappingKeyCertificate"]
    else:
        out["wrapping_key_certificate"] = ""
    if data.get("WrappingKeyCertificateChain") is not None:
        out["wrapping_key_certificate_chain"] = data["WrappingKeyCertificateChain"]
    else:
        out["wrapping_key_certificate_chain"] = ""
    if data.get("WrappingKeyAlgorithm") is not None:
        out["wrapping_key_algorithm"] = data["WrappingKeyAlgorithm"]
    else:
        out["wrapping_key_algorithm"] = ""
    if data.get("ImportToken") is not None:
        out["import_token"] = data["ImportToken"]
    else:
        out["import_token"] = ""
    if data.get("ParametersValidUntilTimestamp") is not None:
        import capo_payment_cryptography.types.timestamp

        out["parameters_valid_until_timestamp"] = (
            capo_payment_cryptography.types.timestamp.deserialize_aws_json_1_0(
                data["ParametersValidUntilTimestamp"]
            )
        )
    else:
        import datetime

        out["parameters_valid_until_timestamp"] = datetime.datetime.fromtimestamp(
            0, tz=datetime.timezone.utc
        )
    return out
