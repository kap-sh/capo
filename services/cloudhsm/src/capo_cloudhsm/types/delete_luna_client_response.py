"""Generated from Smithy shape ``com.amazonaws.cloudhsm#DeleteLunaClientResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_cloudhsm.types.string


class DeleteLunaClientResponse(TypedDict, closed=True):
    status: "capo_cloudhsm.types.string.String"
    """<p>The status of the action.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteLunaClientResponse) -> dict:
    out: dict = {}
    out["Status"] = value["status"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteLunaClientResponse:
    out: DeleteLunaClientResponse = {}  # type: ignore[typeddict-item]
    if data.get("Status") is not None:
        out["status"] = data["Status"]
    else:
        out["status"] = ""
    return out
