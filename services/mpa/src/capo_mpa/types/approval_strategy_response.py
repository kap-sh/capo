"""Generated from Smithy shape ``com.amazonaws.mpa#ApprovalStrategyResponse``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_mpa.errors import DeserializationError, SerializationError
from capo_mpa.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_mpa.types.mof_n_approval_strategy


class _ApprovalStrategyResponse_MofN(TypedDict, closed=True):
    MofN: "capo_mpa.types.mof_n_approval_strategy.MofNApprovalStrategy"


ApprovalStrategyResponse: TypeAlias = (
    _ApprovalStrategyResponse_MofN | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: ApprovalStrategyResponse) -> dict:
    if isinstance(value, UnknownUnionMember):
        raise SerializationError(
            f"ApprovalStrategyResponse: cannot serialize unknown variant {value.name!r}"
        )
    elif "MofN" in value:
        import capo_mpa.types.mof_n_approval_strategy

        return {
            "MofN": capo_mpa.types.mof_n_approval_strategy.serialize_json(value["MofN"])
        }
    else:
        raise SerializationError("ApprovalStrategyResponse: no variant present")


def deserialize_json(data: dict) -> ApprovalStrategyResponse:
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
            return UnknownUnionMember(name)
        raise DeserializationError(
            "ApprovalStrategyResponse: no recognized variant key"
        )
