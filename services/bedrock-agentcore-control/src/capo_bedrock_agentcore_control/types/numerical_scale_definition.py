"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#NumericalScaleDefinition``."""

from typing_extensions import TypedDict


class NumericalScaleDefinition(TypedDict, closed=True):
    definition: "str"
    """<p> The description that explains what this numerical rating represents and when it should be used. </p>"""
    value: "float"
    """<p> The numerical value for this rating scale option. </p>"""
    label: "str"
    """<p> The label or name that describes this numerical rating option. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: NumericalScaleDefinition) -> dict:
    out: dict = {}
    out["definition"] = value["definition"]
    out["value"] = (
        "NaN"
        if value["value"] != value["value"]
        else "Infinity"
        if value["value"] == float("inf")
        else "-Infinity"
        if value["value"] == float("-inf")
        else value["value"]
    )
    out["label"] = value["label"]
    return out


def deserialize_json(data: dict) -> NumericalScaleDefinition:
    out: NumericalScaleDefinition = {}  # type: ignore[typeddict-item]
    if data.get("definition") is not None:
        out["definition"] = data["definition"]
    else:
        out["definition"] = ""
    if data.get("value") is not None:
        out["value"] = float(data["value"])
    else:
        out["value"] = 0.0
    if data.get("label") is not None:
        out["label"] = data["label"]
    else:
        out["label"] = ""
    return out
