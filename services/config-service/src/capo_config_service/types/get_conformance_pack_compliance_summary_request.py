"""Generated from Smithy shape ``com.amazonaws.configservice#GetConformancePackComplianceSummaryRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_config_service.errors import DeserializationError

if TYPE_CHECKING:
    import capo_config_service.types.conformance_pack_names_to_summarize_list
    import capo_config_service.types.next_token
    import capo_config_service.types.page_size_limit


class GetConformancePackComplianceSummaryRequest(TypedDict, closed=True):
    conformance_pack_names: "capo_config_service.types.conformance_pack_names_to_summarize_list.ConformancePackNamesToSummarizeList"
    """<p>Names of conformance packs.</p>"""
    limit: NotRequired["capo_config_service.types.page_size_limit.PageSizeLimit"]
    """<p>The maximum number of conformance packs returned on each page.</p>"""
    next_token: NotRequired["capo_config_service.types.next_token.NextToken"]
    """<p>The nextToken string returned on a previous page that you use to get the next page of results in a paginated response.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetConformancePackComplianceSummaryRequest) -> dict:
    out: dict = {}
    import capo_config_service.types.conformance_pack_names_to_summarize_list

    out["ConformancePackNames"] = (
        capo_config_service.types.conformance_pack_names_to_summarize_list.serialize_aws_json_1_1(
            value["conformance_pack_names"]
        )
    )
    if "limit" in value:
        out["Limit"] = value["limit"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetConformancePackComplianceSummaryRequest:
    out: GetConformancePackComplianceSummaryRequest = {}  # type: ignore[typeddict-item]
    if data.get("ConformancePackNames") is not None:
        import capo_config_service.types.conformance_pack_names_to_summarize_list

        out["conformance_pack_names"] = (
            capo_config_service.types.conformance_pack_names_to_summarize_list.deserialize_aws_json_1_1(
                data["ConformancePackNames"]
            )
        )
    else:
        raise DeserializationError(
            "GetConformancePackComplianceSummaryRequest.conformance_pack_names required"
        )
    if data.get("Limit") is not None:
        out["limit"] = data["Limit"]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
