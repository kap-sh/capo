"""Generated from Smithy shape ``com.amazonaws.connect#ContactLens``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connect.types.conversational_analytics


class ContactLens(TypedDict, closed=True):
    conversational_analytics: NotRequired[
        "capo_connect.types.conversational_analytics.ConversationalAnalytics"
    ]
    """<p>The conversational analytics configuration applied to the contact.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ContactLens) -> dict:
    out: dict = {}
    if "conversational_analytics" in value:
        import capo_connect.types.conversational_analytics

        out["ConversationalAnalytics"] = (
            capo_connect.types.conversational_analytics.serialize_json(
                value["conversational_analytics"]
            )
        )
    return out


def deserialize_json(data: dict) -> ContactLens:
    out: ContactLens = {}  # type: ignore[typeddict-item]
    if data.get("ConversationalAnalytics") is not None:
        import capo_connect.types.conversational_analytics

        out["conversational_analytics"] = (
            capo_connect.types.conversational_analytics.deserialize_json(
                data["ConversationalAnalytics"]
            )
        )
    return out
