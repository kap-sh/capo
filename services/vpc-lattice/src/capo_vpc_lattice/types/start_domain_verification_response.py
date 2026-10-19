"""Generated from Smithy shape ``com.amazonaws.vpclattice#StartDomainVerificationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_vpc_lattice.types.domain_name
    import capo_vpc_lattice.types.domain_verification_arn
    import capo_vpc_lattice.types.domain_verification_id
    import capo_vpc_lattice.types.txt_method_config
    import capo_vpc_lattice.types.verification_status


class StartDomainVerificationResponse(TypedDict, closed=True):
    id: "capo_vpc_lattice.types.domain_verification_id.DomainVerificationId"
    """<p> The ID of the domain verification. </p>"""
    arn: "capo_vpc_lattice.types.domain_verification_arn.DomainVerificationArn"
    """<p> The Amazon Resource Name (ARN) of the domain verification. </p>"""
    domain_name: "capo_vpc_lattice.types.domain_name.DomainName"
    """<p> The domain name being verified. </p>"""
    status: "capo_vpc_lattice.types.verification_status.VerificationStatus"
    """<p> The current status of the domain verification process. </p>"""
    txt_method_config: NotRequired[
        "capo_vpc_lattice.types.txt_method_config.TxtMethodConfig"
    ]
    """<p> The TXT record configuration used for domain verification. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartDomainVerificationResponse) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    out["arn"] = value["arn"]
    out["domainName"] = value["domain_name"]
    out["status"] = value["status"]
    if "txt_method_config" in value:
        import capo_vpc_lattice.types.txt_method_config

        out["txtMethodConfig"] = (
            capo_vpc_lattice.types.txt_method_config.serialize_json(
                value["txt_method_config"]
            )
        )
    return out


def deserialize_json(data: dict) -> StartDomainVerificationResponse:
    out: StartDomainVerificationResponse = {}  # type: ignore[typeddict-item]
    if data.get("id") is not None:
        out["id"] = data["id"]
    else:
        out["id"] = ""
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    else:
        out["arn"] = ""
    if data.get("domainName") is not None:
        out["domain_name"] = data["domainName"]
    else:
        out["domain_name"] = ""
    if data.get("status") is not None:
        out["status"] = data["status"]
    else:
        out["status"] = ""
    if data.get("txtMethodConfig") is not None:
        import capo_vpc_lattice.types.txt_method_config

        out["txt_method_config"] = (
            capo_vpc_lattice.types.txt_method_config.deserialize_json(
                data["txtMethodConfig"]
            )
        )
    return out
