"""Generated from Smithy shape ``com.amazonaws.cloudfront#ResponseHeadersPolicy``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_cloudfront._protocol.xml import Element, SubElement
from capo_cloudfront.errors import DeserializationError

if TYPE_CHECKING:
    import capo_cloudfront.types.response_headers_policy_config
    import capo_cloudfront.types.string
    import capo_cloudfront.types.timestamp


class ResponseHeadersPolicy(TypedDict, closed=True):
    id: "capo_cloudfront.types.string.string"
    """<p>The identifier for the response headers policy.</p>"""
    last_modified_time: "capo_cloudfront.types.timestamp.timestamp"
    """<p>The date and time when the response headers policy was last modified.</p>"""
    response_headers_policy_config: "capo_cloudfront.types.response_headers_policy_config.ResponseHeadersPolicyConfig"
    """<p>A response headers policy configuration.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: ResponseHeadersPolicy, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    SubElement(el, "Id").text = str(value["id"])
    import capo_cloudfront.types.timestamp

    capo_cloudfront.types.timestamp.serialize_xml(
        value["last_modified_time"], el, "LastModifiedTime"
    )
    import capo_cloudfront.types.response_headers_policy_config

    capo_cloudfront.types.response_headers_policy_config.serialize_xml(
        value["response_headers_policy_config"], el, "ResponseHeadersPolicyConfig"
    )


def deserialize_xml(el: Element) -> ResponseHeadersPolicy:
    out: ResponseHeadersPolicy = {}  # type: ignore[typeddict-item]
    child_id = el.find("Id")
    if child_id is not None:
        out["id"] = str(child_id.text or "")
    else:
        out["id"] = ""
    child_last_modified_time = el.find("LastModifiedTime")
    if child_last_modified_time is not None:
        import capo_cloudfront.types.timestamp

        out["last_modified_time"] = capo_cloudfront.types.timestamp.deserialize_xml(
            child_last_modified_time
        )
    else:
        import datetime

        out["last_modified_time"] = datetime.datetime.fromtimestamp(
            0, tz=datetime.timezone.utc
        )
    child_response_headers_policy_config = el.find("ResponseHeadersPolicyConfig")
    if child_response_headers_policy_config is not None:
        import capo_cloudfront.types.response_headers_policy_config

        out["response_headers_policy_config"] = (
            capo_cloudfront.types.response_headers_policy_config.deserialize_xml(
                child_response_headers_policy_config
            )
        )
    else:
        raise DeserializationError(
            "ResponseHeadersPolicy.response_headers_policy_config required"
        )
    return out
