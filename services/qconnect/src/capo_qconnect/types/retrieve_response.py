"""Generated from Smithy shape ``com.amazonaws.qconnect#RetrieveResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_qconnect.types.retrieve_error_list
    import capo_qconnect.types.retrieve_result_list


class RetrieveResponse(TypedDict, closed=True):
    results: "capo_qconnect.types.retrieve_result_list.RetrieveResultList"
    """<p>The results of the content retrieval operation.</p>"""
    errors: NotRequired["capo_qconnect.types.retrieve_error_list.RetrieveErrorList"]
    """<p>The per-association errors returned when one or more knowledge base associations fail during a <code>Retrieve</code> operation that spans multiple assistant associations. The overall operation still succeeds and returns the results from the associations that were queried successfully. This list contains one entry for each association that failed, up to a maximum of five.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RetrieveResponse) -> dict:
    out: dict = {}
    import capo_qconnect.types.retrieve_result_list

    out["results"] = capo_qconnect.types.retrieve_result_list.serialize_json(
        value["results"]
    )
    if "errors" in value:
        import capo_qconnect.types.retrieve_error_list

        out["errors"] = capo_qconnect.types.retrieve_error_list.serialize_json(
            value["errors"]
        )
    return out


def deserialize_json(data: dict) -> RetrieveResponse:
    out: RetrieveResponse = {}  # type: ignore[typeddict-item]
    if data.get("results") is not None:
        import capo_qconnect.types.retrieve_result_list

        out["results"] = capo_qconnect.types.retrieve_result_list.deserialize_json(
            data["results"]
        )
    else:
        out["results"] = []
    if data.get("errors") is not None:
        import capo_qconnect.types.retrieve_error_list

        out["errors"] = capo_qconnect.types.retrieve_error_list.deserialize_json(
            data["errors"]
        )
    return out


def redact_sensitive(value: RetrieveResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "results" in value:
        import capo_qconnect.types.retrieve_result_list

        out["results"] = capo_qconnect.types.retrieve_result_list.redact_sensitive(
            value["results"]
        )
    return out
