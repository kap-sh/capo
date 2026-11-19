"""Generated from Smithy shape ``com.amazonaws.appstream#DescribeStacksResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_appstream.types.stack_list
    import capo_appstream.types.string


class DescribeStacksResult(TypedDict, closed=True):
    stacks: NotRequired["capo_appstream.types.stack_list.StackList"]
    """<p>Information about the stacks.</p>"""
    next_token: NotRequired["capo_appstream.types.string.String"]
    """<p>The pagination token to use to retrieve the next page of results for this operation. If there are no more pages, this value is null.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeStacksResult) -> dict:
    out: dict = {}
    if "stacks" in value:
        import capo_appstream.types.stack_list

        out["Stacks"] = capo_appstream.types.stack_list.serialize_aws_json_1_1(
            value["stacks"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeStacksResult:
    out: DescribeStacksResult = {}  # type: ignore[typeddict-item]
    if data.get("Stacks") is not None:
        import capo_appstream.types.stack_list

        out["stacks"] = capo_appstream.types.stack_list.deserialize_aws_json_1_1(
            data["Stacks"]
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DescribeStacksResult) -> dict:
    out: dict = {}
    if "stacks" in value:
        import capo_appstream.types.stack_list

        out["Stacks"] = capo_appstream.types.stack_list.serialize_cbor(value["stacks"])
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_cbor(data: dict) -> DescribeStacksResult:
    out: DescribeStacksResult = {}  # type: ignore[typeddict-item]
    if data.get("Stacks") is not None:
        import capo_appstream.types.stack_list

        out["stacks"] = capo_appstream.types.stack_list.deserialize_cbor(data["Stacks"])
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
