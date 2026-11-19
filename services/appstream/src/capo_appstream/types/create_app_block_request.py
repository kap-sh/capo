"""Generated from Smithy shape ``com.amazonaws.appstream#CreateAppBlockRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_appstream.types.description
    import capo_appstream.types.display_name
    import capo_appstream.types.name
    import capo_appstream.types.packaging_type
    import capo_appstream.types.s3_location
    import capo_appstream.types.script_details
    import capo_appstream.types.tags


class CreateAppBlockRequest(TypedDict, closed=True):
    name: NotRequired["capo_appstream.types.name.Name"]
    """<p>The name of the app block.</p>"""
    description: NotRequired["capo_appstream.types.description.Description"]
    """<p>The description of the app block.</p>"""
    display_name: NotRequired["capo_appstream.types.display_name.DisplayName"]
    """<p>The display name of the app block. This is not displayed to the user.</p>"""
    source_s3_location: NotRequired["capo_appstream.types.s3_location.S3Location"]
    """<p>The source S3 location of the app block.</p>"""
    setup_script_details: NotRequired[
        "capo_appstream.types.script_details.ScriptDetails"
    ]
    """<p>The setup script details of the app block. This must be provided for the <code>CUSTOM</code> PackagingType.</p>"""
    tags: NotRequired["capo_appstream.types.tags.Tags"]
    """<p>The tags assigned to the app block.</p>"""
    post_setup_script_details: NotRequired[
        "capo_appstream.types.script_details.ScriptDetails"
    ]
    """<p>The post setup script details of the app block. This can only be provided for the <code>APPSTREAM2</code> PackagingType.</p>"""
    packaging_type: NotRequired["capo_appstream.types.packaging_type.PackagingType"]
    """<p>The packaging type of the app block.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateAppBlockRequest) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
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
    if "tags" in value:
        import capo_appstream.types.tags

        out["Tags"] = capo_appstream.types.tags.serialize_aws_json_1_1(value["tags"])
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
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateAppBlockRequest:
    out: CreateAppBlockRequest = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
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
    if data.get("Tags") is not None:
        import capo_appstream.types.tags

        out["tags"] = capo_appstream.types.tags.deserialize_aws_json_1_1(data["Tags"])
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
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: CreateAppBlockRequest) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
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
    if "tags" in value:
        import capo_appstream.types.tags

        out["Tags"] = capo_appstream.types.tags.serialize_cbor(value["tags"])
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
    return out


def deserialize_cbor(data: dict) -> CreateAppBlockRequest:
    out: CreateAppBlockRequest = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
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
    if data.get("Tags") is not None:
        import capo_appstream.types.tags

        out["tags"] = capo_appstream.types.tags.deserialize_cbor(data["Tags"])
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
    return out
