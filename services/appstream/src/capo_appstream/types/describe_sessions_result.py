"""Generated from Smithy shape ``com.amazonaws.appstream#DescribeSessionsResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_appstream.types.session_list
    import capo_appstream.types.string


class DescribeSessionsResult(TypedDict, closed=True):
    sessions: NotRequired["capo_appstream.types.session_list.SessionList"]
    """<p>Information about the streaming sessions.</p>"""
    next_token: NotRequired["capo_appstream.types.string.String"]
    """<p>The pagination token to use to retrieve the next page of results for this operation. If there are no more pages, this value is null.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeSessionsResult) -> dict:
    out: dict = {}
    if "sessions" in value:
        import capo_appstream.types.session_list

        out["Sessions"] = capo_appstream.types.session_list.serialize_aws_json_1_1(
            value["sessions"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeSessionsResult:
    out: DescribeSessionsResult = {}  # type: ignore[typeddict-item]
    if data.get("Sessions") is not None:
        import capo_appstream.types.session_list

        out["sessions"] = capo_appstream.types.session_list.deserialize_aws_json_1_1(
            data["Sessions"]
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DescribeSessionsResult) -> dict:
    out: dict = {}
    if "sessions" in value:
        import capo_appstream.types.session_list

        out["Sessions"] = capo_appstream.types.session_list.serialize_cbor(
            value["sessions"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_cbor(data: dict) -> DescribeSessionsResult:
    out: DescribeSessionsResult = {}  # type: ignore[typeddict-item]
    if data.get("Sessions") is not None:
        import capo_appstream.types.session_list

        out["sessions"] = capo_appstream.types.session_list.deserialize_cbor(
            data["Sessions"]
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
