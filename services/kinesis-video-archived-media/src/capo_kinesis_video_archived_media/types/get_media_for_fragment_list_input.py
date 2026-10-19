"""Generated from Smithy shape ``com.amazonaws.kinesisvideoarchivedmedia#GetMediaForFragmentListInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_kinesis_video_archived_media.types.fragment_number_list
    import capo_kinesis_video_archived_media.types.resource_arn
    import capo_kinesis_video_archived_media.types.stream_name


class GetMediaForFragmentListInput(TypedDict, closed=True):
    stream_name: NotRequired[
        "capo_kinesis_video_archived_media.types.stream_name.StreamName"
    ]
    """<p>The name of the stream from which to retrieve fragment media. Specify either this parameter or the <code>StreamARN</code> parameter.</p>"""
    stream_arn: NotRequired[
        "capo_kinesis_video_archived_media.types.resource_arn.ResourceARN"
    ]
    """<p>The Amazon Resource Name (ARN) of the stream from which to retrieve fragment media. Specify either this parameter or the <code>StreamName</code> parameter.</p>"""
    fragments: "capo_kinesis_video_archived_media.types.fragment_number_list.FragmentNumberList"
    """<p>A list of the numbers of fragments for which to retrieve media. You retrieve these values with <a>ListFragments</a>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetMediaForFragmentListInput) -> dict:
    out: dict = {}
    if "stream_name" in value:
        out["StreamName"] = value["stream_name"]
    if "stream_arn" in value:
        out["StreamARN"] = value["stream_arn"]
    import capo_kinesis_video_archived_media.types.fragment_number_list

    out["Fragments"] = (
        capo_kinesis_video_archived_media.types.fragment_number_list.serialize_json(
            value["fragments"]
        )
    )
    return out


def deserialize_json(data: dict) -> GetMediaForFragmentListInput:
    out: GetMediaForFragmentListInput = {}  # type: ignore[typeddict-item]
    if data.get("StreamName") is not None:
        out["stream_name"] = data["StreamName"]
    if data.get("StreamARN") is not None:
        out["stream_arn"] = data["StreamARN"]
    if data.get("Fragments") is not None:
        import capo_kinesis_video_archived_media.types.fragment_number_list

        out["fragments"] = (
            capo_kinesis_video_archived_media.types.fragment_number_list.deserialize_json(
                data["Fragments"]
            )
        )
    else:
        out["fragments"] = []
    return out
