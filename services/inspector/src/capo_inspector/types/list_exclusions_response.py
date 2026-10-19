"""Generated from Smithy shape ``com.amazonaws.inspector#ListExclusionsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_inspector.types.list_returned_arn_list
    import capo_inspector.types.pagination_token


class ListExclusionsResponse(TypedDict, closed=True):
    exclusion_arns: "capo_inspector.types.list_returned_arn_list.ListReturnedArnList"
    """<p>A list of exclusions' ARNs returned by the action.</p>"""
    next_token: NotRequired["capo_inspector.types.pagination_token.PaginationToken"]
    """<p>When a response is generated, if there is more data to be listed, this parameters is present in the response and contains the value to use for the nextToken parameter in a subsequent pagination request. If there is no more data to be listed, this parameter is set to null.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListExclusionsResponse) -> dict:
    out: dict = {}
    import capo_inspector.types.list_returned_arn_list

    out["exclusionArns"] = (
        capo_inspector.types.list_returned_arn_list.serialize_aws_json_1_1(
            value["exclusion_arns"]
        )
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListExclusionsResponse:
    out: ListExclusionsResponse = {}  # type: ignore[typeddict-item]
    if data.get("exclusionArns") is not None:
        import capo_inspector.types.list_returned_arn_list

        out["exclusion_arns"] = (
            capo_inspector.types.list_returned_arn_list.deserialize_aws_json_1_1(
                data["exclusionArns"]
            )
        )
    else:
        out["exclusion_arns"] = []
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
