"""Generated from Smithy shape ``com.amazonaws.vpclattice#RuleAction``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_vpc_lattice.errors import DeserializationError, SerializationError
from capo_vpc_lattice.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_vpc_lattice.types.fixed_response_action
    import capo_vpc_lattice.types.forward_action


class _RuleAction_forward(TypedDict, closed=True):
    forward: "capo_vpc_lattice.types.forward_action.ForwardAction"


class _RuleAction_fixedResponse(TypedDict, closed=True):
    fixedResponse: "capo_vpc_lattice.types.fixed_response_action.FixedResponseAction"


RuleAction: TypeAlias = (
    _RuleAction_forward | _RuleAction_fixedResponse | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: RuleAction) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"RuleAction: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "forward" in value:
        import capo_vpc_lattice.types.forward_action

        return {
            "forward": capo_vpc_lattice.types.forward_action.serialize_json(
                value["forward"]
            )
        }
    elif "fixedResponse" in value:
        import capo_vpc_lattice.types.fixed_response_action

        return {
            "fixedResponse": capo_vpc_lattice.types.fixed_response_action.serialize_json(
                value["fixedResponse"]
            )
        }
    else:
        raise SerializationError("RuleAction: no variant present")


def deserialize_json(data: dict) -> RuleAction:
    if data.get("forward") is not None:
        import capo_vpc_lattice.types.forward_action

        return {
            "forward": capo_vpc_lattice.types.forward_action.deserialize_json(
                data["forward"]
            )
        }
    elif data.get("fixedResponse") is not None:
        import capo_vpc_lattice.types.fixed_response_action

        return {
            "fixedResponse": capo_vpc_lattice.types.fixed_response_action.deserialize_json(
                data["fixedResponse"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("RuleAction: no recognized variant key")
