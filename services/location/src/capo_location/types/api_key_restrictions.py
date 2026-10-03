"""Generated from Smithy shape ``com.amazonaws.location#ApiKeyRestrictions``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_location.errors import DeserializationError

if TYPE_CHECKING:
    import capo_location.types.android_app_list
    import capo_location.types.api_key_action_list
    import capo_location.types.apple_app_list
    import capo_location.types.geo_arn_list
    import capo_location.types.referer_pattern_list


class ApiKeyRestrictions(TypedDict, closed=True):
    allow_actions: "capo_location.types.api_key_action_list.ApiKeyActionList"
    """<p>A list of allowed actions that an API key resource grants permissions to perform. You must have at least one action for each type of resource. For example, if you have a place resource, you must include at least one place action.</p> <p>The following are valid values for the actions.</p> <ul> <li> <p> <b>Map actions</b> </p> <ul> <li> <p> <code>geo:GetMap*</code> - Allows all actions needed for map rendering.</p> </li> <li> <p> <code>geo-maps:GetTile</code> - Allows retrieving map tiles.</p> </li> <li> <p> <code>geo-maps:GetStaticMap</code> - Allows retrieving static map images.</p> </li> <li> <p> <code>geo-maps:*</code> - Allows all actions related to map functionalities.</p> </li> </ul> </li> <li> <p> <b>Place actions</b> </p> <ul> <li> <p> <code>geo:SearchPlaceIndexForText</code> - Allows geocoding.</p> </li> <li> <p> <code>geo:SearchPlaceIndexForPosition</code> - Allows reverse geocoding.</p> </li> <li> <p> <code>geo:SearchPlaceIndexForSuggestions</code> - Allows generating suggestions from text.</p> </li> <li> <p> <code>GetPlace</code> - Allows finding a place by place ID.</p> </li> <li> <p> <code>geo-places:Geocode</code> - Allows geocoding using place information.</p> </li> <li> <p> <code>geo-places:ReverseGeocode</code> - Allows reverse geocoding from location coordinates.</p> </li> <li> <p> <code>geo-places:SearchNearby</code> - Allows searching for places near a location.</p> </li> <li> <p> <code>geo-places:SearchText</code> - Allows searching for places based on text input.</p> </li> <li> <p> <code>geo-places:Autocomplete</code> - Allows auto-completion of place names based on text input.</p> </li> <li> <p> <code>geo-places:Suggest</code> - Allows generating suggestions for places based on partial input.</p> </li> <li> <p> <code>geo-places:GetPlace</code> - Allows finding a place by its ID.</p> </li> <li> <p> <code>geo-places:*</code> - Allows all actions related to place services.</p> </li> </ul> </li> <li> <p> <b>Route actions</b> </p> <ul> <li> <p> <code>geo:CalculateRoute</code> - Allows point to point routing.</p> </li> <li> <p> <code>geo:CalculateRouteMatrix</code> - Allows calculating a matrix of routes.</p> </li> <li> <p> <code>geo-routes:CalculateRoutes</code> - Allows calculating multiple routes between points.</p> </li> <li> <p> <code>geo-routes:CalculateRouteMatrix</code> - Allows calculating a matrix of routes between points.</p> </li> <li> <p> <code>geo-routes:CalculateIsolines</code> - Allows calculating isolines for a given area.</p> </li> <li> <p> <code>geo-routes:OptimizeWaypoints</code> - Allows optimizing the order of waypoints in a route.</p> </li> <li> <p> <code>geo-routes:SnapToRoads</code> - Allows snapping a route to the nearest roads.</p> </li> <li> <p> <code>geo-routes:*</code> - Allows all actions related to routing functionalities.</p> </li> </ul> </li> </ul> <note> <p>You must use these strings exactly. For example, to provide access to map rendering, the only valid action is <code>geo:GetMap*</code> as an input to the list. <code>["geo:GetMap*"]</code> is valid but <code>["geo:GetMapTile"]</code> is not. Similarly, you cannot use <code>["geo:SearchPlaceIndexFor*"]</code> - you must list each of the Place actions separately.</p> </note>"""
    allow_resources: "capo_location.types.geo_arn_list.GeoArnList"
    """<p>A list of allowed resource ARNs that a API key bearer can perform actions on.</p> <ul> <li> <p>The ARN must be the correct ARN for a map, place, or route ARN. You may include wildcards in the resource-id to match multiple resources of the same type.</p> </li> <li> <p>The resources must be in the same <code>partition</code>, <code>region</code>, and <code>account-id</code> as the key that is being created.</p> </li> <li> <p>Other than wildcards, you must include the full ARN, including the <code>arn</code>, <code>partition</code>, <code>service</code>, <code>region</code>, <code>account-id</code> and <code>resource-id</code> delimited by colons (:).</p> </li> <li> <p>No spaces allowed, even with wildcards. For example, <code>arn:aws:geo:region:<i>account-id</i>:map/ExampleMap*</code>.</p> </li> </ul> <p>For more information about ARN format, see <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html">Amazon Resource Names (ARNs)</a>.</p>"""
    allow_referers: NotRequired[
        "capo_location.types.referer_pattern_list.RefererPatternList"
    ]
    r"""<p>An optional list of allowed HTTP referers for which requests must originate from. Requests using this API key from other domains will not be allowed.</p> <p>Requirements:</p> <ul> <li> <p>Contain only alphanumeric characters (A–Z, a–z, 0–9) or any symbols in this list <code>$\-._+!*`(),;/?:@=&amp;</code> </p> </li> <li> <p>May contain a percent (%) if followed by 2 hexadecimal digits (A-F, a-f, 0-9); this is used for URL encoding purposes.</p> </li> <li> <p>May contain wildcard characters question mark (?) and asterisk (*).</p> <p>Question mark (?) will replace any single character (including hexadecimal digits).</p> <p>Asterisk (*) will replace any multiple characters (including multiple hexadecimal digits).</p> </li> <li> <p>No spaces allowed. For example, <code>https://example.com</code>.</p> </li> </ul>"""
    allow_android_apps: NotRequired[
        "capo_location.types.android_app_list.AndroidAppList"
    ]
    """<p>An optional list of allowed Android applications for which requests must originate from. Requests using this API key from other sources will not be allowed.</p>"""
    allow_apple_apps: NotRequired["capo_location.types.apple_app_list.AppleAppList"]
    """<p>An optional list of allowed Apple applications for which requests must originate from. Requests using this API key from other sources will not be allowed.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ApiKeyRestrictions) -> dict:
    out: dict = {}
    import capo_location.types.api_key_action_list

    out["AllowActions"] = capo_location.types.api_key_action_list.serialize_json(
        value["allow_actions"]
    )
    import capo_location.types.geo_arn_list

    out["AllowResources"] = capo_location.types.geo_arn_list.serialize_json(
        value["allow_resources"]
    )
    if "allow_referers" in value:
        import capo_location.types.referer_pattern_list

        out["AllowReferers"] = capo_location.types.referer_pattern_list.serialize_json(
            value["allow_referers"]
        )
    if "allow_android_apps" in value:
        import capo_location.types.android_app_list

        out["AllowAndroidApps"] = capo_location.types.android_app_list.serialize_json(
            value["allow_android_apps"]
        )
    if "allow_apple_apps" in value:
        import capo_location.types.apple_app_list

        out["AllowAppleApps"] = capo_location.types.apple_app_list.serialize_json(
            value["allow_apple_apps"]
        )
    return out


def deserialize_json(data: dict) -> ApiKeyRestrictions:
    out: ApiKeyRestrictions = {}  # type: ignore[typeddict-item]
    if data.get("AllowActions") is not None:
        import capo_location.types.api_key_action_list

        out["allow_actions"] = capo_location.types.api_key_action_list.deserialize_json(
            data["AllowActions"]
        )
    else:
        raise DeserializationError("ApiKeyRestrictions.allow_actions required")
    if data.get("AllowResources") is not None:
        import capo_location.types.geo_arn_list

        out["allow_resources"] = capo_location.types.geo_arn_list.deserialize_json(
            data["AllowResources"]
        )
    else:
        raise DeserializationError("ApiKeyRestrictions.allow_resources required")
    if data.get("AllowReferers") is not None:
        import capo_location.types.referer_pattern_list

        out["allow_referers"] = (
            capo_location.types.referer_pattern_list.deserialize_json(
                data["AllowReferers"]
            )
        )
    if data.get("AllowAndroidApps") is not None:
        import capo_location.types.android_app_list

        out["allow_android_apps"] = (
            capo_location.types.android_app_list.deserialize_json(
                data["AllowAndroidApps"]
            )
        )
    if data.get("AllowAppleApps") is not None:
        import capo_location.types.apple_app_list

        out["allow_apple_apps"] = capo_location.types.apple_app_list.deserialize_json(
            data["AllowAppleApps"]
        )
    return out
