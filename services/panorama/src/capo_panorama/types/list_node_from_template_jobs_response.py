"""Generated from Smithy shape ``com.amazonaws.panorama#ListNodeFromTemplateJobsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_panorama.types.next_token
    import capo_panorama.types.node_from_template_job_list


class ListNodeFromTemplateJobsResponse(TypedDict, closed=True):
    node_from_template_jobs: (
        "capo_panorama.types.node_from_template_job_list.NodeFromTemplateJobList"
    )
    """<p>A list of jobs.</p>"""
    next_token: NotRequired["capo_panorama.types.next_token.NextToken"]
    """<p>A pagination token that's included if more results are available.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListNodeFromTemplateJobsResponse) -> dict:
    out: dict = {}
    import capo_panorama.types.node_from_template_job_list

    out["NodeFromTemplateJobs"] = (
        capo_panorama.types.node_from_template_job_list.serialize_json(
            value["node_from_template_jobs"]
        )
    )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListNodeFromTemplateJobsResponse:
    out: ListNodeFromTemplateJobsResponse = {}  # type: ignore[typeddict-item]
    if data.get("NodeFromTemplateJobs") is not None:
        import capo_panorama.types.node_from_template_job_list

        out["node_from_template_jobs"] = (
            capo_panorama.types.node_from_template_job_list.deserialize_json(
                data["NodeFromTemplateJobs"]
            )
        )
    else:
        out["node_from_template_jobs"] = []
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
