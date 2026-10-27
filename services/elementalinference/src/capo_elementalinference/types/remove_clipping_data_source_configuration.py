"""Generated from Smithy shape ``com.amazonaws.elementalinference#RemoveClippingDataSourceConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_elementalinference.types.resource_name


class RemoveClippingDataSourceConfiguration(TypedDict, closed=True):
    output_name: "capo_elementalinference.types.resource_name.ResourceName"
    """<p>The name of the output that you want to remove the game from.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RemoveClippingDataSourceConfiguration) -> dict:
    out: dict = {}
    out["outputName"] = value["output_name"]
    return out


def deserialize_json(data: dict) -> RemoveClippingDataSourceConfiguration:
    out: RemoveClippingDataSourceConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("outputName") is not None:
        out["output_name"] = data["outputName"]
    else:
        out["output_name"] = ""
    return out
