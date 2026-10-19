"""Generated from Smithy shape ``com.amazonaws.m2#ListBatchJobDefinitionsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_m2.types.batch_job_definitions
    import capo_m2.types.next_token


class ListBatchJobDefinitionsResponse(TypedDict, closed=True):
    batch_job_definitions: "capo_m2.types.batch_job_definitions.BatchJobDefinitions"
    """<p>The list of batch job definitions.</p>"""
    next_token: NotRequired["capo_m2.types.next_token.NextToken"]
    """<p>If there are more items to return, this contains a token that is passed to a subsequent call to this operation to retrieve the next set of items.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListBatchJobDefinitionsResponse) -> dict:
    out: dict = {}
    import capo_m2.types.batch_job_definitions

    out["batchJobDefinitions"] = capo_m2.types.batch_job_definitions.serialize_json(
        value["batch_job_definitions"]
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListBatchJobDefinitionsResponse:
    out: ListBatchJobDefinitionsResponse = {}  # type: ignore[typeddict-item]
    if data.get("batchJobDefinitions") is not None:
        import capo_m2.types.batch_job_definitions

        out["batch_job_definitions"] = (
            capo_m2.types.batch_job_definitions.deserialize_json(
                data["batchJobDefinitions"]
            )
        )
    else:
        out["batch_job_definitions"] = []
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
