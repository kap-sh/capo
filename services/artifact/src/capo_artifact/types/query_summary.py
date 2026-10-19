"""Generated from Smithy shape ``com.amazonaws.artifact#QuerySummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_artifact.types.citation_list
    import capo_artifact.types.long_string_attribute
    import capo_artifact.types.query_status
    import capo_artifact.types.query_status_message
    import capo_artifact.types.response_version_list
    import capo_artifact.types.review_type
    import capo_artifact.types.timestamp_attribute


class QuerySummary(TypedDict, closed=True):
    query_identifier: "int"
    """<p>Sequential identifier of the query within the inquiry.</p>"""
    query: "capo_artifact.types.long_string_attribute.LongStringAttribute"
    """<p>The actual query text.</p>"""
    response: NotRequired[
        "capo_artifact.types.long_string_attribute.LongStringAttribute"
    ]
    """<p>Generated response to the query.</p>"""
    review_type: NotRequired["capo_artifact.types.review_type.ReviewType"]
    """<p>Type of review for the response.</p>"""
    citations: NotRequired["capo_artifact.types.citation_list.CitationList"]
    """<p>Supporting citations for the response.</p>"""
    status: "capo_artifact.types.query_status.QueryStatus"
    """<p>Current processing status of the query.</p>"""
    status_message: "capo_artifact.types.query_status_message.QueryStatusMessage"
    """<p>Descriptive status message.</p>"""
    created_at: "capo_artifact.types.timestamp_attribute.TimestampAttribute"
    """<p>Timestamp when the query was created.</p>"""
    updated_response_versions: NotRequired[
        "capo_artifact.types.response_version_list.ResponseVersionList"
    ]
    """<p>Ordered list of response version history entries, oldest first.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: QuerySummary) -> dict:
    out: dict = {}
    out["queryIdentifier"] = value["query_identifier"]
    out["query"] = value["query"]
    if "response" in value:
        out["response"] = value["response"]
    if "review_type" in value:
        import capo_artifact.types.review_type

        out["reviewType"] = capo_artifact.types.review_type.serialize_json(
            value["review_type"]
        )
    if "citations" in value:
        import capo_artifact.types.citation_list

        out["citations"] = capo_artifact.types.citation_list.serialize_json(
            value["citations"]
        )
    import capo_artifact.types.query_status

    out["status"] = capo_artifact.types.query_status.serialize_json(value["status"])
    import capo_artifact.types.query_status_message

    out["statusMessage"] = capo_artifact.types.query_status_message.serialize_json(
        value["status_message"]
    )
    import capo_artifact.types.timestamp_attribute

    out["createdAt"] = capo_artifact.types.timestamp_attribute.serialize_json(
        value["created_at"]
    )
    if "updated_response_versions" in value:
        import capo_artifact.types.response_version_list

        out["updatedResponseVersions"] = (
            capo_artifact.types.response_version_list.serialize_json(
                value["updated_response_versions"]
            )
        )
    return out


def deserialize_json(data: dict) -> QuerySummary:
    out: QuerySummary = {}  # type: ignore[typeddict-item]
    if data.get("queryIdentifier") is not None:
        out["query_identifier"] = data["queryIdentifier"]
    else:
        out["query_identifier"] = 0
    if data.get("query") is not None:
        out["query"] = data["query"]
    else:
        out["query"] = ""
    if data.get("response") is not None:
        out["response"] = data["response"]
    if data.get("reviewType") is not None:
        import capo_artifact.types.review_type

        out["review_type"] = capo_artifact.types.review_type.deserialize_json(
            data["reviewType"]
        )
    if data.get("citations") is not None:
        import capo_artifact.types.citation_list

        out["citations"] = capo_artifact.types.citation_list.deserialize_json(
            data["citations"]
        )
    if data.get("status") is not None:
        import capo_artifact.types.query_status

        out["status"] = capo_artifact.types.query_status.deserialize_json(
            data["status"]
        )
    else:
        import typing

        out["status"] = typing.cast("capo_artifact.types.query_status.QueryStatus", "")
    if data.get("statusMessage") is not None:
        import capo_artifact.types.query_status_message

        out["status_message"] = (
            capo_artifact.types.query_status_message.deserialize_json(
                data["statusMessage"]
            )
        )
    else:
        import typing

        out["status_message"] = typing.cast(
            "capo_artifact.types.query_status_message.QueryStatusMessage", ""
        )
    if data.get("createdAt") is not None:
        import capo_artifact.types.timestamp_attribute

        out["created_at"] = capo_artifact.types.timestamp_attribute.deserialize_json(
            data["createdAt"]
        )
    else:
        import datetime

        out["created_at"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    if data.get("updatedResponseVersions") is not None:
        import capo_artifact.types.response_version_list

        out["updated_response_versions"] = (
            capo_artifact.types.response_version_list.deserialize_json(
                data["updatedResponseVersions"]
            )
        )
    return out
