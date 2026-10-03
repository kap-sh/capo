"""Generated from Smithy shape ``com.amazonaws.globalaccelerator#ByoipCidr``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_global_accelerator.types.byoip_cidr_events
    import capo_global_accelerator.types.byoip_cidr_state
    import capo_global_accelerator.types.generic_string


class ByoipCidr(TypedDict, closed=True):
    cidr: NotRequired["capo_global_accelerator.types.generic_string.GenericString"]
    """<p>The address range, in CIDR notation.</p> <p> For more information, see <a href="https://docs.aws.amazon.com/global-accelerator/latest/dg/using-byoip.html">Bring your own IP addresses (BYOIP)</a> in the Global Accelerator Developer Guide.</p>"""
    state: NotRequired["capo_global_accelerator.types.byoip_cidr_state.ByoipCidrState"]
    """<p>The state of the address pool.</p>"""
    events: NotRequired[
        "capo_global_accelerator.types.byoip_cidr_events.ByoipCidrEvents"
    ]
    """<p>A history of status changes for an IP address range that you bring to Global Accelerator through bring your own IP address (BYOIP).</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ByoipCidr) -> dict:
    out: dict = {}
    if "cidr" in value:
        out["Cidr"] = value["cidr"]
    if "state" in value:
        import capo_global_accelerator.types.byoip_cidr_state

        out["State"] = (
            capo_global_accelerator.types.byoip_cidr_state.serialize_aws_json_1_1(
                value["state"]
            )
        )
    if "events" in value:
        import capo_global_accelerator.types.byoip_cidr_events

        out["Events"] = (
            capo_global_accelerator.types.byoip_cidr_events.serialize_aws_json_1_1(
                value["events"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ByoipCidr:
    out: ByoipCidr = {}  # type: ignore[typeddict-item]
    if data.get("Cidr") is not None:
        out["cidr"] = data["Cidr"]
    if data.get("State") is not None:
        import capo_global_accelerator.types.byoip_cidr_state

        out["state"] = (
            capo_global_accelerator.types.byoip_cidr_state.deserialize_aws_json_1_1(
                data["State"]
            )
        )
    if data.get("Events") is not None:
        import capo_global_accelerator.types.byoip_cidr_events

        out["events"] = (
            capo_global_accelerator.types.byoip_cidr_events.deserialize_aws_json_1_1(
                data["Events"]
            )
        )
    return out
