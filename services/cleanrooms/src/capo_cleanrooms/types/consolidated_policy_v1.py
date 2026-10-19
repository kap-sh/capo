"""Generated from Smithy shape ``com.amazonaws.cleanrooms#ConsolidatedPolicyV1``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_cleanrooms.errors import DeserializationError, SerializationError
from capo_cleanrooms.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_cleanrooms.types.consolidated_policy_aggregation
    import capo_cleanrooms.types.consolidated_policy_custom
    import capo_cleanrooms.types.consolidated_policy_list


class _ConsolidatedPolicyV1_list(TypedDict, closed=True):
    list: "capo_cleanrooms.types.consolidated_policy_list.ConsolidatedPolicyList"


class _ConsolidatedPolicyV1_aggregation(TypedDict, closed=True):
    aggregation: "capo_cleanrooms.types.consolidated_policy_aggregation.ConsolidatedPolicyAggregation"


class _ConsolidatedPolicyV1_custom(TypedDict, closed=True):
    custom: "capo_cleanrooms.types.consolidated_policy_custom.ConsolidatedPolicyCustom"


ConsolidatedPolicyV1: TypeAlias = (
    _ConsolidatedPolicyV1_list
    | _ConsolidatedPolicyV1_aggregation
    | _ConsolidatedPolicyV1_custom
    | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: ConsolidatedPolicyV1) -> dict:
    if isinstance(value, UnknownUnionMember):
        raise SerializationError(
            f"ConsolidatedPolicyV1: cannot serialize unknown variant {value.name!r}"
        )
    elif "list" in value:
        import capo_cleanrooms.types.consolidated_policy_list

        return {
            "list": capo_cleanrooms.types.consolidated_policy_list.serialize_json(
                value["list"]
            )
        }
    elif "aggregation" in value:
        import capo_cleanrooms.types.consolidated_policy_aggregation

        return {
            "aggregation": capo_cleanrooms.types.consolidated_policy_aggregation.serialize_json(
                value["aggregation"]
            )
        }
    elif "custom" in value:
        import capo_cleanrooms.types.consolidated_policy_custom

        return {
            "custom": capo_cleanrooms.types.consolidated_policy_custom.serialize_json(
                value["custom"]
            )
        }
    else:
        raise SerializationError("ConsolidatedPolicyV1: no variant present")


def deserialize_json(data: dict) -> ConsolidatedPolicyV1:
    if data.get("list") is not None:
        import capo_cleanrooms.types.consolidated_policy_list

        return {
            "list": capo_cleanrooms.types.consolidated_policy_list.deserialize_json(
                data["list"]
            )
        }
    elif data.get("aggregation") is not None:
        import capo_cleanrooms.types.consolidated_policy_aggregation

        return {
            "aggregation": capo_cleanrooms.types.consolidated_policy_aggregation.deserialize_json(
                data["aggregation"]
            )
        }
    elif data.get("custom") is not None:
        import capo_cleanrooms.types.consolidated_policy_custom

        return {
            "custom": capo_cleanrooms.types.consolidated_policy_custom.deserialize_json(
                data["custom"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return UnknownUnionMember(name)
        raise DeserializationError("ConsolidatedPolicyV1: no recognized variant key")
