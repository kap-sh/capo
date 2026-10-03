"""Generated from Smithy shape ``com.amazonaws.qconnect#SearchQuickResponsesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_qconnect.errors import DeserializationError

if TYPE_CHECKING:
    import capo_qconnect.types.contact_attributes
    import capo_qconnect.types.max_results
    import capo_qconnect.types.non_empty_string
    import capo_qconnect.types.quick_response_search_expression
    import capo_qconnect.types.uuid_or_arn


class SearchQuickResponsesRequest(TypedDict, closed=True):
    knowledge_base_id: "capo_qconnect.types.uuid_or_arn.UuidOrArn"
    """<p>The identifier of the knowledge base. This should be a QUICK_RESPONSES type knowledge base. Can be either the ID or the ARN. URLs cannot contain the ARN.</p>"""
    search_expression: "capo_qconnect.types.quick_response_search_expression.QuickResponseSearchExpression"
    """<p>The search expression for querying the quick response.</p>"""
    next_token: NotRequired["capo_qconnect.types.non_empty_string.NonEmptyString"]
    """<p>The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.</p>"""
    max_results: NotRequired["capo_qconnect.types.max_results.MaxResults"]
    """<p>The maximum number of results to return per page.</p>"""
    attributes: NotRequired["capo_qconnect.types.contact_attributes.ContactAttributes"]
    """<p>The <a href="https://docs.aws.amazon.com/connect/latest/adminguide/connect-attrib-list.html#user-defined-attributes">user-defined Connect Customer contact attributes</a> to be resolved when search results are returned.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SearchQuickResponsesRequest) -> dict:
    out: dict = {}
    import capo_qconnect.types.quick_response_search_expression

    out["searchExpression"] = (
        capo_qconnect.types.quick_response_search_expression.serialize_json(
            value["search_expression"]
        )
    )
    if "attributes" in value:
        import capo_qconnect.types.contact_attributes

        out["attributes"] = capo_qconnect.types.contact_attributes.serialize_json(
            value["attributes"]
        )
    return out


def deserialize_json(data: dict) -> SearchQuickResponsesRequest:
    out: SearchQuickResponsesRequest = {}  # type: ignore[typeddict-item]
    if data.get("searchExpression") is not None:
        import capo_qconnect.types.quick_response_search_expression

        out["search_expression"] = (
            capo_qconnect.types.quick_response_search_expression.deserialize_json(
                data["searchExpression"]
            )
        )
    else:
        raise DeserializationError(
            "SearchQuickResponsesRequest.search_expression required"
        )
    if data.get("attributes") is not None:
        import capo_qconnect.types.contact_attributes

        out["attributes"] = capo_qconnect.types.contact_attributes.deserialize_json(
            data["attributes"]
        )
    return out
