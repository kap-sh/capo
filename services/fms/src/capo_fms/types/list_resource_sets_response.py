"""Generated from Smithy shape ``com.amazonaws.fms#ListResourceSetsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_fms.types.pagination_token
    import capo_fms.types.resource_set_summary_list


class ListResourceSetsResponse(TypedDict, closed=True):
    resource_sets: NotRequired[
        "capo_fms.types.resource_set_summary_list.ResourceSetSummaryList"
    ]
    """<p>An array of <code>ResourceSetSummary</code> objects.</p>"""
    next_token: NotRequired["capo_fms.types.pagination_token.PaginationToken"]
    """<p>When you request a list of objects with a <code>MaxResults</code> setting, if the number of objects that are still available for retrieval exceeds the maximum you requested, Firewall Manager returns a <code>NextToken</code> value in the response. To retrieve the next batch of objects, use the token returned from the prior request in your next request.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListResourceSetsResponse) -> dict:
    out: dict = {}
    if "resource_sets" in value:
        import capo_fms.types.resource_set_summary_list

        out["ResourceSets"] = (
            capo_fms.types.resource_set_summary_list.serialize_aws_json_1_1(
                value["resource_sets"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListResourceSetsResponse:
    out: ListResourceSetsResponse = {}  # type: ignore[typeddict-item]
    if data.get("ResourceSets") is not None:
        import capo_fms.types.resource_set_summary_list

        out["resource_sets"] = (
            capo_fms.types.resource_set_summary_list.deserialize_aws_json_1_1(
                data["ResourceSets"]
            )
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ListResourceSetsResponse) -> dict:
    out: dict = {}
    if "resource_sets" in value:
        import capo_fms.types.resource_set_summary_list

        out["ResourceSets"] = capo_fms.types.resource_set_summary_list.serialize_cbor(
            value["resource_sets"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_cbor(data: dict) -> ListResourceSetsResponse:
    out: ListResourceSetsResponse = {}  # type: ignore[typeddict-item]
    if data.get("ResourceSets") is not None:
        import capo_fms.types.resource_set_summary_list

        out["resource_sets"] = (
            capo_fms.types.resource_set_summary_list.deserialize_cbor(
                data["ResourceSets"]
            )
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
