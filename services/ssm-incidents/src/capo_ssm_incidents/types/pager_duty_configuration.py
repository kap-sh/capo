"""Generated from Smithy shape ``com.amazonaws.ssmincidents#PagerDutyConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_ssm_incidents.errors import DeserializationError

if TYPE_CHECKING:
    import capo_ssm_incidents.types.pager_duty_incident_configuration


class PagerDutyConfiguration(TypedDict, closed=True):
    name: "str"
    """<p>The name of the PagerDuty configuration.</p>"""
    secret_id: "str"
    """<p>The ID of the Amazon Web Services Secrets Manager secret that stores your PagerDuty key, either a General Access REST API Key or User Token REST API Key, and other user credentials.</p>"""
    pager_duty_incident_configuration: "capo_ssm_incidents.types.pager_duty_incident_configuration.PagerDutyIncidentConfiguration"
    """<p>Details about the PagerDuty service associated with the configuration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PagerDutyConfiguration) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    out["secretId"] = value["secret_id"]
    import capo_ssm_incidents.types.pager_duty_incident_configuration

    out["pagerDutyIncidentConfiguration"] = (
        capo_ssm_incidents.types.pager_duty_incident_configuration.serialize_json(
            value["pager_duty_incident_configuration"]
        )
    )
    return out


def deserialize_json(data: dict) -> PagerDutyConfiguration:
    out: PagerDutyConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("secretId") is not None:
        out["secret_id"] = data["secretId"]
    else:
        out["secret_id"] = ""
    if data.get("pagerDutyIncidentConfiguration") is not None:
        import capo_ssm_incidents.types.pager_duty_incident_configuration

        out["pager_duty_incident_configuration"] = (
            capo_ssm_incidents.types.pager_duty_incident_configuration.deserialize_json(
                data["pagerDutyIncidentConfiguration"]
            )
        )
    else:
        raise DeserializationError(
            "PagerDutyConfiguration.pager_duty_incident_configuration required"
        )
    return out
