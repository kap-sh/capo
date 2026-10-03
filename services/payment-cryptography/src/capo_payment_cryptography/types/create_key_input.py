"""Generated from Smithy shape ``com.amazonaws.paymentcryptography#CreateKeyInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_payment_cryptography.errors import DeserializationError

if TYPE_CHECKING:
    import capo_payment_cryptography.types.derive_key_usage
    import capo_payment_cryptography.types.key_attributes
    import capo_payment_cryptography.types.key_check_value_algorithm
    import capo_payment_cryptography.types.regions
    import capo_payment_cryptography.types.tags


class CreateKeyInput(TypedDict, closed=True):
    key_attributes: "capo_payment_cryptography.types.key_attributes.KeyAttributes"
    """<p>The role of the key, the algorithm it supports, and the cryptographic operations allowed with the key. This data is immutable after the key is created.</p>"""
    key_check_value_algorithm: NotRequired[
        "capo_payment_cryptography.types.key_check_value_algorithm.KeyCheckValueAlgorithm"
    ]
    """<p>The algorithm that Amazon Web Services Payment Cryptography uses to calculate the key check value (KCV). It is used to validate the key integrity.</p> <p>For TDES keys, the KCV is computed by encrypting 8 bytes, each with value of zero, with the key to be checked and retaining the 3 highest order bytes of the encrypted result. For AES keys, the KCV is computed using a CMAC algorithm where the input data is 16 bytes of zero and retaining the 3 highest order bytes of the encrypted result. For HMAC keys, the KCV is computed using the hash selected at key creation on a zero-length message, taking the leftmost 3 bytes.</p>"""
    exportable: "bool"
    """<p>Specifies whether the key is exportable from the service.</p>"""
    enabled: NotRequired["bool"]
    """<p>Specifies whether to enable the key. If the key is enabled, it is activated for use within the service. If the key is not enabled, then it is created but not activated. The default value is enabled.</p>"""
    tags: NotRequired["capo_payment_cryptography.types.tags.Tags"]
    """<p>Assigns one or more tags to the Amazon Web Services Payment Cryptography key. Use this parameter to tag a key when it is created. To tag an existing Amazon Web Services Payment Cryptography key, use the <a href="https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_TagResource.html">TagResource</a> operation.</p> <p>Each tag consists of a tag key and a tag value. Both the tag key and the tag value are required, but the tag value can be an empty (null) string. You can't have more than one tag on an Amazon Web Services Payment Cryptography key with the same tag key. </p> <important> <p>Don't include personal, confidential or sensitive information in this field. This field may be displayed in plaintext in CloudTrail logs and other output.</p> </important> <note> <p>Tagging or untagging an Amazon Web Services Payment Cryptography key can allow or deny permission to the key.</p> </note>"""
    derive_key_usage: NotRequired[
        "capo_payment_cryptography.types.derive_key_usage.DeriveKeyUsage"
    ]
    """<p>The intended cryptographic usage of keys derived from the ECC key pair to be created.</p> <p>After creating an ECC key pair, you cannot change the intended cryptographic usage of keys derived from it using ECDH.</p>"""
    replication_regions: NotRequired["capo_payment_cryptography.types.regions.Regions"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CreateKeyInput) -> dict:
    out: dict = {}
    import capo_payment_cryptography.types.key_attributes

    out["KeyAttributes"] = (
        capo_payment_cryptography.types.key_attributes.serialize_aws_json_1_0(
            value["key_attributes"]
        )
    )
    if "key_check_value_algorithm" in value:
        out["KeyCheckValueAlgorithm"] = value["key_check_value_algorithm"]
    out["Exportable"] = value["exportable"]
    if "enabled" in value:
        out["Enabled"] = value["enabled"]
    if "tags" in value:
        import capo_payment_cryptography.types.tags

        out["Tags"] = capo_payment_cryptography.types.tags.serialize_aws_json_1_0(
            value["tags"]
        )
    if "derive_key_usage" in value:
        out["DeriveKeyUsage"] = value["derive_key_usage"]
    if "replication_regions" in value:
        import capo_payment_cryptography.types.regions

        out["ReplicationRegions"] = (
            capo_payment_cryptography.types.regions.serialize_aws_json_1_0(
                value["replication_regions"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> CreateKeyInput:
    out: CreateKeyInput = {}  # type: ignore[typeddict-item]
    if data.get("KeyAttributes") is not None:
        import capo_payment_cryptography.types.key_attributes

        out["key_attributes"] = (
            capo_payment_cryptography.types.key_attributes.deserialize_aws_json_1_0(
                data["KeyAttributes"]
            )
        )
    else:
        raise DeserializationError("CreateKeyInput.key_attributes required")
    if data.get("KeyCheckValueAlgorithm") is not None:
        out["key_check_value_algorithm"] = data["KeyCheckValueAlgorithm"]
    if data.get("Exportable") is not None:
        out["exportable"] = data["Exportable"]
    else:
        raise DeserializationError("CreateKeyInput.exportable required")
    if data.get("Enabled") is not None:
        out["enabled"] = data["Enabled"]
    if data.get("Tags") is not None:
        import capo_payment_cryptography.types.tags

        out["tags"] = capo_payment_cryptography.types.tags.deserialize_aws_json_1_0(
            data["Tags"]
        )
    if data.get("DeriveKeyUsage") is not None:
        out["derive_key_usage"] = data["DeriveKeyUsage"]
    if data.get("ReplicationRegions") is not None:
        import capo_payment_cryptography.types.regions

        out["replication_regions"] = (
            capo_payment_cryptography.types.regions.deserialize_aws_json_1_0(
                data["ReplicationRegions"]
            )
        )
    return out
