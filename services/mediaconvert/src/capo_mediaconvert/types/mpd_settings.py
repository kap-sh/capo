"""Generated from Smithy shape ``com.amazonaws.mediaconvert#MpdSettings``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mediaconvert.types.__string_max1000
    import capo_mediaconvert.types.__string_min1_max2048_pattern_arn_az_secretsmanager_wd12_secret_azaz09
    import capo_mediaconvert.types.__string_min1_pattern_arn_aws_us_gov_cn_kms_az26_east_west_central_north_south_east_west1912_d12_key_afaf098_afaf094_afaf094_afaf094_afaf0912_mrk_afaf0932
    import capo_mediaconvert.types.mpd_accessibility_caption_hints
    import capo_mediaconvert.types.mpd_audio_duration
    import capo_mediaconvert.types.mpd_c2pa_manifest
    import capo_mediaconvert.types.mpd_caption_container_type
    import capo_mediaconvert.types.mpd_klv_metadata
    import capo_mediaconvert.types.mpd_manifest_metadata_signaling
    import capo_mediaconvert.types.mpd_scte35_esam
    import capo_mediaconvert.types.mpd_scte35_source
    import capo_mediaconvert.types.mpd_timed_metadata
    import capo_mediaconvert.types.mpd_timed_metadata_box_version


class MpdSettings(TypedDict, closed=True):
    accessibility_caption_hints: NotRequired[
        "capo_mediaconvert.types.mpd_accessibility_caption_hints.MpdAccessibilityCaptionHints"
    ]
    """Optional. Choose Include to have MediaConvert mark up your DASH manifest with <Accessibility> elements for embedded 608 captions. This markup isn't generally required, but some video players require it to discover and play embedded 608 captions. Keep the default value, Exclude, to leave these elements out. When you enable this setting, this is the markup that MediaConvert includes in your manifest: <Accessibility schemeIdUri="urn:scte:dash:cc:cea-608:2015" value="CC1=eng"/>"""
    audio_duration: NotRequired[
        "capo_mediaconvert.types.mpd_audio_duration.MpdAudioDuration"
    ]
    """Specify this setting only when your output will be consumed by a downstream repackaging workflow that is sensitive to very small duration differences between video and audio. For this situation, choose Match video duration. In all other cases, keep the default value, Default codec duration. When you choose Match video duration, MediaConvert pads the output audio streams with silence or trims them to ensure that the total duration of each audio stream is at least as long as the total duration of the video stream. After padding or trimming, the audio stream duration is no more than one frame longer than the video stream. MediaConvert applies audio padding or trimming only to the end of the last segment of the output. For unsegmented outputs, MediaConvert adds padding only to the end of the file. When you keep the default value, any minor discrepancies between audio and video duration will depend on your output audio codec."""
    c2pa_manifest: NotRequired[
        "capo_mediaconvert.types.mpd_c2pa_manifest.MpdC2paManifest"
    ]
    """When enabled, a C2PA compliant manifest will be generated, signed and embeded in the output. For more information on C2PA, see https://c2pa.org/specifications/specifications/2.1/index.html"""
    caption_container_type: NotRequired[
        "capo_mediaconvert.types.mpd_caption_container_type.MpdCaptionContainerType"
    ]
    """Use this setting only in DASH output groups that include sidecar TTML, IMSC or WEBVTT captions. You specify sidecar captions in a separate output from your audio and video. Choose Raw for captions in a single XML file in a raw container. Choose Fragmented MPEG-4 for captions in XML format contained within fragmented MP4 files. This set of fragmented MP4 files is separate from your video and audio fragmented MP4 files."""
    certificate_secret: NotRequired[
        "capo_mediaconvert.types.__string_min1_max2048_pattern_arn_az_secretsmanager_wd12_secret_azaz09.__stringMin1Max2048PatternArnAZSecretsmanagerWD12SecretAZAZ09"
    ]
    """Specify the name or ARN of the AWS Secrets Manager secret that contains your C2PA public certificate chain in PEM format. Provide a valid secret name or ARN. Note that your MediaConvert service role must allow access to this secret. The public certificate chain is added to the COSE header (x5chain) for signature validation. Include the signer's certificate and all intermediate certificates. Do not include the root certificate. For details on COSE, see: https://opensource.contentauthenticity.org/docs/manifest/signing-manifests"""
    klv_metadata: NotRequired["capo_mediaconvert.types.mpd_klv_metadata.MpdKlvMetadata"]
    """To include key-length-value metadata in this output: Set KLV metadata insertion to Passthrough. MediaConvert reads KLV metadata present in your input and writes each instance to a separate event message box in the output, according to MISB ST1910.1. To exclude this KLV metadata: Set KLV metadata insertion to None or leave blank."""
    manifest_metadata_signaling: NotRequired[
        "capo_mediaconvert.types.mpd_manifest_metadata_signaling.MpdManifestMetadataSignaling"
    ]
    """To add an InbandEventStream element in your output MPD manifest for each type of event message, set Manifest metadata signaling to Enabled. For ID3 event messages, the InbandEventStream element schemeIdUri will be same value that you specify for ID3 metadata scheme ID URI. For SCTE35 event messages, the InbandEventStream element schemeIdUri will be "urn:scte:scte35:2013:bin". To leave these elements out of your output MPD manifest, set Manifest metadata signaling to Disabled. To enable Manifest metadata signaling, you must also set SCTE-35 source to Passthrough, ESAM SCTE-35 to insert, or ID3 metadata to Passthrough."""
    scte35_esam: NotRequired["capo_mediaconvert.types.mpd_scte35_esam.MpdScte35Esam"]
    """Use this setting only when you specify SCTE-35 markers from ESAM. Choose INSERT to put SCTE-35 markers in this output at the insertion points that you specify in an ESAM XML document. Provide the document in the setting SCC XML."""
    scte35_source: NotRequired[
        "capo_mediaconvert.types.mpd_scte35_source.MpdScte35Source"
    ]
    """Ignore this setting unless you have SCTE-35 markers in your input video file. Choose Passthrough if you want SCTE-35 markers that appear in your input to also appear in this output. Choose None if you don't want those SCTE-35 markers in this output. When your input is an HLS manifest, choose Manifest cues to pass through CUE markers in your HLS manifest as segment boundaries and SCTE-35 markers in this output at each EXT-X-CUE-OUT splice point in the input manifest."""
    signing_kms_key: NotRequired[
        "capo_mediaconvert.types.__string_min1_pattern_arn_aws_us_gov_cn_kms_az26_east_west_central_north_south_east_west1912_d12_key_afaf098_afaf094_afaf094_afaf094_afaf0912_mrk_afaf0932.__stringMin1PatternArnAwsUsGovCnKmsAZ26EastWestCentralNorthSouthEastWest1912D12KeyAFAF098AFAF094AFAF094AFAF094AFAF0912MrkAFAF0932"
    ]
    """Specify the ID or ARN of the AWS KMS key used to sign the C2PA manifest in your MP4 output. Provide a valid KMS key ARN. Note that your MediaConvert service role must allow access to this key."""
    timed_metadata: NotRequired[
        "capo_mediaconvert.types.mpd_timed_metadata.MpdTimedMetadata"
    ]
    """To include ID3 metadata in this output: Set ID3 metadata to Passthrough. Specify this ID3 metadata in Custom ID3 metadata inserter. MediaConvert writes each instance of ID3 metadata in a separate Event Message (eMSG) box. To exclude this ID3 metadata: Set ID3 metadata to None or leave blank."""
    timed_metadata_box_version: NotRequired[
        "capo_mediaconvert.types.mpd_timed_metadata_box_version.MpdTimedMetadataBoxVersion"
    ]
    """Specify the event message box (eMSG) version for ID3 timed metadata in your output. For more information, see ISO/IEC 23009-1:2022 section 5.10.3.3.3 Syntax. Leave blank to use the default value Version 0. When you specify Version 1, you must also set ID3 metadata to Passthrough."""
    timed_metadata_scheme_id_uri: NotRequired[
        "capo_mediaconvert.types.__string_max1000.__stringMax1000"
    ]
    """Specify the event message box (eMSG) scheme ID URI for ID3 timed metadata in your output. For more information, see ISO/IEC 23009-1:2022 section 5.10.3.3.4 Semantics. Leave blank to use the default value: https://aomedia.org/emsg/ID3 When you specify a value for ID3 metadata scheme ID URI, you must also set ID3 metadata to Passthrough."""
    timed_metadata_value: NotRequired[
        "capo_mediaconvert.types.__string_max1000.__stringMax1000"
    ]
    """Specify the event message box (eMSG) value for ID3 timed metadata in your output. For more information, see ISO/IEC 23009-1:2022 section 5.10.3.3.4 Semantics. When you specify a value for ID3 Metadata Value, you must also set ID3 metadata to Passthrough."""


