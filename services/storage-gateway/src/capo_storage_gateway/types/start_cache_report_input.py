"""Generated from Smithy shape ``com.amazonaws.storagegateway#StartCacheReportInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_storage_gateway.types.cache_report_filter_list
    import capo_storage_gateway.types.client_token
    import capo_storage_gateway.types.dns_host_name
    import capo_storage_gateway.types.file_share_arn
    import capo_storage_gateway.types.location_arn
    import capo_storage_gateway.types.region_id
    import capo_storage_gateway.types.role
    import capo_storage_gateway.types.tags


class StartCacheReportInput(TypedDict, closed=True):
    file_share_arn: "capo_storage_gateway.types.file_share_arn.FileShareARN"
    role: "capo_storage_gateway.types.role.Role"
    """<p>The ARN of the IAM role used when saving the cache report to Amazon S3.</p>"""
    location_arn: "capo_storage_gateway.types.location_arn.LocationARN"
    """<p>The ARN of the Amazon S3 bucket where you want to save the cache report.</p> <note> <p>We do not recommend saving the cache report to the same Amazon S3 bucket for which you are generating the report.</p> <p>This field does not accept access point ARNs.</p> </note>"""
    bucket_region: "capo_storage_gateway.types.region_id.RegionId"
    """<p>The Amazon Web Services Region of the Amazon S3 bucket where you want to save the cache report.</p>"""
    vpc_endpoint_dns_name: NotRequired[
        "capo_storage_gateway.types.dns_host_name.DNSHostName"
    ]
    """<p>The DNS name of the VPC endpoint associated with the Amazon S3 where you want to save the cache report. Optional.</p>"""
    inclusion_filters: NotRequired[
        "capo_storage_gateway.types.cache_report_filter_list.CacheReportFilterList"
    ]
    """<p>The list of filters and parameters that determine which files are included in the report. You must specify at least one value for <code>InclusionFilters</code> or <code>ExclusionFilters</code> in a <code>StartCacheReport</code> request.</p>"""
    exclusion_filters: NotRequired[
        "capo_storage_gateway.types.cache_report_filter_list.CacheReportFilterList"
    ]
    """<p>The list of filters and parameters that determine which files are excluded from the report. You must specify at least one value for <code>InclusionFilters</code> or <code>ExclusionFilters</code> in a <code>StartCacheReport</code> request.</p>"""
    client_token: "capo_storage_gateway.types.client_token.ClientToken"
    """<p>A unique identifier that you use to ensure idempotent report generation if you need to retry an unsuccessful <code>StartCacheReport</code> request. If you retry a request, use the same <code>ClientToken</code> you specified in the initial request.</p>"""
    tags: NotRequired["capo_storage_gateway.types.tags.Tags"]
    """<p>A list of up to 50 key/value tags that you can assign to the cache report. Using tags can help you categorize your reports and more easily locate them in search results.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StartCacheReportInput) -> dict:
    out: dict = {}
    out["FileShareARN"] = value["file_share_arn"]
    out["Role"] = value["role"]
    out["LocationARN"] = value["location_arn"]
    out["BucketRegion"] = value["bucket_region"]
    if "vpc_endpoint_dns_name" in value:
        out["VPCEndpointDNSName"] = value["vpc_endpoint_dns_name"]
    if "inclusion_filters" in value:
        import capo_storage_gateway.types.cache_report_filter_list

        out["InclusionFilters"] = (
            capo_storage_gateway.types.cache_report_filter_list.serialize_aws_json_1_1(
                value["inclusion_filters"]
            )
        )
    if "exclusion_filters" in value:
        import capo_storage_gateway.types.cache_report_filter_list

        out["ExclusionFilters"] = (
            capo_storage_gateway.types.cache_report_filter_list.serialize_aws_json_1_1(
                value["exclusion_filters"]
            )
        )
    out["ClientToken"] = value["client_token"]
    if "tags" in value:
        import capo_storage_gateway.types.tags

        out["Tags"] = capo_storage_gateway.types.tags.serialize_aws_json_1_1(
            value["tags"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> StartCacheReportInput:
    out: StartCacheReportInput = {}  # type: ignore[typeddict-item]
    if data.get("FileShareARN") is not None:
        out["file_share_arn"] = data["FileShareARN"]
    else:
        out["file_share_arn"] = ""
    if data.get("Role") is not None:
        out["role"] = data["Role"]
    else:
        out["role"] = ""
    if data.get("LocationARN") is not None:
        out["location_arn"] = data["LocationARN"]
    else:
        out["location_arn"] = ""
    if data.get("BucketRegion") is not None:
        out["bucket_region"] = data["BucketRegion"]
    else:
        out["bucket_region"] = ""
    if data.get("VPCEndpointDNSName") is not None:
        out["vpc_endpoint_dns_name"] = data["VPCEndpointDNSName"]
    if data.get("InclusionFilters") is not None:
        import capo_storage_gateway.types.cache_report_filter_list

        out["inclusion_filters"] = (
            capo_storage_gateway.types.cache_report_filter_list.deserialize_aws_json_1_1(
                data["InclusionFilters"]
            )
        )
    if data.get("ExclusionFilters") is not None:
        import capo_storage_gateway.types.cache_report_filter_list

        out["exclusion_filters"] = (
            capo_storage_gateway.types.cache_report_filter_list.deserialize_aws_json_1_1(
                data["ExclusionFilters"]
            )
        )
    if data.get("ClientToken") is not None:
        out["client_token"] = data["ClientToken"]
    else:
        out["client_token"] = ""
    if data.get("Tags") is not None:
        import capo_storage_gateway.types.tags

        out["tags"] = capo_storage_gateway.types.tags.deserialize_aws_json_1_1(
            data["Tags"]
        )
    return out
