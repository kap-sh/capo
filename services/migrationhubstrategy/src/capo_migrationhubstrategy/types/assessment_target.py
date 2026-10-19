"""Generated from Smithy shape ``com.amazonaws.migrationhubstrategy#AssessmentTarget``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_migrationhubstrategy.types.assessment_target_values
    import capo_migrationhubstrategy.types.condition
    import capo_migrationhubstrategy.types.string


class AssessmentTarget(TypedDict, closed=True):
    condition: "capo_migrationhubstrategy.types.condition.Condition"
    """<p>Condition of an assessment.</p>"""
    name: "capo_migrationhubstrategy.types.string.String"
    """<p>Name of an assessment.</p>"""
    values: "capo_migrationhubstrategy.types.assessment_target_values.AssessmentTargetValues"
    """<p>Values of an assessment.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AssessmentTarget) -> dict:
    out: dict = {}
    out["condition"] = value["condition"]
    out["name"] = value["name"]
    import capo_migrationhubstrategy.types.assessment_target_values

    out["values"] = (
        capo_migrationhubstrategy.types.assessment_target_values.serialize_json(
            value["values"]
        )
    )
    return out


def deserialize_json(data: dict) -> AssessmentTarget:
    out: AssessmentTarget = {}  # type: ignore[typeddict-item]
    if data.get("condition") is not None:
        out["condition"] = data["condition"]
    else:
        out["condition"] = ""
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("values") is not None:
        import capo_migrationhubstrategy.types.assessment_target_values

        out["values"] = (
            capo_migrationhubstrategy.types.assessment_target_values.deserialize_json(
                data["values"]
            )
        )
    else:
        out["values"] = []
    return out