# --- restJson1 ser/de ---
def serialize_json(value: MpdSettings) -> dict:
    out: dict = {}
    if "accessibility_caption_hints" in value:
        import capo_mediaconvert.types.mpd_accessibility_caption_hints

        out["accessibilityCaptionHints"] = (
            capo_mediaconvert.types.mpd_accessibility_caption_hints.serialize_json(
                value["accessibility_caption_hints"]
            )
        )
    if "audio_duration" in value:
        import capo_mediaconvert.types.mpd_audio_duration

        out["audioDuration"] = (
            capo_mediaconvert.types.mpd_audio_duration.serialize_json(
                value["audio_duration"]
            )
        )
    if "c2pa_manifest" in value:
        import capo_mediaconvert.types.mpd_c2pa_manifest

        out["c2paManifest"] = capo_mediaconvert.types.mpd_c2pa_manifest.serialize_json(
            value["c2pa_manifest"]
        )
    if "caption_container_type" in value:
        import capo_mediaconvert.types.mpd_caption_container_type

        out["captionContainerType"] = (
            capo_mediaconvert.types.mpd_caption_container_type.serialize_json(
                value["caption_container_type"]
            )
        )
    if "certificate_secret" in value:
        out["certificateSecret"] = value["certificate_secret"]
    if "klv_metadata" in value:
        import capo_mediaconvert.types.mpd_klv_metadata

        out["klvMetadata"] = capo_mediaconvert.types.mpd_klv_metadata.serialize_json(
            value["klv_metadata"]
        )
    if "manifest_metadata_signaling" in value:
        import capo_mediaconvert.types.mpd_manifest_metadata_signaling

        out["manifestMetadataSignaling"] = (
            capo_mediaconvert.types.mpd_manifest_metadata_signaling.serialize_json(
                value["manifest_metadata_signaling"]
            )
        )
    if "scte35_esam" in value:
        import capo_mediaconvert.types.mpd_scte35_esam

        out["scte35Esam"] = capo_mediaconvert.types.mpd_scte35_esam.serialize_json(
            value["scte35_esam"]
        )
    if "scte35_source" in value:
        import capo_mediaconvert.types.mpd_scte35_source

        out["scte35Source"] = capo_mediaconvert.types.mpd_scte35_source.serialize_json(
            value["scte35_source"]
        )
    if "signing_kms_key" in value:
        out["signingKmsKey"] = value["signing_kms_key"]
    if "timed_metadata" in value:
        import capo_mediaconvert.types.mpd_timed_metadata

        out["timedMetadata"] = (
            capo_mediaconvert.types.mpd_timed_metadata.serialize_json(
                value["timed_metadata"]
            )
        )
    if "timed_metadata_box_version" in value:
        import capo_mediaconvert.types.mpd_timed_metadata_box_version

        out["timedMetadataBoxVersion"] = (
            capo_mediaconvert.types.mpd_timed_metadata_box_version.serialize_json(
                value["timed_metadata_box_version"]
            )
        )
    if "timed_metadata_scheme_id_uri" in value:
        out["timedMetadataSchemeIdUri"] = value["timed_metadata_scheme_id_uri"]
    if "timed_metadata_value" in value:
        out["timedMetadataValue"] = value["timed_metadata_value"]
    return out


