"""Generated from Smithy shape ``com.amazonaws.glue#RedshiftSource``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_glue.types.enclosed_in_string_property
    import capo_glue.types.node_name


class RedshiftSource(TypedDict, closed=True):
    name: "capo_glue.types.node_name.NodeName"
    """<p>The name of the Amazon Redshift data store.</p>"""
    database: "capo_glue.types.enclosed_in_string_property.EnclosedInStringProperty"
    """<p>The database to read from.</p>"""
    table: "capo_glue.types.enclosed_in_string_property.EnclosedInStringProperty"
    """<p>The database table to read from.</p>"""
    redshift_tmp_dir: NotRequired[
        "capo_glue.types.enclosed_in_string_property.EnclosedInStringProperty"
    ]
    """<p>The Amazon S3 path where temporary data can be staged when copying out of the database.</p>"""
    tmp_dir_iam_role: NotRequired[
        "capo_glue.types.enclosed_in_string_property.EnclosedInStringProperty"
    ]
    """<p>The IAM role with permissions.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RedshiftSource) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    out["Database"] = value["database"]
    out["Table"] = value["table"]
    if "redshift_tmp_dir" in value:
        out["RedshiftTmpDir"] = value["redshift_tmp_dir"]
    if "tmp_dir_iam_role" in value:
        out["TmpDirIAMRole"] = value["tmp_dir_iam_role"]
    return out


def deserialize_aws_json_1_1(data: dict) -> RedshiftSource:
    out: RedshiftSource = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        out["name"] = ""
    if data.get("Database") is not None:
        out["database"] = data["Database"]
    else:
        out["database"] = ""
    if data.get("Table") is not None:
        out["table"] = data["Table"]
    else:
        out["table"] = ""
    if data.get("RedshiftTmpDir") is not None:
        out["redshift_tmp_dir"] = data["RedshiftTmpDir"]
    if data.get("TmpDirIAMRole") is not None:
        out["tmp_dir_iam_role"] = data["TmpDirIAMRole"]
    return out
