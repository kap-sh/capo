"""Generated from Smithy shape ``com.amazonaws.location#RouteMatrixEntryError``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_location.types.route_matrix_error_code


class RouteMatrixEntryError(TypedDict, closed=True):
    code: "capo_location.types.route_matrix_error_code.RouteMatrixErrorCode"
    """<p>The type of error which occurred for the route calculation.</p>"""
    message: NotRequired["str"]
    """<p>A message about the error that occurred for the route calculation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RouteMatrixEntryError) -> dict:
    out: dict = {}
    out["Code"] = value["code"]
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_json(data: dict) -> RouteMatrixEntryError:
    out: RouteMatrixEntryError = {}  # type: ignore[typeddict-item]
    if data.get("Code") is not None:
        out["code"] = data["Code"]
    else:
        out["code"] = ""
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    return out
