"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#BrowserExtension``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore.types.resource_location


class BrowserExtension(TypedDict, closed=True):
    location: "capo_bedrock_agentcore.types.resource_location.ResourceLocation"
    """<p>The location where the browser extension files are stored. This specifies the source from which the extension will be loaded and installed.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BrowserExtension) -> dict:
    out: dict = {}
    import capo_bedrock_agentcore.types.resource_location

    out["location"] = capo_bedrock_agentcore.types.resource_location.serialize_json(
        value["location"]
    )
    return out


def deserialize_json(data: dict) -> BrowserExtension:
    out: BrowserExtension = {}  # type: ignore[typeddict-item]
    if data.get("location") is not None:
        import capo_bedrock_agentcore.types.resource_location

        out["location"] = (
            capo_bedrock_agentcore.types.resource_location.deserialize_json(
                data["location"]
            )
        )
    else:
        out["location"] = {"$unknown": {"name": ""}}
    return out
