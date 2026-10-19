"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#CreateInputSourceResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_resiliencehubv2.types.arn
    import capo_resiliencehubv2.types.input_source_id


class CreateInputSourceResponse(TypedDict, closed=True):
    service_arn: "capo_resiliencehubv2.types.arn.Arn"
    input_source_id: "capo_resiliencehubv2.types.input_source_id.InputSourceId"
    """<p>The unique identifier assigned to the created input source.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateInputSourceResponse) -> dict:
    out: dict = {}
    out["serviceArn"] = value["service_arn"]
    out["inputSourceId"] = value["input_source_id"]
    return out


def deserialize_json(data: dict) -> CreateInputSourceResponse:
    out: CreateInputSourceResponse = {}  # type: ignore[typeddict-item]
    if data.get("serviceArn") is not None:
        out["service_arn"] = data["serviceArn"]
    else:
        out["service_arn"] = ""
    if data.get("inputSourceId") is not None:
        out["input_source_id"] = data["inputSourceId"]
    else:
        out["input_source_id"] = ""
    return out
