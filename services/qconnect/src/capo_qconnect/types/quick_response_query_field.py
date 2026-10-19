"""Generated from Smithy shape ``com.amazonaws.qconnect#QuickResponseQueryField``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_qconnect.types.non_empty_string
    import capo_qconnect.types.priority
    import capo_qconnect.types.quick_response_query_operator
    import capo_qconnect.types.quick_response_query_value_list


class QuickResponseQueryField(TypedDict, closed=True):
    name: "capo_qconnect.types.non_empty_string.NonEmptyString"
    """<p>The name of the attribute to query the quick responses by.</p>"""
    values: "capo_qconnect.types.quick_response_query_value_list.QuickResponseQueryValueList"
    """<p>The values of the attribute to query the quick responses by.</p>"""
    operator: (
        "capo_qconnect.types.quick_response_query_operator.QuickResponseQueryOperator"
    )
    """<p>The operator to use for matching attribute field values in the query.</p>"""
    allow_fuzziness: NotRequired["bool"]
    """<p>Whether the query expects only exact matches on the attribute field values. The results of the query will only include exact matches if this parameter is set to false.</p>"""
    priority: NotRequired["capo_qconnect.types.priority.Priority"]
    """<p>The importance of the attribute field when calculating query result relevancy scores. The value set for this parameter affects the ordering of search results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: QuickResponseQueryField) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    import capo_qconnect.types.quick_response_query_value_list

    out["values"] = capo_qconnect.types.quick_response_query_value_list.serialize_json(
        value["values"]
    )
    out["operator"] = value["operator"]
    if "allow_fuzziness" in value:
        out["allowFuzziness"] = value["allow_fuzziness"]
    if "priority" in value:
        out["priority"] = value["priority"]
    return out


def deserialize_json(data: dict) -> QuickResponseQueryField:
    out: QuickResponseQueryField = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("values") is not None:
        import capo_qconnect.types.quick_response_query_value_list

        out["values"] = (
            capo_qconnect.types.quick_response_query_value_list.deserialize_json(
                data["values"]
            )
        )
    else:
        out["values"] = []
    if data.get("operator") is not None:
        out["operator"] = data["operator"]
    else:
        out["operator"] = ""
    if data.get("allowFuzziness") is not None:
        out["allow_fuzziness"] = data["allowFuzziness"]
    if data.get("priority") is not None:
        out["priority"] = data["priority"]
    return out
