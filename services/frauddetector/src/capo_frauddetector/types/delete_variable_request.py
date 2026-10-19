"""Generated from Smithy shape ``com.amazonaws.frauddetector#DeleteVariableRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_frauddetector.types.string


class DeleteVariableRequest(TypedDict, closed=True):
    name: "capo_frauddetector.types.string.string"
    """<p>The name of the variable to delete.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteVariableRequest) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteVariableRequest:
    out: DeleteVariableRequest = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    return out
