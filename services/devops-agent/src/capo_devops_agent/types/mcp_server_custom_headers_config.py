"""Generated from Smithy shape ``com.amazonaws.devopsagent#MCPServerCustomHeadersConfig``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_devops_agent.types.custom_headers


class MCPServerCustomHeadersConfig(TypedDict, closed=True):
    headers: "capo_devops_agent.types.custom_headers.CustomHeaders"


# --- restJson1 ser/de ---
def serialize_json(value: MCPServerCustomHeadersConfig) -> dict:
    out: dict = {}
    import capo_devops_agent.types.custom_headers

    out["headers"] = capo_devops_agent.types.custom_headers.serialize_json(
        value["headers"]
    )
    return out


def deserialize_json(data: dict) -> MCPServerCustomHeadersConfig:
    out: MCPServerCustomHeadersConfig = {}  # type: ignore[typeddict-item]
    if data.get("headers") is not None:
        import capo_devops_agent.types.custom_headers

        out["headers"] = capo_devops_agent.types.custom_headers.deserialize_json(
            data["headers"]
        )
    else:
        out["headers"] = {}
    return out


def redact_sensitive(value: MCPServerCustomHeadersConfig) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "headers" in value:
        import capo_devops_agent.types.custom_headers

        out["headers"] = capo_devops_agent.types.custom_headers.redact_sensitive(
            value["headers"]
        )
    return out
