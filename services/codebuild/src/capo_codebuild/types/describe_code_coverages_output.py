"""Generated from Smithy shape ``com.amazonaws.codebuild#DescribeCodeCoveragesOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codebuild.types.code_coverages
    import capo_codebuild.types.string


class DescribeCodeCoveragesOutput(TypedDict, closed=True):
    next_token: NotRequired["capo_codebuild.types.string.String"]
    """<p>If there are more items to return, this contains a token that is passed to a subsequent call to <code>DescribeCodeCoverages</code> to retrieve the next set of items.</p>"""
    code_coverages: NotRequired["capo_codebuild.types.code_coverages.CodeCoverages"]
    """<p>An array of <code>CodeCoverage</code> objects that contain the results.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeCodeCoveragesOutput) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "code_coverages" in value:
        import capo_codebuild.types.code_coverages

        out["codeCoverages"] = (
            capo_codebuild.types.code_coverages.serialize_aws_json_1_1(
                value["code_coverages"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeCodeCoveragesOutput:
    out: DescribeCodeCoveragesOutput = {}  # type: ignore[typeddict-item]
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    if data.get("codeCoverages") is not None:
        import capo_codebuild.types.code_coverages

        out["code_coverages"] = (
            capo_codebuild.types.code_coverages.deserialize_aws_json_1_1(
                data["codeCoverages"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DescribeCodeCoveragesOutput) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "code_coverages" in value:
        import capo_codebuild.types.code_coverages

        out["codeCoverages"] = capo_codebuild.types.code_coverages.serialize_cbor(
            value["code_coverages"]
        )
    return out


def deserialize_cbor(data: dict) -> DescribeCodeCoveragesOutput:
    out: DescribeCodeCoveragesOutput = {}  # type: ignore[typeddict-item]
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    if data.get("codeCoverages") is not None:
        import capo_codebuild.types.code_coverages

        out["code_coverages"] = capo_codebuild.types.code_coverages.deserialize_cbor(
            data["codeCoverages"]
        )
    return out
