"""Generated from Smithy shape ``com.amazonaws.directoryservice#DescribeTrustsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_directory_service.types.directory_id
    import capo_directory_service.types.limit
    import capo_directory_service.types.next_token
    import capo_directory_service.types.trust_ids


class DescribeTrustsRequest(TypedDict, closed=True):
    directory_id: NotRequired["capo_directory_service.types.directory_id.DirectoryId"]
    """<p>The Directory ID of the Amazon Web Services directory that is a part of the requested trust relationship.</p>"""
    trust_ids: NotRequired["capo_directory_service.types.trust_ids.TrustIds"]
    """<p>A list of identifiers of the trust relationships for which to obtain the information. If this member is null, all trust relationships that belong to the current account are returned.</p> <p>An empty list results in an <code>InvalidParameterException</code> being thrown.</p>"""
    next_token: NotRequired["capo_directory_service.types.next_token.NextToken"]
    """<p>The <i>DescribeTrustsResult.NextToken</i> value from a previous call to <a>DescribeTrusts</a>. Pass null if this is the first call.</p>"""
    limit: NotRequired["capo_directory_service.types.limit.Limit"]
    """<p>The maximum number of objects to return.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeTrustsRequest) -> dict:
    out: dict = {}
    if "directory_id" in value:
        out["DirectoryId"] = value["directory_id"]
    if "trust_ids" in value:
        import capo_directory_service.types.trust_ids

        out["TrustIds"] = capo_directory_service.types.trust_ids.serialize_aws_json_1_1(
            value["trust_ids"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "limit" in value:
        out["Limit"] = value["limit"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeTrustsRequest:
    out: DescribeTrustsRequest = {}  # type: ignore[typeddict-item]
    if data.get("DirectoryId") is not None:
        out["directory_id"] = data["DirectoryId"]
    if data.get("TrustIds") is not None:
        import capo_directory_service.types.trust_ids

        out["trust_ids"] = (
            capo_directory_service.types.trust_ids.deserialize_aws_json_1_1(
                data["TrustIds"]
            )
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    if data.get("Limit") is not None:
        out["limit"] = data["Limit"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DescribeTrustsRequest) -> dict:
    out: dict = {}
    if "directory_id" in value:
        out["DirectoryId"] = value["directory_id"]
    if "trust_ids" in value:
        import capo_directory_service.types.trust_ids

        out["TrustIds"] = capo_directory_service.types.trust_ids.serialize_cbor(
            value["trust_ids"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "limit" in value:
        out["Limit"] = value["limit"]
    return out


def deserialize_cbor(data: dict) -> DescribeTrustsRequest:
    out: DescribeTrustsRequest = {}  # type: ignore[typeddict-item]
    if data.get("DirectoryId") is not None:
        out["directory_id"] = data["DirectoryId"]
    if data.get("TrustIds") is not None:
        import capo_directory_service.types.trust_ids

        out["trust_ids"] = capo_directory_service.types.trust_ids.deserialize_cbor(
            data["TrustIds"]
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    if data.get("Limit") is not None:
        out["limit"] = data["Limit"]
    return out
