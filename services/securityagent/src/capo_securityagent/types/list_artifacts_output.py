"""Generated from Smithy shape ``com.amazonaws.securityagent#ListArtifactsOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityagent.types.artifact_summary_list
    import capo_securityagent.types.next_token


class ListArtifactsOutput(TypedDict, closed=True):
    artifact_summaries: (
        "capo_securityagent.types.artifact_summary_list.ArtifactSummaryList"
    )
    """<p>The list of artifact summaries.</p>"""
    next_token: NotRequired["capo_securityagent.types.next_token.NextToken"]
    """<p>A token to use for paginating results that are returned in the response. Set the value of this parameter to null for the first request. For subsequent calls, use the nextToken value returned from the previous request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListArtifactsOutput) -> dict:
    out: dict = {}
    import capo_securityagent.types.artifact_summary_list

    out["artifactSummaries"] = (
        capo_securityagent.types.artifact_summary_list.serialize_json(
            value["artifact_summaries"]
        )
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListArtifactsOutput:
    out: ListArtifactsOutput = {}  # type: ignore[typeddict-item]
    if data.get("artifactSummaries") is not None:
        import capo_securityagent.types.artifact_summary_list

        out["artifact_summaries"] = (
            capo_securityagent.types.artifact_summary_list.deserialize_json(
                data["artifactSummaries"]
            )
        )
    else:
        out["artifact_summaries"] = []
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
