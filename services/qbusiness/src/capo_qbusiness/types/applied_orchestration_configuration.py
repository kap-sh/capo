"""Generated from Smithy shape ``com.amazonaws.qbusiness#AppliedOrchestrationConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_qbusiness.types.orchestration_control


class AppliedOrchestrationConfiguration(TypedDict, closed=True):
    control: "capo_qbusiness.types.orchestration_control.OrchestrationControl"
    """<p> Information about whether chat orchestration is enabled or disabled for an Amazon Q Business application. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AppliedOrchestrationConfiguration) -> dict:
    out: dict = {}
    import capo_qbusiness.types.orchestration_control

    out["control"] = capo_qbusiness.types.orchestration_control.serialize_json(
        value["control"]
    )
    return out


def deserialize_json(data: dict) -> AppliedOrchestrationConfiguration:
    out: AppliedOrchestrationConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("control") is not None:
        import capo_qbusiness.types.orchestration_control

        out["control"] = capo_qbusiness.types.orchestration_control.deserialize_json(
            data["control"]
        )
    else:
        import typing

        out["control"] = typing.cast(
            "capo_qbusiness.types.orchestration_control.OrchestrationControl", ""
        )
    return out
