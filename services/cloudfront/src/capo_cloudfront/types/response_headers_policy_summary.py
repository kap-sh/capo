"""Generated from Smithy shape ``com.amazonaws.cloudfront#ResponseHeadersPolicySummary``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_cloudfront._protocol.xml import Element, SubElement
from capo_cloudfront.errors import DeserializationError

if TYPE_CHECKING:
    import capo_cloudfront.types.response_headers_policy
    import capo_cloudfront.types.response_headers_policy_type


class ResponseHeadersPolicySummary(TypedDict, closed=True):
    type: "capo_cloudfront.types.response_headers_policy_type.ResponseHeadersPolicyType"
    """<p>The type of response headers policy, either <code>managed</code> (created by Amazon Web Services) or <code>custom</code> (created in this Amazon Web Services account).</p>"""
    response_headers_policy: (
        "capo_cloudfront.types.response_headers_policy.ResponseHeadersPolicy"
    )
    """<p>The response headers policy.</p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: ResponseHeadersPolicySummary, parent: Element, tag: str
) -> None:
    el = SubElement(parent, tag)
    import capo_cloudfront.types.response_headers_policy_type

    capo_cloudfront.types.response_headers_policy_type.serialize_xml(
        value["type"], el, "Type"
    )
    import capo_cloudfront.types.response_headers_policy

    capo_cloudfront.types.response_headers_policy.serialize_xml(
        value["response_headers_policy"], el, "ResponseHeadersPolicy"
    )


def deserialize_xml(el: Element) -> ResponseHeadersPolicySummary:
    out: ResponseHeadersPolicySummary = {}  # type: ignore[typeddict-item]
    child_type = el.find("Type")
    if child_type is not None:
        import capo_cloudfront.types.response_headers_policy_type

        out["type"] = (
            capo_cloudfront.types.response_headers_policy_type.deserialize_xml(
                child_type
            )
        )
    else:
        import typing

        out["type"] = typing.cast(
            "capo_cloudfront.types.response_headers_policy_type.ResponseHeadersPolicyType",
            "",
        )
    child_response_headers_policy = el.find("ResponseHeadersPolicy")
    if child_response_headers_policy is not None:
        import capo_cloudfront.types.response_headers_policy

        out["response_headers_policy"] = (
            capo_cloudfront.types.response_headers_policy.deserialize_xml(
                child_response_headers_policy
            )
        )
    else:
        raise DeserializationError(
            "ResponseHeadersPolicySummary.response_headers_policy required"
        )
    return out
