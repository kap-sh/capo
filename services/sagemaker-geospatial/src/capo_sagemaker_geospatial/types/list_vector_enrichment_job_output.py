"""Generated from Smithy shape ``com.amazonaws.sagemakergeospatial#ListVectorEnrichmentJobOutput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker_geospatial.types.next_token
    import capo_sagemaker_geospatial.types.vector_enrichment_job_list


class ListVectorEnrichmentJobOutput(TypedDict, closed=True):
    vector_enrichment_job_summaries: "capo_sagemaker_geospatial.types.vector_enrichment_job_list.VectorEnrichmentJobList"
    """<p>Contains summary information about the Vector Enrichment jobs.</p>"""
    next_token: NotRequired["capo_sagemaker_geospatial.types.next_token.NextToken"]
    """<p>If the previous response was truncated, you receive this token. Use it in your next request to receive the next set of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListVectorEnrichmentJobOutput) -> dict:
    out: dict = {}
    import capo_sagemaker_geospatial.types.vector_enrichment_job_list

    out["VectorEnrichmentJobSummaries"] = (
        capo_sagemaker_geospatial.types.vector_enrichment_job_list.serialize_json(
            value["vector_enrichment_job_summaries"]
        )
    )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListVectorEnrichmentJobOutput:
    out: ListVectorEnrichmentJobOutput = {}  # type: ignore[typeddict-item]
    if data.get("VectorEnrichmentJobSummaries") is not None:
        import capo_sagemaker_geospatial.types.vector_enrichment_job_list

        out["vector_enrichment_job_summaries"] = (
            capo_sagemaker_geospatial.types.vector_enrichment_job_list.deserialize_json(
                data["VectorEnrichmentJobSummaries"]
            )
        )
    else:
        out["vector_enrichment_job_summaries"] = []
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out


def redact_sensitive(value: ListVectorEnrichmentJobOutput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "next_token" in value:
        out["next_token"] = "*** Sensitive Data Redacted ***"
    return out
