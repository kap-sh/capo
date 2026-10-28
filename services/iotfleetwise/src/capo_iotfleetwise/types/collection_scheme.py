"""Generated from Smithy shape ``com.amazonaws.iotfleetwise#CollectionScheme``."""

from typing import TYPE_CHECKING, Any, TypeAlias

from typing_extensions import TypedDict

from capo_iotfleetwise.errors import DeserializationError, SerializationError
from capo_iotfleetwise.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_iotfleetwise.types.condition_based_collection_scheme
    import capo_iotfleetwise.types.time_based_collection_scheme


class CollectionSchemeTimeBasedCollectionSchemeMember(TypedDict, closed=True):
    timeBasedCollectionScheme: (
        "capo_iotfleetwise.types.time_based_collection_scheme.TimeBasedCollectionScheme"
    )


class CollectionSchemeConditionBasedCollectionSchemeMember(TypedDict, closed=True):
    conditionBasedCollectionScheme: "capo_iotfleetwise.types.condition_based_collection_scheme.ConditionBasedCollectionScheme"


CollectionScheme: TypeAlias = (
    CollectionSchemeTimeBasedCollectionSchemeMember
    | CollectionSchemeConditionBasedCollectionSchemeMember
    | UnknownUnionMember
)


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CollectionScheme) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"CollectionScheme: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "timeBasedCollectionScheme" in value:
        import capo_iotfleetwise.types.time_based_collection_scheme

        return {
            "timeBasedCollectionScheme": capo_iotfleetwise.types.time_based_collection_scheme.serialize_aws_json_1_0(
                value["timeBasedCollectionScheme"]
            )
        }
    elif "conditionBasedCollectionScheme" in value:
        import capo_iotfleetwise.types.condition_based_collection_scheme

        return {
            "conditionBasedCollectionScheme": capo_iotfleetwise.types.condition_based_collection_scheme.serialize_aws_json_1_0(
                value["conditionBasedCollectionScheme"]
            )
        }
    else:
        raise SerializationError("CollectionScheme: no variant present")


def deserialize_aws_json_1_0(data: dict) -> CollectionScheme:
    if data.get("timeBasedCollectionScheme") is not None:
        import capo_iotfleetwise.types.time_based_collection_scheme

        return {
            "timeBasedCollectionScheme": capo_iotfleetwise.types.time_based_collection_scheme.deserialize_aws_json_1_0(
                data["timeBasedCollectionScheme"]
            )
        }
    elif data.get("conditionBasedCollectionScheme") is not None:
        import capo_iotfleetwise.types.condition_based_collection_scheme

        return {
            "conditionBasedCollectionScheme": capo_iotfleetwise.types.condition_based_collection_scheme.deserialize_aws_json_1_0(
                data["conditionBasedCollectionScheme"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("CollectionScheme: no recognized variant key")


def redact_sensitive(value: CollectionScheme) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "conditionBasedCollectionScheme" in value:
        import capo_iotfleetwise.types.condition_based_collection_scheme

        out["conditionBasedCollectionScheme"] = (
            capo_iotfleetwise.types.condition_based_collection_scheme.redact_sensitive(
                value["conditionBasedCollectionScheme"]
            )
        )
    return out
