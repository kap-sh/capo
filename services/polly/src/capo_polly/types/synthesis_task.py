"""Generated from Smithy shape ``com.amazonaws.polly#SynthesisTask``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_polly.types.date_time
    import capo_polly.types.engine
    import capo_polly.types.language_code
    import capo_polly.types.lexicon_name_list
    import capo_polly.types.output_format
    import capo_polly.types.output_uri
    import capo_polly.types.request_characters
    import capo_polly.types.sample_rate
    import capo_polly.types.sns_topic_arn
    import capo_polly.types.speech_mark_type_list
    import capo_polly.types.task_id
    import capo_polly.types.task_status
    import capo_polly.types.task_status_reason
    import capo_polly.types.text_type
    import capo_polly.types.voice_id


class SynthesisTask(TypedDict, closed=True):
    engine: NotRequired["capo_polly.types.engine.Engine"]
    """<p>Specifies the engine (<code>standard</code>, <code>neural</code>, <code>long-form</code> or <code>generative</code>) for Amazon Polly to use when processing input text for speech synthesis. Using a voice that is not supported for the engine selected will result in an error.</p>"""
    task_id: NotRequired["capo_polly.types.task_id.TaskId"]
    """<p>The Amazon Polly generated identifier for a speech synthesis task.</p>"""
    task_status: NotRequired["capo_polly.types.task_status.TaskStatus"]
    """<p>Current status of the individual speech synthesis task.</p>"""
    task_status_reason: NotRequired[
        "capo_polly.types.task_status_reason.TaskStatusReason"
    ]
    """<p>Reason for the current status of a specific speech synthesis task, including errors if the task has failed.</p>"""
    output_uri: NotRequired["capo_polly.types.output_uri.OutputUri"]
    """<p>Pathway for the output speech file.</p>"""
    creation_time: NotRequired["capo_polly.types.date_time.DateTime"]
    """<p>Timestamp for the time the synthesis task was started.</p>"""
    request_characters: "capo_polly.types.request_characters.RequestCharacters"
    """<p>Number of billable characters synthesized.</p>"""
    sns_topic_arn: NotRequired["capo_polly.types.sns_topic_arn.SnsTopicArn"]
    """<p>ARN for the SNS topic optionally used for providing status notification for a speech synthesis task.</p>"""
    lexicon_names: NotRequired["capo_polly.types.lexicon_name_list.LexiconNameList"]
    """<p>List of one or more pronunciation lexicon names you want the service to apply during synthesis. Lexicons are applied only if the language of the lexicon is the same as the language of the voice. </p>"""
    output_format: NotRequired["capo_polly.types.output_format.OutputFormat"]
    """<p>The format in which the returned output will be encoded. For audio stream, this will be mp3, ogg_vorbis, ogg_opus, mu-law, a-law, or pcm. For speech marks, this will be json. </p>"""
    sample_rate: NotRequired["capo_polly.types.sample_rate.SampleRate"]
    """<p>The audio frequency specified in Hz.</p> <p>The valid values for mp3 and ogg_vorbis are "8000", "16000", "22050", and "24000". The default value for standard voices is "22050". The default value for neural voices is "24000". The default value for long-form voices is "24000". The default value for generative voices is "24000".</p> <p>Valid values for pcm are "8000" and "16000" The default value is "16000". </p> <p>Valid value for ogg_opus is "48000". </p> <p>Valid value for mu-law and a-law is "8000". </p>"""
    speech_mark_types: NotRequired[
        "capo_polly.types.speech_mark_type_list.SpeechMarkTypeList"
    ]
    """<p>The type of speech marks returned for the input text.</p>"""
    text_type: NotRequired["capo_polly.types.text_type.TextType"]
    """<p>Specifies whether the input text is plain text or SSML. The default value is plain text. </p>"""
    voice_id: NotRequired["capo_polly.types.voice_id.VoiceId"]
    """<p>Voice ID to use for the synthesis. </p>"""
    language_code: NotRequired["capo_polly.types.language_code.LanguageCode"]
    """<p>Optional language code for a synthesis task. This is only necessary if using a bilingual voice, such as Aditi, which can be used for either Indian English (en-IN) or Hindi (hi-IN). </p> <p>If a bilingual voice is used and no language code is specified, Amazon Polly uses the default language of the bilingual voice. The default language for any voice is the one returned by the <a href="https://docs.aws.amazon.com/polly/latest/dg/API_DescribeVoices.html">DescribeVoices</a> operation for the <code>LanguageCode</code> parameter. For example, if no language code is specified, Aditi will use Indian English rather than Hindi.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SynthesisTask) -> dict:
    out: dict = {}
    if "engine" in value:
        import capo_polly.types.engine

        out["Engine"] = capo_polly.types.engine.serialize_json(value["engine"])
    if "task_id" in value:
        out["TaskId"] = value["task_id"]
    if "task_status" in value:
        import capo_polly.types.task_status

        out["TaskStatus"] = capo_polly.types.task_status.serialize_json(
            value["task_status"]
        )
    if "task_status_reason" in value:
        out["TaskStatusReason"] = value["task_status_reason"]
    if "output_uri" in value:
        out["OutputUri"] = value["output_uri"]
    if "creation_time" in value:
        import capo_polly.types.date_time

        out["CreationTime"] = capo_polly.types.date_time.serialize_json(
            value["creation_time"]
        )
    out["RequestCharacters"] = value.get("request_characters", 0)
    if "sns_topic_arn" in value:
        out["SnsTopicArn"] = value["sns_topic_arn"]
    if "lexicon_names" in value:
        import capo_polly.types.lexicon_name_list

        out["LexiconNames"] = capo_polly.types.lexicon_name_list.serialize_json(
            value["lexicon_names"]
        )
    if "output_format" in value:
        import capo_polly.types.output_format

        out["OutputFormat"] = capo_polly.types.output_format.serialize_json(
            value["output_format"]
        )
    if "sample_rate" in value:
        out["SampleRate"] = value["sample_rate"]
    if "speech_mark_types" in value:
        import capo_polly.types.speech_mark_type_list

        out["SpeechMarkTypes"] = capo_polly.types.speech_mark_type_list.serialize_json(
            value["speech_mark_types"]
        )
    if "text_type" in value:
        import capo_polly.types.text_type

        out["TextType"] = capo_polly.types.text_type.serialize_json(value["text_type"])
    if "voice_id" in value:
        import capo_polly.types.voice_id

        out["VoiceId"] = capo_polly.types.voice_id.serialize_json(value["voice_id"])
    if "language_code" in value:
        import capo_polly.types.language_code

        out["LanguageCode"] = capo_polly.types.language_code.serialize_json(
            value["language_code"]
        )
    return out


