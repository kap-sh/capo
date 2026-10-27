"""Generated from Smithy shape ``com.amazonaws.mediaconnect#OwnedResourceShareDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_mediaconnect.types.resource_share_state


class OwnedResourceShareDetails(TypedDict, closed=True):
    share_state: "capo_mediaconnect.types.resource_share_state.ResourceShareState"
    """<p>The sharing state of the endpoint. Valid values include the following:</p> <ul> <li> <p> <code>SHARED</code> – The endpoint is shared with one or more accounts.</p> </li> <li> <p> <code>UNSHARED</code> – The endpoint is not shared with other accounts.</p> </li> </ul>"""


# --- restJson1 ser/de ---
def serialize_json(value: OwnedResourceShareDetails) -> dict:
    out: dict = {}
    import capo_mediaconnect.types.resource_share_state

    out["shareState"] = capo_mediaconnect.types.resource_share_state.serialize_json(
        value["share_state"]
    )
    return out


def deserialize_json(data: dict) -> OwnedResourceShareDetails:
    out: OwnedResourceShareDetails = {}  # type: ignore[typeddict-item]
    if data.get("shareState") is not None:
        import capo_mediaconnect.types.resource_share_state

        out["share_state"] = (
            capo_mediaconnect.types.resource_share_state.deserialize_json(
                data["shareState"]
            )
        )
    else:
        import typing

        out["share_state"] = typing.cast(
            "capo_mediaconnect.types.resource_share_state.ResourceShareState", ""
        )
    return out
