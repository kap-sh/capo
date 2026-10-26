"""Generated from Smithy shape ``com.amazonaws.devopsagent#PagerDutyDetails``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_devops_agent.types.pager_duty_authorization_config
    import capo_devops_agent.types.pager_duty_scopes


class PagerDutyDetails(TypedDict, closed=True):
    scopes: "capo_devops_agent.types.pager_duty_scopes.PagerDutyScopes"
    """<p>PagerDuty scopes.</p>"""
    authorization_config: "capo_devops_agent.types.pager_duty_authorization_config.PagerDutyAuthorizationConfig"
    """<p>PagerDuty authorization configuration</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PagerDutyDetails) -> dict:
    out: dict = {}
    import capo_devops_agent.types.pager_duty_scopes

    out["scopes"] = capo_devops_agent.types.pager_duty_scopes.serialize_json(
        value["scopes"]
    )
    import capo_devops_agent.types.pager_duty_authorization_config

    out["authorizationConfig"] = (
        capo_devops_agent.types.pager_duty_authorization_config.serialize_json(
            value["authorization_config"]
        )
    )
    return out


def deserialize_json(data: dict) -> PagerDutyDetails:
    out: PagerDutyDetails = {}  # type: ignore[typeddict-item]
    if data.get("scopes") is not None:
        import capo_devops_agent.types.pager_duty_scopes

        out["scopes"] = capo_devops_agent.types.pager_duty_scopes.deserialize_json(
            data["scopes"]
        )
    else:
        out["scopes"] = []
    if data.get("authorizationConfig") is not None:
        import capo_devops_agent.types.pager_duty_authorization_config

        out["authorization_config"] = (
            capo_devops_agent.types.pager_duty_authorization_config.deserialize_json(
                data["authorizationConfig"]
            )
        )
    else:
        out["authorization_config"] = {"$unknown": {"name": ""}}
    return out


def redact_sensitive(value: PagerDutyDetails) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "authorization_config" in value:
        import capo_devops_agent.types.pager_duty_authorization_config

        out["authorization_config"] = (
            capo_devops_agent.types.pager_duty_authorization_config.redact_sensitive(
                value["authorization_config"]
            )
        )
    return out
