"""Generated from Smithy shape ``com.amazonaws.xray#IndexingRuleValueUpdate``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_xray.errors import DeserializationError, SerializationError
from capo_xray.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_xray.types.probabilistic_rule_value_update


class _IndexingRuleValueUpdate_Probabilistic(TypedDict, closed=True):
    Probabilistic: (
        "capo_xray.types.probabilistic_rule_value_update.ProbabilisticRuleValueUpdate"
    )


IndexingRuleValueUpdate: TypeAlias = (
    _IndexingRuleValueUpdate_Probabilistic | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: IndexingRuleValueUpdate) -> dict:
    if isinstance(value, UnknownUnionMember):
        raise SerializationError(
            f"IndexingRuleValueUpdate: cannot serialize unknown variant {value.name!r}"
        )
    elif "Probabilistic" in value:
        import capo_xray.types.probabilistic_rule_value_update

        return {
            "Probabilistic": capo_xray.types.probabilistic_rule_value_update.serialize_json(
                value["Probabilistic"]
            )
        }
    else:
        raise SerializationError("IndexingRuleValueUpdate: no variant present")


def deserialize_json(data: dict) -> IndexingRuleValueUpdate:
    if data.get("Probabilistic") is not None:
        import capo_xray.types.probabilistic_rule_value_update

        return {
            "Probabilistic": capo_xray.types.probabilistic_rule_value_update.deserialize_json(
                data["Probabilistic"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return UnknownUnionMember(name)
        raise DeserializationError("IndexingRuleValueUpdate: no recognized variant key")
