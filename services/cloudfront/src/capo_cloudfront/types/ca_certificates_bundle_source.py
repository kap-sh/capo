"""Generated from Smithy shape ``com.amazonaws.cloudfront#CaCertificatesBundleSource``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_cloudfront._protocol.xml import Element, SubElement
from capo_cloudfront.errors import DeserializationError, SerializationError
from capo_cloudfront.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_cloudfront.types.ca_certificates_bundle_s3_location


class _CaCertificatesBundleSource_CaCertificatesBundleS3Location(
    TypedDict, closed=True
):
    CaCertificatesBundleS3Location: "capo_cloudfront.types.ca_certificates_bundle_s3_location.CaCertificatesBundleS3Location"


CaCertificatesBundleSource: TypeAlias = (
    _CaCertificatesBundleSource_CaCertificatesBundleS3Location | UnknownUnionMember
)


# --- restXml ser/de ---
def serialize_xml(value: CaCertificatesBundleSource, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    if "$unknown" in value:
        raise SerializationError(
            f"CaCertificatesBundleSource: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "CaCertificatesBundleS3Location" in value:
        import capo_cloudfront.types.ca_certificates_bundle_s3_location

        capo_cloudfront.types.ca_certificates_bundle_s3_location.serialize_xml(
            value["CaCertificatesBundleS3Location"],
            el,
            "CaCertificatesBundleS3Location",
        )
    else:
        raise SerializationError("CaCertificatesBundleSource: no variant present")


def deserialize_xml(el: Element) -> CaCertificatesBundleSource:
    for child in el:
        if child.tag == "CaCertificatesBundleS3Location":
            import capo_cloudfront.types.ca_certificates_bundle_s3_location

            return {
                "CaCertificatesBundleS3Location": capo_cloudfront.types.ca_certificates_bundle_s3_location.deserialize_xml(
                    child
                )
            }
        else:
            return {"$unknown": {"name": child.tag}}
    raise DeserializationError(
        "CaCertificatesBundleSource: no recognized variant element"
    )
