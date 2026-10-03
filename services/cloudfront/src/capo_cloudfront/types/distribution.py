"""Generated from Smithy shape ``com.amazonaws.cloudfront#Distribution``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudfront._protocol.xml import Element, SubElement
from capo_cloudfront.errors import DeserializationError

if TYPE_CHECKING:
    import capo_cloudfront.types.active_trusted_key_groups
    import capo_cloudfront.types.active_trusted_signers
    import capo_cloudfront.types.alias_icp_recordals
    import capo_cloudfront.types.distribution_config
    import capo_cloudfront.types.integer
    import capo_cloudfront.types.string
    import capo_cloudfront.types.timestamp


class Distribution(TypedDict, closed=True):
    id: "capo_cloudfront.types.string.string"
    """<p>The distribution's identifier. For example: <code>E1U5RQF7T870K0</code>.</p>"""
    arn: "capo_cloudfront.types.string.string"
    """<p>The distribution's Amazon Resource Name (ARN).</p>"""
    status: "capo_cloudfront.types.string.string"
    """<p>The distribution's status. When the status is <code>Deployed</code>, the distribution's information is fully propagated to all CloudFront edge locations.</p>"""
    last_modified_time: "capo_cloudfront.types.timestamp.timestamp"
    """<p>The date and time when the distribution was last modified.</p>"""
    in_progress_invalidation_batches: "capo_cloudfront.types.integer.integer"
    """<p>The number of invalidation batches currently in progress.</p>"""
    domain_name: "capo_cloudfront.types.string.string"
    """<p>The distribution's CloudFront domain name. For example: <code>d111111abcdef8.cloudfront.net</code>.</p>"""
    active_trusted_signers: NotRequired[
        "capo_cloudfront.types.active_trusted_signers.ActiveTrustedSigners"
    ]
    """<important> <p>We recommend using <code>TrustedKeyGroups</code> instead of <code>TrustedSigners</code>.</p> </important> <p>This field contains a list of Amazon Web Services account IDs and the active CloudFront key pairs in each account that CloudFront can use to verify the signatures of signed URLs or signed cookies.</p>"""
    active_trusted_key_groups: NotRequired[
        "capo_cloudfront.types.active_trusted_key_groups.ActiveTrustedKeyGroups"
    ]
    """<p>This field contains a list of key groups and the public keys in each key group that CloudFront can use to verify the signatures of signed URLs or signed cookies.</p>"""
    distribution_config: "capo_cloudfront.types.distribution_config.DistributionConfig"
    """<p>The distribution's configuration.</p>"""
    alias_icp_recordals: NotRequired[
        "capo_cloudfront.types.alias_icp_recordals.AliasICPRecordals"
    ]
    """<p>Amazon Web Services services in China customers must file for an Internet Content Provider (ICP) recordal if they want to serve content publicly on an alternate domain name, also known as a CNAME, that they've added to CloudFront. AliasICPRecordal provides the ICP recordal status for CNAMEs associated with distributions.</p> <p>For more information about ICP recordals, see <a href="https://docs.amazonaws.cn/en_us/aws/latest/userguide/accounts-and-credentials.html"> Signup, Accounts, and Credentials</a> in <i>Getting Started with Amazon Web Services services in China</i>.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: Distribution, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    SubElement(el, "Id").text = str(value["id"])
    SubElement(el, "ARN").text = str(value["arn"])
    SubElement(el, "Status").text = str(value["status"])
    import capo_cloudfront.types.timestamp

    capo_cloudfront.types.timestamp.serialize_xml(
        value["last_modified_time"], el, "LastModifiedTime"
    )
    SubElement(el, "InProgressInvalidationBatches").text = str(
        value["in_progress_invalidation_batches"]
    )
    SubElement(el, "DomainName").text = str(value["domain_name"])
    if "active_trusted_signers" in value:
        import capo_cloudfront.types.active_trusted_signers

        capo_cloudfront.types.active_trusted_signers.serialize_xml(
            value["active_trusted_signers"], el, "ActiveTrustedSigners"
        )
    if "active_trusted_key_groups" in value:
        import capo_cloudfront.types.active_trusted_key_groups

        capo_cloudfront.types.active_trusted_key_groups.serialize_xml(
            value["active_trusted_key_groups"], el, "ActiveTrustedKeyGroups"
        )
    import capo_cloudfront.types.distribution_config

    capo_cloudfront.types.distribution_config.serialize_xml(
        value["distribution_config"], el, "DistributionConfig"
    )
    if "alias_icp_recordals" in value:
        import capo_cloudfront.types.alias_icp_recordals

        capo_cloudfront.types.alias_icp_recordals.serialize_xml(
            value["alias_icp_recordals"], el, "AliasICPRecordals"
        )


def deserialize_xml(el: Element) -> Distribution:
    out: Distribution = {}  # type: ignore[typeddict-item]
    child_id = el.find("Id")
    if child_id is not None:
        out["id"] = str(child_id.text or "")
    else:
        raise DeserializationError("Distribution.id required")
    child_arn = el.find("ARN")
    if child_arn is not None:
        out["arn"] = str(child_arn.text or "")
    else:
        raise DeserializationError("Distribution.arn required")
    child_status = el.find("Status")
    if child_status is not None:
        out["status"] = str(child_status.text or "")
    else:
        raise DeserializationError("Distribution.status required")
    child_last_modified_time = el.find("LastModifiedTime")
    if child_last_modified_time is not None:
        import capo_cloudfront.types.timestamp

        out["last_modified_time"] = capo_cloudfront.types.timestamp.deserialize_xml(
            child_last_modified_time
        )
    else:
        raise DeserializationError("Distribution.last_modified_time required")
    child_in_progress_invalidation_batches = el.find("InProgressInvalidationBatches")
    if child_in_progress_invalidation_batches is not None:
        out["in_progress_invalidation_batches"] = int(
            child_in_progress_invalidation_batches.text or ""
        )
    else:
        raise DeserializationError(
            "Distribution.in_progress_invalidation_batches required"
        )
    child_domain_name = el.find("DomainName")
    if child_domain_name is not None:
        out["domain_name"] = str(child_domain_name.text or "")
    else:
        raise DeserializationError("Distribution.domain_name required")
    child_active_trusted_signers = el.find("ActiveTrustedSigners")
    if child_active_trusted_signers is not None:
        import capo_cloudfront.types.active_trusted_signers

        out["active_trusted_signers"] = (
            capo_cloudfront.types.active_trusted_signers.deserialize_xml(
                child_active_trusted_signers
            )
        )
    child_active_trusted_key_groups = el.find("ActiveTrustedKeyGroups")
    if child_active_trusted_key_groups is not None:
        import capo_cloudfront.types.active_trusted_key_groups

        out["active_trusted_key_groups"] = (
            capo_cloudfront.types.active_trusted_key_groups.deserialize_xml(
                child_active_trusted_key_groups
            )
        )
    child_distribution_config = el.find("DistributionConfig")
    if child_distribution_config is not None:
        import capo_cloudfront.types.distribution_config

        out["distribution_config"] = (
            capo_cloudfront.types.distribution_config.deserialize_xml(
                child_distribution_config
            )
        )
    else:
        raise DeserializationError("Distribution.distribution_config required")
    child_alias_icp_recordals = el.find("AliasICPRecordals")
    if child_alias_icp_recordals is not None:
        import capo_cloudfront.types.alias_icp_recordals

        out["alias_icp_recordals"] = (
            capo_cloudfront.types.alias_icp_recordals.deserialize_xml(
                child_alias_icp_recordals
            )
        )
    return out
