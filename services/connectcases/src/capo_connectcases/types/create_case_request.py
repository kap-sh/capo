"""Generated from Smithy shape ``com.amazonaws.connectcases#CreateCaseRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_connectcases.errors import DeserializationError

if TYPE_CHECKING:
    import capo_connectcases.types.domain_id
    import capo_connectcases.types.field_value_list
    import capo_connectcases.types.mutable_tags
    import capo_connectcases.types.template_id
    import capo_connectcases.types.user_union


class CreateCaseRequest(TypedDict, closed=True):
    domain_id: "capo_connectcases.types.domain_id.DomainId"
    """<p>The unique identifier of the Cases domain. </p>"""
    template_id: "capo_connectcases.types.template_id.TemplateId"
    """<p>A unique identifier of a template.</p>"""
    fields: "capo_connectcases.types.field_value_list.FieldValueList"
    """<p>An array of objects with field ID (matching ListFields/DescribeField) and value union data.</p>"""
    client_token: NotRequired["str"]
    """<p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If not provided, the Amazon Web Services SDK populates this field. For more information about idempotency, see <a href="https://aws.amazon.com/builders-library/making-retries-safe-with-idempotent-APIs/">Making retries safe with idempotent APIs</a>.</p>"""
    performed_by: NotRequired["capo_connectcases.types.user_union.UserUnion"]
    tags: NotRequired["capo_connectcases.types.mutable_tags.MutableTags"]
    """<p>A map of of key-value pairs that represent tags on a resource. Tags are used to organize, track, or control access for this resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateCaseRequest) -> dict:
    out: dict = {}
    out["templateId"] = value["template_id"]
    import capo_connectcases.types.field_value_list

    out["fields"] = capo_connectcases.types.field_value_list.serialize_json(
        value["fields"]
    )
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    if "performed_by" in value:
        import capo_connectcases.types.user_union

        out["performedBy"] = capo_connectcases.types.user_union.serialize_json(
            value["performed_by"]
        )
    if "tags" in value:
        import capo_connectcases.types.mutable_tags

        out["tags"] = capo_connectcases.types.mutable_tags.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> CreateCaseRequest:
    out: CreateCaseRequest = {}  # type: ignore[typeddict-item]
    if data.get("templateId") is not None:
        out["template_id"] = data["templateId"]
    else:
        raise DeserializationError("CreateCaseRequest.template_id required")
    if data.get("fields") is not None:
        import capo_connectcases.types.field_value_list

        out["fields"] = capo_connectcases.types.field_value_list.deserialize_json(
            data["fields"]
        )
    else:
        raise DeserializationError("CreateCaseRequest.fields required")
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    if data.get("performedBy") is not None:
        import capo_connectcases.types.user_union

        out["performed_by"] = capo_connectcases.types.user_union.deserialize_json(
            data["performedBy"]
        )
    if data.get("tags") is not None:
        import capo_connectcases.types.mutable_tags

        out["tags"] = capo_connectcases.types.mutable_tags.deserialize_json(
            data["tags"]
        )
    return out
