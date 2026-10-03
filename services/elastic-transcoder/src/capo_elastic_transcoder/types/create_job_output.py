"""Generated from Smithy shape ``com.amazonaws.elastictranscoder#CreateJobOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_elastic_transcoder.types.captions
    import capo_elastic_transcoder.types.composition
    import capo_elastic_transcoder.types.encryption
    import capo_elastic_transcoder.types.float_string
    import capo_elastic_transcoder.types.id
    import capo_elastic_transcoder.types.job_album_art
    import capo_elastic_transcoder.types.job_watermarks
    import capo_elastic_transcoder.types.key
    import capo_elastic_transcoder.types.rotate
    import capo_elastic_transcoder.types.thumbnail_pattern


class CreateJobOutput(TypedDict, closed=True):
    key: NotRequired["capo_elastic_transcoder.types.key.Key"]
    """<p> The name to assign to the transcoded file. Elastic Transcoder saves the file in the Amazon S3 bucket specified by the <code>OutputBucket</code> object in the pipeline that is specified by the pipeline ID. If a file with the specified name already exists in the output bucket, the job fails. </p>"""
    thumbnail_pattern: NotRequired[
        "capo_elastic_transcoder.types.thumbnail_pattern.ThumbnailPattern"
    ]
    """<p>Whether you want Elastic Transcoder to create thumbnails for your videos and, if so, how you want Elastic Transcoder to name the files.</p> <p>If you don't want Elastic Transcoder to create thumbnails, specify "".</p> <p>If you do want Elastic Transcoder to create thumbnails, specify the information that you want to include in the file name for each thumbnail. You can specify the following values in any sequence:</p> <ul> <li> <p> <b> <code>{count}</code> (Required)</b>: If you want to create thumbnails, you must include <code>{count}</code> in the <code>ThumbnailPattern</code> object. Wherever you specify <code>{count}</code>, Elastic Transcoder adds a five-digit sequence number (beginning with <b>00001</b>) to thumbnail file names. The number indicates where a given thumbnail appears in the sequence of thumbnails for a transcoded file. </p> <important> <p>If you specify a literal value and/or <code>{resolution}</code> but you omit <code>{count}</code>, Elastic Transcoder returns a validation error and does not create the job.</p> </important> </li> <li> <p> <b>Literal values (Optional)</b>: You can specify literal values anywhere in the <code>ThumbnailPattern</code> object. For example, you can include them as a file name prefix or as a delimiter between <code>{resolution}</code> and <code>{count}</code>. </p> </li> <li> <p> <b> <code>{resolution}</code> (Optional)</b>: If you want Elastic Transcoder to include the resolution in the file name, include <code>{resolution}</code> in the <code>ThumbnailPattern</code> object. </p> </li> </ul> <p>When creating thumbnails, Elastic Transcoder automatically saves the files in the format (.jpg or .png) that appears in the preset that you specified in the <code>PresetID</code> value of <code>CreateJobOutput</code>. Elastic Transcoder also appends the applicable file name extension.</p>"""
    thumbnail_encryption: NotRequired[
        "capo_elastic_transcoder.types.encryption.Encryption"
    ]
    """<p>The encryption settings, if any, that you want Elastic Transcoder to apply to your thumbnail.</p>"""
    rotate: NotRequired["capo_elastic_transcoder.types.rotate.Rotate"]
    """<p> The number of degrees clockwise by which you want Elastic Transcoder to rotate the output relative to the input. Enter one of the following values: <code>auto</code>, <code>0</code>, <code>90</code>, <code>180</code>, <code>270</code>. The value <code>auto</code> generally works only if the file that you're transcoding contains rotation metadata. </p>"""
    preset_id: NotRequired["capo_elastic_transcoder.types.id.Id"]
    """<p> The <code>Id</code> of the preset to use for this job. The preset determines the audio, video, and thumbnail settings that Elastic Transcoder uses for transcoding. </p>"""
    segment_duration: NotRequired[
        "capo_elastic_transcoder.types.float_string.FloatString"
    ]
    """<important> <p>(Outputs in Fragmented MP4 or MPEG-TS format only.</p> </important> <p>If you specify a preset in <code>PresetId</code> for which the value of <code>Container</code> is <code>fmp4</code> (Fragmented MP4) or <code>ts</code> (MPEG-TS), <code>SegmentDuration</code> is the target maximum duration of each segment in seconds. For <code>HLSv3</code> format playlists, each media segment is stored in a separate <code>.ts</code> file. For <code>HLSv4</code> and <code>Smooth</code> playlists, all media segments for an output are stored in a single file. Each segment is approximately the length of the <code>SegmentDuration</code>, though individual segments might be shorter or longer.</p> <p>The range of valid values is 1 to 60 seconds. If the duration of the video is not evenly divisible by <code>SegmentDuration</code>, the duration of the last segment is the remainder of total length/SegmentDuration.</p> <p>Elastic Transcoder creates an output-specific playlist for each output <code>HLS</code> output that you specify in OutputKeys. To add an output to the master playlist for this job, include it in the <code>OutputKeys</code> of the associated playlist.</p>"""
    watermarks: NotRequired[
        "capo_elastic_transcoder.types.job_watermarks.JobWatermarks"
    ]
    """<p>Information about the watermarks that you want Elastic Transcoder to add to the video during transcoding. You can specify up to four watermarks for each output. Settings for each watermark must be defined in the preset for the current output.</p>"""
    album_art: NotRequired["capo_elastic_transcoder.types.job_album_art.JobAlbumArt"]
    """<p>Information about the album art that you want Elastic Transcoder to add to the file during transcoding. You can specify up to twenty album artworks for each output. Settings for each artwork must be defined in the job for the current output.</p>"""
    composition: NotRequired["capo_elastic_transcoder.types.composition.Composition"]
    """<p>You can create an output file that contains an excerpt from the input file. This excerpt, called a clip, can come from the beginning, middle, or end of the file. The Composition object contains settings for the clips that make up an output file. For the current release, you can only specify settings for a single clip per output file. The Composition object cannot be null.</p>"""
    captions: NotRequired["capo_elastic_transcoder.types.captions.Captions"]
    """<p>You can configure Elastic Transcoder to transcode captions, or subtitles, from one format to another. All captions must be in UTF-8. Elastic Transcoder supports two types of captions:</p> <ul> <li> <p> <b>Embedded:</b> Embedded captions are included in the same file as the audio and video. Elastic Transcoder supports only one embedded caption per language, to a maximum of 300 embedded captions per file.</p> <p>Valid input values include: <code>CEA-608 (EIA-608</code>, first non-empty channel only), <code>CEA-708 (EIA-708</code>, first non-empty channel only), and <code>mov-text</code> </p> <p>Valid outputs include: <code>mov-text</code> </p> <p>Elastic Transcoder supports a maximum of one embedded format per output.</p> </li> <li> <p> <b>Sidecar:</b> Sidecar captions are kept in a separate metadata file from the audio and video data. Sidecar captions require a player that is capable of understanding the relationship between the video file and the sidecar file. Elastic Transcoder supports only one sidecar caption per language, to a maximum of 20 sidecar captions per file.</p> <p>Valid input values include: <code>dfxp</code> (first div element only), <code>ebu-tt</code>, <code>scc</code>, <code>smpt</code>, <code>srt</code>, <code>ttml</code> (first div element only), and <code>webvtt</code> </p> <p>Valid outputs include: <code>dfxp</code> (first div element only), <code>scc</code>, <code>srt</code>, and <code>webvtt</code>.</p> </li> </ul> <p>If you want ttml or smpte-tt compatible captions, specify dfxp as your output format.</p> <p>Elastic Transcoder does not support OCR (Optical Character Recognition), does not accept pictures as a valid input for captions, and is not available for audio-only transcoding. Elastic Transcoder does not preserve text formatting (for example, italics) during the transcoding process.</p> <p>To remove captions or leave the captions empty, set <code>Captions</code> to null. To pass through existing captions unchanged, set the <code>MergePolicy</code> to <code>MergeRetain</code>, and pass in a null <code>CaptionSources</code> array.</p> <p>For more information on embedded files, see the Subtitles Wikipedia page.</p> <p>For more information on sidecar files, see the Extensible Metadata Platform and Sidecar file Wikipedia pages.</p>"""
    encryption: NotRequired["capo_elastic_transcoder.types.encryption.Encryption"]
    """<p>You can specify encryption settings for any output files that you want to use for a transcoding job. This includes the output file and any watermarks, thumbnails, album art, or captions that you want to use. You must specify encryption settings for each file individually.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateJobOutput) -> dict:
    out: dict = {}
    if "key" in value:
        out["Key"] = value["key"]
    if "thumbnail_pattern" in value:
        out["ThumbnailPattern"] = value["thumbnail_pattern"]
    if "thumbnail_encryption" in value:
        import capo_elastic_transcoder.types.encryption

        out["ThumbnailEncryption"] = (
            capo_elastic_transcoder.types.encryption.serialize_json(
                value["thumbnail_encryption"]
            )
        )
    if "rotate" in value:
        out["Rotate"] = value["rotate"]
    if "preset_id" in value:
        out["PresetId"] = value["preset_id"]
    if "segment_duration" in value:
        out["SegmentDuration"] = value["segment_duration"]
    if "watermarks" in value:
        import capo_elastic_transcoder.types.job_watermarks

        out["Watermarks"] = capo_elastic_transcoder.types.job_watermarks.serialize_json(
            value["watermarks"]
        )
    if "album_art" in value:
        import capo_elastic_transcoder.types.job_album_art

        out["AlbumArt"] = capo_elastic_transcoder.types.job_album_art.serialize_json(
            value["album_art"]
        )
    if "composition" in value:
        import capo_elastic_transcoder.types.composition

        out["Composition"] = capo_elastic_transcoder.types.composition.serialize_json(
            value["composition"]
        )
    if "captions" in value:
        import capo_elastic_transcoder.types.captions

        out["Captions"] = capo_elastic_transcoder.types.captions.serialize_json(
            value["captions"]
        )
    if "encryption" in value:
        import capo_elastic_transcoder.types.encryption

        out["Encryption"] = capo_elastic_transcoder.types.encryption.serialize_json(
            value["encryption"]
        )
    return out


def deserialize_json(data: dict) -> CreateJobOutput:
    out: CreateJobOutput = {}  # type: ignore[typeddict-item]
    if data.get("Key") is not None:
        out["key"] = data["Key"]
    if data.get("ThumbnailPattern") is not None:
        out["thumbnail_pattern"] = data["ThumbnailPattern"]
    if data.get("ThumbnailEncryption") is not None:
        import capo_elastic_transcoder.types.encryption

        out["thumbnail_encryption"] = (
            capo_elastic_transcoder.types.encryption.deserialize_json(
                data["ThumbnailEncryption"]
            )
        )
    if data.get("Rotate") is not None:
        out["rotate"] = data["Rotate"]
    if data.get("PresetId") is not None:
        out["preset_id"] = data["PresetId"]
    if data.get("SegmentDuration") is not None:
        out["segment_duration"] = data["SegmentDuration"]
    if data.get("Watermarks") is not None:
        import capo_elastic_transcoder.types.job_watermarks

        out["watermarks"] = (
            capo_elastic_transcoder.types.job_watermarks.deserialize_json(
                data["Watermarks"]
            )
        )
    if data.get("AlbumArt") is not None:
        import capo_elastic_transcoder.types.job_album_art

        out["album_art"] = capo_elastic_transcoder.types.job_album_art.deserialize_json(
            data["AlbumArt"]
        )
    if data.get("Composition") is not None:
        import capo_elastic_transcoder.types.composition

        out["composition"] = capo_elastic_transcoder.types.composition.deserialize_json(
            data["Composition"]
        )
    if data.get("Captions") is not None:
        import capo_elastic_transcoder.types.captions

        out["captions"] = capo_elastic_transcoder.types.captions.deserialize_json(
            data["Captions"]
        )
    if data.get("Encryption") is not None:
        import capo_elastic_transcoder.types.encryption

        out["encryption"] = capo_elastic_transcoder.types.encryption.deserialize_json(
            data["Encryption"]
        )
    return out
