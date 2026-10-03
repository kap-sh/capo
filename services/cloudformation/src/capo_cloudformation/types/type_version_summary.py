"""Generated from Smithy shape ``com.amazonaws.cloudformation#TypeVersionSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudformation._protocol.xml import Element

if TYPE_CHECKING:
    import capo_cloudformation.types.description
    import capo_cloudformation.types.is_default_version
    import capo_cloudformation.types.public_version_number
    import capo_cloudformation.types.registry_type
    import capo_cloudformation.types.timestamp
    import capo_cloudformation.types.type_arn
    import capo_cloudformation.types.type_name
    import capo_cloudformation.types.type_version_id


class TypeVersionSummary(TypedDict, closed=True):
    type: NotRequired["capo_cloudformation.types.registry_type.RegistryType"]
    """<p>The kind of extension.</p>"""
    type_name: NotRequired["capo_cloudformation.types.type_name.TypeName"]
    """<p>The name of the extension.</p>"""
    version_id: NotRequired["capo_cloudformation.types.type_version_id.TypeVersionId"]
    """<p>The ID of a specific version of the extension. The version ID is the value at the end of the ARN assigned to the extension version when it's registered.</p>"""
    is_default_version: NotRequired[
        "capo_cloudformation.types.is_default_version.IsDefaultVersion"
    ]
    """<p>Whether the specified extension version is set as the default version.</p> <p>This applies only to private extensions you have registered in your account, and extensions published by Amazon. For public third-party extensions, CloudFormation returns <code>null</code>.</p>"""
    arn: NotRequired["capo_cloudformation.types.type_arn.TypeArn"]
    """<p>The ARN of the extension version.</p>"""
    time_created: NotRequired["capo_cloudformation.types.timestamp.Timestamp"]
    """<p>When the version was registered.</p>"""
    description: NotRequired["capo_cloudformation.types.description.Description"]
    """<p>The description of the extension version.</p>"""
    public_version_number: NotRequired[
        "capo_cloudformation.types.public_version_number.PublicVersionNumber"
    ]
    """<p>For public extensions that have been activated for this account and Region, the version of the public extension to be used for CloudFormation operations in this account and Region. For any extensions other than activated third-party extensions, CloudFormation returns <code>null</code>.</p> <p>How you specified <code>AutoUpdate</code> when enabling the extension affects whether CloudFormation automatically updates the extension in this account and Region when a new version is released. For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/registry-public.html#registry-public-enable-auto">Automatically use new versions of extensions</a> in the <i>CloudFormation User Guide</i>.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: TypeVersionSummary, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "type" in value:
        import capo_cloudformation.types.registry_type

        capo_cloudformation.types.registry_type.serialize_query(
            value["type"], pairs, f"{key_prefix}Type"
        )
    if "type_name" in value:
        pairs.append((f"{key_prefix}TypeName", str(value["type_name"])))
    if "version_id" in value:
        pairs.append((f"{key_prefix}VersionId", str(value["version_id"])))
    if "is_default_version" in value:
        pairs.append(
            (
                f"{key_prefix}IsDefaultVersion",
                "true" if value["is_default_version"] else "false",
            )
        )
    if "arn" in value:
        pairs.append((f"{key_prefix}Arn", str(value["arn"])))
    if "time_created" in value:
        import capo_cloudformation.types.timestamp

        capo_cloudformation.types.timestamp.serialize_query(
            value["time_created"], pairs, f"{key_prefix}TimeCreated"
        )
    if "description" in value:
        pairs.append((f"{key_prefix}Description", str(value["description"])))
    if "public_version_number" in value:
        pairs.append(
            (f"{key_prefix}PublicVersionNumber", str(value["public_version_number"]))
        )


def deserialize_query(el: Element) -> TypeVersionSummary:
    out: TypeVersionSummary = {}  # type: ignore[typeddict-item]
    child_type = el.find("Type")
    if child_type is not None:
        import capo_cloudformation.types.registry_type

        out["type"] = capo_cloudformation.types.registry_type.deserialize_query(
            child_type
        )
    child_type_name = el.find("TypeName")
    if child_type_name is not None:
        out["type_name"] = str(child_type_name.text or "")
    child_version_id = el.find("VersionId")
    if child_version_id is not None:
        out["version_id"] = str(child_version_id.text or "")
    child_is_default_version = el.find("IsDefaultVersion")
    if child_is_default_version is not None:
        out["is_default_version"] = (
            child_is_default_version.text or ""
        ).lower() == "true"
    child_arn = el.find("Arn")
    if child_arn is not None:
        out["arn"] = str(child_arn.text or "")
    child_time_created = el.find("TimeCreated")
    if child_time_created is not None:
        import capo_cloudformation.types.timestamp

        out["time_created"] = capo_cloudformation.types.timestamp.deserialize_query(
            child_time_created
        )
    child_description = el.find("Description")
    if child_description is not None:
        out["description"] = str(child_description.text or "")
    child_public_version_number = el.find("PublicVersionNumber")
    if child_public_version_number is not None:
        out["public_version_number"] = str(child_public_version_number.text or "")
    return out
