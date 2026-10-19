"""Generated from Smithy shape ``com.amazonaws.iottwinmaker#IotTwinMakerDestinationConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_iottwinmaker.types.twin_maker_arn


class IotTwinMakerDestinationConfiguration(TypedDict, closed=True):
    workspace: "capo_iottwinmaker.types.twin_maker_arn.TwinMakerArn"
    """<p>The IoT TwinMaker workspace.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: IotTwinMakerDestinationConfiguration) -> dict:
    out: dict = {}
    out["workspace"] = value["workspace"]
    return out


def deserialize_json(data: dict) -> IotTwinMakerDestinationConfiguration:
    out: IotTwinMakerDestinationConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("workspace") is not None:
        out["workspace"] = data["workspace"]
    else:
        out["workspace"] = ""
    return out
