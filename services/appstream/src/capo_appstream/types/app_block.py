"""Generated from Smithy shape ``com.amazonaws.appstream#AppBlock``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_appstream.types.app_block_state
    import capo_appstream.types.arn
    import capo_appstream.types.error_details_list
    import capo_appstream.types.packaging_type
    import capo_appstream.types.s3_location
    import capo_appstream.types.script_details
    import capo_appstream.types.string
    import capo_appstream.types.timestamp


class AppBlock(TypedDict, closed=True):
    name: NotRequired["capo_appstream.types.string.String"]
    """<p>The name of the app block.</p>"""
    arn: NotRequired["capo_appstream.types.arn.Arn"]
    """<p>The ARN of the app block.</p>"""
    description: NotRequired["capo_appstream.types.string.String"]
    """<p>The description of the app block.</p>"""
    display_name: NotRequired["capo_appstream.types.string.String"]
    """<p>The display name of the app block.</p>"""
    source_s3_location: NotRequired["capo_appstream.types.s3_location.S3Location"]
    """<p>The source S3 location of the app block.</p>"""
    setup_script_details: NotRequired[
        "capo_appstream.types.script_details.ScriptDetails"
    ]
    """<p>The setup script details of the app block.</p> <p>This only applies to app blocks with PackagingType <code>CUSTOM</code>.</p>"""
    created_time: NotRequired["capo_appstream.types.timestamp.Timestamp"]
    """<p>The created time of the app block.</p>"""
    post_setup_script_details: NotRequired[
        "capo_appstream.types.script_details.ScriptDetails"
    ]
    """<p>The post setup script details of the app block.</p> <p>This only applies to app blocks with PackagingType <code>APPSTREAM2</code>.</p>"""
    packaging_type: NotRequired["capo_appstream.types.packaging_type.PackagingType"]
    """<p>The packaging type of the app block.</p>"""
    state: NotRequired["capo_appstream.types.app_block_state.AppBlockState"]
    """<p>The state of the app block.</p> <p>An app block with WorkSpaces Applications packaging will be in the <code>INACTIVE</code> state if no application package (VHD) is assigned to it. After an application package (VHD) is created by an app block builder for an app block, it becomes <code>ACTIVE</code>. </p> <p>Custom app blocks are always in the <code>ACTIVE</code> state and no action is required to use them.</p>"""
    app_block_errors: NotRequired[
        "capo_appstream.types.error_details_list.ErrorDetailsList"
    ]
    """<p>The errors of the app block.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AppBlock) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "description" in value:
        out["Description"] = value["description"]
    if "display_name" in value:
        out["DisplayName"] = value["display_name"]
    if "source_s3_location" in value:
        import capo_appstream.types.s3_location

        out["SourceS3Location"] = (
            capo_appstream.types.s3_location.serialize_aws_json_1_1(
                value["source_s3_location"]
            )
        )
    if "setup_script_details" in value:
        import capo_appstream.types.script_details

        out["SetupScriptDetails"] = (
            capo_appstream.types.script_details.serialize_aws_json_1_1(
                value["setup_script_details"]
            )
        )
    if "created_time" in value:
        import capo_appstream.types.timestamp

        out["CreatedTime"] = capo_appstream.types.timestamp.serialize_aws_json_1_1(
            value["created_time"]
        )
    if "post_setup_script_details" in value:
        import capo_appstream.types.script_details

        out["PostSetupScriptDetails"] = (
            capo_appstream.types.script_details.serialize_aws_json_1_1(
                value["post_setup_script_details"]
            )
        )
    if "packaging_type" in value:
        import capo_appstream.types.packaging_type

        out["PackagingType"] = (
            capo_appstream.types.packaging_type.serialize_aws_json_1_1(
                value["packaging_type"]
            )
        )
    if "state" in value:
        import capo_appstream.types.app_block_state

        out["State"] = capo_appstream.types.app_block_state.serialize_aws_json_1_1(
            value["state"]
        )
    if "app_block_errors" in value:
        import capo_appstream.types.error_details_list

        out["AppBlockErrors"] = (
            capo_appstream.types.error_details_list.serialize_aws_json_1_1(
                value["app_block_errors"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> AppBlock:
    out: AppBlock = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("Arn") is not None:
        out["arn"] = data["Arn"]
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("DisplayName") is not None:
        out["display_name"] = data["DisplayName"]
    if data.get("SourceS3Location") is not None:
        import capo_appstream.types.s3_location

        out["source_s3_location"] = (
            capo_appstream.types.s3_location.deserialize_aws_json_1_1(
                data["SourceS3Location"]
            )
        )
    if data.get("SetupScriptDetails") is not None:
        import capo_appstream.types.script_details

        out["setup_script_details"] = (
            capo_appstream.types.script_details.deserialize_aws_json_1_1(
                data["SetupScriptDetails"]
            )
        )
    if data.get("CreatedTime") is not None:
        import capo_appstream.types.timestamp

        out["created_time"] = capo_appstream.types.timestamp.deserialize_aws_json_1_1(
            data["CreatedTime"]
        )
    if data.get("PostSetupScriptDetails") is not None:
        import capo_appstream.types.script_details

        out["post_setup_script_details"] = (
            capo_appstream.types.script_details.deserialize_aws_json_1_1(
                data["PostSetupScriptDetails"]
            )
        )
    if data.get("PackagingType") is not None:
        import capo_appstream.types.packaging_type

        out["packaging_type"] = (
            capo_appstream.types.packaging_type.deserialize_aws_json_1_1(
                data["PackagingType"]
            )
        )
    if data.get("State") is not None:
        import capo_appstream.types.app_block_state

        out["state"] = capo_appstream.types.app_block_state.deserialize_aws_json_1_1(
            data["State"]
        )
    if data.get("AppBlockErrors") is not None:
        import capo_appstream.types.error_details_list

        out["app_block_errors"] = (
            capo_appstream.types.error_details_list.deserialize_aws_json_1_1(
                data["AppBlockErrors"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: AppBlock) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "description" in value:
        out["Description"] = value["description"]
    if "display_name" in value:
        out["DisplayName"] = value["display_name"]
    if "source_s3_location" in value:
        import capo_appstream.types.s3_location

        out["SourceS3Location"] = capo_appstream.types.s3_location.serialize_cbor(
            value["source_s3_location"]
        )
    if "setup_script_details" in value:
        import capo_appstream.types.script_details

        out["SetupScriptDetails"] = capo_appstream.types.script_details.serialize_cbor(
            value["setup_script_details"]
        )
    if "created_time" in value:
        import capo_appstream.types.timestamp

        out["CreatedTime"] = capo_appstream.types.timestamp.serialize_cbor(
            value["created_time"]
        )
    if "post_setup_script_details" in value:
        import capo_appstream.types.script_details

        out["PostSetupScriptDetails"] = (
            capo_appstream.types.script_details.serialize_cbor(
                value["post_setup_script_details"]
            )
        )
    if "packaging_type" in value:
        import capo_appstream.types.packaging_type

        out["PackagingType"] = capo_appstream.types.packaging_type.serialize_cbor(
            value["packaging_type"]
        )
    if "state" in value:
        import capo_appstream.types.app_block_state

        out["State"] = capo_appstream.types.app_block_state.serialize_cbor(
            value["state"]
        )
    if "app_block_errors" in value:
        import capo_appstream.types.error_details_list

        out["AppBlockErrors"] = capo_appstream.types.error_details_list.serialize_cbor(
            value["app_block_errors"]
        )
    return out


def deserialize_cbor(data: dict) -> AppBlock:
    out: AppBlock = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("Arn") is not None:
        out["arn"] = data["Arn"]
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("DisplayName") is not None:
        out["display_name"] = data["DisplayName"]
    if data.get("SourceS3Location") is not None:
        import capo_appstream.types.s3_location

        out["source_s3_location"] = capo_appstream.types.s3_location.deserialize_cbor(
            data["SourceS3Location"]
        )
    if data.get("SetupScriptDetails") is not None:
        import capo_appstream.types.script_details

        out["setup_script_details"] = (
            capo_appstream.types.script_details.deserialize_cbor(
                data["SetupScriptDetails"]
            )
        )
    if data.get("CreatedTime") is not None:
        import capo_appstream.types.timestamp

        out["created_time"] = capo_appstream.types.timestamp.deserialize_cbor(
            data["CreatedTime"]
        )
    if data.get("PostSetupScriptDetails") is not None:
        import capo_appstream.types.script_details

        out["post_setup_script_details"] = (
            capo_appstream.types.script_details.deserialize_cbor(
                data["PostSetupScriptDetails"]
            )
        )
    if data.get("PackagingType") is not None:
        import capo_appstream.types.packaging_type

        out["packaging_type"] = capo_appstream.types.packaging_type.deserialize_cbor(
            data["PackagingType"]
        )
    if data.get("State") is not None:
        import capo_appstream.types.app_block_state

        out["state"] = capo_appstream.types.app_block_state.deserialize_cbor(
            data["State"]
        )
    if data.get("AppBlockErrors") is not None:
        import capo_appstream.types.error_details_list

        out["app_block_errors"] = (
            capo_appstream.types.error_details_list.deserialize_cbor(
                data["AppBlockErrors"]
            )
        )
    return out
