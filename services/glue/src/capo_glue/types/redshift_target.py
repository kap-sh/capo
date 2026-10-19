"""Generated from Smithy shape ``com.amazonaws.glue#RedshiftTarget``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_glue.types.enclosed_in_string_property
    import capo_glue.types.node_name
    import capo_glue.types.one_input
    import capo_glue.types.upsert_redshift_target_options


class RedshiftTarget(TypedDict, closed=True):
    name: "capo_glue.types.node_name.NodeName"
    """<p>The name of the data target.</p>"""
    inputs: "capo_glue.types.one_input.OneInput"
    """<p>The nodes that are inputs to the data target.</p>"""
    database: "capo_glue.types.enclosed_in_string_property.EnclosedInStringProperty"
    """<p>The name of the database to write to.</p>"""
    table: "capo_glue.types.enclosed_in_string_property.EnclosedInStringProperty"
    """<p>The name of the table in the database to write to.</p>"""
    redshift_tmp_dir: NotRequired[
        "capo_glue.types.enclosed_in_string_property.EnclosedInStringProperty"
    ]
    """<p>The Amazon S3 path where temporary data can be staged when copying out of the database.</p>"""
    tmp_dir_iam_role: NotRequired[
        "capo_glue.types.enclosed_in_string_property.EnclosedInStringProperty"
    ]
    """<p>The IAM role with permissions.</p>"""
    upsert_redshift_options: NotRequired[
        "capo_glue.types.upsert_redshift_target_options.UpsertRedshiftTargetOptions"
    ]
    """<p>The set of options to configure an upsert operation when writing to a Redshift target.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RedshiftTarget) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    import capo_glue.types.one_input

    out["Inputs"] = capo_glue.types.one_input.serialize_aws_json_1_1(value["inputs"])
    out["Database"] = value["database"]
    out["Table"] = value["table"]
    if "redshift_tmp_dir" in value:
        out["RedshiftTmpDir"] = value["redshift_tmp_dir"]
    if "tmp_dir_iam_role" in value:
        out["TmpDirIAMRole"] = value["tmp_dir_iam_role"]
    if "upsert_redshift_options" in value:
        import capo_glue.types.upsert_redshift_target_options

        out["UpsertRedshiftOptions"] = (
            capo_glue.types.upsert_redshift_target_options.serialize_aws_json_1_1(
                value["upsert_redshift_options"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> RedshiftTarget:
    out: RedshiftTarget = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        out["name"] = ""
    if data.get("Inputs") is not None:
        import capo_glue.types.one_input

        out["inputs"] = capo_glue.types.one_input.deserialize_aws_json_1_1(
            data["Inputs"]
        )
    else:
        out["inputs"] = []
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
    if data.get("UpsertRedshiftOptions") is not None:
        import capo_glue.types.upsert_redshift_target_options

        out["upsert_redshift_options"] = (
            capo_glue.types.upsert_redshift_target_options.deserialize_aws_json_1_1(
                data["UpsertRedshiftOptions"]
            )
        )
    return out
