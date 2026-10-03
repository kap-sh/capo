"""Generated from Smithy shape ``com.amazonaws.mediaconvert#Mp4Settings``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mediaconvert.types.__integer_min0_max1
    import capo_mediaconvert.types.__string
    import capo_mediaconvert.types.__string_min1_max2048_pattern_arn_az_secretsmanager_wd12_secret_azaz09
    import capo_mediaconvert.types.__string_min1_pattern_arn_aws_us_gov_cn_kms_az26_east_west_central_north_south_east_west1912_d12_key_afaf098_afaf094_afaf094_afaf094_afaf0912_mrk_afaf0932
    import capo_mediaconvert.types.cmfc_audio_duration
    import capo_mediaconvert.types.mp4_c2pa_manifest
    import capo_mediaconvert.types.mp4_cslg_atom
    import capo_mediaconvert.types.mp4_free_space_box
    import capo_mediaconvert.types.mp4_moov_placement


class Mp4Settings(TypedDict, closed=True):
    audio_duration: NotRequired[
        "capo_mediaconvert.types.cmfc_audio_duration.CmfcAudioDuration"
    ]
    """Specify this setting only when your output will be consumed by a downstream repackaging workflow that is sensitive to very small duration differences between video and audio. For this situation, choose Match video duration. In all other cases, keep the default value, Default codec duration. When you choose Match video duration, MediaConvert pads the output audio streams with silence or trims them to ensure that the total duration of each audio stream is at least as long as the total duration of the video stream. After padding or trimming, the audio stream duration is no more than one frame longer than the video stream. MediaConvert applies audio padding or trimming only to the end of the last segment of the output. For unsegmented outputs, MediaConvert adds padding only to the end of the file. When you keep the default value, any minor discrepancies between audio and video duration will depend on your output audio codec."""
    c2pa_manifest: NotRequired[
        "capo_mediaconvert.types.mp4_c2pa_manifest.Mp4C2paManifest"
    ]
    """When enabled, a C2PA compliant manifest will be generated, signed and embeded in the output. For more information on C2PA, see https://c2pa.org/specifications/specifications/2.1/index.html"""
    certificate_secret: NotRequired[
        "capo_mediaconvert.types.__string_min1_max2048_pattern_arn_az_secretsmanager_wd12_secret_azaz09.__stringMin1Max2048PatternArnAZSecretsmanagerWD12SecretAZAZ09"
    ]
    """Specify the name or ARN of the AWS Secrets Manager secret that contains your C2PA public certificate chain in PEM format. Provide a valid secret name or ARN. Note that your MediaConvert service role must allow access to this secret. The public certificate chain is added to the COSE header (x5chain) for signature validation. Include the signer's certificate and all intermediate certificates. Do not include the root certificate. For details on COSE, see: https://opensource.contentauthenticity.org/docs/manifest/signing-manifests"""
    cslg_atom: NotRequired["capo_mediaconvert.types.mp4_cslg_atom.Mp4CslgAtom"]
    """When enabled, file composition times will start at zero, composition times in the 'ctts' (composition time to sample) box for B-frames will be negative, and a 'cslg' (composition shift least greatest) box will be included per 14496-1 amendment 1. This improves compatibility with Apple players and tools."""
    ctts_version: NotRequired[
        "capo_mediaconvert.types.__integer_min0_max1.__integerMin0Max1"
    ]
    """Ignore this setting unless compliance to the CTTS box version specification matters in your workflow. Specify a value of 1 to set your CTTS box version to 1 and make your output compliant with the specification. When you specify a value of 1, you must also set CSLG atom to the value INCLUDE. Keep the default value 0 to set your CTTS box version to 0. This can provide backward compatibility for some players and packagers."""
    free_space_box: NotRequired[
        "capo_mediaconvert.types.mp4_free_space_box.Mp4FreeSpaceBox"
    ]
    """Inserts a free-space box immediately after the moov box."""
    moov_placement: NotRequired[
        "capo_mediaconvert.types.mp4_moov_placement.Mp4MoovPlacement"
    ]
    """To place the MOOV atom at the beginning of your output, which is useful for progressive downloading: Leave blank or choose Progressive download. To place the MOOV at the end of your output: Choose Normal."""
    mp4_major_brand: NotRequired["capo_mediaconvert.types.__string.__string"]
    """Overrides the "Major Brand" field in the output file. Usually not necessary to specify."""
    signing_kms_key: NotRequired[
        "capo_mediaconvert.types.__string_min1_pattern_arn_aws_us_gov_cn_kms_az26_east_west_central_north_south_east_west1912_d12_key_afaf098_afaf094_afaf094_afaf094_afaf0912_mrk_afaf0932.__stringMin1PatternArnAwsUsGovCnKmsAZ26EastWestCentralNorthSouthEastWest1912D12KeyAFAF098AFAF094AFAF094AFAF094AFAF0912MrkAFAF0932"
    ]
    """Specify the ID or ARN of the AWS KMS key used to sign the C2PA manifest in your MP4 output. Provide a valid KMS key ARN. Note that your MediaConvert service role must allow access to this key."""


