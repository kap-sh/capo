"""Generated from Smithy shape ``com.amazonaws.codebuild#BatchDeleteBuildsInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_codebuild.types.build_ids


class BatchDeleteBuildsInput(TypedDict, closed=True):
    ids: "capo_codebuild.types.build_ids.BuildIds"
    """<p>The IDs of the builds to delete.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BatchDeleteBuildsInput) -> dict:
    out: dict = {}
    import capo_codebuild.types.build_ids

    out["ids"] = capo_codebuild.types.build_ids.serialize_aws_json_1_1(value["ids"])
    return out


def deserialize_aws_json_1_1(data: dict) -> BatchDeleteBuildsInput:
    out: BatchDeleteBuildsInput = {}  # type: ignore[typeddict-item]
    if data.get("ids") is not None:
        import capo_codebuild.types.build_ids

        out["ids"] = capo_codebuild.types.build_ids.deserialize_aws_json_1_1(
            data["ids"]
        )
    else:
        out["ids"] = []
    return out
