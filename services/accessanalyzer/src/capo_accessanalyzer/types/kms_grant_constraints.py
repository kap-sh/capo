"""Generated from Smithy shape ``com.amazonaws.accessanalyzer#KmsGrantConstraints``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_accessanalyzer.types.kms_constraints_map


class KmsGrantConstraints(TypedDict, closed=True):
    encryption_context_equals: NotRequired[
        "capo_accessanalyzer.types.kms_constraints_map.KmsConstraintsMap"
    ]
    """<p>A list of key-value pairs that must match the encryption context in the <a href="https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#cryptographic-operations">cryptographic operation</a> request. The grant allows the operation only when the encryption context in the request is the same as the encryption context specified in this constraint.</p>"""
    encryption_context_subset: NotRequired[
        "capo_accessanalyzer.types.kms_constraints_map.KmsConstraintsMap"
    ]
    """<p>A list of key-value pairs that must be included in the encryption context of the <a href="https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#cryptographic-operations">cryptographic operation</a> request. The grant allows the cryptographic operation only when the encryption context in the request includes the key-value pairs specified in this constraint, although it can include additional key-value pairs.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: KmsGrantConstraints) -> dict:
    out: dict = {}
    if "encryption_context_equals" in value:
        import capo_accessanalyzer.types.kms_constraints_map

        out["encryptionContextEquals"] = (
            capo_accessanalyzer.types.kms_constraints_map.serialize_json(
                value["encryption_context_equals"]
            )
        )
    if "encryption_context_subset" in value:
        import capo_accessanalyzer.types.kms_constraints_map

        out["encryptionContextSubset"] = (
            capo_accessanalyzer.types.kms_constraints_map.serialize_json(
                value["encryption_context_subset"]
            )
        )
    return out


def deserialize_json(data: dict) -> KmsGrantConstraints:
    out: KmsGrantConstraints = {}  # type: ignore[typeddict-item]
    if data.get("encryptionContextEquals") is not None:
        import capo_accessanalyzer.types.kms_constraints_map

        out["encryption_context_equals"] = (
            capo_accessanalyzer.types.kms_constraints_map.deserialize_json(
                data["encryptionContextEquals"]
            )
        )
    if data.get("encryptionContextSubset") is not None:
        import capo_accessanalyzer.types.kms_constraints_map

        out["encryption_context_subset"] = (
            capo_accessanalyzer.types.kms_constraints_map.deserialize_json(
                data["encryptionContextSubset"]
            )
        )
    return out
