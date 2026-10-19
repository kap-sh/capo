"""Generated from Smithy shape ``com.amazonaws.waf#Predicate``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_waf.types.negated
    import capo_waf.types.predicate_type
    import capo_waf.types.resource_id


class Predicate(TypedDict, closed=True):
    negated: "capo_waf.types.negated.Negated"
    """<p>Set <code>Negated</code> to <code>False</code> if you want AWS WAF to allow, block, or count requests based on the settings in the specified <a>ByteMatchSet</a>, <a>IPSet</a>, <a>SqlInjectionMatchSet</a>, <a>XssMatchSet</a>, <a>RegexMatchSet</a>, <a>GeoMatchSet</a>, or <a>SizeConstraintSet</a>. For example, if an <code>IPSet</code> includes the IP address <code>192.0.2.44</code>, AWS WAF will allow or block requests based on that IP address.</p> <p>Set <code>Negated</code> to <code>True</code> if you want AWS WAF to allow or block a request based on the negation of the settings in the <a>ByteMatchSet</a>, <a>IPSet</a>, <a>SqlInjectionMatchSet</a>, <a>XssMatchSet</a>, <a>RegexMatchSet</a>, <a>GeoMatchSet</a>, or <a>SizeConstraintSet</a>. For example, if an <code>IPSet</code> includes the IP address <code>192.0.2.44</code>, AWS WAF will allow, block, or count requests based on all IP addresses <i>except</i> <code>192.0.2.44</code>.</p>"""
    type: "capo_waf.types.predicate_type.PredicateType"
    """<p>The type of predicate in a <code>Rule</code>, such as <code>ByteMatch</code> or <code>IPSet</code>.</p>"""
    data_id: "capo_waf.types.resource_id.ResourceId"
    """<p>A unique identifier for a predicate in a <code>Rule</code>, such as <code>ByteMatchSetId</code> or <code>IPSetId</code>. The ID is returned by the corresponding <code>Create</code> or <code>List</code> command.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Predicate) -> dict:
    out: dict = {}
    out["Negated"] = value["negated"]
    import capo_waf.types.predicate_type

    out["Type"] = capo_waf.types.predicate_type.serialize_aws_json_1_1(value["type"])
    out["DataId"] = value["data_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> Predicate:
    out: Predicate = {}  # type: ignore[typeddict-item]
    if data.get("Negated") is not None:
        out["negated"] = data["Negated"]
    else:
        out["negated"] = False
    if data.get("Type") is not None:
        import capo_waf.types.predicate_type

        out["type"] = capo_waf.types.predicate_type.deserialize_aws_json_1_1(
            data["Type"]
        )
    else:
        import typing

        out["type"] = typing.cast("capo_waf.types.predicate_type.PredicateType", "")
    if data.get("DataId") is not None:
        out["data_id"] = data["DataId"]
    else:
        out["data_id"] = ""
    return out
