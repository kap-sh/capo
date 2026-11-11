"""Generated from Smithy shape ``com.amazonaws.connect#ContactLensChannelConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connect.types.contact_lens_analytics_mode_list


class ContactLensChannelConfiguration(TypedDict, closed=True):
    analytics_modes: NotRequired[
        "capo_connect.types.contact_lens_analytics_mode_list.ContactLensAnalyticsModeList"
    ]
    """<p>The conversational analytics modes enabled for the channel. Valid values:</p> <ul> <li> <p> <code>RealTime</code> – Real-time analysis is enabled during the contact. Voice channel only.</p> </li> <li> <p> <code>PostContact</code> – Post-contact analysis is enabled after the contact ends. Voice channel only.</p> </li> <li> <p> <code>ContactLens</code> – Conversational analytics is enabled for the contact. Chat channel only.</p> </li> </ul>"""


# --- restJson1 ser/de ---
def serialize_json(value: ContactLensChannelConfiguration) -> dict:
    out: dict = {}
    if "analytics_modes" in value:
        import capo_connect.types.contact_lens_analytics_mode_list

        out["AnalyticsModes"] = (
            capo_connect.types.contact_lens_analytics_mode_list.serialize_json(
                value["analytics_modes"]
            )
        )
    return out


def deserialize_json(data: dict) -> ContactLensChannelConfiguration:
    out: ContactLensChannelConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("AnalyticsModes") is not None:
        import capo_connect.types.contact_lens_analytics_mode_list

        out["analytics_modes"] = (
            capo_connect.types.contact_lens_analytics_mode_list.deserialize_json(
                data["AnalyticsModes"]
            )
        )
    return out
