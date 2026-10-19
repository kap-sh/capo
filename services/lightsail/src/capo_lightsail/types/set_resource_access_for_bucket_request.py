"""Generated from Smithy shape ``com.amazonaws.lightsail#SetResourceAccessForBucketRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_lightsail.types.bucket_name
    import capo_lightsail.types.resource_bucket_access
    import capo_lightsail.types.resource_name


class SetResourceAccessForBucketRequest(TypedDict, closed=True):
    resource_name: "capo_lightsail.types.resource_name.ResourceName"
    """<p>The name of the Lightsail instance for which to set bucket access. The instance must be in a running or stopped state.</p>"""
    bucket_name: "capo_lightsail.types.bucket_name.BucketName"
    """<p>The name of the bucket for which to set access to another Lightsail resource.</p>"""
    access: "capo_lightsail.types.resource_bucket_access.ResourceBucketAccess"
    """<p>The access setting.</p> <p>The following access settings are available:</p> <ul> <li> <p> <code>allow</code> - Allows access to the bucket and its objects.</p> </li> <li> <p> <code>deny</code> - Denies access to the bucket and its objects. Use this setting to remove access for a resource previously set to <code>allow</code>.</p> </li> </ul>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SetResourceAccessForBucketRequest) -> dict:
    out: dict = {}
    out["resourceName"] = value["resource_name"]
    out["bucketName"] = value["bucket_name"]
    import capo_lightsail.types.resource_bucket_access

    out["access"] = capo_lightsail.types.resource_bucket_access.serialize_aws_json_1_1(
        value["access"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> SetResourceAccessForBucketRequest:
    out: SetResourceAccessForBucketRequest = {}  # type: ignore[typeddict-item]
    if data.get("resourceName") is not None:
        out["resource_name"] = data["resourceName"]
    else:
        out["resource_name"] = ""
    if data.get("bucketName") is not None:
        out["bucket_name"] = data["bucketName"]
    else:
        out["bucket_name"] = ""
    if data.get("access") is not None:
        import capo_lightsail.types.resource_bucket_access

        out["access"] = (
            capo_lightsail.types.resource_bucket_access.deserialize_aws_json_1_1(
                data["access"]
            )
        )
    else:
        import typing

        out["access"] = typing.cast(
            "capo_lightsail.types.resource_bucket_access.ResourceBucketAccess", ""
        )
    return out
