"""Generated from Smithy shape ``com.amazonaws.vpclattice#UpdateListenerRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_vpc_lattice.types.listener_identifier
    import capo_vpc_lattice.types.rule_action
    import capo_vpc_lattice.types.service_identifier


class UpdateListenerRequest(TypedDict, closed=True):
    service_identifier: "capo_vpc_lattice.types.service_identifier.ServiceIdentifier"
    """<p>The ID or ARN of the service.</p>"""
    listener_identifier: "capo_vpc_lattice.types.listener_identifier.ListenerIdentifier"
    """<p>The ID or ARN of the listener.</p>"""
    default_action: "capo_vpc_lattice.types.rule_action.RuleAction"
    """<p>The action for the default rule.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateListenerRequest) -> dict:
    out: dict = {}
    import capo_vpc_lattice.types.rule_action

    out["defaultAction"] = capo_vpc_lattice.types.rule_action.serialize_json(
        value["default_action"]
    )
    return out


def deserialize_json(data: dict) -> UpdateListenerRequest:
    out: UpdateListenerRequest = {}  # type: ignore[typeddict-item]
    if data.get("defaultAction") is not None:
        import capo_vpc_lattice.types.rule_action

        out["default_action"] = capo_vpc_lattice.types.rule_action.deserialize_json(
            data["defaultAction"]
        )
    else:
        import capo_vpc_lattice.types._unknown

        out["default_action"] = capo_vpc_lattice.types._unknown.UnknownUnionMember("")
    return out
