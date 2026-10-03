"""Generated from Smithy shape ``com.amazonaws.ivs#CreatePlaybackRestrictionPolicyRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ivs.types.playback_restriction_policy_allowed_country_list
    import capo_ivs.types.playback_restriction_policy_allowed_origin_list
    import capo_ivs.types.playback_restriction_policy_enable_strict_origin_enforcement
    import capo_ivs.types.playback_restriction_policy_name
    import capo_ivs.types.tags


class CreatePlaybackRestrictionPolicyRequest(TypedDict, closed=True):
    allowed_countries: NotRequired[
        "capo_ivs.types.playback_restriction_policy_allowed_country_list.PlaybackRestrictionPolicyAllowedCountryList"
    ]
    """<p>A list of country codes that control geoblocking restriction. Allowed values are the officially assigned <a href="https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2">ISO 3166-1 alpha-2</a> codes. Default: All countries (an empty array).</p>"""
    allowed_origins: NotRequired[
        "capo_ivs.types.playback_restriction_policy_allowed_origin_list.PlaybackRestrictionPolicyAllowedOriginList"
    ]
    """<p>A list of origin sites that control CORS restriction. Allowed values are the same as valid values of the Origin header defined at <a href="https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Origin">https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Origin</a>. Default: All origins (an empty array).</p>"""
    enable_strict_origin_enforcement: NotRequired[
        "capo_ivs.types.playback_restriction_policy_enable_strict_origin_enforcement.PlaybackRestrictionPolicyEnableStrictOriginEnforcement"
    ]
    """<p>Whether channel playback is constrained by origin site. Default: <code>false</code>.</p>"""
    name: NotRequired[
        "capo_ivs.types.playback_restriction_policy_name.PlaybackRestrictionPolicyName"
    ]
    """<p>Playback-restriction-policy name. The value does not need to be unique.</p>"""
    tags: NotRequired["capo_ivs.types.tags.Tags"]
    """<p>Array of 1-50 maps, each of the form <code>string:string (key:value)</code>. See <a href="https://docs.aws.amazon.com/tag-editor/latest/userguide/best-practices-and-strats.html">Best practices and strategies</a> in <i>Tagging Amazon Web Services Resources and Tag Editor</i> for details, including restrictions that apply to tags and "Tag naming limits and requirements"; Amazon IVS has no service-specific constraints beyond what is documented there.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreatePlaybackRestrictionPolicyRequest) -> dict:
    out: dict = {}
    if "allowed_countries" in value:
        import capo_ivs.types.playback_restriction_policy_allowed_country_list

        out["allowedCountries"] = (
            capo_ivs.types.playback_restriction_policy_allowed_country_list.serialize_json(
                value["allowed_countries"]
            )
        )
    if "allowed_origins" in value:
        import capo_ivs.types.playback_restriction_policy_allowed_origin_list

        out["allowedOrigins"] = (
            capo_ivs.types.playback_restriction_policy_allowed_origin_list.serialize_json(
                value["allowed_origins"]
            )
        )
    if "enable_strict_origin_enforcement" in value:
        out["enableStrictOriginEnforcement"] = value["enable_strict_origin_enforcement"]
    if "name" in value:
        out["name"] = value["name"]
    if "tags" in value:
        import capo_ivs.types.tags

        out["tags"] = capo_ivs.types.tags.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> CreatePlaybackRestrictionPolicyRequest:
    out: CreatePlaybackRestrictionPolicyRequest = {}  # type: ignore[typeddict-item]
    if data.get("allowedCountries") is not None:
        import capo_ivs.types.playback_restriction_policy_allowed_country_list

        out["allowed_countries"] = (
            capo_ivs.types.playback_restriction_policy_allowed_country_list.deserialize_json(
                data["allowedCountries"]
            )
        )
    if data.get("allowedOrigins") is not None:
        import capo_ivs.types.playback_restriction_policy_allowed_origin_list

        out["allowed_origins"] = (
            capo_ivs.types.playback_restriction_policy_allowed_origin_list.deserialize_json(
                data["allowedOrigins"]
            )
        )
    if data.get("enableStrictOriginEnforcement") is not None:
        out["enable_strict_origin_enforcement"] = data["enableStrictOriginEnforcement"]
    if data.get("name") is not None:
        out["name"] = data["name"]
    if data.get("tags") is not None:
        import capo_ivs.types.tags

        out["tags"] = capo_ivs.types.tags.deserialize_json(data["tags"])
    return out
