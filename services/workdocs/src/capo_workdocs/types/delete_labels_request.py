"""Generated from Smithy shape ``com.amazonaws.workdocs#DeleteLabelsRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_workdocs.types.authentication_header_type
    import capo_workdocs.types.boolean_type
    import capo_workdocs.types.resource_id_type
    import capo_workdocs.types.shared_labels


class DeleteLabelsRequest(TypedDict, closed=True):
    resource_id: "capo_workdocs.types.resource_id_type.ResourceIdType"
    """<p>The ID of the resource.</p>"""
    authentication_token: NotRequired[
        "capo_workdocs.types.authentication_header_type.AuthenticationHeaderType"
    ]
    """<p>Amazon WorkDocs authentication token. Not required when using Amazon Web Services administrator credentials to access the API.</p>"""
    labels: NotRequired["capo_workdocs.types.shared_labels.SharedLabels"]
    """<p>List of labels to delete from the resource.</p>"""
    delete_all: "capo_workdocs.types.boolean_type.BooleanType"
    """<p>Flag to request removal of all labels from the specified resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteLabelsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteLabelsRequest:
    out: DeleteLabelsRequest = {}  # type: ignore[typeddict-item]
    return out


def redact_sensitive(value: DeleteLabelsRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "authentication_token" in value:
        out["authentication_token"] = "*** Sensitive Data Redacted ***"
    return out
