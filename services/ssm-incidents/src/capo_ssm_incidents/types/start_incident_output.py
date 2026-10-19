"""Generated from Smithy shape ``com.amazonaws.ssmincidents#StartIncidentOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_ssm_incidents.types.arn


class StartIncidentOutput(TypedDict, closed=True):
    incident_record_arn: "capo_ssm_incidents.types.arn.Arn"
    """<p>The ARN of the newly created incident record.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartIncidentOutput) -> dict:
    out: dict = {}
    out["incidentRecordArn"] = value["incident_record_arn"]
    return out


def deserialize_json(data: dict) -> StartIncidentOutput:
    out: StartIncidentOutput = {}  # type: ignore[typeddict-item]
    if data.get("incidentRecordArn") is not None:
        out["incident_record_arn"] = data["incidentRecordArn"]
    else:
        out["incident_record_arn"] = ""
    return out
