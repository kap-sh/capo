"""Generated from Smithy shape ``com.amazonaws.customerprofiles#CreateSegmentEstimateRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_customer_profiles.types.name
    import capo_customer_profiles.types.segment_group_structure
    import capo_customer_profiles.types.sensitive_string1_to50000


class CreateSegmentEstimateRequest(TypedDict, closed=True):
    domain_name: "capo_customer_profiles.types.name.name"
    """<p>The unique name of the domain.</p>"""
    segment_query: NotRequired[
        "capo_customer_profiles.types.segment_group_structure.SegmentGroupStructure"
    ]
    """<p>The segment query for calculating a segment estimate.</p>"""
    segment_sql_query: NotRequired[
        "capo_customer_profiles.types.sensitive_string1_to50000.sensitiveString1To50000"
    ]
    """<p>The segment SQL query.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateSegmentEstimateRequest) -> dict:
    out: dict = {}
    if "segment_query" in value:
        import capo_customer_profiles.types.segment_group_structure

        out["SegmentQuery"] = (
            capo_customer_profiles.types.segment_group_structure.serialize_json(
                value["segment_query"]
            )
        )
    if "segment_sql_query" in value:
        out["SegmentSqlQuery"] = value["segment_sql_query"]
    return out


def deserialize_json(data: dict) -> CreateSegmentEstimateRequest:
    out: CreateSegmentEstimateRequest = {}  # type: ignore[typeddict-item]
    if data.get("SegmentQuery") is not None:
        import capo_customer_profiles.types.segment_group_structure

        out["segment_query"] = (
            capo_customer_profiles.types.segment_group_structure.deserialize_json(
                data["SegmentQuery"]
            )
        )
    if data.get("SegmentSqlQuery") is not None:
        out["segment_sql_query"] = data["SegmentSqlQuery"]
    return out


def redact_sensitive(value: CreateSegmentEstimateRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "segment_query" in value:
        import capo_customer_profiles.types.segment_group_structure

        out["segment_query"] = (
            capo_customer_profiles.types.segment_group_structure.redact_sensitive(
                value["segment_query"]
            )
        )
    if "segment_sql_query" in value:
        out["segment_sql_query"] = "*** Sensitive Data Redacted ***"
    return out
