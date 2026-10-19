"""Generated from Smithy shape ``com.amazonaws.paymentcryptography#CertificateSubjectType``."""

from typing_extensions import NotRequired, TypedDict


class CertificateSubjectType(TypedDict, closed=True):
    common_name: "str"
    """<p>The name you provide to create the certificate signing request.</p>"""
    organization_unit: NotRequired["str"]
    """<p>The organization unit you provide to create the certificate signing request.</p>"""
    organization: NotRequired["str"]
    """<p>The organization you provide to create the certificate signing request.</p>"""
    city: NotRequired["str"]
    """<p>The city you provide to create the certificate signing request.</p>"""
    country: NotRequired["str"]
    """<p>The country you provide to create the certificate signing request.</p>"""
    state_or_province: NotRequired["str"]
    """<p>The state or province you provide to create the certificate signing request.</p>"""
    email_address: NotRequired["str"]
    """<p>The email address you provide to create the certificate signing request.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CertificateSubjectType) -> dict:
    out: dict = {}
    out["CommonName"] = value["common_name"]
    if "organization_unit" in value:
        out["OrganizationUnit"] = value["organization_unit"]
    if "organization" in value:
        out["Organization"] = value["organization"]
    if "city" in value:
        out["City"] = value["city"]
    if "country" in value:
        out["Country"] = value["country"]
    if "state_or_province" in value:
        out["StateOrProvince"] = value["state_or_province"]
    if "email_address" in value:
        out["EmailAddress"] = value["email_address"]
    return out


def deserialize_aws_json_1_0(data: dict) -> CertificateSubjectType:
    out: CertificateSubjectType = {}  # type: ignore[typeddict-item]
    if data.get("CommonName") is not None:
        out["common_name"] = data["CommonName"]
    else:
        out["common_name"] = ""
    if data.get("OrganizationUnit") is not None:
        out["organization_unit"] = data["OrganizationUnit"]
    if data.get("Organization") is not None:
        out["organization"] = data["Organization"]
    if data.get("City") is not None:
        out["city"] = data["City"]
    if data.get("Country") is not None:
        out["country"] = data["Country"]
    if data.get("StateOrProvince") is not None:
        out["state_or_province"] = data["StateOrProvince"]
    if data.get("EmailAddress") is not None:
        out["email_address"] = data["EmailAddress"]
    return out
