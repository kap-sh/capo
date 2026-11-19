"""Generated from Smithy shape ``com.amazonaws.codebuild#TestCaseFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codebuild.types.string


class TestCaseFilter(TypedDict, closed=True):
    status: NotRequired["capo_codebuild.types.string.String"]
    """<p>The status used to filter test cases. A <code>TestCaseFilter</code> can have one status. Valid values are:</p> <ul> <li> <p> <code>SUCCEEDED</code> </p> </li> <li> <p> <code>FAILED</code> </p> </li> <li> <p> <code>ERROR</code> </p> </li> <li> <p> <code>SKIPPED</code> </p> </li> <li> <p> <code>UNKNOWN</code> </p> </li> </ul>"""
    keyword: NotRequired["capo_codebuild.types.string.String"]
    """<p>A keyword that is used to filter on the <code>name</code> or the <code>prefix</code> of the test cases. Only test cases where the keyword is a substring of the <code>name</code> or the <code>prefix</code> will be returned.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TestCaseFilter) -> dict:
    out: dict = {}
    if "status" in value:
        out["status"] = value["status"]
    if "keyword" in value:
        out["keyword"] = value["keyword"]
    return out


def deserialize_aws_json_1_1(data: dict) -> TestCaseFilter:
    out: TestCaseFilter = {}  # type: ignore[typeddict-item]
    if data.get("status") is not None:
        out["status"] = data["status"]
    if data.get("keyword") is not None:
        out["keyword"] = data["keyword"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: TestCaseFilter) -> dict:
    out: dict = {}
    if "status" in value:
        out["status"] = value["status"]
    if "keyword" in value:
        out["keyword"] = value["keyword"]
    return out


def deserialize_cbor(data: dict) -> TestCaseFilter:
    out: TestCaseFilter = {}  # type: ignore[typeddict-item]
    if data.get("status") is not None:
        out["status"] = data["status"]
    if data.get("keyword") is not None:
        out["keyword"] = data["keyword"]
    return out
