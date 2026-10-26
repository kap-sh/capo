"""Generated from Smithy shape ``com.amazonaws.qconnect#RetrievalFilterConfiguration``."""

from typing import TYPE_CHECKING, Any, TypeAlias

from typing_extensions import TypedDict

from capo_qconnect.errors import DeserializationError, SerializationError
from capo_qconnect.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_qconnect.types.filter_attribute
    import capo_qconnect.types.retrieval_filter_list


class _RetrievalFilterConfiguration_andAll(TypedDict, closed=True):
    andAll: "capo_qconnect.types.retrieval_filter_list.RetrievalFilterList"


class _RetrievalFilterConfiguration_equals(TypedDict, closed=True):
    equals: "capo_qconnect.types.filter_attribute.FilterAttribute"


class _RetrievalFilterConfiguration_greaterThan(TypedDict, closed=True):
    greaterThan: "capo_qconnect.types.filter_attribute.FilterAttribute"


class _RetrievalFilterConfiguration_greaterThanOrEquals(TypedDict, closed=True):
    greaterThanOrEquals: "capo_qconnect.types.filter_attribute.FilterAttribute"


_RetrievalFilterConfiguration_in = TypedDict(
    "_RetrievalFilterConfiguration_in",
    {
        "in": "capo_qconnect.types.filter_attribute.FilterAttribute",
    },
    closed=True,
)


class _RetrievalFilterConfiguration_lessThan(TypedDict, closed=True):
    lessThan: "capo_qconnect.types.filter_attribute.FilterAttribute"


class _RetrievalFilterConfiguration_lessThanOrEquals(TypedDict, closed=True):
    lessThanOrEquals: "capo_qconnect.types.filter_attribute.FilterAttribute"


class _RetrievalFilterConfiguration_listContains(TypedDict, closed=True):
    listContains: "capo_qconnect.types.filter_attribute.FilterAttribute"


class _RetrievalFilterConfiguration_notEquals(TypedDict, closed=True):
    notEquals: "capo_qconnect.types.filter_attribute.FilterAttribute"


class _RetrievalFilterConfiguration_notIn(TypedDict, closed=True):
    notIn: "capo_qconnect.types.filter_attribute.FilterAttribute"


class _RetrievalFilterConfiguration_orAll(TypedDict, closed=True):
    orAll: "capo_qconnect.types.retrieval_filter_list.RetrievalFilterList"


class _RetrievalFilterConfiguration_startsWith(TypedDict, closed=True):
    startsWith: "capo_qconnect.types.filter_attribute.FilterAttribute"


class _RetrievalFilterConfiguration_stringContains(TypedDict, closed=True):
    stringContains: "capo_qconnect.types.filter_attribute.FilterAttribute"


