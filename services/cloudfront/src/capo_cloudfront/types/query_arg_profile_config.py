"""Generated from Smithy shape ``com.amazonaws.cloudfront#QueryArgProfileConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudfront._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_cloudfront.types.boolean
    import capo_cloudfront.types.query_arg_profiles


class QueryArgProfileConfig(TypedDict, closed=True):
    forward_when_query_arg_profile_is_unknown: "capo_cloudfront.types.boolean.boolean"
    """<p>Flag to set if you want a request to be forwarded to the origin even if the profile specified by the field-level encryption query argument, fle-profile, is unknown.</p>"""
    query_arg_profiles: NotRequired[
        "capo_cloudfront.types.query_arg_profiles.QueryArgProfiles"
    ]
    """<p>Profiles specified for query argument-profile mapping for field-level encryption.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: QueryArgProfileConfig, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    SubElement(el, "ForwardWhenQueryArgProfileIsUnknown").text = (
        "true" if value["forward_when_query_arg_profile_is_unknown"] else "false"
    )
    if "query_arg_profiles" in value:
        import capo_cloudfront.types.query_arg_profiles

        capo_cloudfront.types.query_arg_profiles.serialize_xml(
            value["query_arg_profiles"], el, "QueryArgProfiles"
        )


def deserialize_xml(el: Element) -> QueryArgProfileConfig:
    out: QueryArgProfileConfig = {}  # type: ignore[typeddict-item]
    child_forward_when_query_arg_profile_is_unknown = el.find(
        "ForwardWhenQueryArgProfileIsUnknown"
    )
    if child_forward_when_query_arg_profile_is_unknown is not None:
        out["forward_when_query_arg_profile_is_unknown"] = (
            child_forward_when_query_arg_profile_is_unknown.text or ""
        ).lower() == "true"
    else:
        out["forward_when_query_arg_profile_is_unknown"] = False
    child_query_arg_profiles = el.find("QueryArgProfiles")
    if child_query_arg_profiles is not None:
        import capo_cloudfront.types.query_arg_profiles

        out["query_arg_profiles"] = (
            capo_cloudfront.types.query_arg_profiles.deserialize_xml(
                child_query_arg_profiles
            )
        )
    return out
