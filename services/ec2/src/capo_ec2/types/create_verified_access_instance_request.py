"""Generated from Smithy shape ``com.amazonaws.ec2#CreateVerifiedAccessInstanceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.boolean
    import capo_ec2.types.string
    import capo_ec2.types.tag_specification_list


class CreateVerifiedAccessInstanceRequest(TypedDict, closed=True):
    description: NotRequired["capo_ec2.types.string.String"]
    """<p>A description for the Verified Access instance.</p>"""
    tag_specifications: NotRequired[
        "capo_ec2.types.tag_specification_list.TagSpecificationList"
    ]
    """<p>The tags to assign to the Verified Access instance.</p>"""
    client_token: NotRequired["capo_ec2.types.string.String"]
    """<p>A unique, case-sensitive token that you provide to ensure idempotency of your modification request. For more information, see <a href="https://docs.aws.amazon.com/ec2/latest/devguide/ec2-api-idempotency.html">Ensuring idempotency</a>.</p>"""
    dry_run: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
    fips_enabled: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>Enable or disable support for Federal Information Processing Standards (FIPS) on the instance.</p>"""
    cidr_endpoints_custom_sub_domain: NotRequired["capo_ec2.types.string.String"]
    """<p>The custom subdomain.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: CreateVerifiedAccessInstanceRequest,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "description" in value:
        pairs.append((f"{key_prefix}Description", str(value["description"])))
    if "tag_specifications" in value:
        import capo_ec2.types.tag_specification_list

        capo_ec2.types.tag_specification_list.serialize_ec2_query(
            value["tag_specifications"], pairs, f"{key_prefix}TagSpecification"
        )
    if "client_token" in value:
        pairs.append((f"{key_prefix}ClientToken", str(value["client_token"])))
    if "dry_run" in value:
        pairs.append((f"{key_prefix}DryRun", "true" if value["dry_run"] else "false"))
    if "fips_enabled" in value:
        pairs.append(
            (f"{key_prefix}FIPSEnabled", "true" if value["fips_enabled"] else "false")
        )
    if "cidr_endpoints_custom_sub_domain" in value:
        pairs.append(
            (
                f"{key_prefix}CidrEndpointsCustomSubDomain",
                str(value["cidr_endpoints_custom_sub_domain"]),
            )
        )


def deserialize_ec2_query(el: Element) -> CreateVerifiedAccessInstanceRequest:
    out: CreateVerifiedAccessInstanceRequest = {}  # type: ignore[typeddict-item]
    child_description = el.find("Description")
    if child_description is not None:
        out["description"] = str(child_description.text or "")
    child_tag_specifications = el.find("TagSpecification")
    if child_tag_specifications is not None:
        import capo_ec2.types.tag_specification_list

        out["tag_specifications"] = (
            capo_ec2.types.tag_specification_list.deserialize_ec2_query(
                child_tag_specifications
            )
        )
    child_client_token = el.find("ClientToken")
    if child_client_token is not None:
        out["client_token"] = str(child_client_token.text or "")
    child_dry_run = el.find("DryRun")
    if child_dry_run is not None:
        out["dry_run"] = (child_dry_run.text or "").lower() == "true"
    child_fips_enabled = el.find("FIPSEnabled")
    if child_fips_enabled is not None:
        out["fips_enabled"] = (child_fips_enabled.text or "").lower() == "true"
    child_cidr_endpoints_custom_sub_domain = el.find("CidrEndpointsCustomSubDomain")
    if child_cidr_endpoints_custom_sub_domain is not None:
        out["cidr_endpoints_custom_sub_domain"] = str(
            child_cidr_endpoints_custom_sub_domain.text or ""
        )
    return out
