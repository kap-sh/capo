"""Generated from Smithy shape ``com.amazonaws.transcribe#TagResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_transcribe.errors import DeserializationError

if TYPE_CHECKING:
    import capo_transcribe.types.tag_list
    import capo_transcribe.types.transcribe_arn


class TagResourceRequest(TypedDict, closed=True):
    resource_arn: "capo_transcribe.types.transcribe_arn.TranscribeArn"
    """<p>The Amazon Resource Name (ARN) of the resource you want to tag. ARNs have the format <code>arn:partition:service:region:account-id:resource-type/resource-id</code>.</p> <p>For example, <code>arn:aws:transcribe:us-west-2:111122223333:transcription-job/transcription-job-name</code>.</p> <p>Valid values for <code>resource-type</code> are: <code>transcription-job</code>, <code>medical-transcription-job</code>, <code>vocabulary</code>, <code>medical-vocabulary</code>, <code>vocabulary-filter</code>, and <code>language-model</code>.</p>"""
    tags: "capo_transcribe.types.tag_list.TagList"
    """<p>Adds one or more custom tags, each in the form of a key:value pair, to the specified resource.</p> <p>To learn more about using tags with Amazon Transcribe, refer to <a href="https://docs.aws.amazon.com/transcribe/latest/dg/tagging.html">Tagging resources</a>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TagResourceRequest) -> dict:
    out: dict = {}
    out["ResourceArn"] = value["resource_arn"]
    import capo_transcribe.types.tag_list

    out["Tags"] = capo_transcribe.types.tag_list.serialize_aws_json_1_1(value["tags"])
    return out


def deserialize_aws_json_1_1(data: dict) -> TagResourceRequest:
    out: TagResourceRequest = {}  # type: ignore[typeddict-item]
    if data.get("ResourceArn") is not None:
        out["resource_arn"] = data["ResourceArn"]
    else:
        raise DeserializationError("TagResourceRequest.resource_arn required")
    if data.get("Tags") is not None:
        import capo_transcribe.types.tag_list

        out["tags"] = capo_transcribe.types.tag_list.deserialize_aws_json_1_1(
            data["Tags"]
        )
    else:
        raise DeserializationError("TagResourceRequest.tags required")
    return out
