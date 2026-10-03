"""Generated from Smithy shape ``com.amazonaws.paymentcryptography#ImportKeyInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_payment_cryptography.errors import DeserializationError

if TYPE_CHECKING:
    import capo_payment_cryptography.types.import_key_material
    import capo_payment_cryptography.types.key_check_value_algorithm
    import capo_payment_cryptography.types.mpa_requester_comment
    import capo_payment_cryptography.types.regions
    import capo_payment_cryptography.types.tags


class ImportKeyInput(TypedDict, closed=True):
    key_material: (
        "capo_payment_cryptography.types.import_key_material.ImportKeyMaterial"
    )
    """<p>The key or public key certificate type to use during key material import, for example TR-34 or RootCertificatePublicKey.</p>"""
    key_check_value_algorithm: NotRequired[
        "capo_payment_cryptography.types.key_check_value_algorithm.KeyCheckValueAlgorithm"
    ]
    """<p>The algorithm that Amazon Web Services Payment Cryptography uses to calculate the key check value (KCV). It is used to validate the key integrity.</p> <p>For TDES keys, the KCV is computed by encrypting 8 bytes, each with value of zero, with the key to be checked and retaining the 3 highest order bytes of the encrypted result. For AES keys, the KCV is computed using a CMAC algorithm where the input data is 16 bytes of zero and retaining the 3 highest order bytes of the encrypted result. For HMAC keys, the KCV is computed using the hash selected at key creation on a zero-length message, taking the leftmost 3 bytes.</p>"""
    enabled: NotRequired["bool"]
    """<p>Specifies whether import key is enabled.</p>"""
    tags: NotRequired["capo_payment_cryptography.types.tags.Tags"]
    """<p>Assigns one or more tags to the Amazon Web Services Payment Cryptography key. Use this parameter to tag a key when it is imported. To tag an existing Amazon Web Services Payment Cryptography key, use the <a href="https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_TagResource.html">TagResource</a> operation.</p> <p>Each tag consists of a tag key and a tag value. Both the tag key and the tag value are required, but the tag value can be an empty (null) string. You can't have more than one tag on an Amazon Web Services Payment Cryptography key with the same tag key. If you specify an existing tag key with a different tag value, Amazon Web Services Payment Cryptography replaces the current tag value with the specified one.</p> <important> <p>Don't include personal, confidential or sensitive information in this field. This field may be displayed in plaintext in CloudTrail logs and other output.</p> </important> <note> <p>Tagging or untagging an Amazon Web Services Payment Cryptography key can allow or deny permission to the key.</p> </note>"""
    replication_regions: NotRequired["capo_payment_cryptography.types.regions.Regions"]
    requester_comment: NotRequired[
        "capo_payment_cryptography.types.mpa_requester_comment.MpaRequesterComment"
    ]
    """<p>The comment from the requester explaining the reason for the import.</p> <important> <p>Don't include personal, confidential or sensitive information in this field. This field may be displayed in plaintext in CloudTrail logs and other output.</p> </important>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ImportKeyInput) -> dict:
    out: dict = {}
    import capo_payment_cryptography.types.import_key_material

    out["KeyMaterial"] = (
        capo_payment_cryptography.types.import_key_material.serialize_aws_json_1_0(
            value["key_material"]
        )
    )
    if "key_check_value_algorithm" in value:
        out["KeyCheckValueAlgorithm"] = value["key_check_value_algorithm"]
    if "enabled" in value:
        out["Enabled"] = value["enabled"]
    if "tags" in value:
        import capo_payment_cryptography.types.tags

        out["Tags"] = capo_payment_cryptography.types.tags.serialize_aws_json_1_0(
            value["tags"]
        )
    if "replication_regions" in value:
        import capo_payment_cryptography.types.regions

        out["ReplicationRegions"] = (
            capo_payment_cryptography.types.regions.serialize_aws_json_1_0(
                value["replication_regions"]
            )
        )
    if "requester_comment" in value:
        out["RequesterComment"] = value["requester_comment"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ImportKeyInput:
    out: ImportKeyInput = {}  # type: ignore[typeddict-item]
    if data.get("KeyMaterial") is not None:
        import capo_payment_cryptography.types.import_key_material

        out["key_material"] = (
            capo_payment_cryptography.types.import_key_material.deserialize_aws_json_1_0(
                data["KeyMaterial"]
            )
        )
    else:
        raise DeserializationError("ImportKeyInput.key_material required")
    if data.get("KeyCheckValueAlgorithm") is not None:
        out["key_check_value_algorithm"] = data["KeyCheckValueAlgorithm"]
    if data.get("Enabled") is not None:
        out["enabled"] = data["Enabled"]
    if data.get("Tags") is not None:
        import capo_payment_cryptography.types.tags

        out["tags"] = capo_payment_cryptography.types.tags.deserialize_aws_json_1_0(
            data["Tags"]
        )
    if data.get("ReplicationRegions") is not None:
        import capo_payment_cryptography.types.regions

        out["replication_regions"] = (
            capo_payment_cryptography.types.regions.deserialize_aws_json_1_0(
                data["ReplicationRegions"]
            )
        )
    if data.get("RequesterComment") is not None:
        out["requester_comment"] = data["RequesterComment"]
    return out
