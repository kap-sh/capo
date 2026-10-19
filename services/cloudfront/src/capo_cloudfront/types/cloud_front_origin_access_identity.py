"""Generated from Smithy shape ``com.amazonaws.cloudfront#CloudFrontOriginAccessIdentity``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudfront._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_cloudfront.types.cloud_front_origin_access_identity_config
    import capo_cloudfront.types.string


class CloudFrontOriginAccessIdentity(TypedDict, closed=True):
    id: "capo_cloudfront.types.string.string"
    """<p>The ID for the origin access identity, for example, <code>E74FTE3AJFJ256A</code>. </p>"""
    s3_canonical_user_id: "capo_cloudfront.types.string.string"
    """<p>The Amazon S3 canonical user ID for the origin access identity, used when giving the origin access identity read permission to an object in Amazon S3.</p>"""
    cloud_front_origin_access_identity_config: NotRequired[
        "capo_cloudfront.types.cloud_front_origin_access_identity_config.CloudFrontOriginAccessIdentityConfig"
    ]
    """<p>The current configuration information for the identity.</p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: CloudFrontOriginAccessIdentity, parent: Element, tag: str
) -> None:
    el = SubElement(parent, tag)
    SubElement(el, "Id").text = str(value["id"])
    SubElement(el, "S3CanonicalUserId").text = str(value["s3_canonical_user_id"])
    if "cloud_front_origin_access_identity_config" in value:
        import capo_cloudfront.types.cloud_front_origin_access_identity_config

        capo_cloudfront.types.cloud_front_origin_access_identity_config.serialize_xml(
            value["cloud_front_origin_access_identity_config"],
            el,
            "CloudFrontOriginAccessIdentityConfig",
        )


def deserialize_xml(el: Element) -> CloudFrontOriginAccessIdentity:
    out: CloudFrontOriginAccessIdentity = {}  # type: ignore[typeddict-item]
    child_id = el.find("Id")
    if child_id is not None:
        out["id"] = str(child_id.text or "")
    else:
        out["id"] = ""
    child_s3_canonical_user_id = el.find("S3CanonicalUserId")
    if child_s3_canonical_user_id is not None:
        out["s3_canonical_user_id"] = str(child_s3_canonical_user_id.text or "")
    else:
        out["s3_canonical_user_id"] = ""
    child_cloud_front_origin_access_identity_config = el.find(
        "CloudFrontOriginAccessIdentityConfig"
    )
    if child_cloud_front_origin_access_identity_config is not None:
        import capo_cloudfront.types.cloud_front_origin_access_identity_config

        out["cloud_front_origin_access_identity_config"] = (
            capo_cloudfront.types.cloud_front_origin_access_identity_config.deserialize_xml(
                child_cloud_front_origin_access_identity_config
            )
        )
    return out
