"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#StaticRoute``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

from capo_bedrock_agentcore_control.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.target_name


class StaticRoute(TypedDict, closed=True):
    target_name: "capo_bedrock_agentcore_control.types.target_name.TargetName"
    """<p>The name of the target to route requests to.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StaticRoute) -> dict:
    out: dict = {}
    out["targetName"] = value["target_name"]
    return out


def deserialize_json(data: dict) -> StaticRoute:
    out: StaticRoute = {}  # type: ignore[typeddict-item]
    if data.get("targetName") is not None:
        out["target_name"] = data["targetName"]
    else:
        raise DeserializationError("StaticRoute.target_name required")
    return out


def redact_sensitive(value: StaticRoute) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "target_name" in value:
        out["target_name"] = "*** Sensitive Data Redacted ***"
    return out
