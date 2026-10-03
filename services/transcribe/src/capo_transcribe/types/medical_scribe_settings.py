"""Generated from Smithy shape ``com.amazonaws.transcribe#MedicalScribeSettings``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_transcribe.types.boolean
    import capo_transcribe.types.clinical_note_generation_settings
    import capo_transcribe.types.max_speakers
    import capo_transcribe.types.vocabulary_filter_method
    import capo_transcribe.types.vocabulary_filter_name
    import capo_transcribe.types.vocabulary_name


class MedicalScribeSettings(TypedDict, closed=True):
    show_speaker_labels: NotRequired["capo_transcribe.types.boolean.Boolean"]
    """<p>Enables speaker partitioning (diarization) in your Medical Scribe output. Speaker partitioning labels the speech from individual speakers in your media file.</p> <p>If you enable <code>ShowSpeakerLabels</code> in your request, you must also include <code>MaxSpeakerLabels</code>.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/transcribe/latest/dg/diarization.html">Partitioning speakers (diarization)</a>.</p>"""
    max_speaker_labels: NotRequired["capo_transcribe.types.max_speakers.MaxSpeakers"]
    """<p>Specify the maximum number of speakers you want to partition in your media.</p> <p>Note that if your media contains more speakers than the specified number, multiple speakers are treated as a single speaker.</p> <p>If you specify the <code>MaxSpeakerLabels</code> field, you must set the <code>ShowSpeakerLabels</code> field to true.</p>"""
    channel_identification: NotRequired["capo_transcribe.types.boolean.Boolean"]
    """<p>Enables channel identification in multi-channel audio.</p> <p>Channel identification transcribes the audio on each channel independently, then appends the output for each channel into one transcript.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/transcribe/latest/dg/channel-id.html">Transcribing multi-channel audio</a>.</p>"""
    vocabulary_name: NotRequired["capo_transcribe.types.vocabulary_name.VocabularyName"]
    """<p>The name of the custom vocabulary you want to include in your Medical Scribe request. Custom vocabulary names are case sensitive.</p>"""
    vocabulary_filter_name: NotRequired[
        "capo_transcribe.types.vocabulary_filter_name.VocabularyFilterName"
    ]
    """<p>The name of the custom vocabulary filter you want to include in your Medical Scribe request. Custom vocabulary filter names are case sensitive.</p> <p>Note that if you include <code>VocabularyFilterName</code> in your request, you must also include <code>VocabularyFilterMethod</code>.</p>"""
    vocabulary_filter_method: NotRequired[
        "capo_transcribe.types.vocabulary_filter_method.VocabularyFilterMethod"
    ]
    """<p>Specify how you want your custom vocabulary filter applied to your transcript.</p> <p>To replace words with <code>***</code>, choose <code>mask</code>.</p> <p>To delete words, choose <code>remove</code>.</p> <p>To flag words without changing them, choose <code>tag</code>.</p>"""
    clinical_note_generation_settings: NotRequired[
        "capo_transcribe.types.clinical_note_generation_settings.ClinicalNoteGenerationSettings"
    ]
    """<p>Specify settings for the clinical note generation.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: MedicalScribeSettings) -> dict:
    out: dict = {}
    if "show_speaker_labels" in value:
        out["ShowSpeakerLabels"] = value["show_speaker_labels"]
    if "max_speaker_labels" in value:
        out["MaxSpeakerLabels"] = value["max_speaker_labels"]
    if "channel_identification" in value:
        out["ChannelIdentification"] = value["channel_identification"]
    if "vocabulary_name" in value:
        out["VocabularyName"] = value["vocabulary_name"]
    if "vocabulary_filter_name" in value:
        out["VocabularyFilterName"] = value["vocabulary_filter_name"]
    if "vocabulary_filter_method" in value:
        import capo_transcribe.types.vocabulary_filter_method

        out["VocabularyFilterMethod"] = (
            capo_transcribe.types.vocabulary_filter_method.serialize_aws_json_1_1(
                value["vocabulary_filter_method"]
            )
        )
    if "clinical_note_generation_settings" in value:
        import capo_transcribe.types.clinical_note_generation_settings

        out["ClinicalNoteGenerationSettings"] = (
            capo_transcribe.types.clinical_note_generation_settings.serialize_aws_json_1_1(
                value["clinical_note_generation_settings"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> MedicalScribeSettings:
    out: MedicalScribeSettings = {}  # type: ignore[typeddict-item]
    if data.get("ShowSpeakerLabels") is not None:
        out["show_speaker_labels"] = data["ShowSpeakerLabels"]
    if data.get("MaxSpeakerLabels") is not None:
        out["max_speaker_labels"] = data["MaxSpeakerLabels"]
    if data.get("ChannelIdentification") is not None:
        out["channel_identification"] = data["ChannelIdentification"]
    if data.get("VocabularyName") is not None:
        out["vocabulary_name"] = data["VocabularyName"]
    if data.get("VocabularyFilterName") is not None:
        out["vocabulary_filter_name"] = data["VocabularyFilterName"]
    if data.get("VocabularyFilterMethod") is not None:
        import capo_transcribe.types.vocabulary_filter_method

        out["vocabulary_filter_method"] = (
            capo_transcribe.types.vocabulary_filter_method.deserialize_aws_json_1_1(
                data["VocabularyFilterMethod"]
            )
        )
    if data.get("ClinicalNoteGenerationSettings") is not None:
        import capo_transcribe.types.clinical_note_generation_settings

        out["clinical_note_generation_settings"] = (
            capo_transcribe.types.clinical_note_generation_settings.deserialize_aws_json_1_1(
                data["ClinicalNoteGenerationSettings"]
            )
        )
    return out
