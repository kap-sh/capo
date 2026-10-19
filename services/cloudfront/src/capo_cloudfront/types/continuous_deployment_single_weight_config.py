"""Generated from Smithy shape ``com.amazonaws.cloudfront#ContinuousDeploymentSingleWeightConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudfront._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_cloudfront.types.float
    import capo_cloudfront.types.session_stickiness_config


class ContinuousDeploymentSingleWeightConfig(TypedDict, closed=True):
    weight: "capo_cloudfront.types.float.float"
    """<p>The percentage of traffic to send to a staging distribution, expressed as a decimal number between 0 and 0.15. For example, a value of 0.10 means 10% of traffic is sent to the staging distribution.</p>"""
    session_stickiness_config: NotRequired[
        "capo_cloudfront.types.session_stickiness_config.SessionStickinessConfig"
    ]


# --- restXml ser/de ---
def serialize_xml(
    value: ContinuousDeploymentSingleWeightConfig, parent: Element, tag: str
) -> None:
    el = SubElement(parent, tag)
    SubElement(el, "Weight").text = (
        "NaN"
        if value["weight"] != value["weight"]
        else "Infinity"
        if value["weight"] == float("inf")
        else "-Infinity"
        if value["weight"] == float("-inf")
        else str(value["weight"])
    )
    if "session_stickiness_config" in value:
        import capo_cloudfront.types.session_stickiness_config

        capo_cloudfront.types.session_stickiness_config.serialize_xml(
            value["session_stickiness_config"], el, "SessionStickinessConfig"
        )


def deserialize_xml(el: Element) -> ContinuousDeploymentSingleWeightConfig:
    out: ContinuousDeploymentSingleWeightConfig = {}  # type: ignore[typeddict-item]
    child_weight = el.find("Weight")
    if child_weight is not None:
        out["weight"] = float(child_weight.text or "")
    else:
        out["weight"] = 0.0
    child_session_stickiness_config = el.find("SessionStickinessConfig")
    if child_session_stickiness_config is not None:
        import capo_cloudfront.types.session_stickiness_config

        out["session_stickiness_config"] = (
            capo_cloudfront.types.session_stickiness_config.deserialize_xml(
                child_session_stickiness_config
            )
        )
    return out
