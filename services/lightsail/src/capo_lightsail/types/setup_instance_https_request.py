"""Generated from Smithy shape ``com.amazonaws.lightsail#SetupInstanceHttpsRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

from capo_lightsail.errors import DeserializationError

if TYPE_CHECKING:
    import capo_lightsail.types.certificate_provider
    import capo_lightsail.types.email_address
    import capo_lightsail.types.resource_name
    import capo_lightsail.types.setup_domain_name_list


class SetupInstanceHttpsRequest(TypedDict, closed=True):
    instance_name: "capo_lightsail.types.resource_name.ResourceName"
    """<p>The name of the Lightsail instance.</p>"""
    email_address: "capo_lightsail.types.email_address.EmailAddress"
    """<p>The contact method for SSL/TLS certificate renewal alerts. You can enter one email address. </p>"""
    domain_names: "capo_lightsail.types.setup_domain_name_list.SetupDomainNameList"
    """<p>The name of the domain and subdomains that were specified for the SSL/TLS certificate.</p>"""
    certificate_provider: (
        "capo_lightsail.types.certificate_provider.CertificateProvider"
    )
    """<p>The certificate authority that issues the SSL/TLS certificate.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SetupInstanceHttpsRequest) -> dict:
    out: dict = {}
    out["instanceName"] = value["instance_name"]
    out["emailAddress"] = value["email_address"]
    import capo_lightsail.types.setup_domain_name_list

    out["domainNames"] = (
        capo_lightsail.types.setup_domain_name_list.serialize_aws_json_1_1(
            value["domain_names"]
        )
    )
    import capo_lightsail.types.certificate_provider

    out["certificateProvider"] = (
        capo_lightsail.types.certificate_provider.serialize_aws_json_1_1(
            value["certificate_provider"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> SetupInstanceHttpsRequest:
    out: SetupInstanceHttpsRequest = {}  # type: ignore[typeddict-item]
    if data.get("instanceName") is not None:
        out["instance_name"] = data["instanceName"]
    else:
        raise DeserializationError("SetupInstanceHttpsRequest.instance_name required")
    if data.get("emailAddress") is not None:
        out["email_address"] = data["emailAddress"]
    else:
        raise DeserializationError("SetupInstanceHttpsRequest.email_address required")
    if data.get("domainNames") is not None:
        import capo_lightsail.types.setup_domain_name_list

        out["domain_names"] = (
            capo_lightsail.types.setup_domain_name_list.deserialize_aws_json_1_1(
                data["domainNames"]
            )
        )
    else:
        raise DeserializationError("SetupInstanceHttpsRequest.domain_names required")
    if data.get("certificateProvider") is not None:
        import capo_lightsail.types.certificate_provider

        out["certificate_provider"] = (
            capo_lightsail.types.certificate_provider.deserialize_aws_json_1_1(
                data["certificateProvider"]
            )
        )
    else:
        raise DeserializationError(
            "SetupInstanceHttpsRequest.certificate_provider required"
        )
    return out


def redact_sensitive(value: SetupInstanceHttpsRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "email_address" in value:
        out["email_address"] = "*** Sensitive Data Redacted ***"
    return out
