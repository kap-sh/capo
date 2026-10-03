"""Generated from Smithy shape ``com.amazonaws.ec2#InstanceMaintenanceOptionsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.instance_auto_recovery_state


class InstanceMaintenanceOptionsRequest(TypedDict, closed=True):
    auto_recovery: NotRequired[
        "capo_ec2.types.instance_auto_recovery_state.InstanceAutoRecoveryState"
    ]
    """<p>Disables the automatic recovery behavior of your instance or sets it to default. For more information, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-instance-recover.html#instance-configuration-recovery">Simplified automatic recovery</a>.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: InstanceMaintenanceOptionsRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "auto_recovery" in value:
        import capo_ec2.types.instance_auto_recovery_state

        capo_ec2.types.instance_auto_recovery_state.serialize_ec2_query(
            value["auto_recovery"], pairs, f"{key_prefix}AutoRecovery"
        )


def deserialize_ec2_query(el: Element) -> InstanceMaintenanceOptionsRequest:
    out: InstanceMaintenanceOptionsRequest = {}  # type: ignore[typeddict-item]
    child_auto_recovery = el.find("AutoRecovery")
    if child_auto_recovery is not None:
        import capo_ec2.types.instance_auto_recovery_state

        out["auto_recovery"] = (
            capo_ec2.types.instance_auto_recovery_state.deserialize_ec2_query(
                child_auto_recovery
            )
        )
    return out
