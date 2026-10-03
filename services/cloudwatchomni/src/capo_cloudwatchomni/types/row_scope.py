"""Generated from Smithy shape ``com.amazonaws.cloudwatchomni#RowScope``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_cloudwatchomni.errors import DeserializationError

if TYPE_CHECKING:
    import capo_cloudwatchomni.types.row_scope_operator
    import capo_cloudwatchomni.types.row_scope_value_list


class RowScope(TypedDict, closed=True):
    field: "str"
    """The field (column) the allowlist applies to (e.g., "serviceName", "accountId")."""
    operator: "capo_cloudwatchomni.types.row_scope_operator.RowScopeOperator"
    """Match operator applied to this filter's values."""
    values: "capo_cloudwatchomni.types.row_scope_value_list.RowScopeValueList"
    """The values the field is matched against."""


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: RowScope) -> dict:
    out: dict = {}
    out["field"] = value["field"]
    import capo_cloudwatchomni.types.row_scope_operator

    out["operator"] = capo_cloudwatchomni.types.row_scope_operator.serialize_cbor(
        value["operator"]
    )
    import capo_cloudwatchomni.types.row_scope_value_list

    out["values"] = capo_cloudwatchomni.types.row_scope_value_list.serialize_cbor(
        value["values"]
    )
    return out


def deserialize_cbor(data: dict) -> RowScope:
    out: RowScope = {}  # type: ignore[typeddict-item]
    if data.get("field") is not None:
        out["field"] = data["field"]
    else:
        raise DeserializationError("RowScope.field required")
    if data.get("operator") is not None:
        import capo_cloudwatchomni.types.row_scope_operator

        out["operator"] = capo_cloudwatchomni.types.row_scope_operator.deserialize_cbor(
            data["operator"]
        )
    else:
        raise DeserializationError("RowScope.operator required")
    if data.get("values") is not None:
        import capo_cloudwatchomni.types.row_scope_value_list

        out["values"] = capo_cloudwatchomni.types.row_scope_value_list.deserialize_cbor(
            data["values"]
        )
    else:
        raise DeserializationError("RowScope.values required")
    return out
