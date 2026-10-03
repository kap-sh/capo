"""Generated from Smithy shape ``com.amazonaws.connect#ContactFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connect.types.contact_states


class ContactFilter(TypedDict, closed=True):
    contact_states: NotRequired["capo_connect.types.contact_states.ContactStates"]
    """<p>A list of up to 9 <a href="https://docs.aws.amazon.com/connect/latest/adminguide/about-contact-states.html">contact states</a>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ContactFilter) -> dict:
    out: dict = {}
    if "contact_states" in value:
        import capo_connect.types.contact_states

        out["ContactStates"] = capo_connect.types.contact_states.serialize_json(
            value["contact_states"]
        )
    return out


def deserialize_json(data: dict) -> ContactFilter:
    out: ContactFilter = {}  # type: ignore[typeddict-item]
    if data.get("ContactStates") is not None:
        import capo_connect.types.contact_states

        out["contact_states"] = capo_connect.types.contact_states.deserialize_json(
            data["ContactStates"]
        )
    return out
