"""Generated from Smithy shape ``com.amazonaws.devopsagent#RemoteAgentOAuthClientCredentialsConfig``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_devops_agent.types.client_id
    import capo_devops_agent.types.client_secret
    import capo_devops_agent.types.exchange_parameters
    import capo_devops_agent.types.scopes


class RemoteAgentOAuthClientCredentialsConfig(TypedDict, closed=True):
    client_name: NotRequired["str"]
    """<p>User friendly OAuth client name specified by end user.</p>"""
    client_id: "capo_devops_agent.types.client_id.ClientId"
    """<p>OAuth client ID for authenticating with the service.</p>"""
    exchange_parameters: NotRequired[
        "capo_devops_agent.types.exchange_parameters.ExchangeParameters"
    ]
    """<p>OAuth token exchange parameters for authenticating with the service.</p>"""
    client_secret: "capo_devops_agent.types.client_secret.ClientSecret"
    """<p>OAuth client secret for authenticating with the service.</p>"""
    exchange_url: "str"
    """<p>OAuth token exchange URL.</p>"""
    scopes: NotRequired["capo_devops_agent.types.scopes.Scopes"]
    """<p>OAuth scopes for authentication.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RemoteAgentOAuthClientCredentialsConfig) -> dict:
    out: dict = {}
    if "client_name" in value:
        out["clientName"] = value["client_name"]
    out["clientId"] = value["client_id"]
    if "exchange_parameters" in value:
        import capo_devops_agent.types.exchange_parameters

        out["exchangeParameters"] = (
            capo_devops_agent.types.exchange_parameters.serialize_json(
                value["exchange_parameters"]
            )
        )
    out["clientSecret"] = value["client_secret"]
    out["exchangeUrl"] = value["exchange_url"]
    if "scopes" in value:
        import capo_devops_agent.types.scopes

        out["scopes"] = capo_devops_agent.types.scopes.serialize_json(value["scopes"])
    return out


def deserialize_json(data: dict) -> RemoteAgentOAuthClientCredentialsConfig:
    out: RemoteAgentOAuthClientCredentialsConfig = {}  # type: ignore[typeddict-item]
    if data.get("clientName") is not None:
        out["client_name"] = data["clientName"]
    if data.get("clientId") is not None:
        out["client_id"] = data["clientId"]
    else:
        out["client_id"] = ""
    if data.get("exchangeParameters") is not None:
        import capo_devops_agent.types.exchange_parameters

        out["exchange_parameters"] = (
            capo_devops_agent.types.exchange_parameters.deserialize_json(
                data["exchangeParameters"]
            )
        )
    if data.get("clientSecret") is not None:
        out["client_secret"] = data["clientSecret"]
    else:
        out["client_secret"] = ""
    if data.get("exchangeUrl") is not None:
        out["exchange_url"] = data["exchangeUrl"]
    else:
        out["exchange_url"] = ""
    if data.get("scopes") is not None:
        import capo_devops_agent.types.scopes

        out["scopes"] = capo_devops_agent.types.scopes.deserialize_json(data["scopes"])
    return out


def redact_sensitive(value: RemoteAgentOAuthClientCredentialsConfig) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "client_id" in value:
        out["client_id"] = "*** Sensitive Data Redacted ***"
    if "exchange_parameters" in value:
        import capo_devops_agent.types.exchange_parameters

        out["exchange_parameters"] = (
            capo_devops_agent.types.exchange_parameters.redact_sensitive(
                value["exchange_parameters"]
            )
        )
    if "client_secret" in value:
        out["client_secret"] = "*** Sensitive Data Redacted ***"
    return out
