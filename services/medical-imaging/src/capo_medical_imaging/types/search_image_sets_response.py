"""Generated from Smithy shape ``com.amazonaws.medicalimaging#SearchImageSetsResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_medical_imaging.types.image_sets_metadata_summaries
    import capo_medical_imaging.types.next_token
    import capo_medical_imaging.types.sort


class SearchImageSetsResponse(TypedDict, closed=True):
    image_sets_metadata_summaries: "capo_medical_imaging.types.image_sets_metadata_summaries.ImageSetsMetadataSummaries"
    """<p>The model containing the image set results.</p>"""
    sort: NotRequired["capo_medical_imaging.types.sort.Sort"]
    """<p>The sort order for image set search results.</p>"""
    next_token: NotRequired["capo_medical_imaging.types.next_token.NextToken"]
    """<p>The token for pagination results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SearchImageSetsResponse) -> dict:
    out: dict = {}
    import capo_medical_imaging.types.image_sets_metadata_summaries

    out["imageSetsMetadataSummaries"] = (
        capo_medical_imaging.types.image_sets_metadata_summaries.serialize_json(
            value["image_sets_metadata_summaries"]
        )
    )
    if "sort" in value:
        import capo_medical_imaging.types.sort

        out["sort"] = capo_medical_imaging.types.sort.serialize_json(value["sort"])
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> SearchImageSetsResponse:
    out: SearchImageSetsResponse = {}  # type: ignore[typeddict-item]
    if data.get("imageSetsMetadataSummaries") is not None:
        import capo_medical_imaging.types.image_sets_metadata_summaries

        out["image_sets_metadata_summaries"] = (
            capo_medical_imaging.types.image_sets_metadata_summaries.deserialize_json(
                data["imageSetsMetadataSummaries"]
            )
        )
    else:
        out["image_sets_metadata_summaries"] = []
    if data.get("sort") is not None:
        import capo_medical_imaging.types.sort

        out["sort"] = capo_medical_imaging.types.sort.deserialize_json(data["sort"])
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out


def redact_sensitive(value: SearchImageSetsResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "image_sets_metadata_summaries" in value:
        import capo_medical_imaging.types.image_sets_metadata_summaries

        out["image_sets_metadata_summaries"] = (
            capo_medical_imaging.types.image_sets_metadata_summaries.redact_sensitive(
                value["image_sets_metadata_summaries"]
            )
        )
    return out
