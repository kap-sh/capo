"""Generated from Smithy shape ``com.amazonaws.m2#EngineVersionsSummary``."""

from typing_extensions import TypedDict


class EngineVersionsSummary(TypedDict, closed=True):
    engine_type: "str"
    """<p>The type of target platform for the application.</p>"""
    engine_version: "str"
    """<p>The version of the engine type used by the application.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EngineVersionsSummary) -> dict:
    out: dict = {}
    out["engineType"] = value["engine_type"]
    out["engineVersion"] = value["engine_version"]
    return out


def deserialize_json(data: dict) -> EngineVersionsSummary:
    out: EngineVersionsSummary = {}  # type: ignore[typeddict-item]
    if data.get("engineType") is not None:
        out["engine_type"] = data["engineType"]
    else:
        out["engine_type"] = ""
    if data.get("engineVersion") is not None:
        out["engine_version"] = data["engineVersion"]
    else:
        out["engine_version"] = ""
    return out
