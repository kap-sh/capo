"""Generated from Smithy shape ``com.amazonaws.configservice#DescribeConformancePackStatusRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_config_service.types.conformance_pack_names_list
    import capo_config_service.types.next_token
    import capo_config_service.types.page_size_limit


class DescribeConformancePackStatusRequest(TypedDict, closed=True):
    conformance_pack_names: NotRequired[
        "capo_config_service.types.conformance_pack_names_list.ConformancePackNamesList"
    ]
    """<p>Comma-separated list of conformance pack names.</p>"""
    limit: NotRequired["capo_config_service.types.page_size_limit.PageSizeLimit"]
    """<p>The maximum number of conformance packs status returned on each page.</p>"""
    next_token: NotRequired["capo_config_service.types.next_token.NextToken"]
    """<p>The <code>nextToken</code> string returned in a previous request that you use to request the next page of results in a paginated response.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeConformancePackStatusRequest) -> dict:
    out: dict = {}
    if "conformance_pack_names" in value:
        import capo_config_service.types.conformance_pack_names_list

        out["ConformancePackNames"] = (
            capo_config_service.types.conformance_pack_names_list.serialize_aws_json_1_1(
                value["conformance_pack_names"]
            )
        )
    if "limit" in value:
        out["Limit"] = value["limit"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeConformancePackStatusRequest:
    out: DescribeConformancePackStatusRequest = {}  # type: ignore[typeddict-item]
    if data.get("ConformancePackNames") is not None:
        import capo_config_service.types.conformance_pack_names_list

        out["conformance_pack_names"] = (
            capo_config_service.types.conformance_pack_names_list.deserialize_aws_json_1_1(
                data["ConformancePackNames"]
            )
        )
    if data.get("Limit") is not None:
        out["limit"] = data["Limit"]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
