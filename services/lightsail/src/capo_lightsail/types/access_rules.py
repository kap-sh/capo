"""Generated from Smithy shape ``com.amazonaws.lightsail#AccessRules``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lightsail.types.access_type
    import capo_lightsail.types.boolean


class AccessRules(TypedDict, closed=True):
    get_object: NotRequired["capo_lightsail.types.access_type.AccessType"]
    """<p>Specifies the anonymous access to all objects in a bucket.</p> <p>The following options can be specified:</p> <ul> <li> <p> <code>public</code> - Sets all objects in the bucket to public (read-only), making them readable by anyone in the world.</p> <p>If the <code>getObject</code> value is set to <code>public</code>, then all objects in the bucket default to public regardless of the <code>allowPublicOverrides</code> value.</p> </li> <li> <p> <code>private</code> - Sets all objects in the bucket to private, making them readable only by you or anyone you give access to.</p> <p>If the <code>getObject</code> value is set to <code>private</code>, and the <code>allowPublicOverrides</code> value is set to <code>true</code>, then all objects in the bucket default to private unless they are configured with a <code>public-read</code> ACL. Individual objects with a <code>public-read</code> ACL are readable by anyone in the world.</p> </li> </ul>"""
    allow_public_overrides: NotRequired["capo_lightsail.types.boolean.boolean"]
    """<p>A Boolean value that indicates whether the access control list (ACL) permissions that are applied to individual objects override the <code>getObject</code> option that is currently specified.</p> <p>When this is true, you can use the <a href="https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutObjectAcl.html">PutObjectAcl</a> Amazon S3 API action to set individual objects to public (read-only) using the <code>public-read</code> ACL, or to private using the <code>private</code> ACL.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AccessRules) -> dict:
    out: dict = {}
    if "get_object" in value:
        import capo_lightsail.types.access_type

        out["getObject"] = capo_lightsail.types.access_type.serialize_aws_json_1_1(
            value["get_object"]
        )
    if "allow_public_overrides" in value:
        out["allowPublicOverrides"] = value["allow_public_overrides"]
    return out


def deserialize_aws_json_1_1(data: dict) -> AccessRules:
    out: AccessRules = {}  # type: ignore[typeddict-item]
    if data.get("getObject") is not None:
        import capo_lightsail.types.access_type

        out["get_object"] = capo_lightsail.types.access_type.deserialize_aws_json_1_1(
            data["getObject"]
        )
    if data.get("allowPublicOverrides") is not None:
        out["allow_public_overrides"] = data["allowPublicOverrides"]
    return out
