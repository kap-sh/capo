"""Generated from Smithy shape ``com.amazonaws.geoplaces#AddressComponentPhonemes``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_geo_places.types.phoneme_transcription_list


class AddressComponentPhonemes(TypedDict, closed=True):
    country: NotRequired[
        "capo_geo_places.types.phoneme_transcription_list.PhonemeTranscriptionList"
    ]
    """<p>The alpha-2 or alpha-3 character code for the country that the results will be present in.</p>"""
    region: NotRequired[
        "capo_geo_places.types.phoneme_transcription_list.PhonemeTranscriptionList"
    ]
    """<p>How to pronounce the region or state results should be to be present in.</p>"""
    sub_region: NotRequired[
        "capo_geo_places.types.phoneme_transcription_list.PhonemeTranscriptionList"
    ]
    """<p>How to pronounce the sub-region or county for which results should be present in. </p>"""
    locality: NotRequired[
        "capo_geo_places.types.phoneme_transcription_list.PhonemeTranscriptionList"
    ]
    """<p>How to pronounce the city or locality results should be present in. </p> <p>Example: <code>Vancouver</code>.</p>"""
    district: NotRequired[
        "capo_geo_places.types.phoneme_transcription_list.PhonemeTranscriptionList"
    ]
    """<p>How to pronounce the district or division of a city results should be present in.</p>"""
    sub_district: NotRequired[
        "capo_geo_places.types.phoneme_transcription_list.PhonemeTranscriptionList"
    ]
    """<p>How to pronounce the sub-district or division of a city results should be present in.</p>"""
    block: NotRequired[
        "capo_geo_places.types.phoneme_transcription_list.PhonemeTranscriptionList"
    ]
    """<p>How to pronounce the name of the block.</p>"""
    sub_block: NotRequired[
        "capo_geo_places.types.phoneme_transcription_list.PhonemeTranscriptionList"
    ]
    """<p>How to pronounce the name of the sub-block.</p>"""
    street: NotRequired[
        "capo_geo_places.types.phoneme_transcription_list.PhonemeTranscriptionList"
    ]
    """<p>How to pronounce the name of the street results should be present in.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AddressComponentPhonemes) -> dict:
    out: dict = {}
    if "country" in value:
        import capo_geo_places.types.phoneme_transcription_list

        out["Country"] = (
            capo_geo_places.types.phoneme_transcription_list.serialize_json(
                value["country"]
            )
        )
    if "region" in value:
        import capo_geo_places.types.phoneme_transcription_list

        out["Region"] = capo_geo_places.types.phoneme_transcription_list.serialize_json(
            value["region"]
        )
    if "sub_region" in value:
        import capo_geo_places.types.phoneme_transcription_list

        out["SubRegion"] = (
            capo_geo_places.types.phoneme_transcription_list.serialize_json(
                value["sub_region"]
            )
        )
    if "locality" in value:
        import capo_geo_places.types.phoneme_transcription_list

        out["Locality"] = (
            capo_geo_places.types.phoneme_transcription_list.serialize_json(
                value["locality"]
            )
        )
    if "district" in value:
        import capo_geo_places.types.phoneme_transcription_list

        out["District"] = (
            capo_geo_places.types.phoneme_transcription_list.serialize_json(
                value["district"]
            )
        )
    if "sub_district" in value:
        import capo_geo_places.types.phoneme_transcription_list

        out["SubDistrict"] = (
            capo_geo_places.types.phoneme_transcription_list.serialize_json(
                value["sub_district"]
            )
        )
    if "block" in value:
        import capo_geo_places.types.phoneme_transcription_list

        out["Block"] = capo_geo_places.types.phoneme_transcription_list.serialize_json(
            value["block"]
        )
    if "sub_block" in value:
        import capo_geo_places.types.phoneme_transcription_list

        out["SubBlock"] = (
            capo_geo_places.types.phoneme_transcription_list.serialize_json(
                value["sub_block"]
            )
        )
    if "street" in value:
        import capo_geo_places.types.phoneme_transcription_list

        out["Street"] = capo_geo_places.types.phoneme_transcription_list.serialize_json(
            value["street"]
        )
    return out


