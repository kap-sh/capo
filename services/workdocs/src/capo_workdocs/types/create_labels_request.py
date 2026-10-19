"""Generated from Smithy shape ``com.amazonaws.workdocs#CreateLabelsRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_workdocs.types.authentication_header_type
    import capo_workdocs.types.resource_id_type
    import capo_workdocs.types.shared_labels


class CreateLabelsRequest(TypedDict, closed=True):
    resource_id: "capo_workdocs.types.resource_id_type.ResourceIdType"
    """<p>The ID of the resource.</p>"""
    labels: "capo_workdocs.types.shared_labels.SharedLabels"
    """<p>List of labels to add to the resource.</p>"""
    authentication_token: NotRequired[
        "capo_workdocs.types.authentication_header_type.AuthenticationHeaderType"
    ]
    """<p>Amazon WorkDocs authentication token. Not required when using Amazon Web Services administrator credentials to access the API.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateLabelsRequest) -> dict:
    out: dict = {}
    import capo_workdocs.types.shared_labels

    out["Labels"] = capo_workdocs.types.shared_labels.serialize_json(value["labels"])
    return out


def deserialize_json(data: dict) -> CreateLabelsRequest:
    out: CreateLabelsRequest = {}  # type: ignore[typeddict-item]
    if data.get("Labels") is not None:
        import capo_workdocs.types.shared_labels

        out["labels"] = capo_workdocs.types.shared_labels.deserialize_json(
            data["Labels"]
        )
    else:
        out["labels"] = []
    return out


def redact_sensitive(value: CreateLabelsRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "authentication_token" in value:
        out["authentication_token"] = "*** Sensitive Data Redacted ***"
    return out
