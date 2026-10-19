"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#ConnectorParameterOverride``."""

from typing_extensions import NotRequired, TypedDict


class ConnectorParameterOverride(TypedDict, closed=True):
    path: "str"
    """<p>A JSON Pointer path identifying the parameter (for example, <code>/numberOfResults</code> or <code>/filter</code>).</p>"""
    description: NotRequired["str"]
    """<p>An agent-facing description override for this parameter.</p>"""
    visible: NotRequired["bool"]
    """<p>Whether this parameter is visible to the agent. If not specified, uses the service default.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ConnectorParameterOverride) -> dict:
    out: dict = {}
    out["path"] = value["path"]
    if "description" in value:
        out["description"] = value["description"]
    if "visible" in value:
        out["visible"] = value["visible"]
    return out


def deserialize_json(data: dict) -> ConnectorParameterOverride:
    out: ConnectorParameterOverride = {}  # type: ignore[typeddict-item]
    if data.get("path") is not None:
        out["path"] = data["path"]
    else:
        out["path"] = ""
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("visible") is not None:
        out["visible"] = data["visible"]
    return out
