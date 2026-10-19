"""Generated from Smithy shape ``com.amazonaws.signer#HashAlgorithmOptions``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_signer.types.hash_algorithm
    import capo_signer.types.hash_algorithms


class HashAlgorithmOptions(TypedDict, closed=True):
    allowed_values: "capo_signer.types.hash_algorithms.HashAlgorithms"
    """<p>The set of accepted hash algorithms allowed in a code-signing job.</p>"""
    default_value: "capo_signer.types.hash_algorithm.HashAlgorithm"
    """<p>The default hash algorithm that is used in a code-signing job.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: HashAlgorithmOptions) -> dict:
    out: dict = {}
    import capo_signer.types.hash_algorithms

    out["allowedValues"] = capo_signer.types.hash_algorithms.serialize_json(
        value["allowed_values"]
    )
    import capo_signer.types.hash_algorithm

    out["defaultValue"] = capo_signer.types.hash_algorithm.serialize_json(
        value["default_value"]
    )
    return out


def deserialize_json(data: dict) -> HashAlgorithmOptions:
    out: HashAlgorithmOptions = {}  # type: ignore[typeddict-item]
    if data.get("allowedValues") is not None:
        import capo_signer.types.hash_algorithms

        out["allowed_values"] = capo_signer.types.hash_algorithms.deserialize_json(
            data["allowedValues"]
        )
    else:
        out["allowed_values"] = []
    if data.get("defaultValue") is not None:
        import capo_signer.types.hash_algorithm

        out["default_value"] = capo_signer.types.hash_algorithm.deserialize_json(
            data["defaultValue"]
        )
    else:
        import typing

        out["default_value"] = typing.cast(
            "capo_signer.types.hash_algorithm.HashAlgorithm", ""
        )
    return out
