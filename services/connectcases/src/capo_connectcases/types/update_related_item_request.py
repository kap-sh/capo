"""Generated from Smithy shape ``com.amazonaws.connectcases#UpdateRelatedItemRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connectcases.types.case_id
    import capo_connectcases.types.domain_id
    import capo_connectcases.types.related_item_id
    import capo_connectcases.types.related_item_update_content
    import capo_connectcases.types.user_union


class UpdateRelatedItemRequest(TypedDict, closed=True):
    domain_id: "capo_connectcases.types.domain_id.DomainId"
    """<p>The unique identifier of the Cases domain. </p>"""
    case_id: "capo_connectcases.types.case_id.CaseId"
    """<p>A unique identifier of the case.</p>"""
    related_item_id: "capo_connectcases.types.related_item_id.RelatedItemId"
    """<p>Unique identifier of a related item.</p>"""
    content: (
        "capo_connectcases.types.related_item_update_content.RelatedItemUpdateContent"
    )
    """<p>The content of a related item to be updated.</p>"""
    performed_by: NotRequired["capo_connectcases.types.user_union.UserUnion"]
    """<p>Represents the user who performed the update of the related item.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateRelatedItemRequest) -> dict:
    out: dict = {}
    import capo_connectcases.types.related_item_update_content

    out["content"] = capo_connectcases.types.related_item_update_content.serialize_json(
        value["content"]
    )
    if "performed_by" in value:
        import capo_connectcases.types.user_union

        out["performedBy"] = capo_connectcases.types.user_union.serialize_json(
            value["performed_by"]
        )
    return out


def deserialize_json(data: dict) -> UpdateRelatedItemRequest:
    out: UpdateRelatedItemRequest = {}  # type: ignore[typeddict-item]
    if data.get("content") is not None:
        import capo_connectcases.types.related_item_update_content

        out["content"] = (
            capo_connectcases.types.related_item_update_content.deserialize_json(
                data["content"]
            )
        )
    else:
        import capo_connectcases.types._unknown

        out["content"] = capo_connectcases.types._unknown.UnknownUnionMember("")
    if data.get("performedBy") is not None:
        import capo_connectcases.types.user_union

        out["performed_by"] = capo_connectcases.types.user_union.deserialize_json(
            data["performedBy"]
        )
    return out


def redact_sensitive(value: UpdateRelatedItemRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "performed_by" in value:
        import capo_connectcases.types.user_union

        out["performed_by"] = capo_connectcases.types.user_union.redact_sensitive(
            value["performed_by"]
        )
    return out
