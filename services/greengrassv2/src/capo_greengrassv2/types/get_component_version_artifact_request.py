"""Generated from Smithy shape ``com.amazonaws.greengrassv2#GetComponentVersionArtifactRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_greengrassv2.types.component_version_arn
    import capo_greengrassv2.types.iot_endpoint_type
    import capo_greengrassv2.types.non_empty_string
    import capo_greengrassv2.types.s3_endpoint_type


class GetComponentVersionArtifactRequest(TypedDict, closed=True):
    arn: "capo_greengrassv2.types.component_version_arn.ComponentVersionARN"
    """<p>The <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html">ARN</a> of the component version. Specify the ARN of a public or a Lambda component version.</p>"""
    artifact_name: "capo_greengrassv2.types.non_empty_string.NonEmptyString"
    """<p>The name of the artifact.</p> <p>You can use the <a href="https://docs.aws.amazon.com/greengrass/v2/APIReference/API_GetComponent.html">GetComponent</a> operation to download the component recipe, which includes the URI of the artifact. The artifact name is the section of the URI after the scheme. For example, in the artifact URI <code>greengrass:SomeArtifact.zip</code>, the artifact name is <code>SomeArtifact.zip</code>.</p>"""
    s3_endpoint_type: NotRequired[
        "capo_greengrassv2.types.s3_endpoint_type.S3EndpointType"
    ]
    """<p>Specifies the endpoint to use when getting Amazon S3 pre-signed URLs.</p> <p>All Amazon Web Services Regions except US East (N. Virginia) use <code>REGIONAL</code> in all cases. In the US East (N. Virginia) Region the default is <code>GLOBAL</code>, but you can change it to <code>REGIONAL</code> with this parameter.</p>"""
    iot_endpoint_type: NotRequired[
        "capo_greengrassv2.types.iot_endpoint_type.IotEndpointType"
    ]
    """<p>Determines if the Amazon S3 URL returned is a FIPS pre-signed URL endpoint. Specify <code>fips</code> if you want the returned Amazon S3 pre-signed URL to point to an Amazon S3 FIPS endpoint. If you don't specify a value, the default is <code>standard</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetComponentVersionArtifactRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetComponentVersionArtifactRequest:
    out: GetComponentVersionArtifactRequest = {}  # type: ignore[typeddict-item]
    return out
