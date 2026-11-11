"""Generated from Smithy shape ``com.amazonaws.connectcases#BatchCreateRelatedItemRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connectcases.types.batch_create_related_item_identifier_list
    import capo_connectcases.types.domain_id
    import capo_connectcases.types.related_item_input_content
    import capo_connectcases.types.user_union


class BatchCreateRelatedItemRequest(TypedDict, closed=True):
    domain_id: "capo_connectcases.types.domain_id.DomainId"
    """<p>The unique identifier of the Cases domain. </p>"""
    content: (
        "capo_connectcases.types.related_item_input_content.RelatedItemInputContent"
    )
    """<p>The content of the related item to be created. The same content is applied to every case in the request. Only comment content is supported for batch creation.</p>"""
    cases: "capo_connectcases.types.batch_create_related_item_identifier_list.BatchCreateRelatedItemIdentifierList"
    """<p>The list of cases to associate the related item with. All cases must belong to the same domain.</p>"""
    performed_by: NotRequired["capo_connectcases.types.user_union.UserUnion"]
    """<p>The entity that created the related item.</p>"""
    client_token: NotRequired["str"]
    """<p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If not provided, the Amazon Web Services SDK populates this field. For more information about idempotency, see <a href="https://aws.amazon.com/builders-library/making-retries-safe-with-idempotent-APIs/">Making retries safe with idempotent APIs</a>.</p> <p>If you retry a request with the same client token, the service returns the original response instead of processing the request again. If you reuse a client token with different request parameters, the request fails with a <code>ConflictException</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchCreateRelatedItemRequest) -> dict:
    out: dict = {}
    out["domainId"] = value["domain_id"]
    import capo_connectcases.types.related_item_input_content

    out["content"] = capo_connectcases.types.related_item_input_content.serialize_json(
        value["content"]
    )
    import capo_connectcases.types.batch_create_related_item_identifier_list

    out["cases"] = (
        capo_connectcases.types.batch_create_related_item_identifier_list.serialize_json(
            value["cases"]
        )
    )
    if "performed_by" in value:
        import capo_connectcases.types.user_union

        out["performedBy"] = capo_connectcases.types.user_union.serialize_json(
            value["performed_by"]
        )
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    return out


def deserialize_json(data: dict) -> BatchCreateRelatedItemRequest:
    out: BatchCreateRelatedItemRequest = {}  # type: ignore[typeddict-item]
    if data.get("domainId") is not None:
        out["domain_id"] = data["domainId"]
    else:
        out["domain_id"] = ""
    if data.get("content") is not None:
        import capo_connectcases.types.related_item_input_content

        out["content"] = (
            capo_connectcases.types.related_item_input_content.deserialize_json(
                data["content"]
            )
        )
    else:
        out["content"] = {"$unknown": {"name": ""}}
    if data.get("cases") is not None:
        import capo_connectcases.types.batch_create_related_item_identifier_list

        out["cases"] = (
            capo_connectcases.types.batch_create_related_item_identifier_list.deserialize_json(
                data["cases"]
            )
        )
    else:
        out["cases"] = []
    if data.get("performedBy") is not None:
        import capo_connectcases.types.user_union

        out["performed_by"] = capo_connectcases.types.user_union.deserialize_json(
            data["performedBy"]
        )
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    return out


def redact_sensitive(value: BatchCreateRelatedItemRequest) -> dict[str, Any]:
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
