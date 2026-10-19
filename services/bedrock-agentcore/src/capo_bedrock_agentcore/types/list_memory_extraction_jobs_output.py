"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#ListMemoryExtractionJobsOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore.types.extraction_job_metadata_list
    import capo_bedrock_agentcore.types.pagination_token


class ListMemoryExtractionJobsOutput(TypedDict, closed=True):
    jobs: "capo_bedrock_agentcore.types.extraction_job_metadata_list.ExtractionJobMetadataList"
    """<p>List of extraction job metadata matching the specified criteria.</p>"""
    next_token: NotRequired[
        "capo_bedrock_agentcore.types.pagination_token.PaginationToken"
    ]
    """<p>Token to retrieve the next page of results, if available.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListMemoryExtractionJobsOutput) -> dict:
    out: dict = {}
    import capo_bedrock_agentcore.types.extraction_job_metadata_list

    out["jobs"] = (
        capo_bedrock_agentcore.types.extraction_job_metadata_list.serialize_json(
            value["jobs"]
        )
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListMemoryExtractionJobsOutput:
    out: ListMemoryExtractionJobsOutput = {}  # type: ignore[typeddict-item]
    if data.get("jobs") is not None:
        import capo_bedrock_agentcore.types.extraction_job_metadata_list

        out["jobs"] = (
            capo_bedrock_agentcore.types.extraction_job_metadata_list.deserialize_json(
                data["jobs"]
            )
        )
    else:
        out["jobs"] = []
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
