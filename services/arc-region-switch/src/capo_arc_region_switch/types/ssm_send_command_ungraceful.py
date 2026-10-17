"""Generated from Smithy shape ``com.amazonaws.arcregionswitch#SsmSendCommandUngraceful``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_arc_region_switch.types.ssm_send_command_ungraceful_behavior


class SsmSendCommandUngraceful(TypedDict, closed=True):
    behavior: NotRequired[
        "capo_arc_region_switch.types.ssm_send_command_ungraceful_behavior.SsmSendCommandUngracefulBehavior"
    ]
    """<p>Specifies whether to skip running this command during an ungraceful execution. Set to <code>skip</code> to skip the command.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: SsmSendCommandUngraceful) -> dict:
    out: dict = {}
    if "behavior" in value:
        import capo_arc_region_switch.types.ssm_send_command_ungraceful_behavior

        out["behavior"] = (
            capo_arc_region_switch.types.ssm_send_command_ungraceful_behavior.serialize_aws_json_1_0(
                value["behavior"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> SsmSendCommandUngraceful:
    out: SsmSendCommandUngraceful = {}  # type: ignore[typeddict-item]
    if data.get("behavior") is not None:
        import capo_arc_region_switch.types.ssm_send_command_ungraceful_behavior

        out["behavior"] = (
            capo_arc_region_switch.types.ssm_send_command_ungraceful_behavior.deserialize_aws_json_1_0(
                data["behavior"]
            )
        )
    return out
