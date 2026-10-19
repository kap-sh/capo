"""Generated from Smithy shape ``com.amazonaws.waf#SqlInjectionMatchSetUpdate``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_waf.errors import DeserializationError

if TYPE_CHECKING:
    import capo_waf.types.change_action
    import capo_waf.types.sql_injection_match_tuple


class SqlInjectionMatchSetUpdate(TypedDict, closed=True):
    action: "capo_waf.types.change_action.ChangeAction"
    """<p>Specify <code>INSERT</code> to add a <a>SqlInjectionMatchSetUpdate</a> to a <a>SqlInjectionMatchSet</a>. Use <code>DELETE</code> to remove a <code>SqlInjectionMatchSetUpdate</code> from a <code>SqlInjectionMatchSet</code>.</p>"""
    sql_injection_match_tuple: (
        "capo_waf.types.sql_injection_match_tuple.SqlInjectionMatchTuple"
    )
    """<p>Specifies the part of a web request that you want AWS WAF to inspect for snippets of malicious SQL code and, if you want AWS WAF to inspect a header, the name of the header.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SqlInjectionMatchSetUpdate) -> dict:
    out: dict = {}
    import capo_waf.types.change_action

    out["Action"] = capo_waf.types.change_action.serialize_aws_json_1_1(value["action"])
    import capo_waf.types.sql_injection_match_tuple

    out["SqlInjectionMatchTuple"] = (
        capo_waf.types.sql_injection_match_tuple.serialize_aws_json_1_1(
            value["sql_injection_match_tuple"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> SqlInjectionMatchSetUpdate:
    out: SqlInjectionMatchSetUpdate = {}  # type: ignore[typeddict-item]
    if data.get("Action") is not None:
        import capo_waf.types.change_action

        out["action"] = capo_waf.types.change_action.deserialize_aws_json_1_1(
            data["Action"]
        )
    else:
        import typing

        out["action"] = typing.cast("capo_waf.types.change_action.ChangeAction", "")
    if data.get("SqlInjectionMatchTuple") is not None:
        import capo_waf.types.sql_injection_match_tuple

        out["sql_injection_match_tuple"] = (
            capo_waf.types.sql_injection_match_tuple.deserialize_aws_json_1_1(
                data["SqlInjectionMatchTuple"]
            )
        )
    else:
        raise DeserializationError(
            "SqlInjectionMatchSetUpdate.sql_injection_match_tuple required"
        )
    return out
