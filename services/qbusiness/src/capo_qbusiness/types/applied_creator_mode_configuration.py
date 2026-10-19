"""Generated from Smithy shape ``com.amazonaws.qbusiness#AppliedCreatorModeConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_qbusiness.types.creator_mode_control


class AppliedCreatorModeConfiguration(TypedDict, closed=True):
    creator_mode_control: "capo_qbusiness.types.creator_mode_control.CreatorModeControl"
    """<p> Information about whether creator mode is enabled or disabled for an Amazon Q Business application. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AppliedCreatorModeConfiguration) -> dict:
    out: dict = {}
    import capo_qbusiness.types.creator_mode_control

    out["creatorModeControl"] = (
        capo_qbusiness.types.creator_mode_control.serialize_json(
            value["creator_mode_control"]
        )
    )
    return out


def deserialize_json(data: dict) -> AppliedCreatorModeConfiguration:
    out: AppliedCreatorModeConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("creatorModeControl") is not None:
        import capo_qbusiness.types.creator_mode_control

        out["creator_mode_control"] = (
            capo_qbusiness.types.creator_mode_control.deserialize_json(
                data["creatorModeControl"]
            )
        )
    else:
        import typing

        out["creator_mode_control"] = typing.cast(
            "capo_qbusiness.types.creator_mode_control.CreatorModeControl", ""
        )
    return out
