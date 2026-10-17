"""Generated from Smithy shape ``com.amazonaws.lambdaweb#RuntimeConfig``."""

from typing_extensions import TypedDict

from capo_lambda_web.errors import DeserializationError


class RuntimeConfig(TypedDict, closed=True):
    runtime: "str"
    """<p>The runtime identifier for the web function (for example, a Node.js runtime identifier).</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RuntimeConfig) -> dict:
    out: dict = {}
    out["runtime"] = value["runtime"]
    return out


def deserialize_json(data: dict) -> RuntimeConfig:
    out: RuntimeConfig = {}  # type: ignore[typeddict-item]
    if data.get("runtime") is not None:
        out["runtime"] = data["runtime"]
    else:
        raise DeserializationError("RuntimeConfig.runtime required")
    return out
