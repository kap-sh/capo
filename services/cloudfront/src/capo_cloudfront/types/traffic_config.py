"""Generated from Smithy shape ``com.amazonaws.cloudfront#TrafficConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudfront._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_cloudfront.types.continuous_deployment_policy_type
    import capo_cloudfront.types.continuous_deployment_single_header_config
    import capo_cloudfront.types.continuous_deployment_single_weight_config


class TrafficConfig(TypedDict, closed=True):
    single_weight_config: NotRequired[
        "capo_cloudfront.types.continuous_deployment_single_weight_config.ContinuousDeploymentSingleWeightConfig"
    ]
    """<p>Contains the percentage of traffic to send to the staging distribution.</p>"""
    single_header_config: NotRequired[
        "capo_cloudfront.types.continuous_deployment_single_header_config.ContinuousDeploymentSingleHeaderConfig"
    ]
    """<p>Determines which HTTP requests are sent to the staging distribution.</p>"""
    type: "capo_cloudfront.types.continuous_deployment_policy_type.ContinuousDeploymentPolicyType"
    """<p>The type of traffic configuration.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: TrafficConfig, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    if "single_weight_config" in value:
        import capo_cloudfront.types.continuous_deployment_single_weight_config

        capo_cloudfront.types.continuous_deployment_single_weight_config.serialize_xml(
            value["single_weight_config"], el, "SingleWeightConfig"
        )
    if "single_header_config" in value:
        import capo_cloudfront.types.continuous_deployment_single_header_config

        capo_cloudfront.types.continuous_deployment_single_header_config.serialize_xml(
            value["single_header_config"], el, "SingleHeaderConfig"
        )
    import capo_cloudfront.types.continuous_deployment_policy_type

    capo_cloudfront.types.continuous_deployment_policy_type.serialize_xml(
        value["type"], el, "Type"
    )


def deserialize_xml(el: Element) -> TrafficConfig:
    out: TrafficConfig = {}  # type: ignore[typeddict-item]
    child_single_weight_config = el.find("SingleWeightConfig")
    if child_single_weight_config is not None:
        import capo_cloudfront.types.continuous_deployment_single_weight_config

        out["single_weight_config"] = (
            capo_cloudfront.types.continuous_deployment_single_weight_config.deserialize_xml(
                child_single_weight_config
            )
        )
    child_single_header_config = el.find("SingleHeaderConfig")
    if child_single_header_config is not None:
        import capo_cloudfront.types.continuous_deployment_single_header_config

        out["single_header_config"] = (
            capo_cloudfront.types.continuous_deployment_single_header_config.deserialize_xml(
                child_single_header_config
            )
        )
    child_type = el.find("Type")
    if child_type is not None:
        import capo_cloudfront.types.continuous_deployment_policy_type

        out["type"] = (
            capo_cloudfront.types.continuous_deployment_policy_type.deserialize_xml(
                child_type
            )
        )
    else:
        import typing

        out["type"] = typing.cast(
            "capo_cloudfront.types.continuous_deployment_policy_type.ContinuousDeploymentPolicyType",
            "",
        )
    return out
