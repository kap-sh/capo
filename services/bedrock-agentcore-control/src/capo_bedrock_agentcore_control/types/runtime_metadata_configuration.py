"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#RuntimeMetadataConfiguration``."""

from typing_extensions import TypedDict


class RuntimeMetadataConfiguration(TypedDict, closed=True):
    require_mmdsv2: "bool"
    """<p>Enables MMDSv2 (microVM Metadata Service Version 2) requirement for the agent runtime. When set to <code>true</code>, the runtime microVM will only accept MMDSv2 requests.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RuntimeMetadataConfiguration) -> dict:
    out: dict = {}
    out["requireMMDSV2"] = value["require_mmdsv2"]
    return out


def deserialize_json(data: dict) -> RuntimeMetadataConfiguration:
    out: RuntimeMetadataConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("requireMMDSV2") is not None:
        out["require_mmdsv2"] = data["requireMMDSV2"]
    else:
        out["require_mmdsv2"] = False
    return out
