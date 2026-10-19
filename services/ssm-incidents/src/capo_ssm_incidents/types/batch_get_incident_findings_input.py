"""Generated from Smithy shape ``com.amazonaws.ssmincidents#BatchGetIncidentFindingsInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_ssm_incidents.types.arn
    import capo_ssm_incidents.types.finding_id_list


class BatchGetIncidentFindingsInput(TypedDict, closed=True):
    incident_record_arn: "capo_ssm_incidents.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) of the incident for which you want to view finding details.</p>"""
    finding_ids: "capo_ssm_incidents.types.finding_id_list.FindingIdList"
    """<p>A list of IDs of findings for which you want to view details.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchGetIncidentFindingsInput) -> dict:
    out: dict = {}
    out["incidentRecordArn"] = value["incident_record_arn"]
    import capo_ssm_incidents.types.finding_id_list

    out["findingIds"] = capo_ssm_incidents.types.finding_id_list.serialize_json(
        value["finding_ids"]
    )
    return out


def deserialize_json(data: dict) -> BatchGetIncidentFindingsInput:
    out: BatchGetIncidentFindingsInput = {}  # type: ignore[typeddict-item]
    if data.get("incidentRecordArn") is not None:
        out["incident_record_arn"] = data["incidentRecordArn"]
    else:
        out["incident_record_arn"] = ""
    if data.get("findingIds") is not None:
        import capo_ssm_incidents.types.finding_id_list

        out["finding_ids"] = capo_ssm_incidents.types.finding_id_list.deserialize_json(
            data["findingIds"]
        )
    else:
        out["finding_ids"] = []
    return out
