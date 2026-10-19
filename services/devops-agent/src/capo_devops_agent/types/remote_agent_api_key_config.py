"""Generated from Smithy shape ``com.amazonaws.devopsagent#RemoteAgentAPIKeyConfig``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_devops_agent.types.api_key_value


class RemoteAgentAPIKeyConfig(TypedDict, closed=True):
    api_key_name: "str"
    """<p>User friendly API key name specified by end user.</p>"""
    api_key_value: "capo_devops_agent.types.api_key_value.ApiKeyValue"
    """<p>API key value for authenticating with the service.</p>"""
    api_key_header: "str"
    """<p>HTTP header name to send the API key in requests to the service.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RemoteAgentAPIKeyConfig) -> dict:
    out: dict = {}
    out["apiKeyName"] = value["api_key_name"]
    out["apiKeyValue"] = value["api_key_value"]
    out["apiKeyHeader"] = value["api_key_header"]
    return out


def deserialize_json(data: dict) -> RemoteAgentAPIKeyConfig:
    out: RemoteAgentAPIKeyConfig = {}  # type: ignore[typeddict-item]
    if data.get("apiKeyName") is not None:
        out["api_key_name"] = data["apiKeyName"]
    else:
        out["api_key_name"] = ""
    if data.get("apiKeyValue") is not None:
        out["api_key_value"] = data["apiKeyValue"]
    else:
        out["api_key_value"] = ""
    if data.get("apiKeyHeader") is not None:
        out["api_key_header"] = data["apiKeyHeader"]
    else:
        out["api_key_header"] = ""
    return out


def redact_sensitive(value: RemoteAgentAPIKeyConfig) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "api_key_value" in value:
        out["api_key_value"] = "*** Sensitive Data Redacted ***"
    return out
