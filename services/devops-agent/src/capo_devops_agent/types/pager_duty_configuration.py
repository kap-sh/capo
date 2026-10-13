"""Generated from Smithy shape ``com.amazonaws.devopsagent#PagerDutyConfiguration``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

from capo_devops_agent.errors import DeserializationError

if TYPE_CHECKING:
    import capo_devops_agent.types.email_address
    import capo_devops_agent.types.pager_duty_services_list


class PagerDutyConfiguration(TypedDict, closed=True):
    services: "capo_devops_agent.types.pager_duty_services_list.PagerDutyServicesList"
    """<p>List of Pagerduty service available for the association.</p>"""
    customer_email: "capo_devops_agent.types.email_address.EmailAddress"
    """<p>Email to be used in Pagerduty API header</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PagerDutyConfiguration) -> dict:
    out: dict = {}
    import capo_devops_agent.types.pager_duty_services_list

    out["services"] = capo_devops_agent.types.pager_duty_services_list.serialize_json(
        value["services"]
    )
    out["customerEmail"] = value["customer_email"]
    return out


def deserialize_json(data: dict) -> PagerDutyConfiguration:
    out: PagerDutyConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("services") is not None:
        import capo_devops_agent.types.pager_duty_services_list

        out["services"] = (
            capo_devops_agent.types.pager_duty_services_list.deserialize_json(
                data["services"]
            )
        )
    else:
        raise DeserializationError("PagerDutyConfiguration.services required")
    if data.get("customerEmail") is not None:
        out["customer_email"] = data["customerEmail"]
    else:
        raise DeserializationError("PagerDutyConfiguration.customer_email required")
    return out


def redact_sensitive(value: PagerDutyConfiguration) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "customer_email" in value:
        out["customer_email"] = "*** Sensitive Data Redacted ***"
    return out
