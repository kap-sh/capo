"""Generated from Smithy shape ``com.amazonaws.ec2#ClientVpnAuthorizationPolicyStatus``."""

from typing import Literal, TypeAlias, cast

from capo_ec2._protocol.xml import Element

"""<p>Describes the state of an authorization policy for a Client VPN endpoint. Possible states include:</p> <ul> <li> <p> <code>creating</code> - The authorization policy is being created.</p> </li> <li> <p> <code>updating</code> - The authorization policy is being updated.</p> </li> <li> <p> <code>active</code> - The authorization policy has been applied to the Client VPN endpoint.</p> </li> <li> <p> <code>failed</code> - The authorization policy could not be applied to the Client VPN endpoint.</p> </li> <li> <p> <code>deleting</code> - The authorization policy is being deleted.</p> </li> </ul>"""
ClientVpnAuthorizationPolicyStatus: TypeAlias = Literal[
    "creating",
    "updating",
    "active",
    "failed",
    "deleting",
]


# --- ec2Query ser/de ---
def to_ec2_query_text(value: ClientVpnAuthorizationPolicyStatus) -> str:
    return value


def from_ec2_query_text(text: str) -> ClientVpnAuthorizationPolicyStatus:
    return cast(ClientVpnAuthorizationPolicyStatus, text)


def serialize_ec2_query(
    value: ClientVpnAuthorizationPolicyStatus, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> ClientVpnAuthorizationPolicyStatus:
    return from_ec2_query_text(el.text or "")
