"""Generated from Smithy shape ``com.amazonaws.rum#AppMonitorConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_rum.types.arn
    import capo_rum.types.favorite_pages
    import capo_rum.types.identity_pool_id
    import capo_rum.types.pages
    import capo_rum.types.session_sample_rate
    import capo_rum.types.telemetries


class AppMonitorConfiguration(TypedDict, closed=True):
    identity_pool_id: NotRequired["capo_rum.types.identity_pool_id.IdentityPoolId"]
    """<p>The ID of the Amazon Cognito identity pool that is used to authorize the sending of data to RUM.</p>"""
    excluded_pages: NotRequired["capo_rum.types.pages.Pages"]
    """<p>A list of URLs in your website or application to exclude from RUM data collection.</p> <p>You can't include both <code>ExcludedPages</code> and <code>IncludedPages</code> in the same operation.</p>"""
    included_pages: NotRequired["capo_rum.types.pages.Pages"]
    """<p>If this app monitor is to collect data from only certain pages in your application, this structure lists those pages. </p> <p>You can't include both <code>ExcludedPages</code> and <code>IncludedPages</code> in the same operation.</p>"""
    favorite_pages: NotRequired["capo_rum.types.favorite_pages.FavoritePages"]
    """<p>A list of pages in your application that are to be displayed with a "favorite" icon in the CloudWatch RUM console.</p>"""
    session_sample_rate: "capo_rum.types.session_sample_rate.SessionSampleRate"
    """<p>Specifies the portion of user sessions to use for RUM data collection. Choosing a higher portion gives you more data but also incurs more costs.</p> <p>The range for this value is 0 to 1 inclusive. Setting this to 1 means that 100% of user sessions are sampled, and setting it to 0.1 means that 10% of user sessions are sampled.</p> <p>If you omit this parameter, the default of 0.1 is used, and 10% of sessions will be sampled.</p>"""
    guest_role_arn: NotRequired["capo_rum.types.arn.Arn"]
    """<p>The ARN of the guest IAM role that is attached to the Amazon Cognito identity pool that is used to authorize the sending of data to RUM.</p> <note> <p>It is possible that an app monitor does not have a value for <code>GuestRoleArn</code>. For example, this can happen when you use the console to create an app monitor and you allow CloudWatch RUM to create a new identity pool for Authorization. In this case, <code>GuestRoleArn</code> is not present in the <a href="https://docs.aws.amazon.com/cloudwatchrum/latest/APIReference/API_GetAppMonitor.html">GetAppMonitor</a> response because it is not stored by the service.</p> <p>If this issue affects you, you can take one of the following steps:</p> <ul> <li> <p>Use the Cloud Development Kit (CDK) to create an identity pool and the associated IAM role, and use that for your app monitor.</p> </li> <li> <p>Make a separate <a href="https://docs.aws.amazon.com/cognitoidentity/latest/APIReference/API_GetIdentityPoolRoles.html">GetIdentityPoolRoles</a> call to Amazon Cognito to retrieve the <code>GuestRoleArn</code>.</p> </li> </ul> </note>"""
    allow_cookies: NotRequired["bool"]
    """<p>If you set this to <code>true</code>, the RUM web client sets two cookies, a session cookie and a user cookie. The cookies allow the RUM web client to collect data relating to the number of users an application has and the behavior of the application across a sequence of events. Cookies are stored in the top-level domain of the current page.</p>"""
    telemetries: NotRequired["capo_rum.types.telemetries.Telemetries"]
    """<p>An array that lists the types of telemetry data that this app monitor is to collect.</p> <ul> <li> <p> <code>errors</code> indicates that RUM collects data about unhandled JavaScript errors raised by your application.</p> </li> <li> <p> <code>performance</code> indicates that RUM collects performance data about how your application and its resources are loaded and rendered. This includes Core Web Vitals.</p> </li> <li> <p> <code>http</code> indicates that RUM collects data about HTTP errors thrown by your application.</p> </li> </ul>"""
    enable_x_ray: NotRequired["bool"]
    """<p>If you set this to <code>true</code>, RUM enables X-Ray tracing for the user sessions that RUM samples. RUM adds an X-Ray trace header to allowed HTTP requests. It also records an X-Ray segment for allowed HTTP requests. You can see traces and segments from these user sessions in the X-Ray console and the CloudWatch ServiceLens console. For more information, see <a href="https://docs.aws.amazon.com/xray/latest/devguide/aws-xray.html">What is X-Ray?</a> </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AppMonitorConfiguration) -> dict:
    out: dict = {}
    if "identity_pool_id" in value:
        out["IdentityPoolId"] = value["identity_pool_id"]
    if "excluded_pages" in value:
        import capo_rum.types.pages

        out["ExcludedPages"] = capo_rum.types.pages.serialize_json(
            value["excluded_pages"]
        )
    if "included_pages" in value:
        import capo_rum.types.pages

        out["IncludedPages"] = capo_rum.types.pages.serialize_json(
            value["included_pages"]
        )
    if "favorite_pages" in value:
        import capo_rum.types.favorite_pages

        out["FavoritePages"] = capo_rum.types.favorite_pages.serialize_json(
            value["favorite_pages"]
        )
    out["SessionSampleRate"] = (
        "NaN"
        if value.get("session_sample_rate", 0) != value.get("session_sample_rate", 0)
        else "Infinity"
        if value.get("session_sample_rate", 0) == float("inf")
        else "-Infinity"
        if value.get("session_sample_rate", 0) == float("-inf")
        else value.get("session_sample_rate", 0)
    )
    if "guest_role_arn" in value:
        out["GuestRoleArn"] = value["guest_role_arn"]
    if "allow_cookies" in value:
        out["AllowCookies"] = value["allow_cookies"]
    if "telemetries" in value:
        import capo_rum.types.telemetries

        out["Telemetries"] = capo_rum.types.telemetries.serialize_json(
            value["telemetries"]
        )
    if "enable_x_ray" in value:
        out["EnableXRay"] = value["enable_x_ray"]
    return out


def deserialize_json(data: dict) -> AppMonitorConfiguration:
    out: AppMonitorConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("IdentityPoolId") is not None:
        out["identity_pool_id"] = data["IdentityPoolId"]
    if data.get("ExcludedPages") is not None:
        import capo_rum.types.pages

        out["excluded_pages"] = capo_rum.types.pages.deserialize_json(
            data["ExcludedPages"]
        )
    if data.get("IncludedPages") is not None:
        import capo_rum.types.pages

        out["included_pages"] = capo_rum.types.pages.deserialize_json(
            data["IncludedPages"]
        )
    if data.get("FavoritePages") is not None:
        import capo_rum.types.favorite_pages

        out["favorite_pages"] = capo_rum.types.favorite_pages.deserialize_json(
            data["FavoritePages"]
        )
    if data.get("SessionSampleRate") is not None:
        out["session_sample_rate"] = float(data["SessionSampleRate"])
    else:
        out["session_sample_rate"] = 0
    if data.get("GuestRoleArn") is not None:
        out["guest_role_arn"] = data["GuestRoleArn"]
    if data.get("AllowCookies") is not None:
        out["allow_cookies"] = data["AllowCookies"]
    if data.get("Telemetries") is not None:
        import capo_rum.types.telemetries

        out["telemetries"] = capo_rum.types.telemetries.deserialize_json(
            data["Telemetries"]
        )
    if data.get("EnableXRay") is not None:
        out["enable_x_ray"] = data["EnableXRay"]
    return out
