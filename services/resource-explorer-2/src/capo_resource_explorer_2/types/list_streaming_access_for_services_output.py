"""Generated from Smithy shape ``com.amazonaws.resourceexplorer2#ListStreamingAccessForServicesOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_resource_explorer_2.types.streaming_access_details_list


class ListStreamingAccessForServicesOutput(TypedDict, closed=True):
    streaming_access_for_services: "capo_resource_explorer_2.types.streaming_access_details_list.StreamingAccessDetailsList"
    """<p>A list of Amazon Web Services services that have streaming access to your Resource Explorer data, including details about when the access was granted.</p>"""
    next_token: NotRequired["str"]
    """<p>If present, indicates that more output is available than is included in the current response. Use this value in the <code>NextToken</code> request parameter in a subsequent call to the operation to get the next part of the output. You should repeat this until the <code>NextToken</code> response element comes back as <code>null</code>. The pagination tokens expire after 24 hours.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListStreamingAccessForServicesOutput) -> dict:
    out: dict = {}
    import capo_resource_explorer_2.types.streaming_access_details_list

    out["StreamingAccessForServices"] = (
        capo_resource_explorer_2.types.streaming_access_details_list.serialize_json(
            value["streaming_access_for_services"]
        )
    )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListStreamingAccessForServicesOutput:
    out: ListStreamingAccessForServicesOutput = {}  # type: ignore[typeddict-item]
    if data.get("StreamingAccessForServices") is not None:
        import capo_resource_explorer_2.types.streaming_access_details_list

        out["streaming_access_for_services"] = (
            capo_resource_explorer_2.types.streaming_access_details_list.deserialize_json(
                data["StreamingAccessForServices"]
            )
        )
    else:
        out["streaming_access_for_services"] = []
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
