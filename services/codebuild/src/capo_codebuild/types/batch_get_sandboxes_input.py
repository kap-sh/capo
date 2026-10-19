"""Generated from Smithy shape ``com.amazonaws.codebuild#BatchGetSandboxesInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_codebuild.types.sandbox_ids


class BatchGetSandboxesInput(TypedDict, closed=True):
    ids: "capo_codebuild.types.sandbox_ids.SandboxIds"
    """<p>A comma separated list of <code>sandboxIds</code> or <code>sandboxArns</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BatchGetSandboxesInput) -> dict:
    out: dict = {}
    import capo_codebuild.types.sandbox_ids

    out["ids"] = capo_codebuild.types.sandbox_ids.serialize_aws_json_1_1(value["ids"])
    return out


def deserialize_aws_json_1_1(data: dict) -> BatchGetSandboxesInput:
    out: BatchGetSandboxesInput = {}  # type: ignore[typeddict-item]
    if data.get("ids") is not None:
        import capo_codebuild.types.sandbox_ids

        out["ids"] = capo_codebuild.types.sandbox_ids.deserialize_aws_json_1_1(
            data["ids"]
        )
    else:
        out["ids"] = []
    return out
