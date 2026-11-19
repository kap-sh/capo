"""Generated from Smithy shape ``com.amazonaws.appstream#UrlRedirectionConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_appstream.types.boolean_object
    import capo_appstream.types.url_pattern_list


class UrlRedirectionConfig(TypedDict, closed=True):
    enabled: NotRequired["capo_appstream.types.boolean_object.BooleanObject"]
    """<p>Whether URL redirection is enabled for this direction.</p>"""
    allowed_urls: NotRequired["capo_appstream.types.url_pattern_list.UrlPatternList"]
    """<p>List of URL patterns that are allowed to be redirected. URLs matching these patterns will be redirected unless they also match a pattern in the denied list.</p>"""
    denied_urls: NotRequired["capo_appstream.types.url_pattern_list.UrlPatternList"]
    """<p>List of URL patterns that are denied from redirection. This list takes precedence over the allowed list.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UrlRedirectionConfig) -> dict:
    out: dict = {}
    if "enabled" in value:
        out["Enabled"] = value["enabled"]
    if "allowed_urls" in value:
        import capo_appstream.types.url_pattern_list

        out["AllowedUrls"] = (
            capo_appstream.types.url_pattern_list.serialize_aws_json_1_1(
                value["allowed_urls"]
            )
        )
    if "denied_urls" in value:
        import capo_appstream.types.url_pattern_list

        out["DeniedUrls"] = (
            capo_appstream.types.url_pattern_list.serialize_aws_json_1_1(
                value["denied_urls"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> UrlRedirectionConfig:
    out: UrlRedirectionConfig = {}  # type: ignore[typeddict-item]
    if data.get("Enabled") is not None:
        out["enabled"] = data["Enabled"]
    if data.get("AllowedUrls") is not None:
        import capo_appstream.types.url_pattern_list

        out["allowed_urls"] = (
            capo_appstream.types.url_pattern_list.deserialize_aws_json_1_1(
                data["AllowedUrls"]
            )
        )
    if data.get("DeniedUrls") is not None:
        import capo_appstream.types.url_pattern_list

        out["denied_urls"] = (
            capo_appstream.types.url_pattern_list.deserialize_aws_json_1_1(
                data["DeniedUrls"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: UrlRedirectionConfig) -> dict:
    out: dict = {}
    if "enabled" in value:
        out["Enabled"] = value["enabled"]
    if "allowed_urls" in value:
        import capo_appstream.types.url_pattern_list

        out["AllowedUrls"] = capo_appstream.types.url_pattern_list.serialize_cbor(
            value["allowed_urls"]
        )
    if "denied_urls" in value:
        import capo_appstream.types.url_pattern_list

        out["DeniedUrls"] = capo_appstream.types.url_pattern_list.serialize_cbor(
            value["denied_urls"]
        )
    return out


def deserialize_cbor(data: dict) -> UrlRedirectionConfig:
    out: UrlRedirectionConfig = {}  # type: ignore[typeddict-item]
    if data.get("Enabled") is not None:
        out["enabled"] = data["Enabled"]
    if data.get("AllowedUrls") is not None:
        import capo_appstream.types.url_pattern_list

        out["allowed_urls"] = capo_appstream.types.url_pattern_list.deserialize_cbor(
            data["AllowedUrls"]
        )
    if data.get("DeniedUrls") is not None:
        import capo_appstream.types.url_pattern_list

        out["denied_urls"] = capo_appstream.types.url_pattern_list.deserialize_cbor(
            data["DeniedUrls"]
        )
    return out
