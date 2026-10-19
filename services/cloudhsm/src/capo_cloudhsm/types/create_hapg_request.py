"""Generated from Smithy shape ``com.amazonaws.cloudhsm#CreateHapgRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_cloudhsm.types.label


class CreateHapgRequest(TypedDict, closed=True):
    label: "capo_cloudhsm.types.label.Label"
    """<p>The label of the new high-availability partition group.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateHapgRequest) -> dict:
    out: dict = {}
    out["Label"] = value["label"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateHapgRequest:
    out: CreateHapgRequest = {}  # type: ignore[typeddict-item]
    if data.get("Label") is not None:
        out["label"] = data["Label"]
    else:
        out["label"] = ""
    return out
