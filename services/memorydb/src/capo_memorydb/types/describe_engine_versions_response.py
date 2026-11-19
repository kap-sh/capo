"""Generated from Smithy shape ``com.amazonaws.memorydb#DescribeEngineVersionsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_memorydb.types.engine_version_info_list
    import capo_memorydb.types.string


class DescribeEngineVersionsResponse(TypedDict, closed=True):
    next_token: NotRequired["capo_memorydb.types.string.String"]
    """<p>An optional argument to pass in case the total number of records exceeds the value of MaxResults. If nextToken is returned, there are more results available. The value of nextToken is a unique pagination token for each page. Make the call again using the returned token to retrieve the next page. Keep all other arguments unchanged. </p>"""
    engine_versions: NotRequired[
        "capo_memorydb.types.engine_version_info_list.EngineVersionInfoList"
    ]
    """<p>A list of engine version details. Each element in the list contains detailed information about one engine version.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeEngineVersionsResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "engine_versions" in value:
        import capo_memorydb.types.engine_version_info_list

        out["EngineVersions"] = (
            capo_memorydb.types.engine_version_info_list.serialize_aws_json_1_1(
                value["engine_versions"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeEngineVersionsResponse:
    out: DescribeEngineVersionsResponse = {}  # type: ignore[typeddict-item]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    if data.get("EngineVersions") is not None:
        import capo_memorydb.types.engine_version_info_list

        out["engine_versions"] = (
            capo_memorydb.types.engine_version_info_list.deserialize_aws_json_1_1(
                data["EngineVersions"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DescribeEngineVersionsResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "engine_versions" in value:
        import capo_memorydb.types.engine_version_info_list

        out["EngineVersions"] = (
            capo_memorydb.types.engine_version_info_list.serialize_cbor(
                value["engine_versions"]
            )
        )
    return out


def deserialize_cbor(data: dict) -> DescribeEngineVersionsResponse:
    out: DescribeEngineVersionsResponse = {}  # type: ignore[typeddict-item]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    if data.get("EngineVersions") is not None:
        import capo_memorydb.types.engine_version_info_list

        out["engine_versions"] = (
            capo_memorydb.types.engine_version_info_list.deserialize_cbor(
                data["EngineVersions"]
            )
        )
    return out
