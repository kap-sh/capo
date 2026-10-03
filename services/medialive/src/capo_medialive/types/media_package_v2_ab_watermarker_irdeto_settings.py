"""Generated from Smithy shape ``com.amazonaws.medialive#MediaPackageV2AbWatermarkerIrdetoSettings``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_medialive.types.__integer_min1_max511
    import capo_medialive.types.__integer_min1_max1000
    import capo_medialive.types.__list_of_output_location_ref
    import capo_medialive.types.__string
    import capo_medialive.types.ab_watermarker_id_length
    import capo_medialive.types.ab_watermarking_custom_profile
    import capo_medialive.types.ab_watermarking_profile
    import capo_medialive.types.output_location_ref


class MediaPackageV2AbWatermarkerIrdetoSettings(TypedDict, closed=True):
    additional_destinations_alternate_destinations: NotRequired[
        "capo_medialive.types.__list_of_output_location_ref.__listOfOutputLocationRef"
    ]
    """The "B" pipeline renditions for the additional destinations."""
    alternate_destination: NotRequired[
        "capo_medialive.types.output_location_ref.OutputLocationRef"
    ]
    """The "B" pipeline renditions for the main destination."""
    custom_profile: NotRequired[
        "capo_medialive.types.ab_watermarking_custom_profile.AbWatermarkingCustomProfile"
    ]
    """The vendor-provided custom profile values."""
    license: NotRequired["capo_medialive.types.__string.__string"]
    """The name of the Secrets Manager secret containing the license file."""
    operator_id: NotRequired[
        "capo_medialive.types.__integer_min1_max511.__integerMin1Max511"
    ]
    """The vendor-provided Operator ID."""
    poly_period: NotRequired[
        "capo_medialive.types.__integer_min1_max1000.__integerMin1Max1000"
    ]
    """The number of segments per watermarking bit. The total duration of the watermarking bit should be the LCM (least common multiple) of all segments sizes emitted by the downstream packager."""
    profile: NotRequired[
        "capo_medialive.types.ab_watermarking_profile.AbWatermarkingProfile"
    ]
    """The vendor-provided profile choice."""
    watermark_id_length: NotRequired[
        "capo_medialive.types.ab_watermarker_id_length.AbWatermarkerIdLength"
    ]
    """The number of bits that compose the watermarking identifier to be embedded."""


# --- restJson1 ser/de ---
def serialize_json(value: MediaPackageV2AbWatermarkerIrdetoSettings) -> dict:
    out: dict = {}
    if "additional_destinations_alternate_destinations" in value:
        import capo_medialive.types.__list_of_output_location_ref

        out["additionalDestinationsAlternateDestinations"] = (
            capo_medialive.types.__list_of_output_location_ref.serialize_json(
                value["additional_destinations_alternate_destinations"]
            )
        )
    if "alternate_destination" in value:
        import capo_medialive.types.output_location_ref

        out["alternateDestination"] = (
            capo_medialive.types.output_location_ref.serialize_json(
                value["alternate_destination"]
            )
        )
    if "custom_profile" in value:
        import capo_medialive.types.ab_watermarking_custom_profile

        out["customProfile"] = (
            capo_medialive.types.ab_watermarking_custom_profile.serialize_json(
                value["custom_profile"]
            )
        )
    if "license" in value:
        out["license"] = value["license"]
    if "operator_id" in value:
        out["operatorId"] = value["operator_id"]
    if "poly_period" in value:
        out["polyPeriod"] = value["poly_period"]
    if "profile" in value:
        import capo_medialive.types.ab_watermarking_profile

        out["profile"] = capo_medialive.types.ab_watermarking_profile.serialize_json(
            value["profile"]
        )
    if "watermark_id_length" in value:
        import capo_medialive.types.ab_watermarker_id_length

        out["watermarkIdLength"] = (
            capo_medialive.types.ab_watermarker_id_length.serialize_json(
                value["watermark_id_length"]
            )
        )
    return out


def deserialize_json(data: dict) -> MediaPackageV2AbWatermarkerIrdetoSettings:
    out: MediaPackageV2AbWatermarkerIrdetoSettings = {}  # type: ignore[typeddict-item]
    if data.get("additionalDestinationsAlternateDestinations") is not None:
        import capo_medialive.types.__list_of_output_location_ref

        out["additional_destinations_alternate_destinations"] = (
            capo_medialive.types.__list_of_output_location_ref.deserialize_json(
                data["additionalDestinationsAlternateDestinations"]
            )
        )
    if data.get("alternateDestination") is not None:
        import capo_medialive.types.output_location_ref

        out["alternate_destination"] = (
            capo_medialive.types.output_location_ref.deserialize_json(
                data["alternateDestination"]
            )
        )
    if data.get("customProfile") is not None:
        import capo_medialive.types.ab_watermarking_custom_profile

        out["custom_profile"] = (
            capo_medialive.types.ab_watermarking_custom_profile.deserialize_json(
                data["customProfile"]
            )
        )
    if data.get("license") is not None:
        out["license"] = data["license"]
    if data.get("operatorId") is not None:
        out["operator_id"] = data["operatorId"]
    if data.get("polyPeriod") is not None:
        out["poly_period"] = data["polyPeriod"]
    if data.get("profile") is not None:
        import capo_medialive.types.ab_watermarking_profile

        out["profile"] = capo_medialive.types.ab_watermarking_profile.deserialize_json(
            data["profile"]
        )
    if data.get("watermarkIdLength") is not None:
        import capo_medialive.types.ab_watermarker_id_length

        out["watermark_id_length"] = (
            capo_medialive.types.ab_watermarker_id_length.deserialize_json(
                data["watermarkIdLength"]
            )
        )
    return out
