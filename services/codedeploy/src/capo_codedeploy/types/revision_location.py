"""Generated from Smithy shape ``com.amazonaws.codedeploy#RevisionLocation``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codedeploy.types.app_spec_content
    import capo_codedeploy.types.git_hub_location
    import capo_codedeploy.types.raw_string
    import capo_codedeploy.types.revision_location_type
    import capo_codedeploy.types.s3_location


class RevisionLocation(TypedDict, closed=True):
    revision_type: NotRequired[
        "capo_codedeploy.types.revision_location_type.RevisionLocationType"
    ]
    """<p>The type of application revision:</p> <ul> <li> <p>S3: An application revision stored in Amazon S3.</p> </li> <li> <p>GitHub: An application revision stored in GitHub (EC2/On-premises deployments only).</p> </li> <li> <p>String: A YAML-formatted or JSON-formatted string (Lambda deployments only).</p> </li> <li> <p>AppSpecContent: An <code>AppSpecContent</code> object that contains the contents of an AppSpec file for an Lambda or Amazon ECS deployment. The content is formatted as JSON or YAML stored as a RawString.</p> </li> </ul>"""
    s3_location: NotRequired["capo_codedeploy.types.s3_location.S3Location"]
    """<p>Information about the location of a revision stored in Amazon S3. </p>"""
    git_hub_location: NotRequired[
        "capo_codedeploy.types.git_hub_location.GitHubLocation"
    ]
    """<p>Information about the location of application artifacts stored in GitHub.</p>"""
    string: NotRequired["capo_codedeploy.types.raw_string.RawString"]
    """<p>Information about the location of an Lambda deployment revision stored as a RawString.</p>"""
    app_spec_content: NotRequired[
        "capo_codedeploy.types.app_spec_content.AppSpecContent"
    ]
    """<p> The content of an AppSpec file for an Lambda or Amazon ECS deployment. The content is formatted as JSON or YAML and stored as a RawString. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RevisionLocation) -> dict:
    out: dict = {}
    if "revision_type" in value:
        import capo_codedeploy.types.revision_location_type

        out["revisionType"] = (
            capo_codedeploy.types.revision_location_type.serialize_aws_json_1_1(
                value["revision_type"]
            )
        )
    if "s3_location" in value:
        import capo_codedeploy.types.s3_location

        out["s3Location"] = capo_codedeploy.types.s3_location.serialize_aws_json_1_1(
            value["s3_location"]
        )
    if "git_hub_location" in value:
        import capo_codedeploy.types.git_hub_location

        out["gitHubLocation"] = (
            capo_codedeploy.types.git_hub_location.serialize_aws_json_1_1(
                value["git_hub_location"]
            )
        )
    if "string" in value:
        import capo_codedeploy.types.raw_string

        out["string"] = capo_codedeploy.types.raw_string.serialize_aws_json_1_1(
            value["string"]
        )
    if "app_spec_content" in value:
        import capo_codedeploy.types.app_spec_content

        out["appSpecContent"] = (
            capo_codedeploy.types.app_spec_content.serialize_aws_json_1_1(
                value["app_spec_content"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> RevisionLocation:
    out: RevisionLocation = {}  # type: ignore[typeddict-item]
    if data.get("revisionType") is not None:
        import capo_codedeploy.types.revision_location_type

        out["revision_type"] = (
            capo_codedeploy.types.revision_location_type.deserialize_aws_json_1_1(
                data["revisionType"]
            )
        )
    if data.get("s3Location") is not None:
        import capo_codedeploy.types.s3_location

        out["s3_location"] = capo_codedeploy.types.s3_location.deserialize_aws_json_1_1(
            data["s3Location"]
        )
    if data.get("gitHubLocation") is not None:
        import capo_codedeploy.types.git_hub_location

        out["git_hub_location"] = (
            capo_codedeploy.types.git_hub_location.deserialize_aws_json_1_1(
                data["gitHubLocation"]
            )
        )
    if data.get("string") is not None:
        import capo_codedeploy.types.raw_string

        out["string"] = capo_codedeploy.types.raw_string.deserialize_aws_json_1_1(
            data["string"]
        )
    if data.get("appSpecContent") is not None:
        import capo_codedeploy.types.app_spec_content

        out["app_spec_content"] = (
            capo_codedeploy.types.app_spec_content.deserialize_aws_json_1_1(
                data["appSpecContent"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: RevisionLocation) -> dict:
    out: dict = {}
    if "revision_type" in value:
        import capo_codedeploy.types.revision_location_type

        out["revisionType"] = (
            capo_codedeploy.types.revision_location_type.serialize_cbor(
                value["revision_type"]
            )
        )
    if "s3_location" in value:
        import capo_codedeploy.types.s3_location

        out["s3Location"] = capo_codedeploy.types.s3_location.serialize_cbor(
            value["s3_location"]
        )
    if "git_hub_location" in value:
        import capo_codedeploy.types.git_hub_location

        out["gitHubLocation"] = capo_codedeploy.types.git_hub_location.serialize_cbor(
            value["git_hub_location"]
        )
    if "string" in value:
        import capo_codedeploy.types.raw_string

        out["string"] = capo_codedeploy.types.raw_string.serialize_cbor(value["string"])
    if "app_spec_content" in value:
        import capo_codedeploy.types.app_spec_content

        out["appSpecContent"] = capo_codedeploy.types.app_spec_content.serialize_cbor(
            value["app_spec_content"]
        )
    return out


def deserialize_cbor(data: dict) -> RevisionLocation:
    out: RevisionLocation = {}  # type: ignore[typeddict-item]
    if data.get("revisionType") is not None:
        import capo_codedeploy.types.revision_location_type

        out["revision_type"] = (
            capo_codedeploy.types.revision_location_type.deserialize_cbor(
                data["revisionType"]
            )
        )
    if data.get("s3Location") is not None:
        import capo_codedeploy.types.s3_location

        out["s3_location"] = capo_codedeploy.types.s3_location.deserialize_cbor(
            data["s3Location"]
        )
    if data.get("gitHubLocation") is not None:
        import capo_codedeploy.types.git_hub_location

        out["git_hub_location"] = (
            capo_codedeploy.types.git_hub_location.deserialize_cbor(
                data["gitHubLocation"]
            )
        )
    if data.get("string") is not None:
        import capo_codedeploy.types.raw_string

        out["string"] = capo_codedeploy.types.raw_string.deserialize_cbor(
            data["string"]
        )
    if data.get("appSpecContent") is not None:
        import capo_codedeploy.types.app_spec_content

        out["app_spec_content"] = (
            capo_codedeploy.types.app_spec_content.deserialize_cbor(
                data["appSpecContent"]
            )
        )
    return out
