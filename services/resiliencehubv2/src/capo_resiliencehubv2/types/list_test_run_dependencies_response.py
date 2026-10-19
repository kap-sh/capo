"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#ListTestRunDependenciesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_resiliencehubv2.types.next_token
    import capo_resiliencehubv2.types.test_run_dependency_summary_list


class ListTestRunDependenciesResponse(TypedDict, closed=True):
    dependencies: "capo_resiliencehubv2.types.test_run_dependency_summary_list.TestRunDependencySummaryList"
    """<p>The list of dependencies the test run blocked.</p>"""
    next_token: NotRequired["capo_resiliencehubv2.types.next_token.NextToken"]


# --- restJson1 ser/de ---
def serialize_json(value: ListTestRunDependenciesResponse) -> dict:
    out: dict = {}
    import capo_resiliencehubv2.types.test_run_dependency_summary_list

    out["dependencies"] = (
        capo_resiliencehubv2.types.test_run_dependency_summary_list.serialize_json(
            value["dependencies"]
        )
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListTestRunDependenciesResponse:
    out: ListTestRunDependenciesResponse = {}  # type: ignore[typeddict-item]
    if data.get("dependencies") is not None:
        import capo_resiliencehubv2.types.test_run_dependency_summary_list

        out["dependencies"] = (
            capo_resiliencehubv2.types.test_run_dependency_summary_list.deserialize_json(
                data["dependencies"]
            )
        )
    else:
        out["dependencies"] = []
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
