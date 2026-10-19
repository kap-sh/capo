"""Generated from Smithy shape ``com.amazonaws.qconnect#RetrieveRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

from capo_qconnect.errors import DeserializationError

if TYPE_CHECKING:
    import capo_qconnect.types.non_empty_sensitive_string
    import capo_qconnect.types.retrieval_configuration
    import capo_qconnect.types.uuid_or_arn


class RetrieveRequest(TypedDict, closed=True):
    assistant_id: "capo_qconnect.types.uuid_or_arn.UuidOrArn"
    """<p>The identifier of the Amazon Q in Connect assistant for content retrieval.</p>"""
    retrieval_configuration: (
        "capo_qconnect.types.retrieval_configuration.RetrievalConfiguration"
    )
    """<p>The configuration for the content retrieval operation.</p>"""
    retrieval_query: (
        "capo_qconnect.types.non_empty_sensitive_string.NonEmptySensitiveString"
    )
    """<p>The query for content retrieval.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RetrieveRequest) -> dict:
    out: dict = {}
    import capo_qconnect.types.retrieval_configuration

    out["retrievalConfiguration"] = (
        capo_qconnect.types.retrieval_configuration.serialize_json(
            value["retrieval_configuration"]
        )
    )
    out["retrievalQuery"] = value["retrieval_query"]
    return out


def deserialize_json(data: dict) -> RetrieveRequest:
    out: RetrieveRequest = {}  # type: ignore[typeddict-item]
    if data.get("retrievalConfiguration") is not None:
        import capo_qconnect.types.retrieval_configuration

        out["retrieval_configuration"] = (
            capo_qconnect.types.retrieval_configuration.deserialize_json(
                data["retrievalConfiguration"]
            )
        )
    else:
        raise DeserializationError("RetrieveRequest.retrieval_configuration required")
    if data.get("retrievalQuery") is not None:
        out["retrieval_query"] = data["retrievalQuery"]
    else:
        out["retrieval_query"] = ""
    return out


def redact_sensitive(value: RetrieveRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "retrieval_configuration" in value:
        import capo_qconnect.types.retrieval_configuration

        out["retrieval_configuration"] = (
            capo_qconnect.types.retrieval_configuration.redact_sensitive(
                value["retrieval_configuration"]
            )
        )
    if "retrieval_query" in value:
        out["retrieval_query"] = "*** Sensitive Data Redacted ***"
    return out
