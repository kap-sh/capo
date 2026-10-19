"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#RetrievalFilter``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_bedrock_agent_runtime.errors import DeserializationError, SerializationError
from capo_bedrock_agent_runtime.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_bedrock_agent_runtime.types.filter_attribute
    import capo_bedrock_agent_runtime.types.retrieval_filter_list


class _RetrievalFilter_equals(TypedDict, closed=True):
    equals: "capo_bedrock_agent_runtime.types.filter_attribute.FilterAttribute"


class _RetrievalFilter_notEquals(TypedDict, closed=True):
    notEquals: "capo_bedrock_agent_runtime.types.filter_attribute.FilterAttribute"


class _RetrievalFilter_greaterThan(TypedDict, closed=True):
    greaterThan: "capo_bedrock_agent_runtime.types.filter_attribute.FilterAttribute"


class _RetrievalFilter_greaterThanOrEquals(TypedDict, closed=True):
    greaterThanOrEquals: (
        "capo_bedrock_agent_runtime.types.filter_attribute.FilterAttribute"
    )


class _RetrievalFilter_lessThan(TypedDict, closed=True):
    lessThan: "capo_bedrock_agent_runtime.types.filter_attribute.FilterAttribute"


class _RetrievalFilter_lessThanOrEquals(TypedDict, closed=True):
    lessThanOrEquals: (
        "capo_bedrock_agent_runtime.types.filter_attribute.FilterAttribute"
    )


_RetrievalFilter_in = TypedDict(
    "_RetrievalFilter_in",
    {
        "in": "capo_bedrock_agent_runtime.types.filter_attribute.FilterAttribute",
    },
    closed=True,
)


class _RetrievalFilter_notIn(TypedDict, closed=True):
    notIn: "capo_bedrock_agent_runtime.types.filter_attribute.FilterAttribute"


class _RetrievalFilter_startsWith(TypedDict, closed=True):
    startsWith: "capo_bedrock_agent_runtime.types.filter_attribute.FilterAttribute"


class _RetrievalFilter_listContains(TypedDict, closed=True):
    listContains: "capo_bedrock_agent_runtime.types.filter_attribute.FilterAttribute"


class _RetrievalFilter_stringContains(TypedDict, closed=True):
    stringContains: "capo_bedrock_agent_runtime.types.filter_attribute.FilterAttribute"


class _RetrievalFilter_andAll(TypedDict, closed=True):
    andAll: "capo_bedrock_agent_runtime.types.retrieval_filter_list.RetrievalFilterList"


class _RetrievalFilter_orAll(TypedDict, closed=True):
    orAll: "capo_bedrock_agent_runtime.types.retrieval_filter_list.RetrievalFilterList"


RetrievalFilter: TypeAlias = (
    _RetrievalFilter_equals
    | _RetrievalFilter_notEquals
    | _RetrievalFilter_greaterThan
    | _RetrievalFilter_greaterThanOrEquals
    | _RetrievalFilter_lessThan
    | _RetrievalFilter_lessThanOrEquals
    | _RetrievalFilter_in
    | _RetrievalFilter_notIn
    | _RetrievalFilter_startsWith
    | _RetrievalFilter_listContains
    | _RetrievalFilter_stringContains
    | _RetrievalFilter_andAll
    | _RetrievalFilter_orAll
    | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: RetrievalFilter) -> dict:
    if isinstance(value, UnknownUnionMember):
        raise SerializationError(
            f"RetrievalFilter: cannot serialize unknown variant {value.name!r}"
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
            return UnknownUnionMember(name)
        raise DeserializationError("RetrievalFilter: no recognized variant key")
