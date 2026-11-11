"""Generated from Smithy shape ``com.amazonaws.connect#ConversationalAnalyticsConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connect.types.boolean
    import capo_connect.types.contact_lens_channel_configuration
    import capo_connect.types.contact_lens_redaction_configuration
    import capo_connect.types.contact_lens_sentiment_configuration
    import capo_connect.types.contact_lens_summary_configuration
    import capo_connect.types.language_locales
    import capo_connect.types.string


class ConversationalAnalyticsConfiguration(TypedDict, closed=True):
    enabled: NotRequired["capo_connect.types.boolean.Boolean"]
    """<p>Specifies whether conversational analytics is enabled for the contact.</p>"""
    language_locale: NotRequired["capo_connect.types.string.String"]
    """<p>The language locale that conversational analytics uses to analyze the contact (for example, <code>en-US</code>).</p>"""
    language_locales: NotRequired["capo_connect.types.language_locales.LanguageLocales"]
    """<p>The language locales that conversational analytics uses to analyze the contact (for example, <code>en-US</code> and <code>es-ES</code>).</p>"""
    channel_configuration: NotRequired[
        "capo_connect.types.contact_lens_channel_configuration.ContactLensChannelConfiguration"
    ]
    """<p>The per-channel conversational analytics settings for the contact.</p>"""
    redaction_configuration: NotRequired[
        "capo_connect.types.contact_lens_redaction_configuration.ContactLensRedactionConfiguration"
    ]
    """<p>The redaction configuration for the contact transcript.</p>"""
    summary_configuration: NotRequired[
        "capo_connect.types.contact_lens_summary_configuration.ContactLensSummaryConfiguration"
    ]
    """<p>The summary configuration for the contact.</p>"""
    sentiment_configuration: NotRequired[
        "capo_connect.types.contact_lens_sentiment_configuration.ContactLensSentimentConfiguration"
    ]
    """<p>The sentiment analysis configuration for the contact.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ConversationalAnalyticsConfiguration) -> dict:
    out: dict = {}
    if "enabled" in value:
        out["Enabled"] = value["enabled"]
    if "language_locale" in value:
        out["LanguageLocale"] = value["language_locale"]
    if "language_locales" in value:
        import capo_connect.types.language_locales

        out["LanguageLocales"] = capo_connect.types.language_locales.serialize_json(
            value["language_locales"]
        )
    if "channel_configuration" in value:
        import capo_connect.types.contact_lens_channel_configuration

        out["ChannelConfiguration"] = (
            capo_connect.types.contact_lens_channel_configuration.serialize_json(
                value["channel_configuration"]
            )
        )
    if "redaction_configuration" in value:
        import capo_connect.types.contact_lens_redaction_configuration

        out["RedactionConfiguration"] = (
            capo_connect.types.contact_lens_redaction_configuration.serialize_json(
                value["redaction_configuration"]
            )
        )
    if "summary_configuration" in value:
        import capo_connect.types.contact_lens_summary_configuration

        out["SummaryConfiguration"] = (
            capo_connect.types.contact_lens_summary_configuration.serialize_json(
                value["summary_configuration"]
            )
        )
    if "sentiment_configuration" in value:
        import capo_connect.types.contact_lens_sentiment_configuration

        out["SentimentConfiguration"] = (
            capo_connect.types.contact_lens_sentiment_configuration.serialize_json(
                value["sentiment_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> ConversationalAnalyticsConfiguration:
    out: ConversationalAnalyticsConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("Enabled") is not None:
        out["enabled"] = data["Enabled"]
    if data.get("LanguageLocale") is not None:
        out["language_locale"] = data["LanguageLocale"]
    if data.get("LanguageLocales") is not None:
        import capo_connect.types.language_locales

        out["language_locales"] = capo_connect.types.language_locales.deserialize_json(
            data["LanguageLocales"]
        )
    if data.get("ChannelConfiguration") is not None:
        import capo_connect.types.contact_lens_channel_configuration

        out["channel_configuration"] = (
            capo_connect.types.contact_lens_channel_configuration.deserialize_json(
                data["ChannelConfiguration"]
            )
        )
    if data.get("RedactionConfiguration") is not None:
        import capo_connect.types.contact_lens_redaction_configuration

        out["redaction_configuration"] = (
            capo_connect.types.contact_lens_redaction_configuration.deserialize_json(
                data["RedactionConfiguration"]
            )
        )
    if data.get("SummaryConfiguration") is not None:
        import capo_connect.types.contact_lens_summary_configuration

        out["summary_configuration"] = (
            capo_connect.types.contact_lens_summary_configuration.deserialize_json(
                data["SummaryConfiguration"]
            )
        )
    if data.get("SentimentConfiguration") is not None:
        import capo_connect.types.contact_lens_sentiment_configuration

        out["sentiment_configuration"] = (
            capo_connect.types.contact_lens_sentiment_configuration.deserialize_json(
                data["SentimentConfiguration"]
            )
        )
    return out
