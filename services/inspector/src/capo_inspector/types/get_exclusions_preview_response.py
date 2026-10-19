"""Generated from Smithy shape ``com.amazonaws.inspector#GetExclusionsPreviewResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_inspector.types.exclusion_preview_list
    import capo_inspector.types.pagination_token
    import capo_inspector.types.preview_status


class GetExclusionsPreviewResponse(TypedDict, closed=True):
    preview_status: "capo_inspector.types.preview_status.PreviewStatus"
    """<p>Specifies the status of the request to generate an exclusions preview.</p>"""
    exclusion_previews: NotRequired[
        "capo_inspector.types.exclusion_preview_list.ExclusionPreviewList"
    ]
    """<p>Information about the exclusions included in the preview.</p>"""
    next_token: NotRequired["capo_inspector.types.pagination_token.PaginationToken"]
    """<p>When a response is generated, if there is more data to be listed, this parameters is present in the response and contains the value to use for the nextToken parameter in a subsequent pagination request. If there is no more data to be listed, this parameter is set to null.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetExclusionsPreviewResponse) -> dict:
    out: dict = {}
    import capo_inspector.types.preview_status

    out["previewStatus"] = capo_inspector.types.preview_status.serialize_aws_json_1_1(
        value["preview_status"]
    )
    if "exclusion_previews" in value:
        import capo_inspector.types.exclusion_preview_list

        out["exclusionPreviews"] = (
            capo_inspector.types.exclusion_preview_list.serialize_aws_json_1_1(
                value["exclusion_previews"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetExclusionsPreviewResponse:
    out: GetExclusionsPreviewResponse = {}  # type: ignore[typeddict-item]
    if data.get("previewStatus") is not None:
        import capo_inspector.types.preview_status

        out["preview_status"] = (
            capo_inspector.types.preview_status.deserialize_aws_json_1_1(
                data["previewStatus"]
            )
        )
    else:
        import typing

        out["preview_status"] = typing.cast(
            "capo_inspector.types.preview_status.PreviewStatus", ""
        )
    if data.get("exclusionPreviews") is not None:
        import capo_inspector.types.exclusion_preview_list

        out["exclusion_previews"] = (
            capo_inspector.types.exclusion_preview_list.deserialize_aws_json_1_1(
                data["exclusionPreviews"]
            )
        )
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
