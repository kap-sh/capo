"""Generated from Smithy shape ``com.amazonaws.connect#ConversationalAnalytics``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connect.types.contact_analysis_reference_state
    import capo_connect.types.conversational_analytics_configuration


class ConversationalAnalytics(TypedDict, closed=True):
    configuration: NotRequired[
        "capo_connect.types.conversational_analytics_configuration.ConversationalAnalyticsConfiguration"
    ]
    """<p>The conversational analytics settings that apply to the contact.</p>"""
    contact_analysis_reference_state: NotRequired[
        "capo_connect.types.contact_analysis_reference_state.ContactAnalysisReferenceState"
    ]
    """<p>The current state of conversational analytics processing for the contact.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ConversationalAnalytics) -> dict:
    out: dict = {}
    if "configuration" in value:
        import capo_connect.types.conversational_analytics_configuration

        out["Configuration"] = (
            capo_connect.types.conversational_analytics_configuration.serialize_json(
                value["configuration"]
            )
        )
    if "contact_analysis_reference_state" in value:
        import capo_connect.types.contact_analysis_reference_state

        out["ContactAnalysisReferenceState"] = (
            capo_connect.types.contact_analysis_reference_state.serialize_json(
                value["contact_analysis_reference_state"]
            )
        )
    return out


def deserialize_json(data: dict) -> ConversationalAnalytics:
    out: ConversationalAnalytics = {}  # type: ignore[typeddict-item]
    if data.get("Configuration") is not None:
        import capo_connect.types.conversational_analytics_configuration

        out["configuration"] = (
            capo_connect.types.conversational_analytics_configuration.deserialize_json(
                data["Configuration"]
            )
        )
    if data.get("ContactAnalysisReferenceState") is not None:
        import capo_connect.types.contact_analysis_reference_state

        out["contact_analysis_reference_state"] = (
            capo_connect.types.contact_analysis_reference_state.deserialize_json(
                data["ContactAnalysisReferenceState"]
            )
        )
    return out
