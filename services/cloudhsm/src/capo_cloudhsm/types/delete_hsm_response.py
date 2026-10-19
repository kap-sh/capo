"""Generated from Smithy shape ``com.amazonaws.cloudhsm#DeleteHsmResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_cloudhsm.types.string


class DeleteHsmResponse(TypedDict, closed=True):
    status: "capo_cloudhsm.types.string.String"
    """<p>The status of the operation.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteHsmResponse) -> dict:
    out: dict = {}
    out["Status"] = value["status"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteHsmResponse:
    out: DeleteHsmResponse = {}  # type: ignore[typeddict-item]
    if data.get("Status") is not None:
        out["status"] = data["Status"]
    else:
        out["status"] = ""
    return out
