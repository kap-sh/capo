"""Generated from Smithy shape ``com.amazonaws.lightsail#GetBucketsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lightsail.types.boolean
    import capo_lightsail.types.bucket_name
    import capo_lightsail.types.string


class GetBucketsRequest(TypedDict, closed=True):
    bucket_name: NotRequired["capo_lightsail.types.bucket_name.BucketName"]
    """<p>The name of the bucket for which to return information.</p> <p>When omitted, the response includes all of your buckets in the Amazon Web Services Region where the request is made.</p>"""
    page_token: NotRequired["capo_lightsail.types.string.string"]
    """<p>The token to advance to the next page of results from your request.</p> <p>To get a page token, perform an initial <code>GetBuckets</code> request. If your results are paginated, the response will return a next page token that you can specify as the page token in a subsequent request.</p>"""
    include_connected_resources: NotRequired["capo_lightsail.types.boolean.boolean"]
    """<p>A Boolean value that indicates whether to include Lightsail instances that were given access to the bucket using the <a href="https://docs.aws.amazon.com/lightsail/2016-11-28/api-reference/API_SetResourceAccessForBucket.html">SetResourceAccessForBucket</a> action.</p>"""
    include_cors: NotRequired["capo_lightsail.types.boolean.boolean"]
    """<p>A Boolean value that indicates whether to include Lightsail bucket CORS configuration in the response. For more information, see <a href="https://docs.aws.amazon.com/lightsail/latest/userguide/configure-cors.html">Configuring cross-origin resource sharing (CORS)</a>.</p> <note> <p>This parameter is only supported when getting a single bucket with <code>bucketName</code> specified. The default value for this parameter is <code>False</code>.</p> </note>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetBucketsRequest) -> dict:
    out: dict = {}
    if "bucket_name" in value:
        out["bucketName"] = value["bucket_name"]
    if "page_token" in value:
        out["pageToken"] = value["page_token"]
    if "include_connected_resources" in value:
        out["includeConnectedResources"] = value["include_connected_resources"]
    if "include_cors" in value:
        out["includeCors"] = value["include_cors"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetBucketsRequest:
    out: GetBucketsRequest = {}  # type: ignore[typeddict-item]
    if data.get("bucketName") is not None:
        out["bucket_name"] = data["bucketName"]
    if data.get("pageToken") is not None:
        out["page_token"] = data["pageToken"]
    if data.get("includeConnectedResources") is not None:
        out["include_connected_resources"] = data["includeConnectedResources"]
    if data.get("includeCors") is not None:
        out["include_cors"] = data["includeCors"]
    return out
