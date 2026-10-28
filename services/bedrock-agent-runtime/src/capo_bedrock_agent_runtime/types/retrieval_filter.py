"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#RetrievalFilter``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_bedrock_agent_runtime.errors import DeserializationError, SerializationError
from capo_bedrock_agent_runtime.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_bedrock_agent_runtime.types.filter_attribute
    import capo_bedrock_agent_runtime.types.retrieval_filter_list


class RetrievalFilterEqualsMember(TypedDict, closed=True):
    equals: "capo_bedrock_agent_runtime.types.filter_attribute.FilterAttribute"


class RetrievalFilterNotEqualsMember(TypedDict, closed=True):
    notEquals: "capo_bedrock_agent_runtime.types.filter_attribute.FilterAttribute"


class RetrievalFilterGreaterThanMember(TypedDict, closed=True):
    greaterThan: "capo_bedrock_agent_runtime.types.filter_attribute.FilterAttribute"


class RetrievalFilterGreaterThanOrEqualsMember(TypedDict, closed=True):
    greaterThanOrEquals: (
        "capo_bedrock_agent_runtime.types.filter_attribute.FilterAttribute"
    )


class RetrievalFilterLessThanMember(TypedDict, closed=True):
    lessThan: "capo_bedrock_agent_runtime.types.filter_attribute.FilterAttribute"


class RetrievalFilterLessThanOrEqualsMember(TypedDict, closed=True):
    lessThanOrEquals: (
        "capo_bedrock_agent_runtime.types.filter_attribute.FilterAttribute"
    )


RetrievalFilterInMember = TypedDict(
    "RetrievalFilterInMember",
    {
        "in": "capo_bedrock_agent_runtime.types.filter_attribute.FilterAttribute",
    },
    closed=True,
)


class RetrievalFilterNotInMember(TypedDict, closed=True):
    notIn: "capo_bedrock_agent_runtime.types.filter_attribute.FilterAttribute"


class RetrievalFilterStartsWithMember(TypedDict, closed=True):
    startsWith: "capo_bedrock_agent_runtime.types.filter_attribute.FilterAttribute"


class RetrievalFilterListContainsMember(TypedDict, closed=True):
    listContains: "capo_bedrock_agent_runtime.types.filter_attribute.FilterAttribute"


class RetrievalFilterStringContainsMember(TypedDict, closed=True):
    stringContains: "capo_bedrock_agent_runtime.types.filter_attribute.FilterAttribute"


class RetrievalFilterAndAllMember(TypedDict, closed=True):
    andAll: "capo_bedrock_agent_runtime.types.retrieval_filter_list.RetrievalFilterList"


class RetrievalFilterOrAllMember(TypedDict, closed=True):
    orAll: "capo_bedrock_agent_runtime.types.retrieval_filter_list.RetrievalFilterList"


RetrievalFilter: TypeAlias = (
    RetrievalFilterEqualsMember
    | RetrievalFilterNotEqualsMember
    | RetrievalFilterGreaterThanMember
    | RetrievalFilterGreaterThanOrEqualsMember
    | RetrievalFilterLessThanMember
    | RetrievalFilterLessThanOrEqualsMember
    | RetrievalFilterInMember
    | RetrievalFilterNotInMember
    | RetrievalFilterStartsWithMember
    | RetrievalFilterListContainsMember
    | RetrievalFilterStringContainsMember
    | RetrievalFilterAndAllMember
    | RetrievalFilterOrAllMember
    | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: RetrievalFilter) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"RetrievalFilter: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "equals" in value:
        import capo_bedrock_agent_runtime.types.filter_attribute

        return {
            "equals": capo_bedrock_agent_runtime.types.filter_attribute.serialize_json(
                value["equals"]
            )
        }
    elif "notEquals" in value:
        import capo_bedrock_agent_runtime.types.filter_attribute

        return {
            "notEquals": capo_bedrock_agent_runtime.types.filter_attribute.serialize_json(
                value["notEquals"]
            )
        }
    elif "greaterThan" in value:
        import capo_bedrock_agent_runtime.types.filter_attribute

        return {
            "greaterThan": capo_bedrock_agent_runtime.types.filter_attribute.serialize_json(
                value["greaterThan"]
            )
        }
    elif "greaterThanOrEquals" in value:
        import capo_bedrock_agent_runtime.types.filter_attribute

        return {
            "greaterThanOrEquals": capo_bedrock_agent_runtime.types.filter_attribute.serialize_json(
                value["greaterThanOrEquals"]
            )
        }
    elif "lessThan" in value:
        import capo_bedrock_agent_runtime.types.filter_attribute

        return {
            "lessThan": capo_bedrock_agent_runtime.types.filter_attribute.serialize_json(
                value["lessThan"]
            )
        }
    elif "lessThanOrEquals" in value:
        import capo_bedrock_agent_runtime.types.filter_attribute

        return {
            "lessThanOrEquals": capo_bedrock_agent_runtime.types.filter_attribute.serialize_json(
                value["lessThanOrEquals"]
            )
        }
    elif "in" in value:
        import capo_bedrock_agent_runtime.types.filter_attribute

        return {
            "in": capo_bedrock_agent_runtime.types.filter_attribute.serialize_json(
                value["in"]
            )
        }
    elif "notIn" in value:
        import capo_bedrock_agent_runtime.types.filter_attribute

        return {
            "notIn": capo_bedrock_agent_runtime.types.filter_attribute.serialize_json(
                value["notIn"]
            )
        }
    elif "startsWith" in value:
        import capo_bedrock_agent_runtime.types.filter_attribute

        return {
            "startsWith": capo_bedrock_agent_runtime.types.filter_attribute.serialize_json(
                value["startsWith"]
            )
        }
    elif "listContains" in value:
        import capo_bedrock_agent_runtime.types.filter_attribute

        return {
            "listContains": capo_bedrock_agent_runtime.types.filter_attribute.serialize_json(
                value["listContains"]
            )
        }
    elif "stringContains" in value:
        import capo_bedrock_agent_runtime.types.filter_attribute

        return {
            "stringContains": capo_bedrock_agent_runtime.types.filter_attribute.serialize_json(
                value["stringContains"]
            )
        }
    elif "andAll" in value:
        import capo_bedrock_agent_runtime.types.retrieval_filter_list

        return {
            "andAll": capo_bedrock_agent_runtime.types.retrieval_filter_list.serialize_json(
                value["andAll"]
            )
        }
    elif "orAll" in value:
        import capo_bedrock_agent_runtime.types.retrieval_filter_list

        return {
            "orAll": capo_bedrock_agent_runtime.types.retrieval_filter_list.serialize_json(
                value["orAll"]
            )
        }
    else:
        raise SerializationError("RetrievalFilter: no variant present")


