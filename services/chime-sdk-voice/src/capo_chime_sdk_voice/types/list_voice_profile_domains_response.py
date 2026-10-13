"""Generated from Smithy shape ``com.amazonaws.chimesdkvoice#ListVoiceProfileDomainsResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_chime_sdk_voice.types.string
    import capo_chime_sdk_voice.types.voice_profile_domain_summary_list


class ListVoiceProfileDomainsResponse(TypedDict, closed=True):
    voice_profile_domains: NotRequired[
        "capo_chime_sdk_voice.types.voice_profile_domain_summary_list.VoiceProfileDomainSummaryList"
    ]
    """<p>The list of voice profile domains.</p>"""
    next_token: NotRequired["capo_chime_sdk_voice.types.string.String"]
    """<p>The token used to return the next page of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListVoiceProfileDomainsResponse) -> dict:
    out: dict = {}
    if "voice_profile_domains" in value:
        import capo_chime_sdk_voice.types.voice_profile_domain_summary_list

        out["VoiceProfileDomains"] = (
            capo_chime_sdk_voice.types.voice_profile_domain_summary_list.serialize_json(
                value["voice_profile_domains"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListVoiceProfileDomainsResponse:
    out: ListVoiceProfileDomainsResponse = {}  # type: ignore[typeddict-item]
    if data.get("VoiceProfileDomains") is not None:
        import capo_chime_sdk_voice.types.voice_profile_domain_summary_list

        out["voice_profile_domains"] = (
            capo_chime_sdk_voice.types.voice_profile_domain_summary_list.deserialize_json(
                data["VoiceProfileDomains"]
            )
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out


def redact_sensitive(value: ListVoiceProfileDomainsResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "voice_profile_domains" in value:
        import capo_chime_sdk_voice.types.voice_profile_domain_summary_list

        out["voice_profile_domains"] = (
            capo_chime_sdk_voice.types.voice_profile_domain_summary_list.redact_sensitive(
                value["voice_profile_domains"]
            )
        )
    return out
