"""Generated from Smithy shape ``com.amazonaws.servicecatalog#ListLaunchPathsOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_service_catalog.types.launch_path_summaries
    import capo_service_catalog.types.page_token


class ListLaunchPathsOutput(TypedDict, closed=True):
    launch_path_summaries: NotRequired[
        "capo_service_catalog.types.launch_path_summaries.LaunchPathSummaries"
    ]
    """<p>Information about the launch path.</p>"""
    next_page_token: NotRequired["capo_service_catalog.types.page_token.PageToken"]
    """<p>The page token to use to retrieve the next set of results. If there are no additional results, this value is null.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListLaunchPathsOutput) -> dict:
    out: dict = {}
    if "launch_path_summaries" in value:
        import capo_service_catalog.types.launch_path_summaries

        out["LaunchPathSummaries"] = (
            capo_service_catalog.types.launch_path_summaries.serialize_aws_json_1_1(
                value["launch_path_summaries"]
            )
        )
    if "next_page_token" in value:
        out["NextPageToken"] = value["next_page_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListLaunchPathsOutput:
    out: ListLaunchPathsOutput = {}  # type: ignore[typeddict-item]
    if data.get("LaunchPathSummaries") is not None:
        import capo_service_catalog.types.launch_path_summaries

        out["launch_path_summaries"] = (
            capo_service_catalog.types.launch_path_summaries.deserialize_aws_json_1_1(
                data["LaunchPathSummaries"]
            )
        )
    if data.get("NextPageToken") is not None:
        out["next_page_token"] = data["NextPageToken"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ListLaunchPathsOutput) -> dict:
    out: dict = {}
    if "launch_path_summaries" in value:
        import capo_service_catalog.types.launch_path_summaries

        out["LaunchPathSummaries"] = (
            capo_service_catalog.types.launch_path_summaries.serialize_cbor(
                value["launch_path_summaries"]
            )
        )
    if "next_page_token" in value:
        out["NextPageToken"] = value["next_page_token"]
    return out


def deserialize_cbor(data: dict) -> ListLaunchPathsOutput:
    out: ListLaunchPathsOutput = {}  # type: ignore[typeddict-item]
    if data.get("LaunchPathSummaries") is not None:
        import capo_service_catalog.types.launch_path_summaries

        out["launch_path_summaries"] = (
            capo_service_catalog.types.launch_path_summaries.deserialize_cbor(
                data["LaunchPathSummaries"]
            )
        )
    if data.get("NextPageToken") is not None:
        out["next_page_token"] = data["NextPageToken"]
    return out
