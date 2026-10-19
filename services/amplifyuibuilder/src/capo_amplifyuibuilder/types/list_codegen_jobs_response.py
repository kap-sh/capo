"""Generated from Smithy shape ``com.amazonaws.amplifyuibuilder#ListCodegenJobsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_amplifyuibuilder.types.codegen_job_summary_list


class ListCodegenJobsResponse(TypedDict, closed=True):
    entities: (
        "capo_amplifyuibuilder.types.codegen_job_summary_list.CodegenJobSummaryList"
    )
    """<p>The list of code generation jobs for the Amplify app.</p>"""
    next_token: NotRequired["str"]
    """<p>The pagination token that's included if more results are available.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListCodegenJobsResponse) -> dict:
    out: dict = {}
    import capo_amplifyuibuilder.types.codegen_job_summary_list

    out["entities"] = (
        capo_amplifyuibuilder.types.codegen_job_summary_list.serialize_json(
            value["entities"]
        )
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListCodegenJobsResponse:
    out: ListCodegenJobsResponse = {}  # type: ignore[typeddict-item]
    if data.get("entities") is not None:
        import capo_amplifyuibuilder.types.codegen_job_summary_list

        out["entities"] = (
            capo_amplifyuibuilder.types.codegen_job_summary_list.deserialize_json(
                data["entities"]
            )
        )
    else:
        out["entities"] = []
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
