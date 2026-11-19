"""Generated from Smithy shape ``com.amazonaws.codebuild#DescribeTestCasesOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codebuild.types.string
    import capo_codebuild.types.test_cases


class DescribeTestCasesOutput(TypedDict, closed=True):
    next_token: NotRequired["capo_codebuild.types.string.String"]
    """<p> During a previous call, the maximum number of items that can be returned is the value specified in <code>maxResults</code>. If there more items in the list, then a unique string called a <i>nextToken</i> is returned. To get the next batch of items in the list, call this operation again, adding the next token to the call. To get all of the items in the list, keep calling this operation with each subsequent next token that is returned, until no more next tokens are returned. </p>"""
    test_cases: NotRequired["capo_codebuild.types.test_cases.TestCases"]
    """<p> The returned list of test cases. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeTestCasesOutput) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "test_cases" in value:
        import capo_codebuild.types.test_cases

        out["testCases"] = capo_codebuild.types.test_cases.serialize_aws_json_1_1(
            value["test_cases"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeTestCasesOutput:
    out: DescribeTestCasesOutput = {}  # type: ignore[typeddict-item]
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    if data.get("testCases") is not None:
        import capo_codebuild.types.test_cases

        out["test_cases"] = capo_codebuild.types.test_cases.deserialize_aws_json_1_1(
            data["testCases"]
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DescribeTestCasesOutput) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "test_cases" in value:
        import capo_codebuild.types.test_cases

        out["testCases"] = capo_codebuild.types.test_cases.serialize_cbor(
            value["test_cases"]
        )
    return out


def deserialize_cbor(data: dict) -> DescribeTestCasesOutput:
    out: DescribeTestCasesOutput = {}  # type: ignore[typeddict-item]
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    if data.get("testCases") is not None:
        import capo_codebuild.types.test_cases

        out["test_cases"] = capo_codebuild.types.test_cases.deserialize_cbor(
            data["testCases"]
        )
    return out
