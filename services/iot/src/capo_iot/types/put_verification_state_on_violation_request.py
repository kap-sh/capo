"""Generated from Smithy shape ``com.amazonaws.iot#PutVerificationStateOnViolationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot.types.verification_state
    import capo_iot.types.verification_state_description
    import capo_iot.types.violation_id


class PutVerificationStateOnViolationRequest(TypedDict, closed=True):
    violation_id: "capo_iot.types.violation_id.ViolationId"
    """<p>The violation ID.</p>"""
    verification_state: "capo_iot.types.verification_state.VerificationState"
    """<p>The verification state of the violation.</p>"""
    verification_state_description: NotRequired[
        "capo_iot.types.verification_state_description.VerificationStateDescription"
    ]
    """<p>The description of the verification state of the violation (detect alarm).</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PutVerificationStateOnViolationRequest) -> dict:
    out: dict = {}
    import capo_iot.types.verification_state

    out["verificationState"] = capo_iot.types.verification_state.serialize_json(
        value["verification_state"]
    )
    if "verification_state_description" in value:
        out["verificationStateDescription"] = value["verification_state_description"]
    return out


def deserialize_json(data: dict) -> PutVerificationStateOnViolationRequest:
    out: PutVerificationStateOnViolationRequest = {}  # type: ignore[typeddict-item]
    if data.get("verificationState") is not None:
        import capo_iot.types.verification_state

        out["verification_state"] = capo_iot.types.verification_state.deserialize_json(
            data["verificationState"]
        )
    else:
        import typing

        out["verification_state"] = typing.cast(
            "capo_iot.types.verification_state.VerificationState", ""
        )
    if data.get("verificationStateDescription") is not None:
        out["verification_state_description"] = data["verificationStateDescription"]
    return out
