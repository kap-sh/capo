"""Generated from Smithy shape ``com.amazonaws.ec2#CreatePeeringConnectionOptionsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.boolean
    import capo_ec2.types.multipath_resilience_mode


class CreatePeeringConnectionOptionsRequest(TypedDict, closed=True):
    allow_multipath_resilience: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>Specifies whether you allow multipath resilience for the requester VPC. Multipath resilience is supported only for inter-Region VPC peering connections between supported Regions. It takes effect only when both the requester and the accepter allow it. Accepting the VPC peering connection request also allows multipath resilience for the accepter VPC. If you don't specify this parameter, the default is <code>false</code>.</p>"""
    multipath_resilience_mode: NotRequired[
        "capo_ec2.types.multipath_resilience_mode.MultipathResilienceMode"
    ]
    """<p>The multipath resilience mode. You can specify this parameter only if <code>AllowMultipathResilience</code> is <code>true</code>.</p> <p>The following value is valid:</p> <ul> <li> <p> <code>always-on</code> – Replicates traffic across multiple network paths while multipath resilience is in effect.</p> </li> </ul> <p>If <code>AllowMultipathResilience</code> is <code>true</code> and you don't specify a mode, the default is <code>always-on</code>.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: CreatePeeringConnectionOptionsRequest,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "allow_multipath_resilience" in value:
        pairs.append(
            (
                f"{key_prefix}AllowMultipathResilience",
                "true" if value["allow_multipath_resilience"] else "false",
            )
        )
    if "multipath_resilience_mode" in value:
        import capo_ec2.types.multipath_resilience_mode

        capo_ec2.types.multipath_resilience_mode.serialize_ec2_query(
            value["multipath_resilience_mode"],
            pairs,
            f"{key_prefix}MultipathResilienceMode",
        )


def deserialize_ec2_query(el: Element) -> CreatePeeringConnectionOptionsRequest:
    out: CreatePeeringConnectionOptionsRequest = {}  # type: ignore[typeddict-item]
    child_allow_multipath_resilience = el.find("AllowMultipathResilience")
    if child_allow_multipath_resilience is not None:
        out["allow_multipath_resilience"] = (
            child_allow_multipath_resilience.text or ""
        ).lower() == "true"
    child_multipath_resilience_mode = el.find("MultipathResilienceMode")
    if child_multipath_resilience_mode is not None:
        import capo_ec2.types.multipath_resilience_mode

        out["multipath_resilience_mode"] = (
            capo_ec2.types.multipath_resilience_mode.deserialize_ec2_query(
                child_multipath_resilience_mode
            )
        )
    return out
