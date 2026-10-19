"""Generated from Smithy shape ``com.amazonaws.ssmincidents#DeleteIncidentRecordInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_ssm_incidents.types.arn


class DeleteIncidentRecordInput(TypedDict, closed=True):
    arn: "capo_ssm_incidents.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) of the incident record you are deleting.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteIncidentRecordInput) -> dict:
    out: dict = {}
    out["arn"] = value["arn"]
    return out


def deserialize_json(data: dict) -> DeleteIncidentRecordInput:
    out: DeleteIncidentRecordInput = {}  # type: ignore[typeddict-item]
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    else:
        out["arn"] = ""
    return out