def deserialize_json(data: dict) -> AddressComponentPhonemes:
    out: AddressComponentPhonemes = {}  # type: ignore[typeddict-item]
    if data.get("Country") is not None:
        import capo_geo_places.types.phoneme_transcription_list

        out["country"] = (
            capo_geo_places.types.phoneme_transcription_list.deserialize_json(
                data["Country"]
            )
        )
    if data.get("Region") is not None:
        import capo_geo_places.types.phoneme_transcription_list

        out["region"] = (
            capo_geo_places.types.phoneme_transcription_list.deserialize_json(
                data["Region"]
            )
        )
    if data.get("SubRegion") is not None:
        import capo_geo_places.types.phoneme_transcription_list

        out["sub_region"] = (
            capo_geo_places.types.phoneme_transcription_list.deserialize_json(
                data["SubRegion"]
            )
        )
    if data.get("Locality") is not None:
        import capo_geo_places.types.phoneme_transcription_list

        out["locality"] = (
            capo_geo_places.types.phoneme_transcription_list.deserialize_json(
                data["Locality"]
            )
        )
    if data.get("District") is not None:
        import capo_geo_places.types.phoneme_transcription_list

        out["district"] = (
            capo_geo_places.types.phoneme_transcription_list.deserialize_json(
                data["District"]
            )
        )
    if data.get("SubDistrict") is not None:
        import capo_geo_places.types.phoneme_transcription_list

        out["sub_district"] = (
            capo_geo_places.types.phoneme_transcription_list.deserialize_json(
                data["SubDistrict"]
            )
        )
    if data.get("Block") is not None:
        import capo_geo_places.types.phoneme_transcription_list

        out["block"] = (
            capo_geo_places.types.phoneme_transcription_list.deserialize_json(
                data["Block"]
            )
        )
    if data.get("SubBlock") is not None:
        import capo_geo_places.types.phoneme_transcription_list

        out["sub_block"] = (
            capo_geo_places.types.phoneme_transcription_list.deserialize_json(
                data["SubBlock"]
            )
        )
    if data.get("Street") is not None:
        import capo_geo_places.types.phoneme_transcription_list

        out["street"] = (
            capo_geo_places.types.phoneme_transcription_list.deserialize_json(
                data["Street"]
            )
        )
    return out


def redact_sensitive(value: AddressComponentPhonemes) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "country" in value:
        import capo_geo_places.types.phoneme_transcription_list

        out["country"] = (
            capo_geo_places.types.phoneme_transcription_list.redact_sensitive(
                value["country"]
            )
        )
    if "region" in value:
        import capo_geo_places.types.phoneme_transcription_list

        out["region"] = (
            capo_geo_places.types.phoneme_transcription_list.redact_sensitive(
                value["region"]
            )
        )
    if "sub_region" in value:
        import capo_geo_places.types.phoneme_transcription_list

        out["sub_region"] = (
            capo_geo_places.types.phoneme_transcription_list.redact_sensitive(
                value["sub_region"]
            )
        )
    if "locality" in value:
        import capo_geo_places.types.phoneme_transcription_list

        out["locality"] = (
            capo_geo_places.types.phoneme_transcription_list.redact_sensitive(
                value["locality"]
            )
        )
    if "district" in value:
        import capo_geo_places.types.phoneme_transcription_list

        out["district"] = (
            capo_geo_places.types.phoneme_transcription_list.redact_sensitive(
                value["district"]
            )
        )
    if "sub_district" in value:
        import capo_geo_places.types.phoneme_transcription_list

        out["sub_district"] = (
            capo_geo_places.types.phoneme_transcription_list.redact_sensitive(
                value["sub_district"]
            )
        )
    if "block" in value:
        import capo_geo_places.types.phoneme_transcription_list

        out["block"] = (
            capo_geo_places.types.phoneme_transcription_list.redact_sensitive(
                value["block"]
            )
        )
    if "sub_block" in value:
        import capo_geo_places.types.phoneme_transcription_list

        out["sub_block"] = (
            capo_geo_places.types.phoneme_transcription_list.redact_sensitive(
                value["sub_block"]
            )
        )
    if "street" in value:
        import capo_geo_places.types.phoneme_transcription_list

        out["street"] = (
            capo_geo_places.types.phoneme_transcription_list.redact_sensitive(
                value["street"]
            )
        )
    return out
