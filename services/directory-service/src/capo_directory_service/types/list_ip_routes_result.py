"""Generated from Smithy shape ``com.amazonaws.directoryservice#ListIpRoutesResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_directory_service.types.ip_routes_info
    import capo_directory_service.types.next_token


class ListIpRoutesResult(TypedDict, closed=True):
    ip_routes_info: NotRequired[
        "capo_directory_service.types.ip_routes_info.IpRoutesInfo"
    ]
    """<p>A list of <a>IpRoute</a>s.</p>"""
    next_token: NotRequired["capo_directory_service.types.next_token.NextToken"]
    """<p>If not null, more results are available. Pass this value for the <i>NextToken</i> parameter in a subsequent call to <a>ListIpRoutes</a> to retrieve the next set of items.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListIpRoutesResult) -> dict:
    out: dict = {}
    if "ip_routes_info" in value:
        import capo_directory_service.types.ip_routes_info

        out["IpRoutesInfo"] = (
            capo_directory_service.types.ip_routes_info.serialize_aws_json_1_1(
                value["ip_routes_info"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListIpRoutesResult:
    out: ListIpRoutesResult = {}  # type: ignore[typeddict-item]
    if data.get("IpRoutesInfo") is not None:
        import capo_directory_service.types.ip_routes_info

        out["ip_routes_info"] = (
            capo_directory_service.types.ip_routes_info.deserialize_aws_json_1_1(
                data["IpRoutesInfo"]
            )
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ListIpRoutesResult) -> dict:
    out: dict = {}
    if "ip_routes_info" in value:
        import capo_directory_service.types.ip_routes_info

        out["IpRoutesInfo"] = (
            capo_directory_service.types.ip_routes_info.serialize_cbor(
                value["ip_routes_info"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_cbor(data: dict) -> ListIpRoutesResult:
    out: ListIpRoutesResult = {}  # type: ignore[typeddict-item]
    if data.get("IpRoutesInfo") is not None:
        import capo_directory_service.types.ip_routes_info

        out["ip_routes_info"] = (
            capo_directory_service.types.ip_routes_info.deserialize_cbor(
                data["IpRoutesInfo"]
            )
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
