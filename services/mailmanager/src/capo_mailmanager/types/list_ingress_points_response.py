"""Generated from Smithy shape ``com.amazonaws.mailmanager#ListIngressPointsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mailmanager.types.ingress_points_list
    import capo_mailmanager.types.pagination_token


class ListIngressPointsResponse(TypedDict, closed=True):
    ingress_points: NotRequired[
        "capo_mailmanager.types.ingress_points_list.IngressPointsList"
    ]
    """<p>The list of ingress endpoints.</p>"""
    next_token: NotRequired["capo_mailmanager.types.pagination_token.PaginationToken"]
    """<p>If NextToken is returned, there are more results available. The value of NextToken is a unique pagination token for each page. Make the call again using the returned token to retrieve the next page.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListIngressPointsResponse) -> dict:
    out: dict = {}
    if "ingress_points" in value:
        import capo_mailmanager.types.ingress_points_list

        out["IngressPoints"] = (
            capo_mailmanager.types.ingress_points_list.serialize_aws_json_1_0(
                value["ingress_points"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ListIngressPointsResponse:
    out: ListIngressPointsResponse = {}  # type: ignore[typeddict-item]
    if data.get("IngressPoints") is not None:
        import capo_mailmanager.types.ingress_points_list

        out["ingress_points"] = (
            capo_mailmanager.types.ingress_points_list.deserialize_aws_json_1_0(
                data["IngressPoints"]
            )
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ListIngressPointsResponse) -> dict:
    out: dict = {}
    if "ingress_points" in value:
        import capo_mailmanager.types.ingress_points_list

        out["IngressPoints"] = (
            capo_mailmanager.types.ingress_points_list.serialize_cbor(
                value["ingress_points"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_cbor(data: dict) -> ListIngressPointsResponse:
    out: ListIngressPointsResponse = {}  # type: ignore[typeddict-item]
    if data.get("IngressPoints") is not None:
        import capo_mailmanager.types.ingress_points_list

        out["ingress_points"] = (
            capo_mailmanager.types.ingress_points_list.deserialize_cbor(
                data["IngressPoints"]
            )
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
