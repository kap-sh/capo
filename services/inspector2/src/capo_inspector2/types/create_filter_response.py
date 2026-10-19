"""Generated from Smithy shape ``com.amazonaws.inspector2#CreateFilterResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_inspector2.types.filter_arn


class CreateFilterResponse(TypedDict, closed=True):
    arn: "capo_inspector2.types.filter_arn.FilterArn"
    """<p>The Amazon Resource Number (ARN) of the successfully created filter.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateFilterResponse) -> dict:
    out: dict = {}
    out["arn"] = value["arn"]
    return out


def deserialize_json(data: dict) -> CreateFilterResponse:
    out: CreateFilterResponse = {}  # type: ignore[typeddict-item]
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    else:
        out["arn"] = ""
    return out
