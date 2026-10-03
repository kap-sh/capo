"""Generated from Smithy shape ``com.amazonaws.wafv2#GeoMatchStatement``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_wafv2.types.country_codes
    import capo_wafv2.types.forwarded_ip_config


class GeoMatchStatement(TypedDict, closed=True):
    country_codes: NotRequired["capo_wafv2.types.country_codes.CountryCodes"]
    """<p>An array of two-character country codes that you want to match against, for example, <code>[ "US", "CN" ]</code>, from the alpha-2 country ISO codes of the ISO 3166 international standard. </p> <p>When you use a geo match statement just for the region and country labels that it adds to requests, you still have to supply a country code for the rule to evaluate. In this case, you configure the rule to only count matching requests, but it will still generate logging and count metrics for any matches. You can reduce the logging and metrics that the rule produces by specifying a country that's unlikely to be a source of traffic to your site.</p>"""
    forwarded_ip_config: NotRequired[
        "capo_wafv2.types.forwarded_ip_config.ForwardedIPConfig"
    ]
    """<p>The configuration for inspecting IP addresses in an HTTP header that you specify, instead of using the IP address that's reported by the web request origin. Commonly, this is the X-Forwarded-For (XFF) header, but you can specify any header name. </p> <note> <p>If the specified header isn't present in the request, WAF doesn't apply the rule to the web request at all.</p> </note>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GeoMatchStatement) -> dict:
    out: dict = {}
    if "country_codes" in value:
        import capo_wafv2.types.country_codes

        out["CountryCodes"] = capo_wafv2.types.country_codes.serialize_aws_json_1_1(
            value["country_codes"]
        )
    if "forwarded_ip_config" in value:
        import capo_wafv2.types.forwarded_ip_config

        out["ForwardedIPConfig"] = (
            capo_wafv2.types.forwarded_ip_config.serialize_aws_json_1_1(
                value["forwarded_ip_config"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GeoMatchStatement:
    out: GeoMatchStatement = {}  # type: ignore[typeddict-item]
    if data.get("CountryCodes") is not None:
        import capo_wafv2.types.country_codes

        out["country_codes"] = capo_wafv2.types.country_codes.deserialize_aws_json_1_1(
            data["CountryCodes"]
        )
    if data.get("ForwardedIPConfig") is not None:
        import capo_wafv2.types.forwarded_ip_config

        out["forwarded_ip_config"] = (
            capo_wafv2.types.forwarded_ip_config.deserialize_aws_json_1_1(
                data["ForwardedIPConfig"]
            )
        )
    return out