RetrievalFilterConfiguration: TypeAlias = (
    _RetrievalFilterConfiguration_andAll
    | _RetrievalFilterConfiguration_equals
    | _RetrievalFilterConfiguration_greaterThan
    | _RetrievalFilterConfiguration_greaterThanOrEquals
    | _RetrievalFilterConfiguration_in
    | _RetrievalFilterConfiguration_lessThan
    | _RetrievalFilterConfiguration_lessThanOrEquals
    | _RetrievalFilterConfiguration_listContains
    | _RetrievalFilterConfiguration_notEquals
    | _RetrievalFilterConfiguration_notIn
    | _RetrievalFilterConfiguration_orAll
    | _RetrievalFilterConfiguration_startsWith
    | _RetrievalFilterConfiguration_stringContains
    | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: RetrievalFilterConfiguration) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"RetrievalFilterConfiguration: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "andAll" in value:
        import capo_qconnect.types.retrieval_filter_list

        return {
            "andAll": capo_qconnect.types.retrieval_filter_list.serialize_json(
                value["andAll"]
            )
        }
    elif "equals" in value:
        import capo_qconnect.types.filter_attribute

        return {
            "equals": capo_qconnect.types.filter_attribute.serialize_json(
                value["equals"]
            )
        }
    elif "greaterThan" in value:
        import capo_qconnect.types.filter_attribute

        return {
            "greaterThan": capo_qconnect.types.filter_attribute.serialize_json(
                value["greaterThan"]
            )
        }
    elif "greaterThanOrEquals" in value:
        import capo_qconnect.types.filter_attribute

        return {
            "greaterThanOrEquals": capo_qconnect.types.filter_attribute.serialize_json(
                value["greaterThanOrEquals"]
            )
        }
    elif "in" in value:
        import capo_qconnect.types.filter_attribute

        return {"in": capo_qconnect.types.filter_attribute.serialize_json(value["in"])}
    elif "lessThan" in value:
        import capo_qconnect.types.filter_attribute

        return {
            "lessThan": capo_qconnect.types.filter_attribute.serialize_json(
                value["lessThan"]
            )
        }
    elif "lessThanOrEquals" in value:
        import capo_qconnect.types.filter_attribute

        return {
            "lessThanOrEquals": capo_qconnect.types.filter_attribute.serialize_json(
                value["lessThanOrEquals"]
            )
        }
    elif "listContains" in value:
        import capo_qconnect.types.filter_attribute

        return {
            "listContains": capo_qconnect.types.filter_attribute.serialize_json(
                value["listContains"]
            )
        }
    elif "notEquals" in value:
        import capo_qconnect.types.filter_attribute

        return {
            "notEquals": capo_qconnect.types.filter_attribute.serialize_json(
                value["notEquals"]
            )
        }
    elif "notIn" in value:
        import capo_qconnect.types.filter_attribute

        return {
            "notIn": capo_qconnect.types.filter_attribute.serialize_json(value["notIn"])
        }
    elif "orAll" in value:
        import capo_qconnect.types.retrieval_filter_list

        return {
            "orAll": capo_qconnect.types.retrieval_filter_list.serialize_json(
                value["orAll"]
            )
        }
    elif "startsWith" in value:
        import capo_qconnect.types.filter_attribute

        return {
            "startsWith": capo_qconnect.types.filter_attribute.serialize_json(
                value["startsWith"]
            )
        }
    elif "stringContains" in value:
        import capo_qconnect.types.filter_attribute

        return {
            "stringContains": capo_qconnect.types.filter_attribute.serialize_json(
                value["stringContains"]
            )
        }
    else:
        raise SerializationError("RetrievalFilterConfiguration: no variant present")