# --- restJson1 ser/de ---
def serialize_json(value: Mp4Settings) -> dict:
    out: dict = {}
    if "audio_duration" in value:
        import capo_mediaconvert.types.cmfc_audio_duration

        out["audioDuration"] = (
            capo_mediaconvert.types.cmfc_audio_duration.serialize_json(
                value["audio_duration"]
            )
        )
    if "c2pa_manifest" in value:
        import capo_mediaconvert.types.mp4_c2pa_manifest

        out["c2paManifest"] = capo_mediaconvert.types.mp4_c2pa_manifest.serialize_json(
            value["c2pa_manifest"]
        )
    if "certificate_secret" in value:
        out["certificateSecret"] = value["certificate_secret"]
    if "cslg_atom" in value:
        import capo_mediaconvert.types.mp4_cslg_atom

        out["cslgAtom"] = capo_mediaconvert.types.mp4_cslg_atom.serialize_json(
            value["cslg_atom"]
        )
    if "ctts_version" in value:
        out["cttsVersion"] = value["ctts_version"]
    if "free_space_box" in value:
        import capo_mediaconvert.types.mp4_free_space_box

        out["freeSpaceBox"] = capo_mediaconvert.types.mp4_free_space_box.serialize_json(
            value["free_space_box"]
        )
    if "moov_placement" in value:
        import capo_mediaconvert.types.mp4_moov_placement

        out["moovPlacement"] = (
            capo_mediaconvert.types.mp4_moov_placement.serialize_json(
                value["moov_placement"]
            )
        )
    if "mp4_major_brand" in value:
        out["mp4MajorBrand"] = value["mp4_major_brand"]
    if "signing_kms_key" in value:
        out["signingKmsKey"] = value["signing_kms_key"]
    return out


def deserialize_json(data: dict) -> Mp4Settings:
    out: Mp4Settings = {}  # type: ignore[typeddict-item]
    if data.get("audioDuration") is not None:
        import capo_mediaconvert.types.cmfc_audio_duration

        out["audio_duration"] = (
            capo_mediaconvert.types.cmfc_audio_duration.deserialize_json(
                data["audioDuration"]
            )
        )
    if data.get("c2paManifest") is not None:
        import capo_mediaconvert.types.mp4_c2pa_manifest

        out["c2pa_manifest"] = (
            capo_mediaconvert.types.mp4_c2pa_manifest.deserialize_json(
                data["c2paManifest"]
            )
        )
    if data.get("certificateSecret") is not None:
        out["certificate_secret"] = data["certificateSecret"]
    if data.get("cslgAtom") is not None:
        import capo_mediaconvert.types.mp4_cslg_atom

        out["cslg_atom"] = capo_mediaconvert.types.mp4_cslg_atom.deserialize_json(
            data["cslgAtom"]
        )
    if data.get("cttsVersion") is not None:
        out["ctts_version"] = data["cttsVersion"]
    if data.get("freeSpaceBox") is not None:
        import capo_mediaconvert.types.mp4_free_space_box

        out["free_space_box"] = (
            capo_mediaconvert.types.mp4_free_space_box.deserialize_json(
                data["freeSpaceBox"]
            )
        )
    if data.get("moovPlacement") is not None:
        import capo_mediaconvert.types.mp4_moov_placement

        out["moov_placement"] = (
            capo_mediaconvert.types.mp4_moov_placement.deserialize_json(
                data["moovPlacement"]
            )
        )
    if data.get("mp4MajorBrand") is not None:
        out["mp4_major_brand"] = data["mp4MajorBrand"]
    if data.get("signingKmsKey") is not None:
        out["signing_kms_key"] = data["signingKmsKey"]
    return out
