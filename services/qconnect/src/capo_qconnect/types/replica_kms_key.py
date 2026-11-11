"""Generated from Smithy shape ``com.amazonaws.qconnect#ReplicaKmsKey``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_qconnect.types.non_empty_string


class ReplicaKmsKey(TypedDict, closed=True):
    arn: "capo_qconnect.types.non_empty_string.NonEmptyString"
    """<p>The Amazon Resource Name (ARN) of the KMS key in the replica Region.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ReplicaKmsKey) -> dict:
    out: dict = {}
    out["arn"] = value["arn"]
    return out


def deserialize_json(data: dict) -> ReplicaKmsKey:
    out: ReplicaKmsKey = {}  # type: ignore[typeddict-item]
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    else:
        out["arn"] = ""
    return out