def deserialize_json(data: dict) -> RetrievalFilter:
    if data.get("equals") is not None:
        import capo_bedrock_agent_runtime.types.filter_attribute

        return {
            "equals": capo_bedrock_agent_runtime.types.filter_attribute.deserialize_json(
                data["equals"]
            )
        }
    elif data.get("notEquals") is not None:
        import capo_bedrock_agent_runtime.types.filter_attribute

        return {
            "notEquals": capo_bedrock_agent_runtime.types.filter_attribute.deserialize_json(
                data["notEquals"]
            )
        }
    elif data.get("greaterThan") is not None:
        import capo_bedrock_agent_runtime.types.filter_attribute

        return {
            "greaterThan": capo_bedrock_agent_runtime.types.filter_attribute.deserialize_json(
                data["greaterThan"]
            )
        }
    elif data.get("greaterThanOrEquals") is not None:
        import capo_bedrock_agent_runtime.types.filter_attribute

        return {
            "greaterThanOrEquals": capo_bedrock_agent_runtime.types.filter_attribute.deserialize_json(
                data["greaterThanOrEquals"]
            )
        }
    elif data.get("lessThan") is not None:
        import capo_bedrock_agent_runtime.types.filter_attribute

        return {
            "lessThan": capo_bedrock_agent_runtime.types.filter_attribute.deserialize_json(
                data["lessThan"]
            )
        }
    elif data.get("lessThanOrEquals") is not None:
        import capo_bedrock_agent_runtime.types.filter_attribute

        return {
            "lessThanOrEquals": capo_bedrock_agent_runtime.types.filter_attribute.deserialize_json(
                data["lessThanOrEquals"]
            )
        }
    elif data.get("in") is not None:
        import capo_bedrock_agent_runtime.types.filter_attribute

        return {
            "in": capo_bedrock_agent_runtime.types.filter_attribute.deserialize_json(
                data["in"]
            )
        }
    elif data.get("notIn") is not None:
        import capo_bedrock_agent_runtime.types.filter_attribute

        return {
            "notIn": capo_bedrock_agent_runtime.types.filter_attribute.deserialize_json(
                data["notIn"]
            )
        }
    elif data.get("startsWith") is not None:
        import capo_bedrock_agent_runtime.types.filter_attribute

        return {
            "startsWith": capo_bedrock_agent_runtime.types.filter_attribute.deserialize_json(
                data["startsWith"]
            )
        }
    elif data.get("listContains") is not None:
        import capo_bedrock_agent_runtime.types.filter_attribute

        return {
            "listContains": capo_bedrock_agent_runtime.types.filter_attribute.deserialize_json(
                data["listContains"]
            )
        }
    elif data.get("stringContains") is not None:
        import capo_bedrock_agent_runtime.types.filter_attribute

        return {
            "stringContains": capo_bedrock_agent_runtime.types.filter_attribute.deserialize_json(
                data["stringContains"]
            )
        }
    elif data.get("andAll") is not None:
        import capo_bedrock_agent_runtime.types.retrieval_filter_list

        return {
            "andAll": capo_bedrock_agent_runtime.types.retrieval_filter_list.deserialize_json(
                data["andAll"]
            )
        }
    elif data.get("orAll") is not None:
        import capo_bedrock_agent_runtime.types.retrieval_filter_list

        return {
            "orAll": capo_bedrock_agent_runtime.types.retrieval_filter_list.deserialize_json(
                data["orAll"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("RetrievalFilter: no recognized variant key")
