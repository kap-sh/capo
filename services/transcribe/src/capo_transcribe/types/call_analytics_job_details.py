"""Generated from Smithy shape ``com.amazonaws.transcribe#CallAnalyticsJobDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_transcribe.types.call_analytics_skipped_feature_list


class CallAnalyticsJobDetails(TypedDict, closed=True):
    skipped: NotRequired[
        "capo_transcribe.types.call_analytics_skipped_feature_list.CallAnalyticsSkippedFeatureList"
    ]
    """<p>Contains information about any skipped analytics features during the analysis of a call analytics job.</p> <p>This array lists all the analytics features that were skipped, along with their corresponding reason code and message.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CallAnalyticsJobDetails) -> dict:
    out: dict = {}
    if "skipped" in value:
        import capo_transcribe.types.call_analytics_skipped_feature_list

        out["Skipped"] = (
            capo_transcribe.types.call_analytics_skipped_feature_list.serialize_aws_json_1_1(
                value["skipped"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CallAnalyticsJobDetails:
    out: CallAnalyticsJobDetails = {}  # type: ignore[typeddict-item]
    if data.get("Skipped") is not None:
        import capo_transcribe.types.call_analytics_skipped_feature_list

        out["skipped"] = (
            capo_transcribe.types.call_analytics_skipped_feature_list.deserialize_aws_json_1_1(
                data["Skipped"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: CallAnalyticsJobDetails) -> dict:
    out: dict = {}
    if "skipped" in value:
        import capo_transcribe.types.call_analytics_skipped_feature_list

        out["Skipped"] = (
            capo_transcribe.types.call_analytics_skipped_feature_list.serialize_cbor(
                value["skipped"]
            )
        )
    return out


def deserialize_cbor(data: dict) -> CallAnalyticsJobDetails:
    out: CallAnalyticsJobDetails = {}  # type: ignore[typeddict-item]
    if data.get("Skipped") is not None:
        import capo_transcribe.types.call_analytics_skipped_feature_list

        out["skipped"] = (
            capo_transcribe.types.call_analytics_skipped_feature_list.deserialize_cbor(
                data["Skipped"]
            )
        )
    return out
