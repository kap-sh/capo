"""Generated from Smithy shape ``com.amazonaws.qbusiness#PersonalizationConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_qbusiness.types.personalization_control_mode


class PersonalizationConfiguration(TypedDict, closed=True):
    personalization_control_mode: (
        "capo_qbusiness.types.personalization_control_mode.PersonalizationControlMode"
    )
    """<p>An option to allow Amazon Q Business to customize chat responses using user specific metadata—specifically, location and job information—in your IAM Identity Center instance.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PersonalizationConfiguration) -> dict:
    out: dict = {}
    import capo_qbusiness.types.personalization_control_mode

    out["personalizationControlMode"] = (
        capo_qbusiness.types.personalization_control_mode.serialize_json(
            value["personalization_control_mode"]
        )
    )
    return out


def deserialize_json(data: dict) -> PersonalizationConfiguration:
    out: PersonalizationConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("personalizationControlMode") is not None:
        import capo_qbusiness.types.personalization_control_mode

        out["personalization_control_mode"] = (
            capo_qbusiness.types.personalization_control_mode.deserialize_json(
                data["personalizationControlMode"]
            )
        )
    else:
        import typing

        out["personalization_control_mode"] = typing.cast(
            "capo_qbusiness.types.personalization_control_mode.PersonalizationControlMode",
            "",
        )
    return out
