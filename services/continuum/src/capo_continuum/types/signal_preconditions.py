"""Generated from Smithy shape ``com.amazonaws.continuum#SignalPreconditions``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_continuum.types.signal_access_precondition
    import capo_continuum.types.signal_precondition


class SignalPreconditions(TypedDict, closed=True):
    reachable_from_attacker: NotRequired[
        "capo_continuum.types.signal_precondition.SignalPrecondition"
    ]
    """Whether the vulnerable code path is reachable by an attacker."""
    configuration_needed: NotRequired[
        "capo_continuum.types.signal_precondition.SignalPrecondition"
    ]
    """Whether exploitation depends on a non-default configuration."""
    access_level: NotRequired[
        "capo_continuum.types.signal_access_precondition.SignalAccessPrecondition"
    ]
    """What level of access exploitation requires."""
    user_interaction_required: NotRequired[
        "capo_continuum.types.signal_precondition.SignalPrecondition"
    ]
    """Whether exploitation requires a user other than the attacker to take part, for example by opening a link or a file (CVSS User Interaction)."""


# --- restJson1 ser/de ---
def serialize_json(value: SignalPreconditions) -> dict:
    out: dict = {}
    if "reachable_from_attacker" in value:
        import capo_continuum.types.signal_precondition

        out["reachableFromAttacker"] = (
            capo_continuum.types.signal_precondition.serialize_json(
                value["reachable_from_attacker"]
            )
        )
    if "configuration_needed" in value:
        import capo_continuum.types.signal_precondition

        out["configurationNeeded"] = (
            capo_continuum.types.signal_precondition.serialize_json(
                value["configuration_needed"]
            )
        )
    if "access_level" in value:
        import capo_continuum.types.signal_access_precondition

        out["accessLevel"] = (
            capo_continuum.types.signal_access_precondition.serialize_json(
                value["access_level"]
            )
        )
    if "user_interaction_required" in value:
        import capo_continuum.types.signal_precondition

        out["userInteractionRequired"] = (
            capo_continuum.types.signal_precondition.serialize_json(
                value["user_interaction_required"]
            )
        )
    return out


def deserialize_json(data: dict) -> SignalPreconditions:
    out: SignalPreconditions = {}  # type: ignore[typeddict-item]
    if data.get("reachableFromAttacker") is not None:
        import capo_continuum.types.signal_precondition

        out["reachable_from_attacker"] = (
            capo_continuum.types.signal_precondition.deserialize_json(
                data["reachableFromAttacker"]
            )
        )
    if data.get("configurationNeeded") is not None:
        import capo_continuum.types.signal_precondition

        out["configuration_needed"] = (
            capo_continuum.types.signal_precondition.deserialize_json(
                data["configurationNeeded"]
            )
        )
    if data.get("accessLevel") is not None:
        import capo_continuum.types.signal_access_precondition

        out["access_level"] = (
            capo_continuum.types.signal_access_precondition.deserialize_json(
                data["accessLevel"]
            )
        )
    if data.get("userInteractionRequired") is not None:
        import capo_continuum.types.signal_precondition

        out["user_interaction_required"] = (
            capo_continuum.types.signal_precondition.deserialize_json(
                data["userInteractionRequired"]
            )
        )
    return out
