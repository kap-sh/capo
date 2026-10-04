"""Generated from Smithy shape ``com.amazonaws.endusermessaging#UpdateCodeConfigurationParameters``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_endusermessaging.types.code_length
    import capo_endusermessaging.types.code_type
    import capo_endusermessaging.types.max_verification_attempts
    import capo_endusermessaging.types.validity_period_minutes


class UpdateCodeConfigurationParameters(TypedDict, closed=True):
    code_type: NotRequired["capo_endusermessaging.types.code_type.CodeType"]
    """<p>The updated character set used to generate the one-time passcode. Omit this member to preserve the current value.</p>"""
    code_length: NotRequired["capo_endusermessaging.types.code_length.CodeLength"]
    """<p>The updated number of characters in the one-time passcode. Valid values range from 4 through 8. Omit this member to preserve the current value.</p>"""
    validity_period_minutes: NotRequired[
        "capo_endusermessaging.types.validity_period_minutes.ValidityPeriodMinutes"
    ]
    """<p>The updated length of time, in minutes, that the one-time passcode remains valid. Valid values range from 1 through 60. Omit this member to preserve the current value.</p>"""
    max_attempts: NotRequired[
        "capo_endusermessaging.types.max_verification_attempts.MaxVerificationAttempts"
    ]
    """<p>The updated maximum number of validation attempts that are allowed before the verification is locked. Valid values range from 1 through 5. Omit this member to preserve the current value.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateCodeConfigurationParameters) -> dict:
    out: dict = {}
    if "code_type" in value:
        import capo_endusermessaging.types.code_type

        out["codeType"] = capo_endusermessaging.types.code_type.serialize_json(
            value["code_type"]
        )
    if "code_length" in value:
        out["codeLength"] = value["code_length"]
    if "validity_period_minutes" in value:
        out["validityPeriodMinutes"] = value["validity_period_minutes"]
    if "max_attempts" in value:
        out["maxAttempts"] = value["max_attempts"]
    return out


def deserialize_json(data: dict) -> UpdateCodeConfigurationParameters:
    out: UpdateCodeConfigurationParameters = {}  # type: ignore[typeddict-item]
    if data.get("codeType") is not None:
        import capo_endusermessaging.types.code_type

        out["code_type"] = capo_endusermessaging.types.code_type.deserialize_json(
            data["codeType"]
        )
    if data.get("codeLength") is not None:
        out["code_length"] = data["codeLength"]
    if data.get("validityPeriodMinutes") is not None:
        out["validity_period_minutes"] = data["validityPeriodMinutes"]
    if data.get("maxAttempts") is not None:
        out["max_attempts"] = data["maxAttempts"]
    return out
