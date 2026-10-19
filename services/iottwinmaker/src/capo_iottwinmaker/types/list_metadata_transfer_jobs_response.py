"""Generated from Smithy shape ``com.amazonaws.iottwinmaker#ListMetadataTransferJobsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iottwinmaker.types.metadata_transfer_job_summaries
    import capo_iottwinmaker.types.next_token


class ListMetadataTransferJobsResponse(TypedDict, closed=True):
    metadata_transfer_job_summaries: "capo_iottwinmaker.types.metadata_transfer_job_summaries.MetadataTransferJobSummaries"
    """<p>The metadata transfer job summaries.</p>"""
    next_token: NotRequired["capo_iottwinmaker.types.next_token.NextToken"]
    """<p>The string that specifies the next page of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListMetadataTransferJobsResponse) -> dict:
    out: dict = {}
    import capo_iottwinmaker.types.metadata_transfer_job_summaries

    out["metadataTransferJobSummaries"] = (
        capo_iottwinmaker.types.metadata_transfer_job_summaries.serialize_json(
            value["metadata_transfer_job_summaries"]
        )
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListMetadataTransferJobsResponse:
    out: ListMetadataTransferJobsResponse = {}  # type: ignore[typeddict-item]
    if data.get("metadataTransferJobSummaries") is not None:
        import capo_iottwinmaker.types.metadata_transfer_job_summaries

        out["metadata_transfer_job_summaries"] = (
            capo_iottwinmaker.types.metadata_transfer_job_summaries.deserialize_json(
                data["metadataTransferJobSummaries"]
            )
        )
    else:
        out["metadata_transfer_job_summaries"] = []
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
