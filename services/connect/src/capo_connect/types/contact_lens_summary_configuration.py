"""Generated from Smithy shape ``com.amazonaws.connect#ContactLensSummaryConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connect.types.contact_lens_summary_mode_list


class ContactLensSummaryConfiguration(TypedDict, closed=True):
    summary_modes: NotRequired[
        "capo_connect.types.contact_lens_summary_mode_list.ContactLensSummaryModeList"
    ]
    """<p>The conversational analytics summary modes enabled for the contact. Valid values: <code>PostContact</code> | <code>AutomatedInteraction</code> | <code>ContactChain</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ContactLensSummaryConfiguration) -> dict:
    out: dict = {}
    if "summary_modes" in value:
        import capo_connect.types.contact_lens_summary_mode_list

        out["SummaryModes"] = (
            capo_connect.types.contact_lens_summary_mode_list.serialize_json(
                value["summary_modes"]
            )
        )
    return out


def deserialize_json(data: dict) -> ContactLensSummaryConfiguration:
    out: ContactLensSummaryConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("SummaryModes") is not None:
        import capo_connect.types.contact_lens_summary_mode_list

        out["summary_modes"] = (
            capo_connect.types.contact_lens_summary_mode_list.deserialize_json(
                data["SummaryModes"]
            )
        )
    return out
