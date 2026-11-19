"""Generated from Smithy shape ``com.amazonaws.transcribe#CallAnalyticsSkippedFeature``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_transcribe.types.call_analytics_feature
    import capo_transcribe.types.call_analytics_skipped_reason_code
    import capo_transcribe.types.string


class CallAnalyticsSkippedFeature(TypedDict, closed=True):
    feature: NotRequired[
        "capo_transcribe.types.call_analytics_feature.CallAnalyticsFeature"
    ]
    """<p>Indicates the type of analytics feature that was skipped during the analysis of a call analytics job.</p>"""
    reason_code: NotRequired[
        "capo_transcribe.types.call_analytics_skipped_reason_code.CallAnalyticsSkippedReasonCode"
    ]
    """<p>Provides a code indicating the reason why a specific analytics feature was skipped during the analysis of a call analytics job.</p>"""
    message: NotRequired["capo_transcribe.types.string.String"]
    """<p>Contains additional information or a message explaining why a specific analytics feature was skipped during the analysis of a call analytics job.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CallAnalyticsSkippedFeature) -> dict:
    out: dict = {}
    if "feature" in value:
        import capo_transcribe.types.call_analytics_feature

        out["Feature"] = (
            capo_transcribe.types.call_analytics_feature.serialize_aws_json_1_1(
                value["feature"]
            )
        )
    if "reason_code" in value:
        import capo_transcribe.types.call_analytics_skipped_reason_code

        out["ReasonCode"] = (
            capo_transcribe.types.call_analytics_skipped_reason_code.serialize_aws_json_1_1(
                value["reason_code"]
            )
        )
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CallAnalyticsSkippedFeature:
    out: CallAnalyticsSkippedFeature = {}  # type: ignore[typeddict-item]
    if data.get("Feature") is not None:
        import capo_transcribe.types.call_analytics_feature

        out["feature"] = (
            capo_transcribe.types.call_analytics_feature.deserialize_aws_json_1_1(
                data["Feature"]
            )
        )
    if data.get("ReasonCode") is not None:
        import capo_transcribe.types.call_analytics_skipped_reason_code

        out["reason_code"] = (
            capo_transcribe.types.call_analytics_skipped_reason_code.deserialize_aws_json_1_1(
                data["ReasonCode"]
            )
        )
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: CallAnalyticsSkippedFeature) -> dict:
    out: dict = {}
    if "feature" in value:
        import capo_transcribe.types.call_analytics_feature

        out["Feature"] = capo_transcribe.types.call_analytics_feature.serialize_cbor(
            value["feature"]
        )
    if "reason_code" in value:
        import capo_transcribe.types.call_analytics_skipped_reason_code

        out["ReasonCode"] = (
            capo_transcribe.types.call_analytics_skipped_reason_code.serialize_cbor(
                value["reason_code"]
            )
        )
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_cbor(data: dict) -> CallAnalyticsSkippedFeature:
    out: CallAnalyticsSkippedFeature = {}  # type: ignore[typeddict-item]
    if data.get("Feature") is not None:
        import capo_transcribe.types.call_analytics_feature

        out["feature"] = capo_transcribe.types.call_analytics_feature.deserialize_cbor(
            data["Feature"]
        )
    if data.get("ReasonCode") is not None:
        import capo_transcribe.types.call_analytics_skipped_reason_code

        out["reason_code"] = (
            capo_transcribe.types.call_analytics_skipped_reason_code.deserialize_cbor(
                data["ReasonCode"]
            )
        )
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    return out
