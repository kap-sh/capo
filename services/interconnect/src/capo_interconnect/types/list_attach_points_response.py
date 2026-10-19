"""Generated from Smithy shape ``com.amazonaws.interconnect#ListAttachPointsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_interconnect.types.attach_point_descriptor_list
    import capo_interconnect.types.next_token


class ListAttachPointsResponse(TypedDict, closed=True):
    attach_points: (
        "capo_interconnect.types.attach_point_descriptor_list.AttachPointDescriptorList"
    )
    """<p>The valid <a>AttachPoint</a> </p>"""
    next_token: NotRequired["capo_interconnect.types.next_token.NextToken"]
    """<p>A pagination token indicating that there are more results that can be fetched.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListAttachPointsResponse) -> dict:
    out: dict = {}
    import capo_interconnect.types.attach_point_descriptor_list

    out["attachPoints"] = (
        capo_interconnect.types.attach_point_descriptor_list.serialize_aws_json_1_0(
            value["attach_points"]
        )
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ListAttachPointsResponse:
    out: ListAttachPointsResponse = {}  # type: ignore[typeddict-item]
    if data.get("attachPoints") is not None:
        import capo_interconnect.types.attach_point_descriptor_list

        out["attach_points"] = (
            capo_interconnect.types.attach_point_descriptor_list.deserialize_aws_json_1_0(
                data["attachPoints"]
            )
        )
    else:
        out["attach_points"] = []
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
