"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#DeleteTestResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_resiliencehubv2.types.test_id


class DeleteTestResponse(TypedDict, closed=True):
    test_id: "capo_resiliencehubv2.types.test_id.TestId"
    """<p>The identifier of the deleted test.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteTestResponse) -> dict:
    out: dict = {}
    out["testId"] = value["test_id"]
    return out


def deserialize_json(data: dict) -> DeleteTestResponse:
    out: DeleteTestResponse = {}  # type: ignore[typeddict-item]
    if data.get("testId") is not None:
        out["test_id"] = data["testId"]
    else:
        out["test_id"] = ""
    return out
