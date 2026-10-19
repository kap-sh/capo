"""Generated from Smithy shape ``com.amazonaws.observabilityadmin#Encryption``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_observabilityadmin.types.resource_arn
    import capo_observabilityadmin.types.sse_algorithm


class Encryption(TypedDict, closed=True):
    sse_algorithm: "capo_observabilityadmin.types.sse_algorithm.SSEAlgorithm"
    """<p>The server-side encryption algorithm used for encrypting data in the S3 Table integration.</p>"""
    kms_key_arn: NotRequired["capo_observabilityadmin.types.resource_arn.ResourceArn"]
    """<p>The Amazon Resource Name (ARN) of the KMS key used for encryption when using customer-managed keys.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Encryption) -> dict:
    out: dict = {}
    import capo_observabilityadmin.types.sse_algorithm

    out["SseAlgorithm"] = capo_observabilityadmin.types.sse_algorithm.serialize_json(
        value["sse_algorithm"]
    )
    if "kms_key_arn" in value:
        out["KmsKeyArn"] = value["kms_key_arn"]
    return out


def deserialize_json(data: dict) -> Encryption:
    out: Encryption = {}  # type: ignore[typeddict-item]
    if data.get("SseAlgorithm") is not None:
        import capo_observabilityadmin.types.sse_algorithm

        out["sse_algorithm"] = (
            capo_observabilityadmin.types.sse_algorithm.deserialize_json(
                data["SseAlgorithm"]
            )
        )
    else:
        import typing

        out["sse_algorithm"] = typing.cast(
            "capo_observabilityadmin.types.sse_algorithm.SSEAlgorithm", ""
        )
    if data.get("KmsKeyArn") is not None:
        out["kms_key_arn"] = data["KmsKeyArn"]
    return out
