"""Generated from Smithy shape ``com.amazonaws.chimesdkmediapipelines#MediaInsightsPipelineConfigurationElement``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_chime_sdk_media_pipelines.types.amazon_transcribe_call_analytics_processor_configuration
    import capo_chime_sdk_media_pipelines.types.amazon_transcribe_processor_configuration
    import capo_chime_sdk_media_pipelines.types.kinesis_data_stream_sink_configuration
    import capo_chime_sdk_media_pipelines.types.lambda_function_sink_configuration
    import capo_chime_sdk_media_pipelines.types.media_insights_pipeline_configuration_element_type
    import capo_chime_sdk_media_pipelines.types.s3_recording_sink_configuration
    import capo_chime_sdk_media_pipelines.types.sns_topic_sink_configuration
    import capo_chime_sdk_media_pipelines.types.sqs_queue_sink_configuration
    import capo_chime_sdk_media_pipelines.types.voice_analytics_processor_configuration
    import capo_chime_sdk_media_pipelines.types.voice_enhancement_sink_configuration


class MediaInsightsPipelineConfigurationElement(TypedDict, closed=True):
    type: "capo_chime_sdk_media_pipelines.types.media_insights_pipeline_configuration_element_type.MediaInsightsPipelineConfigurationElementType"
    """<p>The element type.</p>"""
    amazon_transcribe_call_analytics_processor_configuration: NotRequired[
        "capo_chime_sdk_media_pipelines.types.amazon_transcribe_call_analytics_processor_configuration.AmazonTranscribeCallAnalyticsProcessorConfiguration"
    ]
    """<p>The analytics configuration settings for transcribing audio in a media insights pipeline configuration element.</p>"""
    amazon_transcribe_processor_configuration: NotRequired[
        "capo_chime_sdk_media_pipelines.types.amazon_transcribe_processor_configuration.AmazonTranscribeProcessorConfiguration"
    ]
    """<p>The transcription processor configuration settings in a media insights pipeline configuration element.</p>"""
    kinesis_data_stream_sink_configuration: NotRequired[
        "capo_chime_sdk_media_pipelines.types.kinesis_data_stream_sink_configuration.KinesisDataStreamSinkConfiguration"
    ]
    """<p>The configuration settings for the Kinesis Data Stream Sink in a media insights pipeline configuration element.</p>"""
    s3_recording_sink_configuration: NotRequired[
        "capo_chime_sdk_media_pipelines.types.s3_recording_sink_configuration.S3RecordingSinkConfiguration"
    ]
    """<p>The configuration settings for the Amazon S3 recording bucket in a media insights pipeline configuration element.</p>"""
    voice_analytics_processor_configuration: NotRequired[
        "capo_chime_sdk_media_pipelines.types.voice_analytics_processor_configuration.VoiceAnalyticsProcessorConfiguration"
    ]
    """<p>The voice analytics configuration settings in a media insights pipeline configuration element.</p>"""
    lambda_function_sink_configuration: NotRequired[
        "capo_chime_sdk_media_pipelines.types.lambda_function_sink_configuration.LambdaFunctionSinkConfiguration"
    ]
    """<p>The configuration settings for the Amazon Web Services Lambda sink in a media insights pipeline configuration element.</p>"""
    sqs_queue_sink_configuration: NotRequired[
        "capo_chime_sdk_media_pipelines.types.sqs_queue_sink_configuration.SqsQueueSinkConfiguration"
    ]
    """<p>The configuration settings for an SQS queue sink in a media insights pipeline configuration element.</p>"""
    sns_topic_sink_configuration: NotRequired[
        "capo_chime_sdk_media_pipelines.types.sns_topic_sink_configuration.SnsTopicSinkConfiguration"
    ]
    """<p>The configuration settings for an SNS topic sink in a media insights pipeline configuration element.</p>"""
    voice_enhancement_sink_configuration: NotRequired[
        "capo_chime_sdk_media_pipelines.types.voice_enhancement_sink_configuration.VoiceEnhancementSinkConfiguration"
    ]
    """<p>The configuration settings for voice enhancement sink in a media insights pipeline configuration element.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MediaInsightsPipelineConfigurationElement) -> dict:
    out: dict = {}
    import capo_chime_sdk_media_pipelines.types.media_insights_pipeline_configuration_element_type

    out["Type"] = (
        capo_chime_sdk_media_pipelines.types.media_insights_pipeline_configuration_element_type.serialize_json(
            value["type"]
        )
    )
    if "amazon_transcribe_call_analytics_processor_configuration" in value:
        import capo_chime_sdk_media_pipelines.types.amazon_transcribe_call_analytics_processor_configuration

        out["AmazonTranscribeCallAnalyticsProcessorConfiguration"] = (
            capo_chime_sdk_media_pipelines.types.amazon_transcribe_call_analytics_processor_configuration.serialize_json(
                value["amazon_transcribe_call_analytics_processor_configuration"]
            )
        )
    if "amazon_transcribe_processor_configuration" in value:
        import capo_chime_sdk_media_pipelines.types.amazon_transcribe_processor_configuration

        out["AmazonTranscribeProcessorConfiguration"] = (
            capo_chime_sdk_media_pipelines.types.amazon_transcribe_processor_configuration.serialize_json(
                value["amazon_transcribe_processor_configuration"]
            )
        )
    if "kinesis_data_stream_sink_configuration" in value:
        import capo_chime_sdk_media_pipelines.types.kinesis_data_stream_sink_configuration

        out["KinesisDataStreamSinkConfiguration"] = (
            capo_chime_sdk_media_pipelines.types.kinesis_data_stream_sink_configuration.serialize_json(
                value["kinesis_data_stream_sink_configuration"]
            )
        )
    if "s3_recording_sink_configuration" in value:
        import capo_chime_sdk_media_pipelines.types.s3_recording_sink_configuration

        out["S3RecordingSinkConfiguration"] = (
            capo_chime_sdk_media_pipelines.types.s3_recording_sink_configuration.serialize_json(
                value["s3_recording_sink_configuration"]
            )
        )
    if "voice_analytics_processor_configuration" in value:
        import capo_chime_sdk_media_pipelines.types.voice_analytics_processor_configuration

        out["VoiceAnalyticsProcessorConfiguration"] = (
            capo_chime_sdk_media_pipelines.types.voice_analytics_processor_configuration.serialize_json(
                value["voice_analytics_processor_configuration"]
            )
        )
    if "lambda_function_sink_configuration" in value:
        import capo_chime_sdk_media_pipelines.types.lambda_function_sink_configuration

        out["LambdaFunctionSinkConfiguration"] = (
            capo_chime_sdk_media_pipelines.types.lambda_function_sink_configuration.serialize_json(
                value["lambda_function_sink_configuration"]
            )
        )
    if "sqs_queue_sink_configuration" in value:
        import capo_chime_sdk_media_pipelines.types.sqs_queue_sink_configuration

        out["SqsQueueSinkConfiguration"] = (
            capo_chime_sdk_media_pipelines.types.sqs_queue_sink_configuration.serialize_json(
                value["sqs_queue_sink_configuration"]
            )
        )
    if "sns_topic_sink_configuration" in value:
        import capo_chime_sdk_media_pipelines.types.sns_topic_sink_configuration

        out["SnsTopicSinkConfiguration"] = (
            capo_chime_sdk_media_pipelines.types.sns_topic_sink_configuration.serialize_json(
                value["sns_topic_sink_configuration"]
            )
        )
    if "voice_enhancement_sink_configuration" in value:
        import capo_chime_sdk_media_pipelines.types.voice_enhancement_sink_configuration

        out["VoiceEnhancementSinkConfiguration"] = (
            capo_chime_sdk_media_pipelines.types.voice_enhancement_sink_configuration.serialize_json(
                value["voice_enhancement_sink_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> MediaInsightsPipelineConfigurationElement:
    out: MediaInsightsPipelineConfigurationElement = {}  # type: ignore[typeddict-item]
    if data.get("Type") is not None:
        import capo_chime_sdk_media_pipelines.types.media_insights_pipeline_configuration_element_type

        out["type"] = (
            capo_chime_sdk_media_pipelines.types.media_insights_pipeline_configuration_element_type.deserialize_json(
                data["Type"]
            )
        )
    else:
        import typing

        out["type"] = typing.cast(
            "capo_chime_sdk_media_pipelines.types.media_insights_pipeline_configuration_element_type.MediaInsightsPipelineConfigurationElementType",
            "",
        )
    if data.get("AmazonTranscribeCallAnalyticsProcessorConfiguration") is not None:
        import capo_chime_sdk_media_pipelines.types.amazon_transcribe_call_analytics_processor_configuration

        out["amazon_transcribe_call_analytics_processor_configuration"] = (
            capo_chime_sdk_media_pipelines.types.amazon_transcribe_call_analytics_processor_configuration.deserialize_json(
                data["AmazonTranscribeCallAnalyticsProcessorConfiguration"]
            )
        )
    if data.get("AmazonTranscribeProcessorConfiguration") is not None:
        import capo_chime_sdk_media_pipelines.types.amazon_transcribe_processor_configuration

        out["amazon_transcribe_processor_configuration"] = (
            capo_chime_sdk_media_pipelines.types.amazon_transcribe_processor_configuration.deserialize_json(
                data["AmazonTranscribeProcessorConfiguration"]
            )
        )
    if data.get("KinesisDataStreamSinkConfiguration") is not None:
        import capo_chime_sdk_media_pipelines.types.kinesis_data_stream_sink_configuration

        out["kinesis_data_stream_sink_configuration"] = (
            capo_chime_sdk_media_pipelines.types.kinesis_data_stream_sink_configuration.deserialize_json(
                data["KinesisDataStreamSinkConfiguration"]
            )
        )
    if data.get("S3RecordingSinkConfiguration") is not None:
        import capo_chime_sdk_media_pipelines.types.s3_recording_sink_configuration

        out["s3_recording_sink_configuration"] = (
            capo_chime_sdk_media_pipelines.types.s3_recording_sink_configuration.deserialize_json(
                data["S3RecordingSinkConfiguration"]
            )
        )
    if data.get("VoiceAnalyticsProcessorConfiguration") is not None:
        import capo_chime_sdk_media_pipelines.types.voice_analytics_processor_configuration

        out["voice_analytics_processor_configuration"] = (
            capo_chime_sdk_media_pipelines.types.voice_analytics_processor_configuration.deserialize_json(
                data["VoiceAnalyticsProcessorConfiguration"]
            )
        )
    if data.get("LambdaFunctionSinkConfiguration") is not None:
        import capo_chime_sdk_media_pipelines.types.lambda_function_sink_configuration

        out["lambda_function_sink_configuration"] = (
            capo_chime_sdk_media_pipelines.types.lambda_function_sink_configuration.deserialize_json(
                data["LambdaFunctionSinkConfiguration"]
            )
        )
    if data.get("SqsQueueSinkConfiguration") is not None:
        import capo_chime_sdk_media_pipelines.types.sqs_queue_sink_configuration

        out["sqs_queue_sink_configuration"] = (
            capo_chime_sdk_media_pipelines.types.sqs_queue_sink_configuration.deserialize_json(
                data["SqsQueueSinkConfiguration"]
            )
        )
    if data.get("SnsTopicSinkConfiguration") is not None:
        import capo_chime_sdk_media_pipelines.types.sns_topic_sink_configuration

        out["sns_topic_sink_configuration"] = (
            capo_chime_sdk_media_pipelines.types.sns_topic_sink_configuration.deserialize_json(
                data["SnsTopicSinkConfiguration"]
            )
        )
    if data.get("VoiceEnhancementSinkConfiguration") is not None:
        import capo_chime_sdk_media_pipelines.types.voice_enhancement_sink_configuration

        out["voice_enhancement_sink_configuration"] = (
            capo_chime_sdk_media_pipelines.types.voice_enhancement_sink_configuration.deserialize_json(
                data["VoiceEnhancementSinkConfiguration"]
            )
        )
    return out


def redact_sensitive(
    value: MediaInsightsPipelineConfigurationElement,
) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "kinesis_data_stream_sink_configuration" in value:
        import capo_chime_sdk_media_pipelines.types.kinesis_data_stream_sink_configuration

        out["kinesis_data_stream_sink_configuration"] = (
            capo_chime_sdk_media_pipelines.types.kinesis_data_stream_sink_configuration.redact_sensitive(
                value["kinesis_data_stream_sink_configuration"]
            )
        )
    if "s3_recording_sink_configuration" in value:
        import capo_chime_sdk_media_pipelines.types.s3_recording_sink_configuration

        out["s3_recording_sink_configuration"] = (
            capo_chime_sdk_media_pipelines.types.s3_recording_sink_configuration.redact_sensitive(
                value["s3_recording_sink_configuration"]
            )
        )
    if "lambda_function_sink_configuration" in value:
        import capo_chime_sdk_media_pipelines.types.lambda_function_sink_configuration

        out["lambda_function_sink_configuration"] = (
            capo_chime_sdk_media_pipelines.types.lambda_function_sink_configuration.redact_sensitive(
                value["lambda_function_sink_configuration"]
            )
        )
    if "sqs_queue_sink_configuration" in value:
        import capo_chime_sdk_media_pipelines.types.sqs_queue_sink_configuration

        out["sqs_queue_sink_configuration"] = (
            capo_chime_sdk_media_pipelines.types.sqs_queue_sink_configuration.redact_sensitive(
                value["sqs_queue_sink_configuration"]
            )
        )
    if "sns_topic_sink_configuration" in value:
        import capo_chime_sdk_media_pipelines.types.sns_topic_sink_configuration

        out["sns_topic_sink_configuration"] = (
            capo_chime_sdk_media_pipelines.types.sns_topic_sink_configuration.redact_sensitive(
                value["sns_topic_sink_configuration"]
            )
        )
    return out
