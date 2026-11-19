"""Generated from Smithy shape ``com.amazonaws.ec2#AssociatedKmsKey``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.string


class AssociatedKmsKey(TypedDict, closed=True):
    kms_key_id: NotRequired["capo_ec2.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the associated KMS key.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: AssociatedKmsKey, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "kms_key_id" in value:
        pairs.append((f"{key_prefix}KmsKeyId", str(value["kms_key_id"])))


def deserialize_ec2_query(el: Element) -> AssociatedKmsKey:
    out: AssociatedKmsKey = {}  # type: ignore[typeddict-item]
    child_kms_key_id = el.find("kmsKeyId")
    if child_kms_key_id is not None:
        out["kms_key_id"] = str(child_kms_key_id.text or "")
    return out
