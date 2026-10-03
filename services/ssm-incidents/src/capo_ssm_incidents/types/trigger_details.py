"""Generated from Smithy shape ``com.amazonaws.ssmincidents#TriggerDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ssm_incidents.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import capo_ssm_incidents.types.arn
    import capo_ssm_incidents.types.incident_source
    import capo_ssm_incidents.types.raw_data


class TriggerDetails(TypedDict, closed=True):
    source: "capo_ssm_incidents.types.incident_source.IncidentSource"
    """<p>Identifies the service that sourced the event. All events sourced from within Amazon Web Services begin with "<code>aws.</code>" Customer-generated events can have any value here, as long as it doesn't begin with "<code>aws.</code>" We recommend the use of Java package-name style reverse domain-name strings. </p>"""
    trigger_arn: NotRequired["capo_ssm_incidents.types.arn.Arn"]
    """<p>The Amazon Resource Name (ARN) of the source that detected the incident.</p>"""
    timestamp: "datetime.datetime"
    """<p>The timestamp for when the incident was detected.</p>"""
    raw_data: NotRequired["capo_ssm_incidents.types.raw_data.RawData"]
    """<p>Raw data passed from either Amazon EventBridge, Amazon CloudWatch, or Incident Manager when an incident is created.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TriggerDetails) -> dict:
    out: dict = {}
    out["source"] = value["source"]
    if "trigger_arn" in value:
        out["triggerArn"] = value["trigger_arn"]
    import capo_ssm_incidents.types._prelude.timestamp

    out["timestamp"] = capo_ssm_incidents.types._prelude.timestamp.serialize_json(
        value["timestamp"]
    )
    if "raw_data" in value:
        out["rawData"] = value["raw_data"]
    return out


def deserialize_json(data: dict) -> TriggerDetails:
    out: TriggerDetails = {}  # type: ignore[typeddict-item]
    if data.get("source") is not None:
        out["source"] = data["source"]
    else:
        raise DeserializationError("TriggerDetails.source required")
    if data.get("triggerArn") is not None:
        out["trigger_arn"] = data["triggerArn"]
    if data.get("timestamp") is not None:
        import capo_ssm_incidents.types._prelude.timestamp

        out["timestamp"] = capo_ssm_incidents.types._prelude.timestamp.deserialize_json(
            data["timestamp"]
        )
    else:
        raise DeserializationError("TriggerDetails.timestamp required")
    if data.get("rawData") is not None:
        out["raw_data"] = data["rawData"]
    return out
