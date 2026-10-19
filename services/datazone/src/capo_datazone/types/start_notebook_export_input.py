"""Generated from Smithy shape ``com.amazonaws.datazone#StartNotebookExportInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_datazone.types.client_token
    import capo_datazone.types.domain_id
    import capo_datazone.types.file_format
    import capo_datazone.types.notebook_id
    import capo_datazone.types.project_id


class StartNotebookExportInput(TypedDict, closed=True):
    domain_identifier: "capo_datazone.types.domain_id.DomainId"
    """<p>The identifier of the Amazon SageMaker Unified Studio domain in which to export the notebook.</p>"""
    notebook_identifier: "capo_datazone.types.notebook_id.NotebookId"
    """<p>The identifier of the notebook to export.</p>"""
    owning_project_identifier: "capo_datazone.types.project_id.ProjectId"
    """<p>The identifier of the project that owns the notebook.</p>"""
    file_format: "capo_datazone.types.file_format.FileFormat"
    """<p>The file format for the notebook export. Valid values are <code>PDF</code> and <code>IPYNB</code>.</p>"""
    client_token: NotRequired["capo_datazone.types.client_token.ClientToken"]
    """<p>A unique, case-sensitive identifier to ensure idempotency of the request. This field is automatically populated if not provided.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartNotebookExportInput) -> dict:
    out: dict = {}
    out["notebookIdentifier"] = value["notebook_identifier"]
    out["owningProjectIdentifier"] = value["owning_project_identifier"]
    import capo_datazone.types.file_format

    out["fileFormat"] = capo_datazone.types.file_format.serialize_json(
        value["file_format"]
    )
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    return out


def deserialize_json(data: dict) -> StartNotebookExportInput:
    out: StartNotebookExportInput = {}  # type: ignore[typeddict-item]
    if data.get("notebookIdentifier") is not None:
        out["notebook_identifier"] = data["notebookIdentifier"]
    else:
        out["notebook_identifier"] = ""
    if data.get("owningProjectIdentifier") is not None:
        out["owning_project_identifier"] = data["owningProjectIdentifier"]
    else:
        out["owning_project_identifier"] = ""
    if data.get("fileFormat") is not None:
        import capo_datazone.types.file_format

        out["file_format"] = capo_datazone.types.file_format.deserialize_json(
            data["fileFormat"]
        )
    else:
        import typing

        out["file_format"] = typing.cast(
            "capo_datazone.types.file_format.FileFormat", ""
        )
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    return out
