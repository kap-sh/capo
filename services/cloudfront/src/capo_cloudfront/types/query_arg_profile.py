"""Generated from Smithy shape ``com.amazonaws.cloudfront#QueryArgProfile``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_cloudfront._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_cloudfront.types.string


class QueryArgProfile(TypedDict, closed=True):
    query_arg: "capo_cloudfront.types.string.string"
    """<p>Query argument for field-level encryption query argument-profile mapping.</p>"""
    profile_id: "capo_cloudfront.types.string.string"
    """<p>ID of profile to use for field-level encryption query argument-profile mapping</p>"""


# --- restXml ser/de ---
def serialize_xml(value: QueryArgProfile, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    SubElement(el, "QueryArg").text = str(value["query_arg"])
    SubElement(el, "ProfileId").text = str(value["profile_id"])


def deserialize_xml(el: Element) -> QueryArgProfile:
    out: QueryArgProfile = {}  # type: ignore[typeddict-item]
    child_query_arg = el.find("QueryArg")
    if child_query_arg is not None:
        out["query_arg"] = str(child_query_arg.text or "")
    else:
        out["query_arg"] = ""
    child_profile_id = el.find("ProfileId")
    if child_profile_id is not None:
        out["profile_id"] = str(child_profile_id.text or "")
    else:
        out["profile_id"] = ""
    return out
