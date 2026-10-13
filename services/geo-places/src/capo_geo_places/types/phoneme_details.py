"""Generated from Smithy shape ``com.amazonaws.geoplaces#PhonemeDetails``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_geo_places.types.address_component_phonemes
    import capo_geo_places.types.phoneme_transcription_list


class PhonemeDetails(TypedDict, closed=True):
    title: NotRequired[
        "capo_geo_places.types.phoneme_transcription_list.PhonemeTranscriptionList"
    ]
    """<p>List of <code>PhonemeTranscription</code>. See <code>PhonemeTranscription</code> for fields.</p>"""
    address: NotRequired[
        "capo_geo_places.types.address_component_phonemes.AddressComponentPhonemes"
    ]
    """<p>How to pronounce the address.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PhonemeDetails) -> dict:
    out: dict = {}
    if "title" in value:
        import capo_geo_places.types.phoneme_transcription_list

        out["Title"] = capo_geo_places.types.phoneme_transcription_list.serialize_json(
            value["title"]
        )
    if "address" in value:
        import capo_geo_places.types.address_component_phonemes

        out["Address"] = (
            capo_geo_places.types.address_component_phonemes.serialize_json(
                value["address"]
            )
        )
    return out


def deserialize_json(data: dict) -> PhonemeDetails:
    out: PhonemeDetails = {}  # type: ignore[typeddict-item]
    if data.get("Title") is not None:
        import capo_geo_places.types.phoneme_transcription_list

        out["title"] = (
            capo_geo_places.types.phoneme_transcription_list.deserialize_json(
                data["Title"]
            )
        )
    if data.get("Address") is not None:
        import capo_geo_places.types.address_component_phonemes

        out["address"] = (
            capo_geo_places.types.address_component_phonemes.deserialize_json(
                data["Address"]
            )
        )
    return out


def redact_sensitive(value: PhonemeDetails) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "title" in value:
        import capo_geo_places.types.phoneme_transcription_list

        out["title"] = (
            capo_geo_places.types.phoneme_transcription_list.redact_sensitive(
                value["title"]
            )
        )
    if "address" in value:
        import capo_geo_places.types.address_component_phonemes

        out["address"] = (
            capo_geo_places.types.address_component_phonemes.redact_sensitive(
                value["address"]
            )
        )
    return out
