"""Generated from Smithy shape ``com.amazonaws.devopsagent#ServiceNowServiceDetails``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_devops_agent.errors import DeserializationError

if TYPE_CHECKING:
    import capo_devops_agent.types.service_now_instance_url
    import capo_devops_agent.types.service_now_service_authorization_config


class ServiceNowServiceDetails(TypedDict, closed=True):
    instance_url: (
        "capo_devops_agent.types.service_now_instance_url.ServiceNowInstanceUrl"
    )
    """<p>ServiceNow instance URL.</p>"""
    authorization_config: NotRequired[
        "capo_devops_agent.types.service_now_service_authorization_config.ServiceNowServiceAuthorizationConfig"
    ]
    """<p>ServiceNow OAuth client credentials configuration. Use this when registering with OAuth client credentials flow.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ServiceNowServiceDetails) -> dict:
    out: dict = {}
    out["instanceUrl"] = value["instance_url"]
    if "authorization_config" in value:
        import capo_devops_agent.types.service_now_service_authorization_config

        out["authorizationConfig"] = (
            capo_devops_agent.types.service_now_service_authorization_config.serialize_json(
                value["authorization_config"]
            )
        )
    return out


def deserialize_json(data: dict) -> ServiceNowServiceDetails:
    out: ServiceNowServiceDetails = {}  # type: ignore[typeddict-item]
    if data.get("instanceUrl") is not None:
        out["instance_url"] = data["instanceUrl"]
    else:
        raise DeserializationError("ServiceNowServiceDetails.instance_url required")
    if data.get("authorizationConfig") is not None:
        import capo_devops_agent.types.service_now_service_authorization_config

        out["authorization_config"] = (
            capo_devops_agent.types.service_now_service_authorization_config.deserialize_json(
                data["authorizationConfig"]
            )
        )
    return out


def redact_sensitive(value: ServiceNowServiceDetails) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "authorization_config" in value:
        import capo_devops_agent.types.service_now_service_authorization_config

        out["authorization_config"] = (
            capo_devops_agent.types.service_now_service_authorization_config.redact_sensitive(
                value["authorization_config"]
            )
        )
    return out
