"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#CategoricalScaleDefinition``."""

from typing_extensions import TypedDict


class CategoricalScaleDefinition(TypedDict, closed=True):
    definition: "str"
    """<p> The description that explains what this categorical rating represents and when it should be used. </p>"""
    label: "str"
    """<p> The label or name of this categorical rating option. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CategoricalScaleDefinition) -> dict:
    out: dict = {}
    out["definition"] = value["definition"]
    out["label"] = value["label"]
    return out


def deserialize_json(data: dict) -> CategoricalScaleDefinition:
    out: CategoricalScaleDefinition = {}  # type: ignore[typeddict-item]
    if data.get("definition") is not None:
        out["definition"] = data["definition"]
    else:
        out["definition"] = ""
    if data.get("label") is not None:
        out["label"] = data["label"]
    else:
        out["label"] = ""
    return out
