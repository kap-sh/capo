"""Generated from Smithy shape ``com.amazonaws.ec2#ClientVpnAuthorizationPolicyShadowMode``."""

from typing import Literal, TypeAlias, cast

from capo_ec2._protocol.xml import Element

"""<p>Indicates whether the authorization policy for a Client VPN endpoint is evaluated in shadow mode. Possible values include:</p> <ul> <li> <p> <code>enabled</code> - The authorization policy is evaluated and the results are logged, but access is not enforced.</p> </li> <li> <p> <code>disabled</code> - The authorization policy is enforced.</p> </li> </ul>"""
ClientVpnAuthorizationPolicyShadowMode: TypeAlias = Literal[
    "enabled",
    "disabled",
]


# --- ec2Query ser/de ---
def to_ec2_query_text(value: ClientVpnAuthorizationPolicyShadowMode) -> str:
    return value


def from_ec2_query_text(text: str) -> ClientVpnAuthorizationPolicyShadowMode:
    return cast(ClientVpnAuthorizationPolicyShadowMode, text)


def serialize_ec2_query(
    value: ClientVpnAuthorizationPolicyShadowMode,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> ClientVpnAuthorizationPolicyShadowMode:
    return from_ec2_query_text(el.text or "")
