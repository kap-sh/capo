"""Generated from Smithy shape ``com.amazonaws.codecommit#GetBlobOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_codecommit.types.blob


class GetBlobOutput(TypedDict, closed=True):
    content: "capo_codecommit.types.blob.blob"
    """<p>The content of the blob, usually a file.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetBlobOutput) -> dict:
    out: dict = {}
    import capo_codecommit.types.blob

    out["content"] = capo_codecommit.types.blob.serialize_aws_json_1_1(value["content"])
    return out


def deserialize_aws_json_1_1(data: dict) -> GetBlobOutput:
    out: GetBlobOutput = {}  # type: ignore[typeddict-item]
    if data.get("content") is not None:
        import capo_codecommit.types.blob

        out["content"] = capo_codecommit.types.blob.deserialize_aws_json_1_1(
            data["content"]
        )
    else:
        out["content"] = b""
    return out
