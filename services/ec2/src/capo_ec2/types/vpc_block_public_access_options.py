"""Generated from Smithy shape ``com.amazonaws.ec2#VpcBlockPublicAccessOptions``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.internet_gateway_block_mode
    import capo_ec2.types.managed_by
    import capo_ec2.types.millisecond_date_time
    import capo_ec2.types.string
    import capo_ec2.types.vpc_block_public_access_exclusions_allowed
    import capo_ec2.types.vpc_block_public_access_state


class VpcBlockPublicAccessOptions(TypedDict, closed=True):
    aws_account_id: NotRequired["capo_ec2.types.string.String"]
    """<p>An Amazon Web Services account ID.</p>"""
    aws_region: NotRequired["capo_ec2.types.string.String"]
    """<p>An Amazon Web Services Region.</p>"""
    state: NotRequired[
        "capo_ec2.types.vpc_block_public_access_state.VpcBlockPublicAccessState"
    ]
    """<p>The current state of VPC BPA.</p>"""
    internet_gateway_block_mode: NotRequired[
        "capo_ec2.types.internet_gateway_block_mode.InternetGatewayBlockMode"
    ]
    """<p>The current mode of VPC BPA.</p> <ul> <li> <p> <code>off</code>: VPC BPA is not enabled and traffic is allowed to and from internet gateways and egress-only internet gateways in this Region.</p> </li> <li> <p> <code>block-bidirectional</code>: Block all traffic to and from internet gateways and egress-only internet gateways in this Region (except for excluded VPCs and subnets).</p> </li> <li> <p> <code>block-ingress</code>: Block all internet traffic to the VPCs in this Region (except for VPCs or subnets which are excluded). Only traffic to and from NAT gateways and egress-only internet gateways is allowed because these gateways only allow outbound connections to be established.</p> </li> </ul>"""
    reason: NotRequired["capo_ec2.types.string.String"]
    """<p>The reason for the current state.</p>"""
    last_update_timestamp: NotRequired[
        "capo_ec2.types.millisecond_date_time.MillisecondDateTime"
    ]
    """<p>The last time the VPC BPA mode was updated.</p>"""
    managed_by: NotRequired["capo_ec2.types.managed_by.ManagedBy"]
    """<p>The entity that manages the state of VPC BPA. Possible values include:</p> <ul> <li> <p> <code>account</code> - The state is managed by the account.</p> </li> <li> <p> <code>declarative-policy</code> - The state is managed by a declarative policy and can't be modified by the account.</p> </li> </ul>"""
    exclusions_allowed: NotRequired[
        "capo_ec2.types.vpc_block_public_access_exclusions_allowed.VpcBlockPublicAccessExclusionsAllowed"
    ]
    """<p>Determines if exclusions are allowed. If you have <a href="https://docs.aws.amazon.com/vpc/latest/userguide/security-vpc-bpa.html#security-vpc-bpa-exclusions-orgs">enabled VPC BPA at the Organization level</a>, exclusions may be <code>not-allowed</code>. Otherwise, they are <code>allowed</code>.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: VpcBlockPublicAccessOptions, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "aws_account_id" in value:
        pairs.append((f"{key_prefix}AwsAccountId", str(value["aws_account_id"])))
    if "aws_region" in value:
        pairs.append((f"{key_prefix}AwsRegion", str(value["aws_region"])))
    if "state" in value:
        import capo_ec2.types.vpc_block_public_access_state

        capo_ec2.types.vpc_block_public_access_state.serialize_ec2_query(
            value["state"], pairs, f"{key_prefix}State"
        )
    if "internet_gateway_block_mode" in value:
        import capo_ec2.types.internet_gateway_block_mode

        capo_ec2.types.internet_gateway_block_mode.serialize_ec2_query(
            value["internet_gateway_block_mode"],
            pairs,
            f"{key_prefix}InternetGatewayBlockMode",
        )
    if "reason" in value:
        pairs.append((f"{key_prefix}Reason", str(value["reason"])))
    if "last_update_timestamp" in value:
        import capo_ec2.types.millisecond_date_time

        capo_ec2.types.millisecond_date_time.serialize_ec2_query(
            value["last_update_timestamp"], pairs, f"{key_prefix}LastUpdateTimestamp"
        )
    if "managed_by" in value:
        import capo_ec2.types.managed_by

        capo_ec2.types.managed_by.serialize_ec2_query(
            value["managed_by"], pairs, f"{key_prefix}ManagedBy"
        )
    if "exclusions_allowed" in value:
        import capo_ec2.types.vpc_block_public_access_exclusions_allowed

        capo_ec2.types.vpc_block_public_access_exclusions_allowed.serialize_ec2_query(
            value["exclusions_allowed"], pairs, f"{key_prefix}ExclusionsAllowed"
        )


def deserialize_ec2_query(el: Element) -> VpcBlockPublicAccessOptions:
    out: VpcBlockPublicAccessOptions = {}  # type: ignore[typeddict-item]
    child_aws_account_id = el.find("awsAccountId")
    if child_aws_account_id is not None:
        out["aws_account_id"] = str(child_aws_account_id.text or "")
    child_aws_region = el.find("awsRegion")
    if child_aws_region is not None:
        out["aws_region"] = str(child_aws_region.text or "")
    child_state = el.find("state")
    if child_state is not None:
        import capo_ec2.types.vpc_block_public_access_state

        out["state"] = (
            capo_ec2.types.vpc_block_public_access_state.deserialize_ec2_query(
                child_state
            )
        )
    child_internet_gateway_block_mode = el.find("internetGatewayBlockMode")
    if child_internet_gateway_block_mode is not None:
        import capo_ec2.types.internet_gateway_block_mode

        out["internet_gateway_block_mode"] = (
            capo_ec2.types.internet_gateway_block_mode.deserialize_ec2_query(
                child_internet_gateway_block_mode
            )
        )
    child_reason = el.find("reason")
    if child_reason is not None:
        out["reason"] = str(child_reason.text or "")
    child_last_update_timestamp = el.find("lastUpdateTimestamp")
    if child_last_update_timestamp is not None:
        import capo_ec2.types.millisecond_date_time

        out["last_update_timestamp"] = (
            capo_ec2.types.millisecond_date_time.deserialize_ec2_query(
                child_last_update_timestamp
            )
        )
    child_managed_by = el.find("managedBy")
    if child_managed_by is not None:
        import capo_ec2.types.managed_by

        out["managed_by"] = capo_ec2.types.managed_by.deserialize_ec2_query(
            child_managed_by
        )
    child_exclusions_allowed = el.find("exclusionsAllowed")
    if child_exclusions_allowed is not None:
        import capo_ec2.types.vpc_block_public_access_exclusions_allowed

        out["exclusions_allowed"] = (
            capo_ec2.types.vpc_block_public_access_exclusions_allowed.deserialize_ec2_query(
                child_exclusions_allowed
            )
        )
    return out
