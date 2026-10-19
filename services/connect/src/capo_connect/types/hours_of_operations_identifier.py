"""Generated from Smithy shape ``com.amazonaws.connect#HoursOfOperationsIdentifier``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connect.types.arn
    import capo_connect.types.common_name_length127
    import capo_connect.types.hours_of_operation_id


class HoursOfOperationsIdentifier(TypedDict, closed=True):
    name: "capo_connect.types.common_name_length127.CommonNameLength127"
    """<p>Name of the hours of operation</p>"""
    id: "capo_connect.types.hours_of_operation_id.HoursOfOperationId"
    """<p>Unique identifier of the hours of operation.</p>"""
    arn: NotRequired["capo_connect.types.arn.ARN"]
    """<p>Amazon Resource Name (ARN) of the hours of operations.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: HoursOfOperationsIdentifier) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    out["Id"] = value["id"]
    if "arn" in value:
        out["Arn"] = value["arn"]
    return out


def deserialize_json(data: dict) -> HoursOfOperationsIdentifier:
    out: HoursOfOperationsIdentifier = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        out["name"] = ""
    if data.get("Id") is not None:
        out["id"] = data["Id"]
    else:
        out["id"] = ""
    if data.get("Arn") is not None:
        out["arn"] = data["Arn"]
    return out
