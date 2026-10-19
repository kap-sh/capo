"""Generated from Smithy shape ``com.amazonaws.glue#ListGlossaryTermsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_glue.types.glossary_id
    import capo_glue.types.page_size
    import capo_glue.types.token


class ListGlossaryTermsRequest(TypedDict, closed=True):
    glossary_identifier: "capo_glue.types.glossary_id.GlossaryId"
    """<p>The unique identifier of the glossary whose terms to list.</p>"""
    max_results: NotRequired["capo_glue.types.page_size.PageSize"]
    """<p>The maximum number of results to return in the response.</p>"""
    next_token: NotRequired["capo_glue.types.token.Token"]
    """<p>A continuation token, if this is a continuation call.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListGlossaryTermsRequest) -> dict:
    out: dict = {}
    out["GlossaryIdentifier"] = value["glossary_identifier"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListGlossaryTermsRequest:
    out: ListGlossaryTermsRequest = {}  # type: ignore[typeddict-item]
    if data.get("GlossaryIdentifier") is not None:
        out["glossary_identifier"] = data["GlossaryIdentifier"]
    else:
        out["glossary_identifier"] = ""
    if data.get("MaxResults") is not None:
        out["max_results"] = data["MaxResults"]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
