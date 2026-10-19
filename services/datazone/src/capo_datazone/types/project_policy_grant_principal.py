"""Generated from Smithy shape ``com.amazonaws.datazone#ProjectPolicyGrantPrincipal``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_datazone.types.project_designation
    import capo_datazone.types.project_grant_filter
    import capo_datazone.types.project_id


class ProjectPolicyGrantPrincipal(TypedDict, closed=True):
    project_designation: "capo_datazone.types.project_designation.ProjectDesignation"
    """<p>The project designation of the project policy grant principal.</p>"""
    project_identifier: NotRequired["capo_datazone.types.project_id.ProjectId"]
    """<p>The project ID of the project policy grant principal.</p>"""
    project_grant_filter: NotRequired[
        "capo_datazone.types.project_grant_filter.ProjectGrantFilter"
    ]
    """<p>The project grant filter of the project policy grant principal.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ProjectPolicyGrantPrincipal) -> dict:
    out: dict = {}
    import capo_datazone.types.project_designation

    out["projectDesignation"] = capo_datazone.types.project_designation.serialize_json(
        value["project_designation"]
    )
    if "project_identifier" in value:
        out["projectIdentifier"] = value["project_identifier"]
    if "project_grant_filter" in value:
        import capo_datazone.types.project_grant_filter

        out["projectGrantFilter"] = (
            capo_datazone.types.project_grant_filter.serialize_json(
                value["project_grant_filter"]
            )
        )
    return out


def deserialize_json(data: dict) -> ProjectPolicyGrantPrincipal:
    out: ProjectPolicyGrantPrincipal = {}  # type: ignore[typeddict-item]
    if data.get("projectDesignation") is not None:
        import capo_datazone.types.project_designation

        out["project_designation"] = (
            capo_datazone.types.project_designation.deserialize_json(
                data["projectDesignation"]
            )
        )
    else:
        import typing

        out["project_designation"] = typing.cast(
            "capo_datazone.types.project_designation.ProjectDesignation", ""
        )
    if data.get("projectIdentifier") is not None:
        out["project_identifier"] = data["projectIdentifier"]
    if data.get("projectGrantFilter") is not None:
        import capo_datazone.types.project_grant_filter

        out["project_grant_filter"] = (
            capo_datazone.types.project_grant_filter.deserialize_json(
                data["projectGrantFilter"]
            )
        )
    return out
