"""Generated from Smithy shape ``com.amazonaws.mpa#ApprovalStrategy``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_mpa.errors import DeserializationError, SerializationError
from capo_mpa.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_mpa.types.mof_n_approval_strategy


class ApprovalStrategyMofNMember(TypedDict, closed=True):
    MofN: "capo_mpa.types.mof_n_approval_strategy.MofNApprovalStrategy"


ApprovalStrategy: TypeAlias = ApprovalStrategyMofNMember | UnknownUnionMember


# --- restJson1 ser/de ---
def serialize_json(value: ApprovalStrategy) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"ApprovalStrategy: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "MofN" in value:
        import capo_mpa.types.mof_n_approval_strategy

        return {
            "MofN": capo_mpa.types.mof_n_approval_strategy.serialize_json(value["MofN"])
        }
    else:
        raise SerializationError("ApprovalStrategy: no variant present")


def deserialize_json(data: dict) -> ApprovalStrategy:
    if data.get("MofN") is not None:
        import capo_mpa.types.mof_n_approval_strategy

        return {
            "MofN": capo_mpa.types.mof_n_approval_strategy.deserialize_json(
                data["MofN"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("ApprovalStrategy: no recognized variant key")
