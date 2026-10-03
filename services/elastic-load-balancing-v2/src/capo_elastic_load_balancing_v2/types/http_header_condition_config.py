"""Generated from Smithy shape ``com.amazonaws.elasticloadbalancingv2#HttpHeaderConditionConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_elastic_load_balancing_v2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_elastic_load_balancing_v2.types.http_header_condition_name
    import capo_elastic_load_balancing_v2.types.list_of_string


class HttpHeaderConditionConfig(TypedDict, closed=True):
    http_header_name: NotRequired[
        "capo_elastic_load_balancing_v2.types.http_header_condition_name.HttpHeaderConditionName"
    ]
    """<p>The name of the HTTP header field. The maximum length is 40 characters. The header name is case insensitive. The allowed characters are specified by RFC 7230. Wildcards are not supported.</p> <p>You can't use an HTTP header condition to specify the host header. Instead, use a <a href="https://docs.aws.amazon.com/elasticloadbalancing/latest/application/load-balancer-listeners.html#host-conditions">host condition</a>.</p>"""
    values: NotRequired[
        "capo_elastic_load_balancing_v2.types.list_of_string.ListOfString"
    ]
    """<p>The strings to compare against the value of the HTTP header. The maximum length of each string is 128 characters. The comparison strings are case insensitive. The following wildcard characters are supported: * (matches 0 or more characters) and ? (matches exactly 1 character).</p> <p>If the same header appears multiple times in the request, we search them in order until a match is found.</p> <p>If you specify multiple strings, the condition is satisfied if one of the strings matches the value of the HTTP header. To require that all of the strings are a match, create one condition per string.</p>"""
    regex_values: NotRequired[
        "capo_elastic_load_balancing_v2.types.list_of_string.ListOfString"
    ]
    """<p>The regular expression to compare against the HTTP header. The maximum length of each string is 128 characters.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: HttpHeaderConditionConfig, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "http_header_name" in value:
        pairs.append((f"{key_prefix}HttpHeaderName", str(value["http_header_name"])))
    if "values" in value:
        import capo_elastic_load_balancing_v2.types.list_of_string

        capo_elastic_load_balancing_v2.types.list_of_string.serialize_query(
            value["values"], pairs, f"{key_prefix}Values"
        )
    if "regex_values" in value:
        import capo_elastic_load_balancing_v2.types.list_of_string

        capo_elastic_load_balancing_v2.types.list_of_string.serialize_query(
            value["regex_values"], pairs, f"{key_prefix}RegexValues"
        )


def deserialize_query(el: Element) -> HttpHeaderConditionConfig:
    out: HttpHeaderConditionConfig = {}  # type: ignore[typeddict-item]
    child_http_header_name = el.find("HttpHeaderName")
    if child_http_header_name is not None:
        out["http_header_name"] = str(child_http_header_name.text or "")
    child_values = el.find("Values")
    if child_values is not None:
        import capo_elastic_load_balancing_v2.types.list_of_string

        out["values"] = (
            capo_elastic_load_balancing_v2.types.list_of_string.deserialize_query(
                child_values
            )
        )
    child_regex_values = el.find("RegexValues")
    if child_regex_values is not None:
        import capo_elastic_load_balancing_v2.types.list_of_string

        out["regex_values"] = (
            capo_elastic_load_balancing_v2.types.list_of_string.deserialize_query(
                child_regex_values
            )
        )
    return out
