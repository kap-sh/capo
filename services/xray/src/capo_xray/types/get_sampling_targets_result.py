"""Generated from Smithy shape ``com.amazonaws.xray#GetSamplingTargetsResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_xray.types.sampling_target_document_list
    import capo_xray.types.timestamp
    import capo_xray.types.unprocessed_statistics_list


class GetSamplingTargetsResult(TypedDict, closed=True):
    sampling_target_documents: NotRequired[
        "capo_xray.types.sampling_target_document_list.SamplingTargetDocumentList"
    ]
    """<p>Updated rules that the service should use to sample requests.</p>"""
    last_rule_modification: NotRequired["capo_xray.types.timestamp.Timestamp"]
    """<p>The last time a user changed the sampling rule configuration. If the sampling rule configuration changed since the service last retrieved it, the service should call <a href="https://docs.aws.amazon.com/xray/latest/api/API_GetSamplingRules.html">GetSamplingRules</a> to get the latest version.</p>"""
    unprocessed_statistics: NotRequired[
        "capo_xray.types.unprocessed_statistics_list.UnprocessedStatisticsList"
    ]
    """<p>Information about <a href="https://docs.aws.amazon.com/xray/latest/api/API_SamplingStatisticsDocument.html">SamplingStatisticsDocument</a> that X-Ray could not process.</p>"""
    unprocessed_boost_statistics: NotRequired[
        "capo_xray.types.unprocessed_statistics_list.UnprocessedStatisticsList"
    ]
    """<p>Information about <a href="https://docs.aws.amazon.com/xray/latest/api/API_SamplingBoostStatisticsDocument.html">SamplingBoostStatisticsDocument</a> that X-Ray could not process.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetSamplingTargetsResult) -> dict:
    out: dict = {}
    if "sampling_target_documents" in value:
        import capo_xray.types.sampling_target_document_list

        out["SamplingTargetDocuments"] = (
            capo_xray.types.sampling_target_document_list.serialize_json(
                value["sampling_target_documents"]
            )
        )
    if "last_rule_modification" in value:
        import capo_xray.types.timestamp

        out["LastRuleModification"] = capo_xray.types.timestamp.serialize_json(
            value["last_rule_modification"]
        )
    if "unprocessed_statistics" in value:
        import capo_xray.types.unprocessed_statistics_list

        out["UnprocessedStatistics"] = (
            capo_xray.types.unprocessed_statistics_list.serialize_json(
                value["unprocessed_statistics"]
            )
        )
    if "unprocessed_boost_statistics" in value:
        import capo_xray.types.unprocessed_statistics_list

        out["UnprocessedBoostStatistics"] = (
            capo_xray.types.unprocessed_statistics_list.serialize_json(
                value["unprocessed_boost_statistics"]
            )
        )
    return out


def deserialize_json(data: dict) -> GetSamplingTargetsResult:
    out: GetSamplingTargetsResult = {}  # type: ignore[typeddict-item]
    if data.get("SamplingTargetDocuments") is not None:
        import capo_xray.types.sampling_target_document_list

        out["sampling_target_documents"] = (
            capo_xray.types.sampling_target_document_list.deserialize_json(
                data["SamplingTargetDocuments"]
            )
        )
    if data.get("LastRuleModification") is not None:
        import capo_xray.types.timestamp

        out["last_rule_modification"] = capo_xray.types.timestamp.deserialize_json(
            data["LastRuleModification"]
        )
    if data.get("UnprocessedStatistics") is not None:
        import capo_xray.types.unprocessed_statistics_list

        out["unprocessed_statistics"] = (
            capo_xray.types.unprocessed_statistics_list.deserialize_json(
                data["UnprocessedStatistics"]
            )
        )
    if data.get("UnprocessedBoostStatistics") is not None:
        import capo_xray.types.unprocessed_statistics_list

        out["unprocessed_boost_statistics"] = (
            capo_xray.types.unprocessed_statistics_list.deserialize_json(
                data["UnprocessedBoostStatistics"]
            )
        )
    return out
