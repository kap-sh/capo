"""Generated from Smithy shape ``com.amazonaws.elementalinference#UpdateOutputStatus``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_elementalinference.types.output_status
    import capo_elementalinference.types.resource_name


class UpdateOutputStatus(TypedDict, closed=True):
    output_name: "capo_elementalinference.types.resource_name.ResourceName"
    """<p>The name of the output that you want to enable or disable. The output must exist in the feed when you create the action. </p>"""
    status: "capo_elementalinference.types.output_status.OutputStatus"
    """<p>Specifies whether the output is enabled or disabled after the action runs.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateOutputStatus) -> dict:
    out: dict = {}
    out["outputName"] = value["output_name"]
    import capo_elementalinference.types.output_status

    out["status"] = capo_elementalinference.types.output_status.serialize_json(
        value["status"]
    )
    return out


def deserialize_json(data: dict) -> UpdateOutputStatus:
    out: UpdateOutputStatus = {}  # type: ignore[typeddict-item]
    if data.get("outputName") is not None:
        out["output_name"] = data["outputName"]
    else:
        out["output_name"] = ""
    if data.get("status") is not None:
        import capo_elementalinference.types.output_status

        out["status"] = capo_elementalinference.types.output_status.deserialize_json(
            data["status"]
        )
    else:
        import typing

        out["status"] = typing.cast(
            "capo_elementalinference.types.output_status.OutputStatus", ""
        )
    return out
