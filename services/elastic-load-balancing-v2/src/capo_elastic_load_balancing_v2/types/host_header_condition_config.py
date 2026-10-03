"""Generated from Smithy shape ``com.amazonaws.elasticloadbalancingv2#HostHeaderConditionConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_elastic_load_balancing_v2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_elastic_load_balancing_v2.types.list_of_string


class HostHeaderConditionConfig(TypedDict, closed=True):
    values: NotRequired[
        "capo_elastic_load_balancing_v2.types.list_of_string.ListOfString"
    ]
    """<p>The host names. The maximum length of each string is 128 characters. The comparison is case insensitive. The following wildcard characters are supported: * (matches 0 or more characters) and ? (matches exactly 1 character). You must include at least one "." character. You can include only alphabetical characters after the final "." character.</p> <p>If you specify multiple strings, the condition is satisfied if one of the strings matches the host name.</p>"""
    regex_values: NotRequired[
        "capo_elastic_load_balancing_v2.types.list_of_string.ListOfString"
    ]
    """<p>The regular expressions to compare against the host header. The maximum length of each string is 128 characters.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: HostHeaderConditionConfig, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
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


def deserialize_query(el: Element) -> HostHeaderConditionConfig:
    out: HostHeaderConditionConfig = {}  # type: ignore[typeddict-item]
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
