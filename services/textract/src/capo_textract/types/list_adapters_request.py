"""Generated from Smithy shape ``com.amazonaws.textract#ListAdaptersRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_textract.types.date_time
    import capo_textract.types.max_results
    import capo_textract.types.pagination_token


class ListAdaptersRequest(TypedDict, closed=True):
    after_creation_time: NotRequired["capo_textract.types.date_time.DateTime"]
    """<p>Specifies the lower bound for the ListAdapters operation. Ensures ListAdapters returns only adapters created after the specified creation time.</p>"""
    before_creation_time: NotRequired["capo_textract.types.date_time.DateTime"]
    """<p>Specifies the upper bound for the ListAdapters operation. Ensures ListAdapters returns only adapters created before the specified creation time.</p>"""
    max_results: NotRequired["capo_textract.types.max_results.MaxResults"]
    """<p>The maximum number of results to return when listing adapters.</p>"""
    next_token: NotRequired["capo_textract.types.pagination_token.PaginationToken"]
    """<p>Identifies the next page of results to return when listing adapters.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListAdaptersRequest) -> dict:
    out: dict = {}
    if "after_creation_time" in value:
        import capo_textract.types.date_time

        out["AfterCreationTime"] = capo_textract.types.date_time.serialize_aws_json_1_1(
            value["after_creation_time"]
        )
    if "before_creation_time" in value:
        import capo_textract.types.date_time

        out["BeforeCreationTime"] = (
            capo_textract.types.date_time.serialize_aws_json_1_1(
                value["before_creation_time"]
            )
        )
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListAdaptersRequest:
    out: ListAdaptersRequest = {}  # type: ignore[typeddict-item]
    if data.get("AfterCreationTime") is not None:
        import capo_textract.types.date_time

        out["after_creation_time"] = (
            capo_textract.types.date_time.deserialize_aws_json_1_1(
                data["AfterCreationTime"]
            )
        )
    if data.get("BeforeCreationTime") is not None:
        import capo_textract.types.date_time

        out["before_creation_time"] = (
            capo_textract.types.date_time.deserialize_aws_json_1_1(
                data["BeforeCreationTime"]
            )
        )
    if data.get("MaxResults") is not None:
        out["max_results"] = data["MaxResults"]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ListAdaptersRequest) -> dict:
    out: dict = {}
    if "after_creation_time" in value:
        import capo_textract.types.date_time

        out["AfterCreationTime"] = capo_textract.types.date_time.serialize_cbor(
            value["after_creation_time"]
        )
    if "before_creation_time" in value:
        import capo_textract.types.date_time

        out["BeforeCreationTime"] = capo_textract.types.date_time.serialize_cbor(
            value["before_creation_time"]
        )
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_cbor(data: dict) -> ListAdaptersRequest:
    out: ListAdaptersRequest = {}  # type: ignore[typeddict-item]
    if data.get("AfterCreationTime") is not None:
        import capo_textract.types.date_time

        out["after_creation_time"] = capo_textract.types.date_time.deserialize_cbor(
            data["AfterCreationTime"]
        )
    if data.get("BeforeCreationTime") is not None:
        import capo_textract.types.date_time

        out["before_creation_time"] = capo_textract.types.date_time.deserialize_cbor(
            data["BeforeCreationTime"]
        )
    if data.get("MaxResults") is not None:
        out["max_results"] = data["MaxResults"]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
