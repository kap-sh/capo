"""Generated from Smithy shape ``com.amazonaws.cloudfront#ContinuousDeploymentPolicyConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudfront._protocol.xml import Element, SubElement
from capo_cloudfront.errors import DeserializationError

if TYPE_CHECKING:
    import capo_cloudfront.types.boolean
    import capo_cloudfront.types.staging_distribution_dns_names
    import capo_cloudfront.types.traffic_config


class ContinuousDeploymentPolicyConfig(TypedDict, closed=True):
    staging_distribution_dns_names: "capo_cloudfront.types.staging_distribution_dns_names.StagingDistributionDnsNames"
    """<p>The CloudFront domain name of the staging distribution. For example: <code>d111111abcdef8.cloudfront.net</code>.</p>"""
    enabled: "capo_cloudfront.types.boolean.boolean"
    """<p>A Boolean that indicates whether this continuous deployment policy is enabled (in effect). When this value is <code>true</code>, this policy is enabled and in effect. When this value is <code>false</code>, this policy is not enabled and has no effect.</p>"""
    traffic_config: NotRequired["capo_cloudfront.types.traffic_config.TrafficConfig"]
    """<p>Contains the parameters for routing production traffic from your primary to staging distributions.</p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: ContinuousDeploymentPolicyConfig, parent: Element, tag: str
) -> None:
    el = SubElement(parent, tag)
    import capo_cloudfront.types.staging_distribution_dns_names

    capo_cloudfront.types.staging_distribution_dns_names.serialize_xml(
        value["staging_distribution_dns_names"], el, "StagingDistributionDnsNames"
    )
    SubElement(el, "Enabled").text = "true" if value["enabled"] else "false"
    if "traffic_config" in value:
        import capo_cloudfront.types.traffic_config

        capo_cloudfront.types.traffic_config.serialize_xml(
            value["traffic_config"], el, "TrafficConfig"
        )


def deserialize_xml(el: Element) -> ContinuousDeploymentPolicyConfig:
    out: ContinuousDeploymentPolicyConfig = {}  # type: ignore[typeddict-item]
    child_staging_distribution_dns_names = el.find("StagingDistributionDnsNames")
    if child_staging_distribution_dns_names is not None:
        import capo_cloudfront.types.staging_distribution_dns_names

        out["staging_distribution_dns_names"] = (
            capo_cloudfront.types.staging_distribution_dns_names.deserialize_xml(
                child_staging_distribution_dns_names
            )
        )
    else:
        raise DeserializationError(
            "ContinuousDeploymentPolicyConfig.staging_distribution_dns_names required"
        )
    child_enabled = el.find("Enabled")
    if child_enabled is not None:
        out["enabled"] = (child_enabled.text or "").lower() == "true"
    else:
        out["enabled"] = False
    child_traffic_config = el.find("TrafficConfig")
    if child_traffic_config is not None:
        import capo_cloudfront.types.traffic_config

        out["traffic_config"] = capo_cloudfront.types.traffic_config.deserialize_xml(
            child_traffic_config
        )
    return out
