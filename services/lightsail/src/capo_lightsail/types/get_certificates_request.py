"""Generated from Smithy shape ``com.amazonaws.lightsail#GetCertificatesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lightsail.types.certificate_name
    import capo_lightsail.types.certificate_status_list
    import capo_lightsail.types.include_certificate_details
    import capo_lightsail.types.string


class GetCertificatesRequest(TypedDict, closed=True):
    certificate_statuses: NotRequired[
        "capo_lightsail.types.certificate_status_list.CertificateStatusList"
    ]
    """<p>The status of the certificates for which to return information.</p> <p>For example, specify <code>ISSUED</code> to return only certificates with an <code>ISSUED</code> status.</p> <p>When omitted, the response includes all of your certificates in the Amazon Web Services Region where the request is made, regardless of their current status.</p>"""
    include_certificate_details: NotRequired[
        "capo_lightsail.types.include_certificate_details.IncludeCertificateDetails"
    ]
    """<p>Indicates whether to include detailed information about the certificates in the response.</p> <p>When omitted, the response includes only the certificate names, Amazon Resource Names (ARNs), domain names, and tags.</p>"""
    certificate_name: NotRequired[
        "capo_lightsail.types.certificate_name.CertificateName"
    ]
    """<p>The name for the certificate for which to return information.</p> <p>When omitted, the response includes all of your certificates in the Amazon Web Services Region where the request is made.</p>"""
    page_token: NotRequired["capo_lightsail.types.string.string"]
    """<p>The token to advance to the next page of results from your request.</p> <p>To get a page token, perform an initial <code>GetCertificates</code> request. If your results are paginated, the response will return a next page token that you can specify as the page token in a subsequent request.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetCertificatesRequest) -> dict:
    out: dict = {}
    if "certificate_statuses" in value:
        import capo_lightsail.types.certificate_status_list

        out["certificateStatuses"] = (
            capo_lightsail.types.certificate_status_list.serialize_aws_json_1_1(
                value["certificate_statuses"]
            )
        )
    if "include_certificate_details" in value:
        out["includeCertificateDetails"] = value["include_certificate_details"]
    if "certificate_name" in value:
        out["certificateName"] = value["certificate_name"]
    if "page_token" in value:
        out["pageToken"] = value["page_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetCertificatesRequest:
    out: GetCertificatesRequest = {}  # type: ignore[typeddict-item]
    if data.get("certificateStatuses") is not None:
        import capo_lightsail.types.certificate_status_list

        out["certificate_statuses"] = (
            capo_lightsail.types.certificate_status_list.deserialize_aws_json_1_1(
                data["certificateStatuses"]
            )
        )
    if data.get("includeCertificateDetails") is not None:
        out["include_certificate_details"] = data["includeCertificateDetails"]
    if data.get("certificateName") is not None:
        out["certificate_name"] = data["certificateName"]
    if data.get("pageToken") is not None:
        out["page_token"] = data["pageToken"]
    return out
