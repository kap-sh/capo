"""Generated from Smithy shape ``com.amazonaws.transcribe#CallAnalyticsSkippedFeatureList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_transcribe.types.call_analytics_skipped_feature

CallAnalyticsSkippedFeatureList: TypeAlias = list[
    "capo_transcribe.types.call_analytics_skipped_feature.CallAnalyticsSkippedFeature"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CallAnalyticsSkippedFeatureList) -> list:
    import capo_transcribe.types.call_analytics_skipped_feature

    out: list = []
    for item in value:
        out.append(
            capo_transcribe.types.call_analytics_skipped_feature.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> CallAnalyticsSkippedFeatureList:
    import capo_transcribe.types.call_analytics_skipped_feature

    out: CallAnalyticsSkippedFeatureList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_transcribe.types.call_analytics_skipped_feature.deserialize_aws_json_1_1(
                item
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: CallAnalyticsSkippedFeatureList) -> list:
    import capo_transcribe.types.call_analytics_skipped_feature

    out: list = []
    for item in value:
        out.append(
            capo_transcribe.types.call_analytics_skipped_feature.serialize_cbor(item)
        )
    return out


def deserialize_cbor(data: list) -> CallAnalyticsSkippedFeatureList:
    import capo_transcribe.types.call_analytics_skipped_feature

    out: CallAnalyticsSkippedFeatureList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_transcribe.types.call_analytics_skipped_feature.deserialize_cbor(item)
        )
    return out
