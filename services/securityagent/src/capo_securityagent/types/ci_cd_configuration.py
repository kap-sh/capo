"""Generated from Smithy shape ``com.amazonaws.securityagent#CiCdConfiguration``."""

from typing_extensions import NotRequired, TypedDict


class CiCdConfiguration(TypedDict, closed=True):
    enabled: NotRequired["bool"]
    """<p>Whether CI/CD pentesting is enabled for this pentest.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CiCdConfiguration) -> dict:
    out: dict = {}
    if "enabled" in value:
        out["enabled"] = value["enabled"]
    return out


def deserialize_json(data: dict) -> CiCdConfiguration:
    out: CiCdConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("enabled") is not None:
        out["enabled"] = data["enabled"]
    return out
