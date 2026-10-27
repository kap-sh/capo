"""Generated from Smithy shape ``com.amazonaws.kms#DecapsulateResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_kms.types.encapsulation_algorithm_spec
    import capo_kms.types.key_id_type
    import capo_kms.types.plaintext_type


class DecapsulateResponse(TypedDict, closed=True):
    key_id: NotRequired["capo_kms.types.key_id_type.KeyIdType"]
    """<p>The identifier of the ML-KEM KMS key used to decapsulate the shared secret.</p>"""
    shared_secret: NotRequired["capo_kms.types.plaintext_type.PlaintextType"]
    """<p>The plaintext shared secret recovered from the encapsulated form. It is a 32-byte value that matches the shared secret held by the encapsulating party. When you use the HTTP API or the Amazon Web Services CLI, the value is Base64-encoded. Otherwise, it is not Base64-encoded.</p>"""
    encapsulation_algorithm: NotRequired[
        "capo_kms.types.encapsulation_algorithm_spec.EncapsulationAlgorithmSpec"
    ]
    """<p>The key encapsulation algorithm used to recover the shared secret.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DecapsulateResponse) -> dict:
    out: dict = {}
    if "key_id" in value:
        out["KeyId"] = value["key_id"]
    if "shared_secret" in value:
        import capo_kms.types.plaintext_type

        out["SharedSecret"] = capo_kms.types.plaintext_type.serialize_aws_json_1_1(
            value["shared_secret"]
        )
    if "encapsulation_algorithm" in value:
        import capo_kms.types.encapsulation_algorithm_spec

        out["EncapsulationAlgorithm"] = (
            capo_kms.types.encapsulation_algorithm_spec.serialize_aws_json_1_1(
                value["encapsulation_algorithm"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DecapsulateResponse:
    out: DecapsulateResponse = {}  # type: ignore[typeddict-item]
    if data.get("KeyId") is not None:
        out["key_id"] = data["KeyId"]
    if data.get("SharedSecret") is not None:
        import capo_kms.types.plaintext_type

        out["shared_secret"] = capo_kms.types.plaintext_type.deserialize_aws_json_1_1(
            data["SharedSecret"]
        )
    if data.get("EncapsulationAlgorithm") is not None:
        import capo_kms.types.encapsulation_algorithm_spec

        out["encapsulation_algorithm"] = (
            capo_kms.types.encapsulation_algorithm_spec.deserialize_aws_json_1_1(
                data["EncapsulationAlgorithm"]
            )
        )
    return out


def redact_sensitive(value: DecapsulateResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "shared_secret" in value:
        out["shared_secret"] = "*** Sensitive Data Redacted ***"
    return out
