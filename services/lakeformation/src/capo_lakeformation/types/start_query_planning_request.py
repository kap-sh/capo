"""Generated from Smithy shape ``com.amazonaws.lakeformation#StartQueryPlanningRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

from capo_lakeformation.errors import DeserializationError

if TYPE_CHECKING:
    import capo_lakeformation.types.query_planning_context
    import capo_lakeformation.types.synthetic_start_query_planning_request_query_string


class StartQueryPlanningRequest(TypedDict, closed=True):
    query_planning_context: (
        "capo_lakeformation.types.query_planning_context.QueryPlanningContext"
    )
    """<p>A structure containing information about the query plan.</p>"""
    query_string: "capo_lakeformation.types.synthetic_start_query_planning_request_query_string.SyntheticStartQueryPlanningRequestQueryString"
    """<p>A PartiQL query statement used as an input to the planner service.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartQueryPlanningRequest) -> dict:
    out: dict = {}
    import capo_lakeformation.types.query_planning_context

    out["QueryPlanningContext"] = (
        capo_lakeformation.types.query_planning_context.serialize_json(
            value["query_planning_context"]
        )
    )
    out["QueryString"] = value["query_string"]
    return out


def deserialize_json(data: dict) -> StartQueryPlanningRequest:
    out: StartQueryPlanningRequest = {}  # type: ignore[typeddict-item]
    if data.get("QueryPlanningContext") is not None:
        import capo_lakeformation.types.query_planning_context

        out["query_planning_context"] = (
            capo_lakeformation.types.query_planning_context.deserialize_json(
                data["QueryPlanningContext"]
            )
        )
    else:
        raise DeserializationError(
            "StartQueryPlanningRequest.query_planning_context required"
        )
    if data.get("QueryString") is not None:
        out["query_string"] = data["QueryString"]
    else:
        raise DeserializationError("StartQueryPlanningRequest.query_string required")
    return out


def redact_sensitive(value: StartQueryPlanningRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "query_string" in value:
        out["query_string"] = "*** Sensitive Data Redacted ***"
    return out
