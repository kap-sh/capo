"""Generated from Smithy shape ``com.amazonaws.kendra#UpdateThesaurusRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_kendra.types.description
    import capo_kendra.types.index_id
    import capo_kendra.types.role_arn
    import capo_kendra.types.s3_path
    import capo_kendra.types.thesaurus_id
    import capo_kendra.types.thesaurus_name


class UpdateThesaurusRequest(TypedDict, closed=True):
    id: "capo_kendra.types.thesaurus_id.ThesaurusId"
    """<p>The identifier of the thesaurus you want to update.</p>"""
    name: NotRequired["capo_kendra.types.thesaurus_name.ThesaurusName"]
    """<p>A new name for the thesaurus.</p>"""
    index_id: "capo_kendra.types.index_id.IndexId"
    """<p>The identifier of the index for the thesaurus.</p>"""
    description: NotRequired["capo_kendra.types.description.Description"]
    """<p>A new description for the thesaurus.</p>"""
    role_arn: NotRequired["capo_kendra.types.role_arn.RoleArn"]
    """<p>An IAM role that gives Amazon Kendra permissions to access thesaurus file specified in <code>SourceS3Path</code>.</p>"""
    source_s3_path: NotRequired["capo_kendra.types.s3_path.S3Path"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateThesaurusRequest) -> dict:
    out: dict = {}
    out["Id"] = value["id"]
    if "name" in value:
        out["Name"] = value["name"]
    out["IndexId"] = value["index_id"]
    if "description" in value:
        out["Description"] = value["description"]
    if "role_arn" in value:
        out["RoleArn"] = value["role_arn"]
    if "source_s3_path" in value:
        import capo_kendra.types.s3_path

        out["SourceS3Path"] = capo_kendra.types.s3_path.serialize_aws_json_1_1(
            value["source_s3_path"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateThesaurusRequest:
    out: UpdateThesaurusRequest = {}  # type: ignore[typeddict-item]
    if data.get("Id") is not None:
        out["id"] = data["Id"]
    else:
        out["id"] = ""
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("IndexId") is not None:
        out["index_id"] = data["IndexId"]
    else:
        out["index_id"] = ""
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("RoleArn") is not None:
        out["role_arn"] = data["RoleArn"]
    if data.get("SourceS3Path") is not None:
        import capo_kendra.types.s3_path

        out["source_s3_path"] = capo_kendra.types.s3_path.deserialize_aws_json_1_1(
            data["SourceS3Path"]
        )
    return out
