"""Generated from Smithy shape ``com.amazonaws.ssmincidents#IncidentRecordSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ssm_incidents.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import capo_ssm_incidents.types.arn
    import capo_ssm_incidents.types.impact
    import capo_ssm_incidents.types.incident_record_source
    import capo_ssm_incidents.types.incident_record_status
    import capo_ssm_incidents.types.incident_title


class IncidentRecordSummary(TypedDict, closed=True):
    arn: "capo_ssm_incidents.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) of the incident.</p>"""
    title: "capo_ssm_incidents.types.incident_title.IncidentTitle"
    """<p>The title of the incident. This value is either provided by the response plan or overwritten on creation.</p>"""
    status: "capo_ssm_incidents.types.incident_record_status.IncidentRecordStatus"
    """<p>The current status of the incident.</p>"""
    impact: "capo_ssm_incidents.types.impact.Impact"
    """<p>Defines the impact to customers and applications.</p>"""
    creation_time: "datetime.datetime"
    """<p>The timestamp for when the incident was created.</p>"""
    resolved_time: NotRequired["datetime.datetime"]
    """<p>The timestamp for when the incident was resolved.</p>"""
    incident_record_source: (
        "capo_ssm_incidents.types.incident_record_source.IncidentRecordSource"
    )
    """<p>What caused Incident Manager to create the incident.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: IncidentRecordSummary) -> dict:
    out: dict = {}
    out["arn"] = value["arn"]
    out["title"] = value["title"]
    out["status"] = value["status"]
    out["impact"] = value["impact"]
    import capo_ssm_incidents.types._prelude.timestamp

    out["creationTime"] = capo_ssm_incidents.types._prelude.timestamp.serialize_json(
        value["creation_time"]
    )
    if "resolved_time" in value:
        import capo_ssm_incidents.types._prelude.timestamp

        out["resolvedTime"] = (
            capo_ssm_incidents.types._prelude.timestamp.serialize_json(
                value["resolved_time"]
            )
        )
    import capo_ssm_incidents.types.incident_record_source

    out["incidentRecordSource"] = (
        capo_ssm_incidents.types.incident_record_source.serialize_json(
            value["incident_record_source"]
        )
    )
    return out


def deserialize_json(data: dict) -> IncidentRecordSummary:
    out: IncidentRecordSummary = {}  # type: ignore[typeddict-item]
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    else:
        out["arn"] = ""
    if data.get("title") is not None:
        out["title"] = data["title"]
    else:
        out["title"] = ""
    if data.get("status") is not None:
        out["status"] = data["status"]
    else:
        out["status"] = ""
    if data.get("impact") is not None:
        out["impact"] = data["impact"]
    else:
        out["impact"] = 0
    if data.get("creationTime") is not None:
        import capo_ssm_incidents.types._prelude.timestamp

        out["creation_time"] = (
            capo_ssm_incidents.types._prelude.timestamp.deserialize_json(
                data["creationTime"]
            )
        )
    else:
        import datetime

        out["creation_time"] = datetime.datetime.fromtimestamp(
            0, tz=datetime.timezone.utc
        )
    if data.get("resolvedTime") is not None:
        import capo_ssm_incidents.types._prelude.timestamp

        out["resolved_time"] = (
            capo_ssm_incidents.types._prelude.timestamp.deserialize_json(
                data["resolvedTime"]
            )
        )
    if data.get("incidentRecordSource") is not None:
        import capo_ssm_incidents.types.incident_record_source

        out["incident_record_source"] = (
            capo_ssm_incidents.types.incident_record_source.deserialize_json(
                data["incidentRecordSource"]
            )
        )
    else:
        raise DeserializationError(
            "IncidentRecordSummary.incident_record_source required"
        )
    return out
