"""Generated from Smithy shape ``com.amazonaws.kendra#OnPremiseConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_kendra.errors import DeserializationError

if TYPE_CHECKING:
    import capo_kendra.types.organization_name
    import capo_kendra.types.s3_path
    import capo_kendra.types.url


class OnPremiseConfiguration(TypedDict, closed=True):
    host_url: "capo_kendra.types.url.Url"
    """<p>The GitHub host URL or API endpoint URL. For example, <i>https://on-prem-host-url/api/v3/</i> </p>"""
    organization_name: "capo_kendra.types.organization_name.OrganizationName"
    """<p>The name of the organization of the GitHub Enterprise Server (on-premises) account you want to connect to. You can find your organization name by logging into GitHub desktop and selecting <b>Your organizations</b> under your profile picture dropdown.</p>"""
    ssl_certificate_s3_path: "capo_kendra.types.s3_path.S3Path"
    """<p>The path to the SSL certificate stored in an Amazon S3 bucket. You use this to connect to GitHub if you require a secure SSL connection.</p> <p>You can simply generate a self-signed X509 certificate on any computer using OpenSSL. For an example of using OpenSSL to create an X509 certificate, see <a href="https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/configuring-https-ssl.html">Create and sign an X509 certificate</a>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: OnPremiseConfiguration) -> dict:
    out: dict = {}
    out["HostUrl"] = value["host_url"]
    out["OrganizationName"] = value["organization_name"]
    import capo_kendra.types.s3_path

    out["SslCertificateS3Path"] = capo_kendra.types.s3_path.serialize_aws_json_1_1(
        value["ssl_certificate_s3_path"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> OnPremiseConfiguration:
    out: OnPremiseConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("HostUrl") is not None:
        out["host_url"] = data["HostUrl"]
    else:
        raise DeserializationError("OnPremiseConfiguration.host_url required")
    if data.get("OrganizationName") is not None:
        out["organization_name"] = data["OrganizationName"]
    else:
        raise DeserializationError("OnPremiseConfiguration.organization_name required")
    if data.get("SslCertificateS3Path") is not None:
        import capo_kendra.types.s3_path

        out["ssl_certificate_s3_path"] = (
            capo_kendra.types.s3_path.deserialize_aws_json_1_1(
                data["SslCertificateS3Path"]
            )
        )
    else:
        raise DeserializationError(
            "OnPremiseConfiguration.ssl_certificate_s3_path required"
        )
    return out
