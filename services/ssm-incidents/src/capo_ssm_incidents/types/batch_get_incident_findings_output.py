"""Generated from Smithy shape ``com.amazonaws.ssmincidents#BatchGetIncidentFindingsOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_ssm_incidents.types.batch_get_incident_findings_error_list
    import capo_ssm_incidents.types.finding_list


class BatchGetIncidentFindingsOutput(TypedDict, closed=True):
    findings: "capo_ssm_incidents.types.finding_list.FindingList"
    """<p>Information about the requested findings.</p>"""
    errors: "capo_ssm_incidents.types.batch_get_incident_findings_error_list.BatchGetIncidentFindingsErrorList"
    """<p>A list of errors encountered during the operation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchGetIncidentFindingsOutput) -> dict:
    out: dict = {}
    import capo_ssm_incidents.types.finding_list

    out["findings"] = capo_ssm_incidents.types.finding_list.serialize_json(
        value["findings"]
    )
    import capo_ssm_incidents.types.batch_get_incident_findings_error_list

    out["errors"] = (
        capo_ssm_incidents.types.batch_get_incident_findings_error_list.serialize_json(
            value["errors"]
        )
    )
    return out


def deserialize_json(data: dict) -> BatchGetIncidentFindingsOutput:
    out: BatchGetIncidentFindingsOutput = {}  # type: ignore[typeddict-item]
    if data.get("findings") is not None:
        import capo_ssm_incidents.types.finding_list

        out["findings"] = capo_ssm_incidents.types.finding_list.deserialize_json(
            data["findings"]
        )
    else:
        out["findings"] = []
    if data.get("errors") is not None:
        import capo_ssm_incidents.types.batch_get_incident_findings_error_list

        out["errors"] = (
            capo_ssm_incidents.types.batch_get_incident_findings_error_list.deserialize_json(
                data["errors"]
            )
        )
    else:
        out["errors"] = []
    return out