def deserialize_json(data: dict) -> RetrievalFilterConfiguration:
    if data.get("andAll") is not None:
        import capo_qconnect.types.retrieval_filter_list

        return {
            "andAll": capo_qconnect.types.retrieval_filter_list.deserialize_json(
                data["andAll"]
            )
        }
    elif data.get("equals") is not None:
        import capo_qconnect.types.filter_attribute

        return {
            "equals": capo_qconnect.types.filter_attribute.deserialize_json(
                data["equals"]
            )
        }
    elif data.get("greaterThan") is not None:
        import capo_qconnect.types.filter_attribute

        return {
            "greaterThan": capo_qconnect.types.filter_attribute.deserialize_json(
                data["greaterThan"]
            )
        }
    elif data.get("greaterThanOrEquals") is not None:
        import capo_qconnect.types.filter_attribute

        return {
            "greaterThanOrEquals": capo_qconnect.types.filter_attribute.deserialize_json(
                data["greaterThanOrEquals"]
            )
        }
    elif data.get("in") is not None:
        import capo_qconnect.types.filter_attribute

        return {"in": capo_qconnect.types.filter_attribute.deserialize_json(data["in"])}
    elif data.get("lessThan") is not None:
        import capo_qconnect.types.filter_attribute

        return {
            "lessThan": capo_qconnect.types.filter_attribute.deserialize_json(
                data["lessThan"]
            )
        }
    elif data.get("lessThanOrEquals") is not None:
        import capo_qconnect.types.filter_attribute

        return {
            "lessThanOrEquals": capo_qconnect.types.filter_attribute.deserialize_json(
                data["lessThanOrEquals"]
            )
        }
    elif data.get("listContains") is not None:
        import capo_qconnect.types.filter_attribute

        return {
            "listContains": capo_qconnect.types.filter_attribute.deserialize_json(
                data["listContains"]
            )
        }
    elif data.get("notEquals") is not None:
        import capo_qconnect.types.filter_attribute

        return {
            "notEquals": capo_qconnect.types.filter_attribute.deserialize_json(
                data["notEquals"]
            )
        }
    elif data.get("notIn") is not None:
        import capo_qconnect.types.filter_attribute

        return {
            "notIn": capo_qconnect.types.filter_attribute.deserialize_json(
                data["notIn"]
            )
        }
    elif data.get("orAll") is not None:
        import capo_qconnect.types.retrieval_filter_list

        return {
            "orAll": capo_qconnect.types.retrieval_filter_list.deserialize_json(
                data["orAll"]
            )
        }
    elif data.get("startsWith") is not None:
        import capo_qconnect.types.filter_attribute

        return {
            "startsWith": capo_qconnect.types.filter_attribute.deserialize_json(
                data["startsWith"]
            )
        }
    elif data.get("stringContains") is not None:
        import capo_qconnect.types.filter_attribute

        return {
            "stringContains": capo_qconnect.types.filter_attribute.deserialize_json(
                data["stringContains"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError(
            "RetrievalFilterConfiguration: no recognized variant key"
        )


def redact_sensitive(value: RetrievalFilterConfiguration) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "andAll" in value:
        import capo_qconnect.types.retrieval_filter_list

        out["andAll"] = capo_qconnect.types.retrieval_filter_list.redact_sensitive(
            value["andAll"]
        )
    if "equals" in value:
        import capo_qconnect.types.filter_attribute

        out["equals"] = capo_qconnect.types.filter_attribute.redact_sensitive(
            value["equals"]
        )
    if "greaterThan" in value:
        import capo_qconnect.types.filter_attribute

        out["greaterThan"] = capo_qconnect.types.filter_attribute.redact_sensitive(
            value["greaterThan"]
        )
    if "greaterThanOrEquals" in value:
        import capo_qconnect.types.filter_attribute

        out["greaterThanOrEquals"] = (
            capo_qconnect.types.filter_attribute.redact_sensitive(
                value["greaterThanOrEquals"]
            )
        )
    if "in" in value:
        import capo_qconnect.types.filter_attribute

        out["in"] = capo_qconnect.types.filter_attribute.redact_sensitive(value["in"])
    if "lessThan" in value:
        import capo_qconnect.types.filter_attribute

        out["lessThan"] = capo_qconnect.types.filter_attribute.redact_sensitive(
            value["lessThan"]
        )
    if "lessThanOrEquals" in value:
        import capo_qconnect.types.filter_attribute

        out["lessThanOrEquals"] = capo_qconnect.types.filter_attribute.redact_sensitive(
            value["lessThanOrEquals"]
        )
    if "listContains" in value:
        import capo_qconnect.types.filter_attribute

        out["listContains"] = capo_qconnect.types.filter_attribute.redact_sensitive(
            value["listContains"]
        )
    if "notEquals" in value:
        import capo_qconnect.types.filter_attribute

        out["notEquals"] = capo_qconnect.types.filter_attribute.redact_sensitive(
            value["notEquals"]
        )
    if "notIn" in value:
        import capo_qconnect.types.filter_attribute

        out["notIn"] = capo_qconnect.types.filter_attribute.redact_sensitive(
            value["notIn"]
        )
    if "orAll" in value:
        import capo_qconnect.types.retrieval_filter_list

        out["orAll"] = capo_qconnect.types.retrieval_filter_list.redact_sensitive(
            value["orAll"]
        )
    if "startsWith" in value:
        import capo_qconnect.types.filter_attribute

        out["startsWith"] = capo_qconnect.types.filter_attribute.redact_sensitive(
            value["startsWith"]
        )
    if "stringContains" in value:
        import capo_qconnect.types.filter_attribute

        out["stringContains"] = capo_qconnect.types.filter_attribute.redact_sensitive(
            value["stringContains"]
        )
    return out
