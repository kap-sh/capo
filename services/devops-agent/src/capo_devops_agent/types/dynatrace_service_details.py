"""Generated from Smithy shape ``com.amazonaws.devopsagent#DynatraceServiceDetails``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_devops_agent.errors import DeserializationError

if TYPE_CHECKING:
    import capo_devops_agent.types.dynatrace_service_authorization_config


class DynatraceServiceDetails(TypedDict, closed=True):
    account_urn: "str"
    """<p>Dynatrace resource account urn.</p>"""
    authorization_config: NotRequired[
        "capo_devops_agent.types.dynatrace_service_authorization_config.DynatraceServiceAuthorizationConfig"
    ]
    """<p>Dynatrace OAuth client credentials configuration. Use this when registering with OAuth client credentials flow.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DynatraceServiceDetails) -> dict:
    out: dict = {}
    out["accountUrn"] = value["account_urn"]
    if "authorization_config" in value:
        import capo_devops_agent.types.dynatrace_service_authorization_config

        out["authorizationConfig"] = (
            capo_devops_agent.types.dynatrace_service_authorization_config.serialize_json(
                value["authorization_config"]
            )
        )
    return out


def deserialize_json(data: dict) -> DynatraceServiceDetails:
    out: DynatraceServiceDetails = {}  # type: ignore[typeddict-item]
    if data.get("accountUrn") is not None:
        out["account_urn"] = data["accountUrn"]
    else:
        raise DeserializationError("DynatraceServiceDetails.account_urn required")
    if data.get("authorizationConfig") is not None:
        import capo_devops_agent.types.dynatrace_service_authorization_config

        out["authorization_config"] = (
            capo_devops_agent.types.dynatrace_service_authorization_config.deserialize_json(
                data["authorizationConfig"]
            )
        )
    return out


def redact_sensitive(value: DynatraceServiceDetails) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "authorization_config" in value:
        out["authorization_config"] = "*** Sensitive Data Redacted ***"
    return out
