"""Generated from Smithy shape ``com.amazonaws.connectcases#UpdateCaseRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_connectcases.errors import DeserializationError

if TYPE_CHECKING:
    import capo_connectcases.types.case_id
    import capo_connectcases.types.domain_id
    import capo_connectcases.types.field_value_list
    import capo_connectcases.types.user_union


class UpdateCaseRequest(TypedDict, closed=True):
    domain_id: "capo_connectcases.types.domain_id.DomainId"
    """<p>The unique identifier of the Cases domain. </p>"""
    case_id: "capo_connectcases.types.case_id.CaseId"
    """<p>A unique identifier of the case.</p>"""
    fields: "capo_connectcases.types.field_value_list.FieldValueList"
    """<p>An array of objects with <code>fieldId</code> (matching ListFields/DescribeField) and value union data, structured identical to <code>CreateCase</code>.</p>"""
    performed_by: NotRequired["capo_connectcases.types.user_union.UserUnion"]


# --- restJson1 ser/de ---
def serialize_json(value: UpdateCaseRequest) -> dict:
    out: dict = {}
    import capo_connectcases.types.field_value_list

    out["fields"] = capo_connectcases.types.field_value_list.serialize_json(
        value["fields"]
    )
    if "performed_by" in value:
        import capo_connectcases.types.user_union

        out["performedBy"] = capo_connectcases.types.user_union.serialize_json(
            value["performed_by"]
        )
    return out


def deserialize_json(data: dict) -> UpdateCaseRequest:
    out: UpdateCaseRequest = {}  # type: ignore[typeddict-item]
    if data.get("fields") is not None:
        import capo_connectcases.types.field_value_list

        out["fields"] = capo_connectcases.types.field_value_list.deserialize_json(
            data["fields"]
        )
    else:
        raise DeserializationError("UpdateCaseRequest.fields required")
    if data.get("performedBy") is not None:
        import capo_connectcases.types.user_union

        out["performed_by"] = capo_connectcases.types.user_union.deserialize_json(
            data["performedBy"]
        )
    return out


def redact_sensitive(value: UpdateCaseRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "performed_by" in value:
        import capo_connectcases.types.user_union

        out["performed_by"] = capo_connectcases.types.user_union.redact_sensitive(
            value["performed_by"]
        )
    return out
