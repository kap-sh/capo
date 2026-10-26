"""Generated from Smithy shape ``com.amazonaws.xray#IndexingRuleValue``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_xray.errors import DeserializationError, SerializationError
from capo_xray.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_xray.types.probabilistic_rule_value


class _IndexingRuleValue_Probabilistic(TypedDict, closed=True):
    Probabilistic: "capo_xray.types.probabilistic_rule_value.ProbabilisticRuleValue"


IndexingRuleValue: TypeAlias = _IndexingRuleValue_Probabilistic | UnknownUnionMember


# --- restJson1 ser/de ---
def serialize_json(value: IndexingRuleValue) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"IndexingRuleValue: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "Probabilistic" in value:
        import capo_xray.types.probabilistic_rule_value

        return {
            "Probabilistic": capo_xray.types.probabilistic_rule_value.serialize_json(
                value["Probabilistic"]
            )
        }
    else:
        raise SerializationError("IndexingRuleValue: no variant present")


def deserialize_json(data: dict) -> IndexingRuleValue:
    if data.get("Probabilistic") is not None:
        import capo_xray.types.probabilistic_rule_value

        return {
            "Probabilistic": capo_xray.types.probabilistic_rule_value.deserialize_json(
                data["Probabilistic"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("IndexingRuleValue: no recognized variant key")
