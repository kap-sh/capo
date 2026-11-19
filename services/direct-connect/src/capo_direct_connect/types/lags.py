"""Generated from Smithy shape ``com.amazonaws.directconnect#Lags``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_direct_connect.types.lag_list
    import capo_direct_connect.types.pagination_token


class Lags(TypedDict, closed=True):
    lags: NotRequired["capo_direct_connect.types.lag_list.LagList"]
    """<p>The LAGs.</p>"""
    next_token: NotRequired[
        "capo_direct_connect.types.pagination_token.PaginationToken"
    ]
    """<p>The token to use to retrieve the next page of results. This value is <code>null</code> when there are no more results to return.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Lags) -> dict:
    out: dict = {}
    if "lags" in value:
        import capo_direct_connect.types.lag_list

        out["lags"] = capo_direct_connect.types.lag_list.serialize_aws_json_1_1(
            value["lags"]
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> Lags:
    out: Lags = {}  # type: ignore[typeddict-item]
    if data.get("lags") is not None:
        import capo_direct_connect.types.lag_list

        out["lags"] = capo_direct_connect.types.lag_list.deserialize_aws_json_1_1(
            data["lags"]
        )
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: Lags) -> dict:
    out: dict = {}
    if "lags" in value:
        import capo_direct_connect.types.lag_list

        out["lags"] = capo_direct_connect.types.lag_list.serialize_cbor(value["lags"])
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_cbor(data: dict) -> Lags:
    out: Lags = {}  # type: ignore[typeddict-item]
    if data.get("lags") is not None:
        import capo_direct_connect.types.lag_list

        out["lags"] = capo_direct_connect.types.lag_list.deserialize_cbor(data["lags"])
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
