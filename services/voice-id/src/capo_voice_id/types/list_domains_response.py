"""Generated from Smithy shape ``com.amazonaws.voiceid#ListDomainsResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_voice_id.types.domain_summaries
    import capo_voice_id.types.string


class ListDomainsResponse(TypedDict, closed=True):
    domain_summaries: NotRequired[
        "capo_voice_id.types.domain_summaries.DomainSummaries"
    ]
    """<p>A list containing details about each domain in the Amazon Web Services account.</p>"""
    next_token: NotRequired["capo_voice_id.types.string.String"]
    """<p>If <code>NextToken</code> is returned, there are more results available. The value of <code>NextToken</code> is a unique pagination token for each page. Make the call again using the returned token to retrieve the next page. Keep all other arguments unchanged. Each pagination token expires after 24 hours.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListDomainsResponse) -> dict:
    out: dict = {}
    if "domain_summaries" in value:
        import capo_voice_id.types.domain_summaries

        out["DomainSummaries"] = (
            capo_voice_id.types.domain_summaries.serialize_aws_json_1_0(
                value["domain_summaries"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ListDomainsResponse:
    out: ListDomainsResponse = {}  # type: ignore[typeddict-item]
    if data.get("DomainSummaries") is not None:
        import capo_voice_id.types.domain_summaries

        out["domain_summaries"] = (
            capo_voice_id.types.domain_summaries.deserialize_aws_json_1_0(
                data["DomainSummaries"]
            )
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out


def redact_sensitive(value: ListDomainsResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "domain_summaries" in value:
        import capo_voice_id.types.domain_summaries

        out["domain_summaries"] = capo_voice_id.types.domain_summaries.redact_sensitive(
            value["domain_summaries"]
        )
    return out
