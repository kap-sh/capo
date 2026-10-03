"""Generated from Smithy shape ``com.amazonaws.kms#GenerateMacResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_kms.types.ciphertext_type
    import capo_kms.types.key_id_type
    import capo_kms.types.mac_algorithm_spec


class GenerateMacResponse(TypedDict, closed=True):
    mac: NotRequired["capo_kms.types.ciphertext_type.CiphertextType"]
    """<p>The hash-based message authentication code (HMAC) that was generated for the specified message, HMAC KMS key, and MAC algorithm.</p> <p>This is the standard, raw HMAC defined in <a href="https://datatracker.ietf.org/doc/html/rfc2104">RFC 2104</a>.</p>"""
    mac_algorithm: NotRequired["capo_kms.types.mac_algorithm_spec.MacAlgorithmSpec"]
    """<p>The MAC algorithm that was used to generate the HMAC.</p>"""
    key_id: NotRequired["capo_kms.types.key_id_type.KeyIdType"]
    """<p>The HMAC KMS key used in the operation.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GenerateMacResponse) -> dict:
    out: dict = {}
    if "mac" in value:
        import capo_kms.types.ciphertext_type

        out["Mac"] = capo_kms.types.ciphertext_type.serialize_aws_json_1_1(value["mac"])
    if "mac_algorithm" in value:
        import capo_kms.types.mac_algorithm_spec

        out["MacAlgorithm"] = capo_kms.types.mac_algorithm_spec.serialize_aws_json_1_1(
            value["mac_algorithm"]
        )
    if "key_id" in value:
        out["KeyId"] = value["key_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GenerateMacResponse:
    out: GenerateMacResponse = {}  # type: ignore[typeddict-item]
    if data.get("Mac") is not None:
        import capo_kms.types.ciphertext_type

        out["mac"] = capo_kms.types.ciphertext_type.deserialize_aws_json_1_1(
            data["Mac"]
        )
    if data.get("MacAlgorithm") is not None:
        import capo_kms.types.mac_algorithm_spec

        out["mac_algorithm"] = (
            capo_kms.types.mac_algorithm_spec.deserialize_aws_json_1_1(
                data["MacAlgorithm"]
            )
        )
    if data.get("KeyId") is not None:
        out["key_id"] = data["KeyId"]
    return out
