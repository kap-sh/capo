"""Generated from Smithy shape ``com.amazonaws.cloudfront#OriginRequestPolicySummary``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_cloudfront._protocol.xml import Element, SubElement
from capo_cloudfront.errors import DeserializationError

if TYPE_CHECKING:
    import capo_cloudfront.types.origin_request_policy
    import capo_cloudfront.types.origin_request_policy_type


class OriginRequestPolicySummary(TypedDict, closed=True):
    type: "capo_cloudfront.types.origin_request_policy_type.OriginRequestPolicyType"
    """<p>The type of origin request policy, either <code>managed</code> (created by Amazon Web Services) or <code>custom</code> (created in this Amazon Web Services account).</p>"""
    origin_request_policy: (
        "capo_cloudfront.types.origin_request_policy.OriginRequestPolicy"
    )
    """<p>The origin request policy.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: OriginRequestPolicySummary, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    import capo_cloudfront.types.origin_request_policy_type

    capo_cloudfront.types.origin_request_policy_type.serialize_xml(
        value["type"], el, "Type"
    )
    import capo_cloudfront.types.origin_request_policy

    capo_cloudfront.types.origin_request_policy.serialize_xml(
        value["origin_request_policy"], el, "OriginRequestPolicy"
    )


def deserialize_xml(el: Element) -> OriginRequestPolicySummary:
    out: OriginRequestPolicySummary = {}  # type: ignore[typeddict-item]
    child_type = el.find("Type")
    if child_type is not None:
        import capo_cloudfront.types.origin_request_policy_type

        out["type"] = capo_cloudfront.types.origin_request_policy_type.deserialize_xml(
            child_type
        )
    else:
        import typing

        out["type"] = typing.cast(
            "capo_cloudfront.types.origin_request_policy_type.OriginRequestPolicyType",
            "",
        )
    child_origin_request_policy = el.find("OriginRequestPolicy")
    if child_origin_request_policy is not None:
        import capo_cloudfront.types.origin_request_policy

        out["origin_request_policy"] = (
            capo_cloudfront.types.origin_request_policy.deserialize_xml(
                child_origin_request_policy
            )
        )
    else:
        raise DeserializationError(
            "OriginRequestPolicySummary.origin_request_policy required"
        )
    return out
