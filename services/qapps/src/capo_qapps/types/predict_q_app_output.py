"""Generated from Smithy shape ``com.amazonaws.qapps#PredictQAppOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_qapps.errors import DeserializationError

if TYPE_CHECKING:
    import capo_qapps.types.predict_app_definition


class PredictQAppOutput(TypedDict, closed=True):
    app: "capo_qapps.types.predict_app_definition.PredictAppDefinition"
    """<p>The generated Q App definition.</p>"""
    problem_statement: "str"
    """<p>The problem statement extracted from the input conversation, if provided.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PredictQAppOutput) -> dict:
    out: dict = {}
    import capo_qapps.types.predict_app_definition

    out["app"] = capo_qapps.types.predict_app_definition.serialize_json(value["app"])
    out["problemStatement"] = value["problem_statement"]
    return out


def deserialize_json(data: dict) -> PredictQAppOutput:
    out: PredictQAppOutput = {}  # type: ignore[typeddict-item]
    if data.get("app") is not None:
        import capo_qapps.types.predict_app_definition

        out["app"] = capo_qapps.types.predict_app_definition.deserialize_json(
            data["app"]
        )
    else:
        raise DeserializationError("PredictQAppOutput.app required")
    if data.get("problemStatement") is not None:
        out["problem_statement"] = data["problemStatement"]
    else:
        out["problem_statement"] = ""
    return out
