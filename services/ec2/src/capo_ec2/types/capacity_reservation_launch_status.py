"""Generated from Smithy shape ``com.amazonaws.ec2#CapacityReservationLaunchStatus``."""

from typing import Literal, TypeAlias, cast

from capo_ec2._protocol.xml import Element

CapacityReservationLaunchStatus: TypeAlias = Literal[
    "launchable",
    "unlaunchable",
]


# --- ec2Query ser/de ---
def to_ec2_query_text(value: CapacityReservationLaunchStatus) -> str:
    return value


def from_ec2_query_text(text: str) -> CapacityReservationLaunchStatus:
    return cast(CapacityReservationLaunchStatus, text)


def serialize_ec2_query(
    value: CapacityReservationLaunchStatus, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> CapacityReservationLaunchStatus:
    return from_ec2_query_text(el.text or "")
