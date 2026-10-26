"""Generated from Smithy shape ``com.amazonaws.devopsagent#NewRelicServiceDetails``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_devops_agent.types.new_relic_service_authorization_config


class NewRelicServiceDetails(TypedDict, closed=True):
    authorization_config: "capo_devops_agent.types.new_relic_service_authorization_config.NewRelicServiceAuthorizationConfig"
    """<p>New Relic MCP server authorization configuration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: NewRelicServiceDetails) -> dict:
    out: dict = {}
    import capo_devops_agent.types.new_relic_service_authorization_config

    out["authorizationConfig"] = (
        capo_devops_agent.types.new_relic_service_authorization_config.serialize_json(
            value["authorization_config"]
        )
    )
    return out


def deserialize_json(data: dict) -> NewRelicServiceDetails:
    out: NewRelicServiceDetails = {}  # type: ignore[typeddict-item]
    if data.get("authorizationConfig") is not None:
        import capo_devops_agent.types.new_relic_service_authorization_config

        out["authorization_config"] = (
            capo_devops_agent.types.new_relic_service_authorization_config.deserialize_json(
                data["authorizationConfig"]
            )
        )
    else:
        out["authorization_config"] = {"$unknown": {"name": ""}}
    return out


def redact_sensitive(value: NewRelicServiceDetails) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "authorization_config" in value:
        import capo_devops_agent.types.new_relic_service_authorization_config

        out["authorization_config"] = (
            capo_devops_agent.types.new_relic_service_authorization_config.redact_sensitive(
                value["authorization_config"]
            )
        )
    return out
