"""Generated from Smithy shape ``com.amazonaws.omics#CreateRunCacheRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_omics.errors import DeserializationError

if TYPE_CHECKING:
    import capo_omics.types.aws_account_id
    import capo_omics.types.cache_behavior
    import capo_omics.types.run_cache_request_id
    import capo_omics.types.s3_uri_for_bucket_or_object
    import capo_omics.types.tag_map
    import capo_omics.types.user_custom_description
    import capo_omics.types.user_custom_name


class CreateRunCacheRequest(TypedDict, closed=True):
    cache_behavior: NotRequired["capo_omics.types.cache_behavior.CacheBehavior"]
    """<p>Default cache behavior for runs that use this cache. Supported values are:</p> <p> <code>CACHE_ON_FAILURE</code>: Caches task outputs from completed tasks for runs that fail. This setting is useful if you're debugging a workflow that fails after several tasks completed successfully. The subsequent run uses the cache outputs for previously-completed tasks if the task definition, inputs, and container in ECR are identical to the prior run.</p> <p> <code>CACHE_ALWAYS</code>: Caches task outputs from completed tasks for all runs. This setting is useful in development mode, but do not use it in a production setting.</p> <p>If you don't specify a value, the default behavior is CACHE_ON_FAILURE. When you start a run that uses this cache, you can override the default cache behavior.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/omics/latest/dev/how-run-cache.html#run-cache-behavior">Run cache behavior</a> in the <i>Amazon Web Services HealthOmics User Guide</i>.</p>"""
    cache_s3_location: (
        "capo_omics.types.s3_uri_for_bucket_or_object.S3UriForBucketOrObject"
    )
    """<p>Specify the S3 location for storing the cached task outputs. This data must be immediately accessible (not in an archived state).</p>"""
    description: NotRequired[
        "capo_omics.types.user_custom_description.UserCustomDescription"
    ]
    """<p>Enter a description of the run cache.</p>"""
    name: NotRequired["capo_omics.types.user_custom_name.UserCustomName"]
    """<p>Enter a user-friendly name for the run cache.</p>"""
    request_id: "capo_omics.types.run_cache_request_id.RunCacheRequestId"
    """<p>A unique request token, to ensure idempotency. If you don't specify a token, Amazon Web Services HealthOmics automatically generates a universally unique identifier (UUID) for the request.</p>"""
    tags: NotRequired["capo_omics.types.tag_map.TagMap"]
    """<p>Specify one or more tags to associate with this run cache.</p>"""
    cache_bucket_owner_id: NotRequired["capo_omics.types.aws_account_id.AwsAccountId"]
    """<p>The Amazon Web Services account ID of the expected owner of the S3 bucket for the run cache. If not provided, your account ID is set as the owner of the bucket.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateRunCacheRequest) -> dict:
    out: dict = {}
    if "cache_behavior" in value:
        out["cacheBehavior"] = value["cache_behavior"]
    out["cacheS3Location"] = value["cache_s3_location"]
    if "description" in value:
        out["description"] = value["description"]
    if "name" in value:
        out["name"] = value["name"]
    out["requestId"] = value["request_id"]
    if "tags" in value:
        import capo_omics.types.tag_map

        out["tags"] = capo_omics.types.tag_map.serialize_json(value["tags"])
    if "cache_bucket_owner_id" in value:
        out["cacheBucketOwnerId"] = value["cache_bucket_owner_id"]
    return out


def deserialize_json(data: dict) -> CreateRunCacheRequest:
    out: CreateRunCacheRequest = {}  # type: ignore[typeddict-item]
    if data.get("cacheBehavior") is not None:
        out["cache_behavior"] = data["cacheBehavior"]
    if data.get("cacheS3Location") is not None:
        out["cache_s3_location"] = data["cacheS3Location"]
    else:
        raise DeserializationError("CreateRunCacheRequest.cache_s3_location required")
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("name") is not None:
        out["name"] = data["name"]
    if data.get("requestId") is not None:
        out["request_id"] = data["requestId"]
    else:
        raise DeserializationError("CreateRunCacheRequest.request_id required")
    if data.get("tags") is not None:
        import capo_omics.types.tag_map

        out["tags"] = capo_omics.types.tag_map.deserialize_json(data["tags"])
    if data.get("cacheBucketOwnerId") is not None:
        out["cache_bucket_owner_id"] = data["cacheBucketOwnerId"]
    return out
