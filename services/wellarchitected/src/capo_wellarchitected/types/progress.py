"""Generated from Smithy shape ``com.amazonaws.wellarchitected#Progress``."""

from typing_extensions import TypedDict


class Progress(TypedDict, closed=True):
    steps_completed: "int"
    """<p>The number of generation steps that have been completed.</p>"""
    total_steps: "int"
    """<p>The total number of steps in the generation process.</p>"""
    completion_percentage: "float"
    """<p>The completion percentage of the generation process (0-100).</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Progress) -> dict:
    out: dict = {}
    out["stepsCompleted"] = value["steps_completed"]
    out["totalSteps"] = value["total_steps"]
    out["completionPercentage"] = (
        "NaN"
        if value["completion_percentage"] != value["completion_percentage"]
        else "Infinity"
        if value["completion_percentage"] == float("inf")
        else "-Infinity"
        if value["completion_percentage"] == float("-inf")
        else value["completion_percentage"]
    )
    return out


def deserialize_json(data: dict) -> Progress:
    out: Progress = {}  # type: ignore[typeddict-item]
    if data.get("stepsCompleted") is not None:
        out["steps_completed"] = data["stepsCompleted"]
    else:
        out["steps_completed"] = 0
    if data.get("totalSteps") is not None:
        out["total_steps"] = data["totalSteps"]
    else:
        out["total_steps"] = 0
    if data.get("completionPercentage") is not None:
        out["completion_percentage"] = float(data["completionPercentage"])
    else:
        out["completion_percentage"] = 0.0
    return out
