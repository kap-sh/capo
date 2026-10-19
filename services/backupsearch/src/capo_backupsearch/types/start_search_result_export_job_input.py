"""Generated from Smithy shape ``com.amazonaws.backupsearch#StartSearchResultExportJobInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_backupsearch.types.export_specification
    import capo_backupsearch.types.generic_id
    import capo_backupsearch.types.iam_role_arn
    import capo_backupsearch.types.tag_map


class StartSearchResultExportJobInput(TypedDict, closed=True):
    search_job_identifier: "capo_backupsearch.types.generic_id.GenericId"
    """<p>The unique string that specifies the search job.</p>"""
    export_specification: (
        "capo_backupsearch.types.export_specification.ExportSpecification"
    )
    """<p>This specification contains a required string of the destination bucket; optionally, you can include the destination prefix.</p>"""
    client_token: NotRequired["str"]
    """<p>Include this parameter to allow multiple identical calls for idempotency.</p> <p>A client token is valid for 8 hours after the first request that uses it is completed. After this time, any request with the same token is treated as a new request.</p>"""
    tags: NotRequired["capo_backupsearch.types.tag_map.TagMap"]
    """<p>Optional tags to include. A tag is a key-value pair you can use to manage, filter, and search for your resources. Allowed characters include UTF-8 letters, numbers, spaces, and the following characters: + - = . _ : /. </p>"""
    role_arn: NotRequired["capo_backupsearch.types.iam_role_arn.IamRoleArn"]
    """<p>This parameter specifies the role ARN used to start the search results export jobs.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartSearchResultExportJobInput) -> dict:
    out: dict = {}
    out["SearchJobIdentifier"] = value["search_job_identifier"]
    import capo_backupsearch.types.export_specification

    out["ExportSpecification"] = (
        capo_backupsearch.types.export_specification.serialize_json(
            value["export_specification"]
        )
    )
    if "client_token" in value:
        out["ClientToken"] = value["client_token"]
    if "tags" in value:
        import capo_backupsearch.types.tag_map

        out["Tags"] = capo_backupsearch.types.tag_map.serialize_json(value["tags"])
    if "role_arn" in value:
        out["RoleArn"] = value["role_arn"]
    return out


def deserialize_json(data: dict) -> StartSearchResultExportJobInput:
    out: StartSearchResultExportJobInput = {}  # type: ignore[typeddict-item]
    if data.get("SearchJobIdentifier") is not None:
        out["search_job_identifier"] = data["SearchJobIdentifier"]
    else:
        out["search_job_identifier"] = ""
    if data.get("ExportSpecification") is not None:
        import capo_backupsearch.types.export_specification

        out["export_specification"] = (
            capo_backupsearch.types.export_specification.deserialize_json(
                data["ExportSpecification"]
            )
        )
    else:
        import capo_backupsearch.types._unknown

        out["export_specification"] = (
            capo_backupsearch.types._unknown.UnknownUnionMember("")
        )
    if data.get("ClientToken") is not None:
        out["client_token"] = data["ClientToken"]
    if data.get("Tags") is not None:
        import capo_backupsearch.types.tag_map

        out["tags"] = capo_backupsearch.types.tag_map.deserialize_json(data["Tags"])
    if data.get("RoleArn") is not None:
        out["role_arn"] = data["RoleArn"]
    return out
