"""Generated from Smithy shape ``com.amazonaws.sqs#ChangeMessageVisibilityBatchResultEntry``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_sqs.types.string


class ChangeMessageVisibilityBatchResultEntry(TypedDict, closed=True):
    id: "capo_sqs.types.string.String"
    """<p>Represents a message whose visibility timeout has been changed successfully.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ChangeMessageVisibilityBatchResultEntry) -> dict:
    out: dict = {}
    out["Id"] = value["id"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ChangeMessageVisibilityBatchResultEntry:
    out: ChangeMessageVisibilityBatchResultEntry = {}  # type: ignore[typeddict-item]
    if data.get("Id") is not None:
        out["id"] = data["Id"]
    else:
        out["id"] = ""
    return out
