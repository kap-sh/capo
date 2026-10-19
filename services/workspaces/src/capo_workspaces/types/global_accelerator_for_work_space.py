"""Generated from Smithy shape ``com.amazonaws.workspaces#GlobalAcceleratorForWorkSpace``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_workspaces.types.aga_mode_for_work_space_enum
    import capo_workspaces.types.aga_preferred_protocol_for_work_space


class GlobalAcceleratorForWorkSpace(TypedDict, closed=True):
    mode: "capo_workspaces.types.aga_mode_for_work_space_enum.AGAModeForWorkSpaceEnum"
    """<p>Indicates if Global Accelerator for WorkSpaces is enabled, disabled, or the same mode as the associated directory.</p>"""
    preferred_protocol: NotRequired[
        "capo_workspaces.types.aga_preferred_protocol_for_work_space.AGAPreferredProtocolForWorkSpace"
    ]
    """<p>Indicates the preferred protocol for Global Accelerator.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GlobalAcceleratorForWorkSpace) -> dict:
    out: dict = {}
    import capo_workspaces.types.aga_mode_for_work_space_enum

    out["Mode"] = (
        capo_workspaces.types.aga_mode_for_work_space_enum.serialize_aws_json_1_1(
            value["mode"]
        )
    )
    if "preferred_protocol" in value:
        import capo_workspaces.types.aga_preferred_protocol_for_work_space

        out["PreferredProtocol"] = (
            capo_workspaces.types.aga_preferred_protocol_for_work_space.serialize_aws_json_1_1(
                value["preferred_protocol"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GlobalAcceleratorForWorkSpace:
    out: GlobalAcceleratorForWorkSpace = {}  # type: ignore[typeddict-item]
    if data.get("Mode") is not None:
        import capo_workspaces.types.aga_mode_for_work_space_enum

        out["mode"] = (
            capo_workspaces.types.aga_mode_for_work_space_enum.deserialize_aws_json_1_1(
                data["Mode"]
            )
        )
    else:
        import typing

        out["mode"] = typing.cast(
            "capo_workspaces.types.aga_mode_for_work_space_enum.AGAModeForWorkSpaceEnum",
            "",
        )
    if data.get("PreferredProtocol") is not None:
        import capo_workspaces.types.aga_preferred_protocol_for_work_space

        out["preferred_protocol"] = (
            capo_workspaces.types.aga_preferred_protocol_for_work_space.deserialize_aws_json_1_1(
                data["PreferredProtocol"]
            )
        )
    return out
