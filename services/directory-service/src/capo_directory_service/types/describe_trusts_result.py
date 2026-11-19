"""Generated from Smithy shape ``com.amazonaws.directoryservice#DescribeTrustsResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_directory_service.types.next_token
    import capo_directory_service.types.trusts


class DescribeTrustsResult(TypedDict, closed=True):
    trusts: NotRequired["capo_directory_service.types.trusts.Trusts"]
    """<p>The list of Trust objects that were retrieved.</p> <p>It is possible that this list contains less than the number of items specified in the <i>Limit</i> member of the request. This occurs if there are less than the requested number of items left to retrieve, or if the limitations of the operation have been exceeded.</p>"""
    next_token: NotRequired["capo_directory_service.types.next_token.NextToken"]
    """<p>If not null, more results are available. Pass this value for the <i>NextToken</i> parameter in a subsequent call to <a>DescribeTrusts</a> to retrieve the next set of items.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeTrustsResult) -> dict:
    out: dict = {}
    if "trusts" in value:
        import capo_directory_service.types.trusts

        out["Trusts"] = capo_directory_service.types.trusts.serialize_aws_json_1_1(
            value["trusts"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeTrustsResult:
    out: DescribeTrustsResult = {}  # type: ignore[typeddict-item]
    if data.get("Trusts") is not None:
        import capo_directory_service.types.trusts

        out["trusts"] = capo_directory_service.types.trusts.deserialize_aws_json_1_1(
            data["Trusts"]
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DescribeTrustsResult) -> dict:
    out: dict = {}
    if "trusts" in value:
        import capo_directory_service.types.trusts

        out["Trusts"] = capo_directory_service.types.trusts.serialize_cbor(
            value["trusts"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_cbor(data: dict) -> DescribeTrustsResult:
    out: DescribeTrustsResult = {}  # type: ignore[typeddict-item]
    if data.get("Trusts") is not None:
        import capo_directory_service.types.trusts

        out["trusts"] = capo_directory_service.types.trusts.deserialize_cbor(
            data["Trusts"]
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
