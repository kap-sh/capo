"""Generated from Smithy shape ``com.amazonaws.continuum#ValidationExecutedProof``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_continuum.errors import DeserializationError

if TYPE_CHECKING:
    import capo_continuum.types.exploit_effect
    import capo_continuum.types.validation_proof_code
    import capo_continuum.types.validation_proof_output


class ValidationExecutedProof(TypedDict, closed=True):
    code: "capo_continuum.types.validation_proof_code.ValidationProofCode"
    """The code that was run. Not a request payload: it imports the repository's own modules and drives the vulnerable code path directly."""
    output: NotRequired[
        "capo_continuum.types.validation_proof_output.ValidationProofOutput"
    ]
    """What the execution printed, including the agent's own PASS/FAIL assertions. Absent when the run printed nothing retained."""
    observed_effect: NotRequired["capo_continuum.types.exploit_effect.ExploitEffect"]
    """Effect the execution actually produced. `observedEffect` rather than `effect`: this one was witnessed, and the name has to stay distinguishable from `ValidationSourceAnalysis.inferredEffect`, which was not."""


# --- restJson1 ser/de ---
def serialize_json(value: ValidationExecutedProof) -> dict:
    out: dict = {}
    import capo_continuum.types.validation_proof_code

    out["code"] = capo_continuum.types.validation_proof_code.serialize_json(
        value["code"]
    )
    if "output" in value:
        import capo_continuum.types.validation_proof_output

        out["output"] = capo_continuum.types.validation_proof_output.serialize_json(
            value["output"]
        )
    if "observed_effect" in value:
        import capo_continuum.types.exploit_effect

        out["observedEffect"] = capo_continuum.types.exploit_effect.serialize_json(
            value["observed_effect"]
        )
    return out


def deserialize_json(data: dict) -> ValidationExecutedProof:
    out: ValidationExecutedProof = {}  # type: ignore[typeddict-item]
    if data.get("code") is not None:
        import capo_continuum.types.validation_proof_code

        out["code"] = capo_continuum.types.validation_proof_code.deserialize_json(
            data["code"]
        )
    else:
        raise DeserializationError("ValidationExecutedProof.code required")
    if data.get("output") is not None:
        import capo_continuum.types.validation_proof_output

        out["output"] = capo_continuum.types.validation_proof_output.deserialize_json(
            data["output"]
        )
    if data.get("observedEffect") is not None:
        import capo_continuum.types.exploit_effect

        out["observed_effect"] = capo_continuum.types.exploit_effect.deserialize_json(
            data["observedEffect"]
        )
    return out
