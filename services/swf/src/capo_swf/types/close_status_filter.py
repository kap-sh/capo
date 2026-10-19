"""Generated from Smithy shape ``com.amazonaws.swf#CloseStatusFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_swf.types.close_status


class CloseStatusFilter(TypedDict, closed=True):
    status: "capo_swf.types.close_status.CloseStatus"
    """<p> The close status that must match the close status of an execution for it to meet the criteria of this filter.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CloseStatusFilter) -> dict:
    out: dict = {}
    import capo_swf.types.close_status

    out["status"] = capo_swf.types.close_status.serialize_aws_json_1_0(value["status"])
    return out


def deserialize_aws_json_1_0(data: dict) -> CloseStatusFilter:
    out: CloseStatusFilter = {}  # type: ignore[typeddict-item]
    if data.get("status") is not None:
        import capo_swf.types.close_status

        out["status"] = capo_swf.types.close_status.deserialize_aws_json_1_0(
            data["status"]
        )
    else:
        import typing

        out["status"] = typing.cast("capo_swf.types.close_status.CloseStatus", "")
    return out
