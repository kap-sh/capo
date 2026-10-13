"""Generated from Smithy shape ``com.amazonaws.connect#ListInstancesResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connect.types.instance_summary_list
    import capo_connect.types.next_token


class ListInstancesResponse(TypedDict, closed=True):
    instance_summary_list: NotRequired[
        "capo_connect.types.instance_summary_list.InstanceSummaryList"
    ]
    """<p>Information about the instances.</p>"""
    next_token: NotRequired["capo_connect.types.next_token.NextToken"]
    """<p>If there are additional results, this is the token for the next set of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListInstancesResponse) -> dict:
    out: dict = {}
    if "instance_summary_list" in value:
        import capo_connect.types.instance_summary_list

        out["InstanceSummaryList"] = (
            capo_connect.types.instance_summary_list.serialize_json(
                value["instance_summary_list"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListInstancesResponse:
    out: ListInstancesResponse = {}  # type: ignore[typeddict-item]
    if data.get("InstanceSummaryList") is not None:
        import capo_connect.types.instance_summary_list

        out["instance_summary_list"] = (
            capo_connect.types.instance_summary_list.deserialize_json(
                data["InstanceSummaryList"]
            )
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out


def redact_sensitive(value: ListInstancesResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "instance_summary_list" in value:
        import capo_connect.types.instance_summary_list

        out["instance_summary_list"] = (
            capo_connect.types.instance_summary_list.redact_sensitive(
                value["instance_summary_list"]
            )
        )
    return out