def deserialize_json(data: dict) -> SynthesisTask:
    out: SynthesisTask = {}  # type: ignore[typeddict-item]
    if data.get("Engine") is not None:
        import capo_polly.types.engine

        out["engine"] = capo_polly.types.engine.deserialize_json(data["Engine"])
    if data.get("TaskId") is not None:
        out["task_id"] = data["TaskId"]
    if data.get("TaskStatus") is not None:
        import capo_polly.types.task_status

        out["task_status"] = capo_polly.types.task_status.deserialize_json(
            data["TaskStatus"]
        )
    if data.get("TaskStatusReason") is not None:
        out["task_status_reason"] = data["TaskStatusReason"]
    if data.get("OutputUri") is not None:
        out["output_uri"] = data["OutputUri"]
    if data.get("CreationTime") is not None:
        import capo_polly.types.date_time

        out["creation_time"] = capo_polly.types.date_time.deserialize_json(
            data["CreationTime"]
        )
    if data.get("RequestCharacters") is not None:
        out["request_characters"] = data["RequestCharacters"]
    else:
        out["request_characters"] = 0
    if data.get("SnsTopicArn") is not None:
        out["sns_topic_arn"] = data["SnsTopicArn"]
    if data.get("LexiconNames") is not None:
        import capo_polly.types.lexicon_name_list

        out["lexicon_names"] = capo_polly.types.lexicon_name_list.deserialize_json(
            data["LexiconNames"]
        )
    if data.get("OutputFormat") is not None:
        import capo_polly.types.output_format

        out["output_format"] = capo_polly.types.output_format.deserialize_json(
            data["OutputFormat"]
        )
    if data.get("SampleRate") is not None:
        out["sample_rate"] = data["SampleRate"]
    if data.get("SpeechMarkTypes") is not None:
        import capo_polly.types.speech_mark_type_list

        out["speech_mark_types"] = (
            capo_polly.types.speech_mark_type_list.deserialize_json(
                data["SpeechMarkTypes"]
            )
        )
    if data.get("TextType") is not None:
        import capo_polly.types.text_type

        out["text_type"] = capo_polly.types.text_type.deserialize_json(data["TextType"])
    if data.get("VoiceId") is not None:
        import capo_polly.types.voice_id

        out["voice_id"] = capo_polly.types.voice_id.deserialize_json(data["VoiceId"])
    if data.get("LanguageCode") is not None:
        import capo_polly.types.language_code

        out["language_code"] = capo_polly.types.language_code.deserialize_json(
            data["LanguageCode"]
        )
    return out
