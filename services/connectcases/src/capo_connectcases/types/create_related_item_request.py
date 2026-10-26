"""Generated from Smithy shape ``com.amazonaws.connectcases#CreateRelatedItemRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connectcases.types.case_id
    import capo_connectcases.types.domain_id
    import capo_connectcases.types.related_item_input_content
    import capo_connectcases.types.related_item_type
    import capo_connectcases.types.user_union


class CreateRelatedItemRequest(TypedDict, closed=True):
    domain_id: "capo_connectcases.types.domain_id.DomainId"
    """<p>The unique identifier of the Cases domain. </p>"""
    case_id: "capo_connectcases.types.case_id.CaseId"
    """<p>A unique identifier of the case.</p>"""
    type: "capo_connectcases.types.related_item_type.RelatedItemType"
    """<p>The type of a related item.</p>"""
    content: (
        "capo_connectcases.types.related_item_input_content.RelatedItemInputContent"
    )
    """<p>The content of a related item to be created.</p>"""
    performed_by: NotRequired["capo_connectcases.types.user_union.UserUnion"]
    """<p>Represents the creator of the related item.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateRelatedItemRequest) -> dict:
    out: dict = {}
    out["type"] = value["type"]
    import capo_connectcases.types.related_item_input_content

    out["content"] = capo_connectcases.types.related_item_input_content.serialize_json(
        value["content"]
    )
    if "performed_by" in value:
        import capo_connectcases.types.user_union

        out["performedBy"] = capo_connectcases.types.user_union.serialize_json(
            value["performed_by"]
        )
    return out


def deserialize_json(data: dict) -> CreateRelatedItemRequest:
    out: CreateRelatedItemRequest = {}  # type: ignore[typeddict-item]
    if data.get("type") is not None:
        out["type"] = data["type"]
    else:
        out["type"] = ""
    if data.get("content") is not None:
        import capo_connectcases.types.related_item_input_content

        out["content"] = (
            capo_connectcases.types.related_item_input_content.deserialize_json(
                data["content"]
            )
        )
    else:
        out["content"] = {"$unknown": {"name": ""}}
    if data.get("performedBy") is not None:
        import capo_connectcases.types.user_union

        out["performed_by"] = capo_connectcases.types.user_union.deserialize_json(
            data["performedBy"]
        )
    return out


def redact_sensitive(value: CreateRelatedItemRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "content" in value:
        import capo_connectcases.types.related_item_input_content

        out["content"] = (
            capo_connectcases.types.related_item_input_content.redact_sensitive(
                value["content"]
            )
        )
    if "performed_by" in value:
        import capo_connectcases.types.user_union

        out["performed_by"] = capo_connectcases.types.user_union.redact_sensitive(
            value["performed_by"]
        )
    return out