def deserialize_json(data: dict) -> MpdSettings:
    out: MpdSettings = {}  # type: ignore[typeddict-item]
    if data.get("accessibilityCaptionHints") is not None:
        import capo_mediaconvert.types.mpd_accessibility_caption_hints

        out["accessibility_caption_hints"] = (
            capo_mediaconvert.types.mpd_accessibility_caption_hints.deserialize_json(
                data["accessibilityCaptionHints"]
            )
        )
    if data.get("audioDuration") is not None:
        import capo_mediaconvert.types.mpd_audio_duration

        out["audio_duration"] = (
            capo_mediaconvert.types.mpd_audio_duration.deserialize_json(
                data["audioDuration"]
            )
        )
    if data.get("c2paManifest") is not None:
        import capo_mediaconvert.types.mpd_c2pa_manifest

        out["c2pa_manifest"] = (
            capo_mediaconvert.types.mpd_c2pa_manifest.deserialize_json(
                data["c2paManifest"]
            )
        )
    if data.get("captionContainerType") is not None:
        import capo_mediaconvert.types.mpd_caption_container_type

        out["caption_container_type"] = (
            capo_mediaconvert.types.mpd_caption_container_type.deserialize_json(
                data["captionContainerType"]
            )
        )
    if data.get("certificateSecret") is not None:
        out["certificate_secret"] = data["certificateSecret"]
    if data.get("klvMetadata") is not None:
        import capo_mediaconvert.types.mpd_klv_metadata

        out["klv_metadata"] = capo_mediaconvert.types.mpd_klv_metadata.deserialize_json(
            data["klvMetadata"]
        )
    if data.get("manifestMetadataSignaling") is not None:
        import capo_mediaconvert.types.mpd_manifest_metadata_signaling

        out["manifest_metadata_signaling"] = (
            capo_mediaconvert.types.mpd_manifest_metadata_signaling.deserialize_json(
                data["manifestMetadataSignaling"]
            )
        )
    if data.get("scte35Esam") is not None:
        import capo_mediaconvert.types.mpd_scte35_esam

        out["scte35_esam"] = capo_mediaconvert.types.mpd_scte35_esam.deserialize_json(
            data["scte35Esam"]
        )
    if data.get("scte35Source") is not None:
        import capo_mediaconvert.types.mpd_scte35_source

        out["scte35_source"] = (
            capo_mediaconvert.types.mpd_scte35_source.deserialize_json(
                data["scte35Source"]
            )
        )
    if data.get("signingKmsKey") is not None:
        out["signing_kms_key"] = data["signingKmsKey"]
    if data.get("timedMetadata") is not None:
        import capo_mediaconvert.types.mpd_timed_metadata

        out["timed_metadata"] = (
            capo_mediaconvert.types.mpd_timed_metadata.deserialize_json(
                data["timedMetadata"]
            )
        )
    if data.get("timedMetadataBoxVersion") is not None:
        import capo_mediaconvert.types.mpd_timed_metadata_box_version

        out["timed_metadata_box_version"] = (
            capo_mediaconvert.types.mpd_timed_metadata_box_version.deserialize_json(
                data["timedMetadataBoxVersion"]
            )
        )
    if data.get("timedMetadataSchemeIdUri") is not None:
        out["timed_metadata_scheme_id_uri"] = data["timedMetadataSchemeIdUri"]
    if data.get("timedMetadataValue") is not None:
        out["timed_metadata_value"] = data["timedMetadataValue"]
    return out
