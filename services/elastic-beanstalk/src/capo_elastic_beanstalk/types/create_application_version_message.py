"""Generated from Smithy shape ``com.amazonaws.elasticbeanstalk#CreateApplicationVersionMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_elastic_beanstalk._protocol.xml import Element

if TYPE_CHECKING:
    import capo_elastic_beanstalk.types.application_name
    import capo_elastic_beanstalk.types.application_version_proccess
    import capo_elastic_beanstalk.types.auto_create_application
    import capo_elastic_beanstalk.types.build_configuration
    import capo_elastic_beanstalk.types.description
    import capo_elastic_beanstalk.types.image_configuration
    import capo_elastic_beanstalk.types.s3_location
    import capo_elastic_beanstalk.types.source_build_information
    import capo_elastic_beanstalk.types.tags
    import capo_elastic_beanstalk.types.version_label


class CreateApplicationVersionMessage(TypedDict, closed=True):
    application_name: "capo_elastic_beanstalk.types.application_name.ApplicationName"
    """<p> The name of the application. If no application is found with this name, and <code>AutoCreateApplication</code> is <code>false</code>, returns an <code>InvalidParameterValue</code> error. </p>"""
    version_label: "capo_elastic_beanstalk.types.version_label.VersionLabel"
    """<p>A label identifying this version.</p> <p>Constraint: Must be unique per application. If an application version already exists with this label for the specified application, Elastic Beanstalk returns an <code>InvalidParameterValue</code> error. </p>"""
    description: NotRequired["capo_elastic_beanstalk.types.description.Description"]
    """<p>A description of this application version.</p>"""
    source_build_information: NotRequired[
        "capo_elastic_beanstalk.types.source_build_information.SourceBuildInformation"
    ]
    """<p>Specify a commit in an CodeCommit Git repository to use as the source code for the application version.</p>"""
    source_bundle: NotRequired["capo_elastic_beanstalk.types.s3_location.S3Location"]
    """<p>The Amazon S3 bucket and key that identify the location of the source bundle for this version.</p> <note> <p>The Amazon S3 bucket must be in the same region as the environment.</p> <p>Unless you're specifying a source bundle in the bucket that Elastic Beanstalk manages in your account, you must assign a custom policy to your user, and grant <code>Allow</code> permission to the <code>s3:Get*</code> actions on your S3 object resource, for example, <code>arn:aws:s3:::your-bucket/your-source-bundle-object</code>.</p> </note> <p>Specify a source bundle in Amazon S3 or a commit in an CodeCommit repository (with <code>SourceBuildInformation</code>), but not both. If neither <code>SourceBundle</code> nor <code>SourceBuildInformation</code> are provided, Elastic Beanstalk uses a sample application.</p>"""
    build_configuration: NotRequired[
        "capo_elastic_beanstalk.types.build_configuration.BuildConfiguration"
    ]
    """<p>Settings for an CodeBuild build.</p> <p>Don't specify <code>BuildConfiguration</code> together with <code>ImageConfiguration</code>, which configures a container image build instead.</p>"""
    auto_create_application: NotRequired[
        "capo_elastic_beanstalk.types.auto_create_application.AutoCreateApplication"
    ]
    """<p>Set to <code>true</code> to create an application with the specified name if it doesn't already exist.</p>"""
    process: NotRequired[
        "capo_elastic_beanstalk.types.application_version_proccess.ApplicationVersionProccess"
    ]
    """<p>Pre-processes and validates the environment manifest (<code>env.yaml</code>) and configuration files (<code>*.config</code> files in the <code>.ebextensions</code> folder) in the source bundle. Validating configuration files can identify issues prior to deploying the application version to an environment.</p> <p>You must turn processing on for application versions that you create using CodeBuild or CodeCommit. For application versions built from a source bundle in Amazon S3, processing is optional.</p> <note> <p>The <code>Process</code> option validates Elastic Beanstalk configuration files. It doesn't validate your application's configuration files, like proxy server or Docker configuration.</p> </note>"""
    tags: NotRequired["capo_elastic_beanstalk.types.tags.Tags"]
    """<p>Specifies the tags applied to the application version.</p> <p>Elastic Beanstalk applies these tags only to the application version. Environments that use the application version don't inherit the tags.</p>"""
    image_configuration: NotRequired[
        "capo_elastic_beanstalk.types.image_configuration.ImageConfiguration"
    ]
    """<p>The source of the container image for this application version. You can specify an image that you built and pushed to a container registry yourself, or settings for Elastic Beanstalk to build one from your source bundle. Specify exactly one of the <code>Source</code> and <code>Build</code> members.</p> <p>Don't specify <code>ImageConfiguration</code> together with <code>BuildConfiguration</code>, which configures an CodeBuild build instead.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: CreateApplicationVersionMessage, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    pairs.append((f"{key_prefix}ApplicationName", str(value["application_name"])))
    pairs.append((f"{key_prefix}VersionLabel", str(value["version_label"])))
    if "description" in value:
        pairs.append((f"{key_prefix}Description", str(value["description"])))
    if "source_build_information" in value:
        import capo_elastic_beanstalk.types.source_build_information

        capo_elastic_beanstalk.types.source_build_information.serialize_query(
            value["source_build_information"],
            pairs,
            f"{key_prefix}SourceBuildInformation",
        )
    if "source_bundle" in value:
        import capo_elastic_beanstalk.types.s3_location

        capo_elastic_beanstalk.types.s3_location.serialize_query(
            value["source_bundle"], pairs, f"{key_prefix}SourceBundle"
        )
    if "build_configuration" in value:
        import capo_elastic_beanstalk.types.build_configuration

        capo_elastic_beanstalk.types.build_configuration.serialize_query(
            value["build_configuration"], pairs, f"{key_prefix}BuildConfiguration"
        )
    if "auto_create_application" in value:
        pairs.append(
            (
                f"{key_prefix}AutoCreateApplication",
                "true" if value["auto_create_application"] else "false",
            )
        )
    if "process" in value:
        pairs.append((f"{key_prefix}Process", "true" if value["process"] else "false"))
    if "tags" in value:
        import capo_elastic_beanstalk.types.tags

        capo_elastic_beanstalk.types.tags.serialize_query(
            value["tags"], pairs, f"{key_prefix}Tags"
        )
    if "image_configuration" in value:
        import capo_elastic_beanstalk.types.image_configuration

        capo_elastic_beanstalk.types.image_configuration.serialize_query(
            value["image_configuration"], pairs, f"{key_prefix}ImageConfiguration"
        )


def deserialize_query(el: Element) -> CreateApplicationVersionMessage:
    out: CreateApplicationVersionMessage = {}  # type: ignore[typeddict-item]
    child_application_name = el.find("ApplicationName")
    if child_application_name is not None:
        out["application_name"] = str(child_application_name.text or "")
    else:
        out["application_name"] = ""
    child_version_label = el.find("VersionLabel")
    if child_version_label is not None:
        out["version_label"] = str(child_version_label.text or "")
    else:
        out["version_label"] = ""
    child_description = el.find("Description")
    if child_description is not None:
        out["description"] = str(child_description.text or "")
    child_source_build_information = el.find("SourceBuildInformation")
    if child_source_build_information is not None:
        import capo_elastic_beanstalk.types.source_build_information

        out["source_build_information"] = (
            capo_elastic_beanstalk.types.source_build_information.deserialize_query(
                child_source_build_information
            )
        )
    child_source_bundle = el.find("SourceBundle")
    if child_source_bundle is not None:
        import capo_elastic_beanstalk.types.s3_location

        out["source_bundle"] = (
            capo_elastic_beanstalk.types.s3_location.deserialize_query(
                child_source_bundle
            )
        )
    child_build_configuration = el.find("BuildConfiguration")
    if child_build_configuration is not None:
        import capo_elastic_beanstalk.types.build_configuration

        out["build_configuration"] = (
            capo_elastic_beanstalk.types.build_configuration.deserialize_query(
                child_build_configuration
            )
        )
    child_auto_create_application = el.find("AutoCreateApplication")
    if child_auto_create_application is not None:
        out["auto_create_application"] = (
            child_auto_create_application.text or ""
        ).lower() == "true"
    child_process = el.find("Process")
    if child_process is not None:
        out["process"] = (child_process.text or "").lower() == "true"
    child_tags = el.find("Tags")
    if child_tags is not None:
        import capo_elastic_beanstalk.types.tags

        out["tags"] = capo_elastic_beanstalk.types.tags.deserialize_query(child_tags)
    child_image_configuration = el.find("ImageConfiguration")
    if child_image_configuration is not None:
        import capo_elastic_beanstalk.types.image_configuration

        out["image_configuration"] = (
            capo_elastic_beanstalk.types.image_configuration.deserialize_query(
                child_image_configuration
            )
        )
    return out
